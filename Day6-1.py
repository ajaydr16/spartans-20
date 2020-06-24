#Day6-1
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        i=0
        m = -1
        l = []
        while i<len(A):
            while i<len(A) and A[i]<0:
                i += 1
            l1 = []
            while i<len(A) and A[i]>=0:
                l1.append(A[i])
                i += 1
            if sum(l1)>m:
                l = l1
                m = sum(l1)
        return l