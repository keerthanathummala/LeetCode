'''
Docstring for #3510
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

Example 1:

Input: nums = [5,2,3,1]

Output: 2

Explanation:

The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
The array nums became non-decreasing in two operations.'''
from sortedcontainers import SortedList
class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        inversionsCount = sum(nums[i + 1] < nums[i] for i in range(n - 1))
        nextIndices = [i + 1 for i in range(n)]
        prevIndices = [i - 1 for i in range(n)]
        pairSums = SortedList((a + b, i)
                            for i, (a, b) in enumerate(zip(nums, nums[1:])))
        while inversionsCount > 0:
            ans += 1
            smallestPair = pairSums.pop(0)
            pairSum, currIndex = smallestPair
            nextIndex = nextIndices[currIndex]
            prevIndex = prevIndices[currIndex]

            if prevIndex >= 0:
                oldPairSum = nums[prevIndex] + nums[currIndex]
                newPairSum = nums[prevIndex] + pairSum
                pairSums.remove((oldPairSum, prevIndex))
                pairSums.add((newPairSum, prevIndex))
                if nums[prevIndex] > nums[currIndex]:
                    inversionsCount -= 1
                if nums[prevIndex] > pairSum:
                    inversionsCount += 1

            if nums[nextIndex] < nums[currIndex]:
                inversionsCount -= 1

            nextNextIndex = nextIndices[nextIndex] if nextIndex < n else n
            if nextNextIndex < n:
                oldPairSum = nums[nextIndex] + nums[nextNextIndex]
                newPairSum = pairSum + nums[nextNextIndex]
                pairSums.remove((oldPairSum, nextIndex))
                pairSums.add((newPairSum, currIndex))
                if nums[nextNextIndex] < nums[nextIndex]:
                    inversionsCount -= 1
                if nums[nextNextIndex] < pairSum:
                    inversionsCount += 1
                prevIndices[nextNextIndex] = currIndex

            nextIndices[currIndex] = nextNextIndex
            nums[currIndex] = pairSum
        return ans