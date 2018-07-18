class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        retDic={}
        isDown=True
        for i in range(numRows):
            retDic[i]=''
        for j in range(len(s)):
            if j%(2*numRows-2)==0:
                isDown=True
            elif (j%(2*numRows-2)==int(numRows-1)):
                isDown=False

            if isDown:
                k=j%(2*numRows-2)
            else:
                k=2*numRows-2-j%(2*numRows-2)
            retDic[k]+=s[j]
        retstr=''
        for m in range(numRows):
            retstr+=retDic[m]
        return retstr
        

x=Solution()
print(x.convert('PAYPALISHIRING',3))