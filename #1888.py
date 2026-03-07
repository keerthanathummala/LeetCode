'''ou are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
74,016/154.5K
Acceptance Rate
47.9%
Topics
icon
Companies
Hint 1
Note what actually matters is how many 0s and 1s are in odd and even positions
Hint 2
For every cyclic shift we need to count how many 0s and 1s are at each parity and convert the minimum between them for each parity
'''
class Solution:
    def minFlips(self, s: str) -> int:
            n = len(s)
      
            # Target pattern for alternating string starting with '0'
            target_pattern = "01"
        
            # Count mismatches when comparing s with pattern "010101..."
            # For each position i, check if s[i] matches the expected character
            mismatch_count = sum(char != target_pattern[i & 1] for i, char in enumerate(s))
        
            # The answer is minimum between:
            # 1. Flips needed for pattern "010101..." (mismatch_count)
            # 2. Flips needed for pattern "101010..." (n - mismatch_count)
            min_flips = min(mismatch_count, n - mismatch_count)
        
            # Simulate rotating the string by removing from front and adding to back
            # This handles the Type-1 operation (moving first char to end)
            for i in range(n):
                # Remove contribution of character at position i (as if it's moved to end)
                mismatch_count -= s[i] != target_pattern[i & 1]
            
                # Add contribution of the same character at its new position (i + n)
                mismatch_count += s[i] != target_pattern[(i + n) & 1]
            
                # Update minimum flips considering both alternating patterns
                min_flips = min(min_flips, mismatch_count, n - mismatch_count)
        
            return min_flips

            