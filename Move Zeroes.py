class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in sorted(nums):
            if i == 0:
                nums.remove(i)
                nums.append(0)
