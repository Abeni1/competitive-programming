class Solution(object):
    def removeDuplicates(self, nums):
        """
            nums (_type_):  Lists[int]
            rtype: int
        """
        for num in nums:
            while(nums.count(num) > 1):
                 nums.remove(num)
        return len(nums)


if (__name__ == "__main__"):
    test = Solution()
    array = [0,0,1,1,1,2,2,3,3,4]
    print(test.removeDuplicates(array))