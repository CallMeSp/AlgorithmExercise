class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in num_dict.keys():
                return [num_dict[sub], index]
            else:
                num_dict[value] = index

        return []
