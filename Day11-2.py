
#Day11-2
class Solution:
	# @param A : integer
	# @return a strings
	def intToRoman(self, A):
        s=""
        num=A
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        i=0
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        while num>0:
            for x in range(num//val[i]):
                s=s+syb[i]
                num=num-val[i]
            i=i+1
        return s