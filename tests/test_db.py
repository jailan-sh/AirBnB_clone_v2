#!/usr/bin/python3
"""
module to test console 
"""

import unittest
from models.engine.file_storage import DBStorage
import os


class test_dbstorage(unittest.TestCase):
    """
    test dbstorage 
    """
    @unittest.skipIF(os.getenv("HBNB_TYPE_STORAGE") != "db")
    def test_console_documentation(self):
        """ test db docs"""
        self.assertIsNOTNone(DBStorage.__doc__)