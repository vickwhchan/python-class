import sqlite3

class SQLDict:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        c = self.conn.cursor()
        try:
            c.execute('Create table dict (key TEXT, value TEXT')
        except OperationalError:
            pass

    def __setitem__(self, key, value):
        item = key, value
        c = self.conn.cursor()
        c.execute('INSERT INTO Dict VALUES (?, ?)', item)
        c.execute('Create unique index Kndx On Dict (key)')



d = SQLDict('chan.db')