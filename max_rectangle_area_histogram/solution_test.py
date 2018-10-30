import unittest
from solution import solution


class TestMaxRectangleAreaHistogram(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(8, solution([1,2,3,4,2,1]))

    def test_classic(self):
        self.assertEqual(4, solution([2,1,2,3,1]))

if __name__ == '__main__':
    unittest.main()
