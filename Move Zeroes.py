# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        nums[:] = nums[:] + [0]*x
        
        ############## METHOD 2 ############
        def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for j in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
            
        ################ METHOD 3 ############
        def moveZeroes(self, nums):
            zero = 0  # records the position of "0"
            for i in xrange(len(nums)):
                if nums[i] != 0:
                    nums[i], nums[zero] = nums[zero], nums[i]
                    zero += 1
