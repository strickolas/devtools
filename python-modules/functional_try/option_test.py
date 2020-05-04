import unittest
from option import *


class OptionTest(unittest.TestCase):
    def test_nothing(self):
        ls = []
        x = Try(lambda: ls[0])
        self.assertTrue(isinstance(x, Option))
        self.assertEqual(type(x), Nothing)
        self.assertEqual(type(x.get()), IndexError)

    def test_something(self):
        ls = ["asdf"]
        x = Try(lambda: ls[0])
        self.assertTrue(isinstance(x, Option))
        self.assertEqual(type(x), Something)
        self.assertEqual(type(x.get()), str)
