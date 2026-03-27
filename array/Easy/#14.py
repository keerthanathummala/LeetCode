'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count=0
        common = strs[0]

        for j in range(len(strs)-1):
            first = strs[j]
            second = strs[j+1]
            minimum = min(len(first),len(second))

            while minimum != 0:
                if (second[:minimum]) == (common[:minimum]):
                    common = common[:minimum]
                    count+=1 
                    minimum =0
                else:
                    minimum -=1
                    
        if count == (len(strs) -1):          
            return common
        else:
            return ""
