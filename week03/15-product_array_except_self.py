# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity?
# (The output array does not count as extra space for the purpose of space complexity analysis.)

#  First try
from numpy import prod


def productExceptSelf(nums):
    lst = list(nums)
    for idx, no in enumerate(lst):
        lst[idx] = 1
        nums[idx] = prod(lst)
        lst[idx] = no

    return nums

#  Next try


def productExceptSelfv2(nums):
 # initialize product_before_a_number to an empty list
    product_before_a_number = []
    # start product_so_far to 1
    product_so_far = 1
    # BUILD THE LIST OF PRODUCT BEFORE EACH INDEX
    # loop through every number in nums
    for num in nums:
        # append to product_before_a_number the product of every number that
        # comes before it
        product_before_a_number.append(product_so_far)
        # set product_so_far to the product of current number and product_so_far
        product_so_far *= num
    # BUILD THE PRODUCT OF NUMBERS AFTER EACH INDEX
    # reset product_so_far to one
    product_so_far = 1
    # loop backwards for index of every number in nums starting from
    # index of last number
    for index in range(len(nums) - 1, -1, -1):
        # multiply the current product with the product of every number
        # that came after it.
        # That is, current product before each index multiplied by the product of numbers after the                 
        # index (product_so_far)
        product_before_a_number[index] *= product_so_far
        # set product_so_far to the product of current number and product_so_far
        product_so_far *= nums[index]
    # return product_before_a_number
    return product_before_a_number

print(productExceptSelfv2([1,2,3,4]))
