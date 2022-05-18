class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        short = len(strs[0])
        index = 0
        for i, _ in enumerate(strs):
            if short > len(_):
                short = len(_)
                index = i
        if short == 0:
            return ""

        isSame = True
        short_str = strs[index]
        strs.remove(short_str)
        for i, _ in enumerate(short_str):
            for j in strs:
                if j[i] != _:
                    isSame = False
            if isSame == False:
                return short_str[:i]
        if isSame == True:
            return short_str

# Anser on App <-- more efficient
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        
        strs.sort()
        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]