# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4


def singleNumber(nums):
    counts = {}
    for i in nums:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    for key, val in counts.items():
        if val == 1:
            return key


print(singleNumber([4, 1, 2, 1, 2]))
