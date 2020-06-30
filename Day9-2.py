#Day9-2
from math import factorial as f
def fun(n,r):
    return f(n)//(f(r)*f(n-r))
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        return fun((A+B-2),A-1)