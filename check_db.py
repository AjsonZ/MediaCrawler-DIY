# -*- coding: utf-8 -*-
import sys, io, os, sqlite3
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

db = os.path.join(os.path.dirname(__file__), "database", "sqlite_tables.db")
conn = sqlite3.connect(db)
cur = conn.cursor()

# All non-image rows
cur.execute("SELECT title, source_keyword, aweme_type FROM douyin_aweme WHERE aweme_type != '68'")
rows = cur.fetchall()

# Check broad keyword match: 万魔 or S20 or 1MORE
matched = []
unmatched = []
for r in rows:
    t = (r[0] or "").lower()
    if any(k in t for k in ['万魔', 's20', '1more']):
        matched.append(r)
    else:
        unmatched.append(r)

print(f"Total non-image: {len(rows)}")
print(f"Matched (万魔/S20/1MORE): {len(matched)}")
print(f"Unmatched: {len(unmatched)}")

if unmatched:
    print("\n--- Unmatched titles ---")
    for r in unmatched[:20]:
        print(f"  [kw={r[1][:15]}] type={r[2]} | {r[0][:80]}")

conn.close()
