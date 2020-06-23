#Day5-1
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        x, y, total = A[0], B[0], 0
        for x1, x2 in zip(A, B):
            dx, dy = abs(x1 - x), abs(x2 - y)
            if dx < dy:
                total += dy
            else:
                total += dx
            x, y = x1, x2
        return total
 
