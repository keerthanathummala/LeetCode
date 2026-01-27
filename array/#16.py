'''Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        '''
        # Sort the array to use the two-pointer technique
        nums.sort()
        n = len(nums)
        # Initialize with a sum from the first three elements
        closest_sum =float('inf')
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                sums = nums[i]+nums[left]+nums[right]
                if abs(target-sums) < abs(target-closest_sum):
                    closest_sum = sums
                
                if sums>target:
                    right-=1
                elif sums<target:
                    left+=1
        return closest_sum'''
        # Sort the array to use the two-pointer technique
        nums.sort()
        n = len(nums)
        # Initialize with a sum from the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # Optional: Skip duplicate values for the first element to save time
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we found the exact target, return it immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if the current_sum is nearer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on how current_sum compares to target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum