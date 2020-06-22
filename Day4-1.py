class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        x = 0
        for a in A:
            x ^= a 
        for i in range(1, len(A)):
            x ^= i 
        return x 
