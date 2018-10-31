import unittest
from solution import solution


class TestChessQueens(unittest.TestCase):

    def test_basic(self):
        s = [
            [0,1,0,0],
            [0,0,0,1],
            [1,0,0,0],
            [0,0,1,0],
        ]
        self.assertEqual(s, solution(4))

if __name__ == '__main__':
    unittest.main()
