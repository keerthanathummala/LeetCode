'''You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.

 

Example 1:

Input: nums = [1,3,5,4,2,6]

Output: true

Explanation:

Pick p = 2, q = 4:

nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
nums[4...5] = [2, 6] is strictly increasing (2 < 6).'''
class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = 0
        
        # Phase 1: Strictly Increasing
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == 0: return False # Must have an initial increase
        
        # Phase 2: Strictly Decreasing
        p = i
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
        if i == p: return False # Must have a decrease
        
        # Phase 3: Strictly Increasing
        q = i
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == q: return False # Must have a final increase
        
        # Return true if we reached the end of the array
        return i == n - 1
            