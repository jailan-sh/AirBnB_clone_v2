#!/usr/bin/python3
"""
test console
"""

import unittest
import console


class TestConsole(unittest.TestCase):
    """
    test console
    """
    def test_console_documentation(self):
        """ test console docs"""
        self.assertIsNOTNone(console.__doc__)
