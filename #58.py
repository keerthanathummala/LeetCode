'''Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        s = list(s.split(" "))
        if  s == [""]:
            return 0
        n = len(s)
        return len(s[n-1])
        
        