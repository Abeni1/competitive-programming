class Solution(object):
    def removeElement(self, nums, val):
        """Given an integer array nums and an integer val, remove all
        occurrences of val in nums "IN-PLACE".The relative order of the elements may be changed.         

        Args:
            nums (int): integer array
            val (int): integer number
            rtype (int):
        """

        ###Not finished
        for i in range(len(nums)):
            if (val == nums[i]):
                del nums[i]
        return len(nums)
if __name__ == __main__:
    Solution = 