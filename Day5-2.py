#Day5-2
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A[0])
        if(n == 0):
            return 0
        l = []
        sol = []
        for d in range((2*(n-1))+1):
            for i in range(d+1):
                j = d-i
                if(j >= n or i >= n):
                    pass
                else:
                    l.append(A[i][j])
            sol.append(l)
            l = []
        return sol
