class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        temp = 0
        for i in nums:
            if i >= target:
                return temp
            temp += 1
        return temp