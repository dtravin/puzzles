class ChessQueens:
    def __init__(self, n):
        self.n = n
        self.b = [[0 for c in range(n)] for r in range(n)]


    def printBoard(self, msg):
        print("=====%s====" % msg)
        for i in self.b:
            print(''.join(['Q' if e else '.' for e in i]))

        print("=============\n")

    def isSquareValid(self, r, c):
        return c >= 0 and c < self.n and r >=0 and r < self.n

    def isSquareOccupied(self, r, c):
        return self.b[r][c] == 1


    def rec(self, r):
        self.printBoard("Entered %s" % r)
        if r == self.n:
            return True

        for c in range(self.n):
            self.printBoard("Trying (%s, %s)" % (r,c))
            if self.isSafe(r, c):
                self.b[r][c] = 1
                if self.rec(r+1):
                    return True

                print("Backtracking to (%s, %s)" % (r,c))
                self.b[r][c] = 0

        return False

    def isSafe(self, r, c):
        for _r in range(self.n):
            if self.b[_r][c]:
                return False

        for _c in range(self.n):
            if self.b[r][_c]:
                return False

        d = 0
        def isDiagOccupied(dr, dc):
            _r = r + d*dr
            _c = c + d*dc
            valid = self.isSquareValid(_r, _c)
            if not valid:
                return False
            else:
                return self.isSquareOccupied(_r, _c)

        while d < self.n:

            d += 1
            if isDiagOccupied(1, 1) or \
               isDiagOccupied(-1, 1) or \
               isDiagOccupied(1, -1) or \
               isDiagOccupied(-1, -1):
                return False

        return True

def solution(n):
    s = ChessQueens(n)
    if s.rec(0):
        return s.b

    return None
