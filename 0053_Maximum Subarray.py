class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        temp = 0
        _max = float("-inf")
        for num in nums:
            if temp > 0:
                temp += num
            else:
                temp = num
                
            _max = max(_max, temp)
                
        return _max