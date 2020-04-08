# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


def moveZeroes(nums):
    counter = 0
    zero = 0
    while counter < len(nums):
        if nums[counter] == 0:
            nums.remove(0)
            zero += 1
        else:
            counter += 1
    zeros = [0] * zero
    return nums.extend(zeros)
