import unittest
from solution import solution


class TestHighestProductOf3(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(300, solution([-100, -1, 0, 1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
