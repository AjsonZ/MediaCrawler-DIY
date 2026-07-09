# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import sqlite3

conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\sqlite_tables.db")
cur = conn.cursor()

# Show what type=68 rows are before deleting
cur.execute("""SELECT aweme_id, aweme_type, title FROM douyin_aweme WHERE aweme_type = '68'""")
rows = cur.fetchall()
print(f"Deleting {len(rows)} rows with aweme_type=68:")
for r in rows:
    print(f"  {r[0]} | {r[2][:60]}")

# Delete
cur.execute("""DELETE FROM douyin_aweme WHERE aweme_type = '68'""")
print(f"\nDeleted {cur.rowcount} rows")

conn.commit()
cur.execute("""SELECT COUNT(*) FROM douyin_aweme""")
print(f"Remaining: {cur.fetchone()[0]} rows")
conn.close()
