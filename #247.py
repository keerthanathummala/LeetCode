'''
Input: s = "anagram", t = "nagaram"

Output: true'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_s = list(s)
        sorted_t = list(t)

        sorted_s.sort()
        sorted_t.sort()

        return sorted_s == sorted_t