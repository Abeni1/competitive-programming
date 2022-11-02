class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        if nums.count(target) == 0:
            return []
        else:
            return [nums.index(target) + nums.count(target) - i for i in range(nums.count(target),0,-1)]
