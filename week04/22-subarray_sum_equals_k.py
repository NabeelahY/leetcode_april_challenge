# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


def subarraySum(nums, k) -> int:
    if len(nums) == 0:
        return 0

    sums = {}
    curr = 0
    sumSub = 0

    for i in nums:
        curr += i
        if curr == k:
            sumSub += 1
        x = curr - k
        if curr - k in sums:
            sumSub += sums[x]

        if curr in sums:
            sums[curr] += 1
        else:
            sums[curr] = 1

    return sumSub

print(subarraySum([1,1,1], 2))
