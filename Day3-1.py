class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s=''
        for i in range(len(A)):
            s+=str(A[i])
        s=str(int(s)+1)
        s=s.lstrip('0')
        return list(s)