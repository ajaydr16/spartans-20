#Day6-2
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        l = [1]*(A+1)
        if A<2 : return l
        
        p = self.getRow(A-1)
        for i in range(1,A):
            l[i] = p[i]+p[i-1]
        
        return l
