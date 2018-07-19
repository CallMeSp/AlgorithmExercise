class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        curstr=str(x)
        return curstr==curstr[::-1]