class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        output, left = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                if k == 0:
                    while nums[left] != 0 : left += 1
                    left += 1
                else : k-= 1
            output = max(output, right - left + 1)
        return output
