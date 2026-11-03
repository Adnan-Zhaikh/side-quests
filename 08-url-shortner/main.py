from fastapi import FastAPI
from db import get_db, init_db
from fastapi import Depends, HTTPException
from pydantic import BaseModel, HttpUrl
from base62 import encode
from fastapi import Request
from fastapi.responses import RedirectResponse


app = FastAPI()

class ShortenRequest(BaseModel):
    url: HttpUrl


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/shorten")
def shorten(body: ShortenRequest, db=Depends(get_db)):
    cur = db.execute(
        "INSERT INTO urls (code, long_url) VALUES (?, ?)",
        ("pending", str(body.url)),
    )
    url_id = cur.lastrowid
    code = encode(url_id)
    db.execute("UPDATE urls SET code = ? WHERE id = ?", (code, url_id))
    db.commit()
    return {"code": code, "short_url": f"http://127.0.0.1:8000/{code}"}

@app.get("/{code}")
def redirect(code: str, request: Request, db=Depends(get_db)):
    row = db.execute("SELECT id, long_url FROM urls WHERE code = ?", (code,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Short link not found")

    db.execute(
        "INSERT INTO clicks (url_id, referrer, user_agent) VALUES (?, ?, ?)",
        (row["id"], request.headers.get("referer"), request.headers.get("user-agent")),
    )
    db.commit()
    return RedirectResponse(row["long_url"], status_code=307)