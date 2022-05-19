class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        next_ = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[next_] = nums[i]
                next_ += 1
        
        return next_