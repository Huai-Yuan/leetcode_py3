class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:
            count = 0
            for i in range(m+n):
                if i >= m:
                    nums1[i] = nums2[count]
                    count += 1
                elif nums1[i] > nums2[count]:
                    nums2[count], nums1[i] = nums1[i], nums2[count]
                    nums2.sort()