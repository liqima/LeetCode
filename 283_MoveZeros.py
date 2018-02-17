class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num = 0
        length = len(nums)
        while num < length:
            if nums[num] == 0:
                nums.append(nums.pop(num))
                length -= 1
            else:
                num += 1
        print(nums)

s = Solution()
a_list = [1, 3, 6, 0, 0, 3, 0, 1]
s.moveZeroes(a_list)