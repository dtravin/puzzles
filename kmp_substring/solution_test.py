import unittest
from solution import solution, build_prefix


class TestKMP(unittest.TestCase):

    def test_prefix(self):
        self.assertEqual([0, 0, 0], build_prefix("ab3"))
        self.assertEqual([0, 0, 0, 0, 1, 2, 3, 0], build_prefix("abc1abc2"))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7], build_prefix("aaaaaaaa"))

    def test_basic(self):
        self.assertEqual(6, solution("ab1ab2ab3ab4", "ab3"))
        self.assertEqual(7, solution("abcabc3abcabc5abc6", "abcabc5"))

if __name__ == '__main__':
    unittest.main()
