# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import sqlite3

conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\sqlite_tables.db")
cur = conn.cursor()

# Add duration column if not exists
try:
    cur.execute("ALTER TABLE douyin_aweme ADD COLUMN duration INTEGER DEFAULT 0")
    print("Added 'duration' column")
except sqlite3.OperationalError as e:
    if "duplicate column" in str(e):
        print("Column 'duration' already exists")
    else:
        raise

conn.commit()
conn.close()
print("Done.")
