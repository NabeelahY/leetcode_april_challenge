# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Example 1:

# Input: [5,7]
# Output: 4
# Example 2:

# Input: [0,1]
# Output: 0


# O(n) solution (not recommended)

def rangeBitwiseAnd(m: int, n: int) -> int:
    if m == 0:
        return 0
    i = m + 1
    result = m
    while i <= n:
        if result == 0:
            break
        result = result & i
        i += 1
    return result


# Best solution

def rangeBitwiseAnd2(m: int, n: int) -> int:
    count = 0
    while m < n:
        m = m >> 1
        n = n >> 1
        count += 1
    return m << count

print(rangeBitwiseAnd2(5,7))
