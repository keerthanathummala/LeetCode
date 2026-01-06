'''
Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = {}

        # Build frequency map
        for n in nums:
            if n in freq_map:
                freq_map[n] += 1
            else:
                freq_map[n] = 1

        # Sort the map by frequency (descending) and return top k keys
        sorted_nums = sorted(freq_map, key=lambda x: freq_map[x], reverse=True)
        return sorted_nums[:k]