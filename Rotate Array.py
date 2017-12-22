# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

def rotate_by_k(nums, k):
  k = k%len(nums)
  # the modulo is found incase nums size is 2 and k is 3. Modulo will give k as 1
  nums[:] = nums[-k:] + nums[:-k]
  
