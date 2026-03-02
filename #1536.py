'''
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

Example 1:


Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Example 2:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:


Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
grid[i][j] is either 0 or 1
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
34,947/59K
Acceptance Rate
59.2%
Topics
icon
Companies
Hint 1
For each row of the grid calculate the most right 1 in the grid in the array maxRight.
Hint 2
To check if there exist answer, sort maxRight and check if maxRight[i] ≤ i for all possible i's.
Hint 3
If there exist an answer, simulate the swaps.'''
class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
      
        # Find the rightmost 1 position in each row
        # This tells us how many trailing zeros each row has
        rightmost_one_positions = [-1] * n
      
        for row_idx in range(n):
            for col_idx in range(n - 1, -1, -1):
                if grid[row_idx][col_idx] == 1:
                    rightmost_one_positions[row_idx] = col_idx
                    break
      
        total_swaps = 0
      
        # For each row position, find a suitable row that can be placed there
        for target_row in range(n):
            # Find the first row from current position onwards that can fit
            # A row can fit at position i if its rightmost 1 is at position <= i
            suitable_row_idx = -1
          
            for candidate_row in range(target_row, n):
                if rightmost_one_positions[candidate_row] <= target_row:
                    # Found a suitable row
                    total_swaps += candidate_row - target_row
                    suitable_row_idx = candidate_row
                    break
          
            # If no suitable row found, it's impossible to form upper triangular matrix
            if suitable_row_idx == -1:
                return -1
          
            # Bubble the suitable row up to the target position
            # This simulates the actual row swaps
            while suitable_row_idx > target_row:
                rightmost_one_positions[suitable_row_idx], rightmost_one_positions[suitable_row_idx - 1] = \
                    rightmost_one_positions[suitable_row_idx - 1], rightmost_one_positions[suitable_row_idx]
                suitable_row_idx -= 1
      
        return total_swaps