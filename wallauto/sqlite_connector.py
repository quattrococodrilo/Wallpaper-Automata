""" Sqlite module. """

import pathlib
import sqlite3


class SqliteHandler:

    db_file = None

    db_name_default = 'images.db'

    def __init__(self):
        pass

    def _db_file_handler(self):
        self.db_file = db_file if db_file else db_name_default

    def _connect(self):
        pass
