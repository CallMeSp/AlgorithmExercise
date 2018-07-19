class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ans = 0
        start = 0
        sign = 0
        if str.isspace() is True:
            print(0)
        for i in str:
            if start == 0:
                if i.isspace() is True:
                    continue
                if i == '+':
                    sign = 1
                elif i == '-':
                    sign = -1
                elif i.isdigit() is True:
                    sign = 1
                    ans = ans * 10 + int(i)
                else:
                    break
                start = 1
            else:
                if i.isdigit() is True:
                    ans = ans * 10 + int(i)
                else:
                    break
        ans = sign * ans
        if ans >= 2147483647:
            return 2147483647
        elif ans <= -2147483648:
            return -2147483648
        else:
            return ans