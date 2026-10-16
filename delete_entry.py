
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "urls.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

entry_id = int(input("Enter the ID to delete: "))

cursor.execute("DELETE FROM urls WHERE id = ?", (entry_id,))
conn.commit()

print("Entries deleted:", cursor.rowcount)

conn.close()
