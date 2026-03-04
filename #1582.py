'''Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:


Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:


Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.'''
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        num_rows = len(mat)
        num_cols = len(mat[0])
      
        # Initialize arrays to store sum of each row and column
        row_sums = [0] * num_rows
        col_sums = [0] * num_cols
      
        # Calculate the sum of 1s in each row and column
        for i in range(num_rows):
            for j in range(num_cols):
                value = mat[i][j]
                row_sums[i] += value
                col_sums[j] += value
      
        # Count special positions
        special_count = 0
      
        # Check each position in the matrix
        for i in range(num_rows):
            for j in range(num_cols):
                # A position is special if:
                # 1. The value at position (i,j) is 1
                # 2. The sum of row i equals 1 (only one 1 in the row)
                # 3. The sum of column j equals 1 (only one 1 in the column)
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    special_count += 1
      
        return special_count
        