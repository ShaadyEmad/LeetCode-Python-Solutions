class Solution(object):
    def moveZeroes(self, nums):
        index = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[i], nums[index] = nums[index],  nums[i]
                index +=1
