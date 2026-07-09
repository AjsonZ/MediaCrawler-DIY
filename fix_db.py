import sqlite3, os
db = os.path.join(os.path.dirname(__file__), "database", "sqlite_tables.db")
conn = sqlite3.connect(db)
conn.execute("DELETE FROM douyin_aweme")
conn.commit()
print("Cleared douyin_aweme")
conn.close()
