class Solution:
    def twoSum(self, nums, target):
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                return [my_dict[nums[i]], i]
            else:
                my_dict[target - nums[i]] = i
