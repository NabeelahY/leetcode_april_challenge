# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


# Solution 1

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def deleteOnes(grid, i, j, rows, cols):
    q = Queue()
    q.enqueue([i, j])
    grid[i][j] = '0'

    while q.size() > 0:
        node = q.dequeue()
        row = node[0]
        col = node[1]
        for row2, col2 in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if 0 <= row2 < rows and 0 <= col2 < cols and grid[row2][col2] != '0':
                grid[row2][col2] = '0'
                q.enqueue([row2, col2])


def numIslands(grid) -> int:
    if len(grid) == 0:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                deleteOnes(grid, i, j, rows, cols)
                count += 1

    return count


islands = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
           ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

print(numIslands(islands))


# Solution 2

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def get_neighbors(x, y, grid):
    neighbors = []

    if x > 0 and grid[y][x - 1] == '1':
        neighbors.append((x - 1, y))
    if x < len(grid[0]) - 1 and grid[y][x + 1] == '1':
        neighbors.append((x + 1, y))
    if y > 0 and grid[y - 1][x] == '1':
        neighbors.append((x, y - 1))
    if y < len(grid) - 1 and grid[y + 1][x] == '1':
        neighbors.append((x, y + 1))

    return neighbors


def dft(x, y, grid, visited):
    s = Stack()
    s.push((x, y))

    while s.size() > 0:
        v = s.pop()

        x = v[0]
        y = v[1]

        if not visited[y][x]:
            visited[y][x] = True

            for neighbor in get_neighbors(x, y, grid):
                s.push(neighbor)

    return visited


def numIslands2(grid) -> int:
    if len(grid) == 0:
        return 0

    visited = []
    for _ in range(len(grid)):
        visited.append([False] * len(grid[0]))

    island_count = 0

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if not visited[j][i]:
                if grid[j][i] == '1':
                    visited = dft(i, j, grid, visited)
                    island_count += 1
                else:
                    visited[j][i] = True

    return island_count


islands = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
           ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(numIslands2(islands))
