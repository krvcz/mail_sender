import sqlite3



class Connector:

    def __init__(self, db_path, query):
        self.db_path = db_path
        self.query = query
        self.cursor = self.connect_db()

    def connect_db(self):
        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()
            return cursor

    @property
    def query_result(self):
        return self.cursor.execute(self.query).fetchall()