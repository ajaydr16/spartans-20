#Day7-1
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
       return ' '.join(A.strip().split()[-1::-1])
        #for i in range(len(l)):
        #    print(l[len(l)-i-1])
