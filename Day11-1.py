#Day11-1
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        n = len(B)
        for i in range(len(A)):
            if A[i:i+n]==B:
                return i
        return -1
