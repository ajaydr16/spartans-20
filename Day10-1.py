#Day10-1
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        return A.index(B) if B in A else -1
