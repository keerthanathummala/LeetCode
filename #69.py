'''Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
'''
import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.floor(pow(x,0.5)))
        