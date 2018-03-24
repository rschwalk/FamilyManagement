"""
Family Management application - rschwalk 2018
Module to handle the required data.
"""
import sqlite3


class ItemDatabase(object):
    """ Database class for sglite """
    location = 'family_management.db'

    def __init__(self):
        self._db = sqlite3.connect(self.location)

        sql = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, ' \
              'name TEXT, username TEXT, password TEXT)'

        self._cursor = self._db.cursor()
        self._cursor.execute(sql)
        self._db.commit()

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
