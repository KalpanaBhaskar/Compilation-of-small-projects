'''
Minimize the Maximum Weighted Meeting Distance

You are given an m x n integer matrix grid where grid[i][j] represents the weight of a person located at cell (i, j). If grid[i][j] == 0, it means there is no person at that cell.

You want to organize a meeting at some valid cell (x, y) on the grid. The meeting point can be chosen on any cell, regardless of whether it is currently empty or occupied.

The weighted Manhattan distance that a person at cell (r, c) must travel to reach the meeting point (x, y) is defined as: grid[r][c] * (|r - x| + |c - y|)

Return the minimum possible value of the maximum distance any person has to travel to reach the meeting point.

Example 1:
Input: grid = [[2,0,3],[0,5,0],[1,0,4]] Output: 6 Explanation: If we choose the meeting point at (1, 2), the distances for each person are:

Person at (0, 0): 2 * (|0 - 1| + |0 - 2|) = 2 * 3 = 6

Person at (0, 2): 3 * (|0 - 1| + |2 - 2|) = 3 * 1 = 3

Person at (1, 1): 5 * (|1 - 1| + |1 - 2|) = 5 * 1 = 5

Person at (2, 0): 1 * (|2 - 1| + |0 - 2|) = 1 * 3 = 3

Person at (2, 2): 4 * (|2 - 1| + |2 - 2|) = 4 * 1 = 4

The maximum distance any person travels is 6. It can be shown that no other meeting point yields a smaller maximum distance.

Example 2:
Input: grid = [[1,0],[0,1]] Output: 1 Explanation: Choosing the meeting point at (0, 0):

Person at (0, 0): 1 * 0 = 0

Person at (1, 1): 1 * 2 = 2 (Max is 2) Choosing the meeting point at (0, 1):

Person at (0, 0): 1 * 1 = 1

Person at (1, 1): 1 * 1 = 1 (Max is 1) The minimum possible maximum distance is 1.

Constraints:
m == grid.length

n == grid[i].length

1 <= m, n <= 1000

0 <= grid[i][j] <= 10^4
'''

class Solution:
    def maxWeightedDistance(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])

        mx = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    dist = grid[i][j] * (abs(i - x) + abs(j - y))
                    mx = max(mx, dist)
        return mx

    def minValofMaxDist(self, grid):
        n = len(grid)
        m = len(grid[0])

        ans = float("inf")

        for x in range(n):
            for y in range(m):
                ans = min(ans, self.maxWeightedDistance(grid, x, y))

        return ans
    
if __name__ == "__main__":
    solution = Solution()
    