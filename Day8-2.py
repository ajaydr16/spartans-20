#Day8-2
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        sign = 1
        j = 0
        while j < len(A) and A[j] == " ":
            j += 1

        if j == len(A):
            return 0
        
        if A[j] == "+":
            j += 1
        elif A[j] == '-':
            j += 1
            sign = -1
        
        start = j
        while j < len(A) and A[j].isnumeric():
            j += 1
        
        if start == j:
            return 0
        
        r = sign * int(A[start:j])
        return max(-2147483648, min(r, 2147483647))

