import sqlite3


def initalise_db():
    conn = sqlite3.connect("coins.db")
    cursor = conn.cursor()
    create_schema(cursor)
    conn.commit()

    return cursor, conn


def create_schema(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS coins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ticker TEXT NOT NULL UNIQUE,
        market_cap REAL NOT NULL,
        last_fetched TEXT NOT NULL
        )"""
    )


def insert_coin_data(name, ticker, market_cap, last_updated, cursor):
    cursor.execute(
        """
        INSERT INTO coins (name, ticker, market_cap, last_fetched)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(ticker) DO UPDATE SET
            market_cap = excluded.market_cap,
            last_fetched = excluded.last_fetched
        """,
        (name, ticker, market_cap, last_updated),
    )


cursor, conn = initalise_db()
