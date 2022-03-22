class Solution:
    def twoSum(self, nums: "list[int]", target: "int") -> "list[int]":

        temp_dict = {}

        for i, num in enumerate(nums):
            residue = target - num
            if residue in temp_dict:
                return [temp_dict[residue], i]
            temp_dict[num] = i