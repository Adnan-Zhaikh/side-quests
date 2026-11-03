import sqlite3

DB_PATH = "shortener.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute(""PRAGMA foreign_keys = ON"")
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS urls (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        code        TEXT UNIQUE NOT NULL,
        long_url    TEXT NOT NULL,
        created_at  TEXT NOT NULL DEFAULT (datetime('now'))
    );

    CREATE TABLE IF NOT EXISTS clicks (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        url_id      INTEGER NOT NULL REFERENCES urls(id) ON DELETE CASCADE,
        clicked_at  TEXT NOT NULL DEFAULT (datetime('now')),
        referrer    TEXT,
        user_agent  TEXT
    );

    CREATE INDEX IF NOT EXISTS idx_clicks_url_id ON clicks(url_id);
    """)
    conn.commit()
    conn.close()