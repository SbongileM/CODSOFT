import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('TaskMasterTo_Do_list.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS lists (
                id INTEGER PRIMARY KEY,
                name BLOB
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                list_id INTEGER,
                name TEXT,
                notes TEXT,
                FOREIGN KEY(list_id) REFERENCES lists(id)
            )
        ''')
        self.conn.commit()

    def add_list(self, name):
        self.cursor.execute('''
            INSERT INTO lists (name) VALUES (?)
        ''', (name,))
        self.conn.commit()

    def add_task(self, list_id, name,notes):
        self.cursor.execute('''
            INSERT INTO tasks (list_id, name, notes) VALUES (?, ?)
        ''', (list_id, name, notes))
        self.conn.commit()

    def get_lists(self):
        self.cursor.execute('''
            SELECT id, name FROM lists
        ''')
        return self.cursor.fetchall()

    def get_tasks(self, list_id):
        self.cursor.execute('''
            SELECT id, name FROM tasks WHERE list_id = ?
        ''', (list_id,))
        self.cursor.fetchall()