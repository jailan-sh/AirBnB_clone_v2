#!/usr/bin/python3
"""
module to test console
"""

import unittest
from models.engine.file_storage import DBStorage
import os


@unittest.skipIF(os.getenv("HBNB_TYPE_STORAGE") != "db")
class TestDBstorage(unittest.TestCase):
    """
    test dbstorage
    """
    def test_documentation(self):
        """ test db docs"""
        self.assertIsNotNone(DBStorage.__doc__)
