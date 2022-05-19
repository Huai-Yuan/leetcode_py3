class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(' : ')', '{' : '}', '[' : ']'}
        temp = []
        for i in s:
            if i in d:
                temp.append(d[i])
            else:
                if temp != [] and temp.pop() == i:
                    pass
                else:
                    return False
        if temp == []:
            return True
        else:
            return False 