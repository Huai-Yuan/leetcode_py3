class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        control = False
        temp = ""
        for i in s[::-1]:
            if control and i == " ":
                return len(temp)
            elif i != " ":
                temp = temp + i
                control = True
        return len(temp)