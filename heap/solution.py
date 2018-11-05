operatorGreater = lambda x, y: x >= y
operatorLesser = lambda x, y: x <= y

class Heap:
    def __init__(self, max_size, op):
        self.op = op
        self.max_size = max_size
        self.a = []


    def push(self, e):
        self.a.append(e)
        self._sift_down(0, len(self.a) - 1)


    def _sift_down(self, dst, src):
        val = self.a[src]
        idx = src
        while idx > dst:
            parentIdx = idx // 2
            parentVal = self.a[parentIdx]
            print("%s %s %s %s" % (idx, parentIdx, val, parentVal))
            if self.op(val, parentVal):
                self.a[idx] = parentVal
                self.a[parentIdx] = val
                idx = parentIdx
            else:
                break

    def get(self, idx):
        return self.a[idx]

class MaxHeap(Heap):
    def __init__(self, max_size):
        Heap.__init__(self, max_size, operatorGreater)

class MinHeap(Heap):
    def __init__(self, max_size):
        Heap.__init__(self, max_size, operatorLesser)
