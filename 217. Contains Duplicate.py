class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        previous = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != previous:
                previous = nums[i]
            else:
                return True
        return False
