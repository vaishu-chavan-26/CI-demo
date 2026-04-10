import unittest
from math_utils import add, multiply
from buggy_math import multiply as buggy_multiply

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_multiply_correct(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_bug(self):
        self.assertEqual(buggy_multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
