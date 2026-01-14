'''Example 1:

Input: a = "11", b = "1"
Output: "100"
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = int(a,2)+int(b,2)
        return format(result,'b')
        