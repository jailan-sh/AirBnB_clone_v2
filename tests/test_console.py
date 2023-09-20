#!/usr/bin/python3
""" """

import unittest
import console


class test_console(unittest.TestCase):
    """
    test console 
    """
    def test_console_documentation(self):
        self.assertIsNOTNone(console.__doc__)
    