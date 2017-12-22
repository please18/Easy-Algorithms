# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


########## METHOD 1 #############
class Solution:
    def twoSum(self, nums, target):
      hash = {}
      for indx, i in enumerate(nums):
          if target - i in hash:
              return [nums.index(target- i), indx]
          else:
              hash[i] = target - i                

########## METHOD 2 ###############
class Solution:
  def twoSum(self, nums, target):
    d={}
    for i,num in enumerate(nums):
      if target-num in d:
          return d[target-num], i
      d[num]=i
      
######### METHOD 3 ###################
