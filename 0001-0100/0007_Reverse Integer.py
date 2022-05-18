class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: 
            return 0
        if x < 0:
            x *= (-1)
            ans = int(str(x)[::-1])*(-1)
        else:
            ans = int(str(x)[::-1])
        if ans >= 2**31-1 or ans <= -2**31: 
            return 0
        else:
            return ans