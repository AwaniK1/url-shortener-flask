
import sqlite3
import os


def create_db():
    print("Database location:", os.path.abspath('urls.db'))
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT NOT NULL
        )
    ''')

    # Add the clicks column to an existing database if needed
    columns = [
        row[1] for row in cursor.execute(
            "PRAGMA table_info(urls)"
        ).fetchall()
    ]

    if 'clicks' not in columns:
        cursor.execute(
            'ALTER TABLE urls ADD COLUMN clicks INTEGER DEFAULT 0'
        )

    conn.commit()
    conn.close()


def insert_url(original_url, short_code):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO urls (original_url, short_code) VALUES (?, ?)',
        (original_url, short_code)
    )

    conn.commit()
    conn.close()


def find_url(short_code):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute(
        'SELECT original_url FROM urls WHERE short_code = ?',
        (short_code,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]

    return None


def increment_clicks(short_code):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?',
        (short_code,)
    )

    conn.commit()
    conn.close()


def get_clicks(short_code):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute(
        'SELECT clicks FROM urls WHERE short_code = ?',
        (short_code,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]

    return None


def find_short_code_by_url(original_url):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute(
        'SELECT short_code FROM urls WHERE original_url = ?',
        (original_url,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]

    return None
