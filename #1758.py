'''You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".'''
class Solution:
    def minOperations(self, s: str) -> int:
        # Count operations needed to match pattern starting with '0'
        # Pattern: '0' at even indices, '1' at odd indices (0101...)
        operations_start_with_zero = 0
      
        for index, char in enumerate(s):
            # Determine expected character based on index parity
            # Even index -> '0', Odd index -> '1'
            expected_char = '01'[index & 1]  # Bitwise AND with 1 gives 0 for even, 1 for odd
          
            # Count mismatch if current character doesn't match expected
            if char != expected_char:
                operations_start_with_zero += 1
      
        # The other pattern (starting with '1') would need the remaining operations
        # Total operations for pattern '1010...' = len(s) - operations for '0101...'
        operations_start_with_one = len(s) - operations_start_with_zero
      
        # Return minimum operations needed for either pattern
        return min(operations_start_with_zero, operations_start_with_one)