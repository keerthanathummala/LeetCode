'''Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        string_length = len(s)
        total_possible_codes = 1 << k  # Calculate 2^k using bit shift
      
        # Early termination: if there aren't enough positions to generate all codes
        # We need at least 2^k different starting positions for substrings
        if string_length - k + 1 < total_possible_codes:
            return False
      
        # Generate all unique substrings of length k using set comprehension
        unique_substrings = {s[i:i + k] for i in range(string_length - k + 1)}
      
        # Check if we found all possible binary codes
        return len(unique_substrings) == total_possible_codes

        