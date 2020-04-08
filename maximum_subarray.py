# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def maxSubArray(nums):
    maxSum = 0
    maxEnd = 0
    for i in nums:
        maxEnd += i

        if maxEnd < 0:
            maxEnd = 0
        if maxEnd > maxSum:
            maxSum = maxEnd
    if maxSum == 0 and 0 not in nums:
        return max(nums)

    return maxSum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
