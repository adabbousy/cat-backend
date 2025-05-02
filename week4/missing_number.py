class Solution(object):
    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        return self.quicksort(left) + [pivot] + self.quicksort(right)



    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sorted_nums = self.quicksort(nums)
        if sorted_nums[0] != 0:
            return 0
        if sorted_nums[n-1] != n:
            return n
        for i in range(1, n):
            if sorted_nums[i] > i:
                return i