class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # simple code
        c_count = [0, 0, 0]
        for num in nums:
            if num == 0:
                c_count[0] += 1
            elif num == 1:
                c_count[1] += 1
            else:
                c_count[2] += 1
        
        count = 0
        for i in range(3):
            while True:
                if c_count[i] == 0:
                    break
                nums[count] = i
                c_count[i] -= 1
                count += 1

        # other algorithms
        