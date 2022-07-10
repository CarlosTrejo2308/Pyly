import sqlite3

class SQDBManager:
    def __init__(self):
        self.dbName = "alias.db"
        self.conn = sqlite3.connect(self.dbName, check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS users (alias TEXT PRIMARY KEY, url TEXT, ttl TEXT)""")
        self.conn.commit()

    def add(self, url, alias, ttl):
        self.c.execute("INSERT INTO users VALUES (?, ?, ?)", (alias, url, ttl))
        self.conn.commit()
    
    def get(self, alias):
        print("alias: " + alias)
        self.c.execute("SELECT * FROM users WHERE alias=?", [alias])
        return self.c.fetchone()

    def get_alias(self, url):
        self.c.execute("SELECT alias FROM users WHERE url=?", [url])
        all = self.c.fetchall()
        return all if len(all) > 0 else None