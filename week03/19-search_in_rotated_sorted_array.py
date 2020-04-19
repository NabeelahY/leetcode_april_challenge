# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


def search(nums, target) -> int:
    first = 0
    last = len(nums) - 1

    while first < last:
        mid = (first + last)//2
        if nums[mid] > nums[last]:
            first = mid + 1
        else:
            last = mid

    rot = first

    first = 0
    last = len(nums) - 1
    while first <= last:
        mid = (first + last)//2
        actual_mid = (mid+rot) % len(nums)
        if nums[actual_mid] == target:
            return actual_mid
        if nums[actual_mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return -1

print(search([4,5,6,7,0,1,2], 0))
