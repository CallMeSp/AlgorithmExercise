class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        s=str(x)
        l=len(s)
        while s[l-1]=='0':
            l-=1
        retstr=''
        if s[0]=='-':
            retstr='-'+s[1:l][::-1]
        else:
            retstr=s[:l][::-1]
        if int(retstr)>2**31-1 or int(retstr)<-2**31:
            return 0
        return   int(retstr)

x=Solution()
print(x.reverse(-2))