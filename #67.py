'''Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''
from functools import reduce

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        int_result = reduce(lambda x, y: x * 10 + y, digits)
        int_result +=1
        res = list(map(int, str(int_result)))
        return res
