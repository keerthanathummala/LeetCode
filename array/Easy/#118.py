'''Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [[]]
        # Initialize Pascal's triangle with the first row [1]
        triangle = [[1]]
      
        # Generate each subsequent row
        for row_index in range(numRows - 1):
            # Create new row starting with 1
            # Add sums of adjacent pairs from previous row
            # End with 1
            current_row = [1]
          
            # Get the last row from triangle
            previous_row = triangle[-1]
          
            # Calculate middle elements by summing adjacent pairs
            for j in range(len(previous_row) - 1):
                current_row.append(previous_row[j] + previous_row[j + 1])
          
            # Add trailing 1
            current_row.append(1)
          
            # Add the completed row to triangle
            triangle.append(current_row)
      
        return triangle