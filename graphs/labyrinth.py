"""
You are given a map of a labyrinth, and your task is to find a path from start to end. You can walk left, right, up and down.
Input
The first input line has two integers n and m: the height and width of the map.
Then there are n lines of m characters describing the labyrinth. Each character is . (floor), # (wall), A (start), or B (end). There is exactly one A and one B in the input.
Output
First print "YES", if there is a path, and "NO" otherwise.
If there is a path, print the length of the shortest such path and its description as a string consisting of characters L (left), R (right), U (up), and D (down). You can print any valid solution.
Constraints

1 <= n,m <= 1000

Example
Input:
5 8
########
#.A#...#
#.##.#B#
#......#
########

Output:
YES
9
LDDRRRRRU
"""
from collections import deque

def solve_labyrinth(grid):
    n = len(grid)
    m = len(grid[0])
    
    # 1. Find the starting point 'A' and ending point 'B'
    start = None
    end = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'B':
                end = (i, j)

    # Move deltas mapped to their direction characters
    # (row_change, col_change): "Direction"
    moves = {
        (-1, 0): "U",
        (1, 0): "D",
        (0, -1): "L",
        (0, 1): "R"
    }

    # 2. Setup BFS tracking structures
    # visited keeps track of visited cells
    visited = [[False] * m for _ in range(n)]
    
    # parent stores where we came from: (prev_row, prev_col, direction_char)
    parent = [[None] * m for _ in range(n)]
    
    # Queue stores coordinates: (row, col)
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    found = False

    # 3. Standard BFS loop
    while queue:
        r, c = queue.popleft()        
        if (r, c) == end:
            found = True
            break            
        for (dr, dc), move_char in moves.items():
            nr, nc = r + dr, c + dc
            
            # Check boundaries, obstacles, and visited status
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    parent[nr][nc] = (r, c, move_char)
                    queue.append((nr, nc))

    # 4. Process and print output
    if not found:
        print("NO")
        return

    print("YES")
    
    # Reconstruct the path backwards from 'B' to 'A'
    path_chars = []
    curr = end
    while curr != start:
        prev_r, prev_col, move_char = parent[curr[0]][curr[1]]
        path_chars.append(move_char)
        curr = (prev_r, prev_col)
        
    # Reverse path since we tracked it backwards
    path_chars.reverse()
    
    print(len(path_chars))
    print("".join(path_chars))

# Test Example
grid = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', 'A', '#', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '.', '#', 'B', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

solve_labyrinth(grid)
