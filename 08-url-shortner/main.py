from fastapi import FastAPI
from db import init_db

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


