import unittest
from demo import *


class TestDemo(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizz(3), 1)
        self.assertEqual(fizz(5), 0)
        self.assertEqual(fizz(6), 1)
        self.assertEqual(fizz(13), 1)

    def test_buzz(self):
        self.assertEqual(buzz(3), 0)
        self.assertEqual(buzz(5), 1)
        self.assertEqual(buzz(6), 0)
        self.assertEqual(buzz(51), 1)
