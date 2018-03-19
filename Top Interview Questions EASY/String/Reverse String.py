class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # first, last = 0, len(s) - 1
        # while first < last:
        #     s = s[:first] + s[last] + s[first + 1:last] + s[first] + s[last + 1:]
        #     first += 1
        #     last -= 1
        # return s
        
        return s[::-1]