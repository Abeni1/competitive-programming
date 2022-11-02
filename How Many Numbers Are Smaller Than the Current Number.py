class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = []
        for i in nums:
            count.append(sorted(nums).index(i))
        
        return count
