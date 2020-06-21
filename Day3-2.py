inf=float('inf')
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        m = -inf
	    c = 0
	    for x in A:
	        c += x
	        m = max(c, m)
	        c = max(c, 0)
	    return m
