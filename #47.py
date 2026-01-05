'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}

        for word in strs:
            key = "".join(sorted(word))  # sorted version becomes the key
            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = [word]

        return list(anagram_map.values())
