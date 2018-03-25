"""
Family Management application - rschwalk 2018
Module to handle the required data.
"""
import sqlite3


class UserData(object):
    """ Database class of the users for sglite """
    location = 'family_management.db'

    def __init__(self):
        self._db = sqlite3.connect(self.location)

        sql = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, ' \
              'name TEXT, username TEXT, password TEXT)'

        self._cursor = self._db.cursor()
        self._cursor.execute(sql)
        self._db.commit()
        
    def add_user(self, name, username, password):
        self._cursor.execute('''INSERT INTO users(name, username, password)
              VALUES(?, ?, ?)''', (name, username, password))
        self._db.commit()
        # self.all_rows.append()

    def get_user(self, username):
        self._cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        rows = self._cursor.fetchall()

        return rows

    def read_all(self):
        self._cursor.execute('''SELECT id, name, username, password FROM users''')
        all_rows = self._cursor.fetchall()

        return all_rows

def items():
    """ Helper function to create test data """
    items_list = [
        {
            'id': 1,
            'title': 'Task One',
            'notes': 'Notes to task 1',
            'creator': 'Richard',
            'date': '24.03.2018'
        },
        {
            'id': 2,
            'title': 'Task Two',
            'notes': 'Notes to task 2',
            'creator': 'Vanessa',
            'date': '24.03.2018'
        },
        {
            'id': 3,
            'title': 'Task Three',
            'notes': 'Notes to task 3',
            'creator': 'Vanessa',
            'date': '24.03.2018'
        }
    ]

    return items_list
