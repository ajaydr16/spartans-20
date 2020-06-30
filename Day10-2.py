#Day10-2
class Solution:
    def findMedianSortedArrays(self, A, B):
        import sys
        if len(A) > len(B):
            A, B = B, A
        m = len(A)
        n = len(B)
        startx = 0
        endx = m

        while startx <= endx:
            x = (startx+endx)/2
            y = (m+n+1)/2 - x

            Ax = A[x-1] if (x-1) >= 0 else None
            Ax_1 = A[x] if (x < m) else sys.maxint

            By = B[y-1] if (y-1) >= 0 else None
            By_1 = B[y] if (y < n) else sys.maxint


            if Ax <= By_1 and By <= Ax_1:
                if (n+m) & 1:
                    return max(Ax, By)
                else:
                    return (max(Ax,By) + min(Ax_1, By_1))/2.0
            elif Ax > By_1:
                endx = x-1
            else:
                startx = x+1
        return None


