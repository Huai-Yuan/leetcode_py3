class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return n
        else:
            sum_ = 3
            n1, n2 = 1, 1
            for i in range(1, n-2):
                n1, n2 = n2, n1+n2
                sum_ += n2
            return sum_