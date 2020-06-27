#Day7-2
def pal(s):
    i=0
    j=len(s)-1
    
    while i<j:
        if s[i]!=s[j]:
            return 0
        i+=1
        j-=1
    return 1


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        i=0
        j=len(A)
        #print(pal('bb'))
        m=0
        
        while len(A)-i>m:
            if j-i==1:
                j=len(A)
                i+=1
                continue
            
            if pal(A[i:j]):
                if m<j-i:
                    
                    m=j-i
                    x=A[i:j]
                i+=1
                j=len(A)

                continue
            j-=1
            
        if m==0:
            return A[0]
        else:
            return x
        