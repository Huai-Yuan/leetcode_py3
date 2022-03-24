class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        for digit in digits:
            a += str(digit)
        return list(str(int(a) + 1))