import sqlite3

def create_db():
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS urls(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        original_url TEXT NOT NULL,
                        short_code TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

def insert_url(original_url, short_code):
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)', (original_url, short_code))
    conn.commit()
    conn.close()