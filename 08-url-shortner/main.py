from fastapi import FastAPI
from db import get_db, init_db, DB_PATH
from fastapi import Depends, HTTPException
from pydantic import BaseModel, HttpUrl
from base62 import encode
from fastapi import Request
from fastapi.responses import RedirectResponse
import time
from collections import defaultdict
import sqlite3
import re
from contextlib import asynccontextmanager
from fastapi.responses import FileResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

CODE_RE = re.compile(r"^[0-9a-zA-Z]{1,10}$")

class ShortenRequest(BaseModel):
    url: HttpUrl

def client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()   # leftmost = original client
    return request.client.host if request.client else "unknown"

WINDOW_SECONDS = 60
MAX_REQUESTS = 10
hits = defaultdict(list)   # ip -> list of timestamps

def rate_limit(request: Request):
    ip = client_ip(request)
    now = time.time()
    hits[ip] = [t for t in hits[ip] if now - t < WINDOW_SECONDS]
    if len(hits[ip]) >= MAX_REQUESTS:
        raise HTTPException(status_code=429, detail="Too many requests, slow down")
    hits[ip].append(now)


@app.get("/")
def index():
    return FileResponse("index.html")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/shorten", dependencies=[Depends(rate_limit)])
def shorten(body: ShortenRequest, request: Request, db=Depends(get_db)):
    cur = db.execute(
        "INSERT INTO urls (code, long_url) VALUES (?, ?)",
        ("pending", str(body.url)),
    )
    url_id = cur.lastrowid
    code = encode(url_id)
    db.execute("UPDATE urls SET code = ? WHERE id = ?", (code, url_id))
    db.commit()
    return {"code": code, "short_url": str(request.base_url).rstrip("/") + "/" + code}


@app.get("/{code}")
def redirect(code: str, request: Request, db=Depends(get_db)):
    if not CODE_RE.match(code):
        raise HTTPException(status_code=404, detail="Not found")

    row = db.execute(
        "SELECT id, long_url FROM urls WHERE code = ?", (code,)
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Short link not found")

    db.execute(
        "INSERT INTO clicks (url_id, referrer, user_agent) VALUES (?, ?, ?)",
        (row["id"], request.headers.get("referer"), request.headers.get("user-agent")),
    )
    db.commit()
    return RedirectResponse(row["long_url"], status_code=307)


@app.get("/stats/{code}")
def stats(code: str, db=Depends(get_db)):
    row = db.execute("SELECT id, long_url, created_at FROM urls WHERE code = ?", (code,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Short link not found")

    total = db.execute(
        "SELECT COUNT(*) AS n FROM clicks WHERE url_id = ?", (row["id"],)
    ).fetchone()["n"]

    by_day = db.execute("""
        SELECT date(clicked_at) AS day, COUNT(*) AS clicks
        FROM clicks WHERE url_id = ?
        GROUP BY day ORDER BY day
    """, (row["id"],)).fetchall()

    by_referrer = db.execute("""
        SELECT COALESCE(referrer, 'direct') AS source, COUNT(*) AS clicks
        FROM clicks WHERE url_id = ?
        GROUP BY source ORDER BY clicks DESC LIMIT 10
    """, (row["id"],)).fetchall()

    return {
        "code": code,
        "long_url": row["long_url"],
        "created_at": row["created_at"],
        "total_clicks": total,
        "clicks_by_day": [dict(r) for r in by_day],
        "top_referrers": [dict(r) for r in by_referrer],
    }