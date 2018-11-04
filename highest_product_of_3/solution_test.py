import unittest
from solution import solution


class TestHighestProductOf3(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(60, solution([1, 2, 3, 4, 5, 1]))
        self.assertEqual(150, solution([-10, -5, 0, 1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
