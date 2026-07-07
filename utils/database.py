import sqlite3

DATABASE = "database.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS portfolio(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            shares INTEGER NOT NULL,
            buy_price REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_stock(ticker, shares, buy_price):
    conn = get_connection()

    conn.execute("""
        INSERT INTO portfolio(ticker, shares, buy_price)
        VALUES (?, ?, ?)
    """, (ticker, shares, buy_price))

    conn.commit()
    conn.close()


def get_all_stocks():
    conn = get_connection()

    stocks = conn.execute("""
        SELECT * FROM portfolio
    """).fetchall()

    conn.close()

    return stocks

def delete_stock(stock_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM portfolio WHERE id = ?",
        (stock_id,)
    )

    conn.commit()
    conn.close()