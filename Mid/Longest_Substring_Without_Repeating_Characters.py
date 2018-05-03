class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return 1
        letterSet=set([])
        maxLength=0
        for i in range(len(s)):
            letterSet.add(s[i])
            for j in range(i+1,len(s)):
                if s[j] in letterSet:
                    if maxLength<len(letterSet):
                        maxLength=len(letterSet)
                    letterSet.clear()
                    break
                else:
                    letterSet.add(s[j])
                    if maxLength<len(letterSet):
                        maxLength=len(letterSet)
        return maxLength
