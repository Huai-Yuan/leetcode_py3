class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        for i in range(s_len, 0, -1):
            for j in range(s_len-i+1):
                s_ = s[j:j+i]
                if s_ == s_[::-1]:
                    return s_