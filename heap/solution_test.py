import unittest
from solution import MaxHeap


class TestHeap(unittest.TestCase):

    def test_basic(self):
        h = MaxHeap(5)
        h.push(1)
        self.assertEqual([1], h.a)
        h.push(2)
        self.assertEqual([2,1], h.a)
        h.push(3)
        self.assertEqual([3,2,1], h.a)
        h.push(4)
        self.assertEqual([4,3,1,2], h.a)
        h.push(5)
        self.assertEqual([5,4,3,2,1], h.a)
        h.push(6)
        self.assertEqual([6,5,4,2,1,3], h.a)
        h.push(7)
        self.assertEqual([7,6,4,5,1,3,2], h.a)


if __name__ == '__main__':
    unittest.main()
