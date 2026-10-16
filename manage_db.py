
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "urls.db")

print("Database:", db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
    SELECT id, original_url, short_code, clicks
    FROM urls
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
