class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = list(s)
        max_len = len(set(s_list))
        if max_len == 0:
            return 0
        for i in range(max_len, 0, -1):
            for j in range(len(s)-i+1):
                if len(set(s[j:j+i])) == i:
                    return i