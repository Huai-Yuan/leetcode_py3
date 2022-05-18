class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)[::-1]
        if temp == str(x):
            return True
        else:
            return False

# Anser on App
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True