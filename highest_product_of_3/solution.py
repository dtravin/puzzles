import sys
sys.path.insert(0, '..')

import heap
import heap

def solutionOn(a):
    heapMax = heap.MaxHeap(3)
    heapMin = heap.MinHeap(2)

    for e in a:
        heapMax.push(e)
        heapMin.push(e)

    return max(heapMax[-1] * heapMax[-2] * heapMax[-3],
               heapMax[-1] * heapMin[0] * heapMin[1])

def solutionOnlogn(a):
    a.sort()
    return max(a[-1] * a[-2] * a[-3], a[-1] * a[0] * a[1])

solution = solutionOnlogn
