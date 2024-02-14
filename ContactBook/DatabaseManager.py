import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('Contact_Book.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                number TEXT,
                email TEXT,
                store TEXT,
                address TEXT      
            )
        ''')

    def add_contact(self, name, number, email, store, address):
        self.cursor.execute('''
            INSERT INTO contacts (name, number, email, store, address) VALUES (?,?,?,?,?)
        ''', (name,number, email, store, address))
        self.conn.commit()

    def get_contact(self, search_iterm):
        self.cursor.execute('''
           SELECT * FROM contacts WHERE number LIKE ? OR name LIKE ? OR store LIKE ?
        ''', (search_iterm,search_iterm,search_iterm))
        return self.cursor.fetchall()
    
    def get_contacts(self):
        self.cursor.execute('''
            SELECT name, number, email, store, address FROM contacts
        ''')
        return self.cursor.fetchall()
