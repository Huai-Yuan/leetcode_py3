class Solution:
    def mySqrt(self, x: int) -> int:
        a = (x + 1) // 2
        while (a * a) > x:
            a = (a + x//a) // 2
        return a