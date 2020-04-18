# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


def minPathSum(grid) -> int:
    if len(grid) == 0:
        return 0
    matrix = []
    for _ in range(len(grid)):
        matrix.append([0] * len(grid[0]))

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] += grid[x][y]
            if x > 0 and y > 0:
                matrix[x][y] += min(matrix[x - 1][y], matrix[x][y - 1])
            elif x > 0:
                matrix[x][y] += matrix[x - 1][y]
            elif y > 0:
                matrix[x][y] += matrix[x][y - 1]

    return matrix[len(matrix) - 1][len(matrix[0]) - 1]


print(minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
