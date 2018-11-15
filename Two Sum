class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = dict()
        for i in range(len(nums)):
            dict_nums[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict_nums and dict_nums[diff] != i:
                return [i, dict_nums[diff]]
