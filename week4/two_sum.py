class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = {}
        for i, num in enumerate(nums):
            if num in idx:
                return [idx[num], i]
            idx[target-num] = i