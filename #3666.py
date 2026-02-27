'''You are given a binary string s, and an integer k.

In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.

Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.

 

Example 1:

Input: s = "110", k = 1

Output: 1

Explanation:

There is one '0' in s.
Since k = 1, we can flip it directly in one operation.
Example 2:

Input: s = "0101", k = 3

Output: 2

Explanation:

One optimal set of operations choosing k = 3 indices in each operation is:

Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".
Thus, the minimum number of operations is 2.'''
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # O(n) time complexity
        # O(1) space complexity

        n = len(s)
        z = s.count('0')
        
        if n == k:
            if z == 0:
                return 0
            elif z == n:
                return 1
            else:
                return -1
        
        def ceil(x, y):
            return (x + y - 1) // y
        
        ans = inf
        
        if z % 2 == 0:
            m = max(ceil(z, k), ceil(z, n - k))
            if m % 2 == 1:
                m += 1
            ans = min(ans, m)
        
        if z % 2 == k % 2:
            m = max(ceil(z, k), ceil(n - z, n - k))
            if m % 2 == 0:
                m += 1
            ans = min(ans, m)
        
        return ans if ans < inf else -1