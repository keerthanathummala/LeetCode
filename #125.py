'''
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome
'''
#popular
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # lst = list(s.lower())
        # for i in range(len(s)):
        #     if not lst[i].isalnum():
        #         lst.pop(i)
            
        # return lst == lst[::-1]

        # time: O(n)
        # space: 0(1)
        l = 0
        r = len(s) -1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        # s = s.lower()

        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     if not s[left].isalnum():
        #         left += 1
        #     elif not s[right].isalnum():
        #         right -= 1 
        #     elif s[left] != s[right]:
        #         return False
        #     else:
        #         left += 1
        #         right -= 1
        # return True
        # '''
#mine
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=''.join(s)
        s= (s.replace(' ','')).lower()
        s=re.sub(r'[^a-zA-Z0-9]', '', s)
        s= list(s)
        n=len(s)
        for i in range(n/2):
            if s[i]!=s[n-i-1]:
                return False
        return True
        