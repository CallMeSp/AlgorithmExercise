class Solution:
    def expandAround(self,str,left,right):
        L=left;R=right
        while((L>=0)and(R<len(str))and(str[L]==str[R])):       
            L-=1
            R+=1
        return R-L-1
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start=0;end=0
        for i in range(0,len(s)):
            len1=self.expandAround(s,i,i)
            len2=self.expandAround(s,i,i+1)
            maxlen=max(len1,len2)
            if maxlen>end-start:
                start=i-int((maxlen-1)/2)
                end=i+int(maxlen/2)
        return s[start:end+1]
x=Solution()
print(x.longestPalindrome('xgagsafdasfete'))
