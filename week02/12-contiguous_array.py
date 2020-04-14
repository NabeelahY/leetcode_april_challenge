# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

# This youtube video helped https://youtu.be/nSEO5zOwP7g


def findMaxLength(nums) -> int:
    if len(nums) == 0:
        return 0

    maxLen = 0
    tempAns = 0
    counts = {0: -1}

    for idx, no in enumerate(nums):
        if no == 1:
            tempAns += 1
        else:
            tempAns -= 1

        if tempAns not in counts.keys():
            counts[tempAns] = idx

        else:
            if idx - counts[tempAns] > maxLen:
                maxLen = idx - counts[tempAns]

    return maxLen
