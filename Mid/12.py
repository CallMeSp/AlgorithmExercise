class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        carry = 1
        roman = ''

        while num != 0:
            n = num % 10
            num //= 10
            if carry == 1:
                numeral_1 = 'I'
                numeral_5 = 'V'
                numeral_10 = 'X'
            elif carry == 10:
                numeral_1 = 'X'
                numeral_5 = 'L'
                numeral_10 = 'C'
            elif carry == 100:
                numeral_1 = 'C'
                numeral_5 = 'D'
                numeral_10 = 'M'
            else:
                numeral_1 = 'M'
                numeral_5 = ''
                numeral_10 = ''

            if 1 <= n <= 3:
                roman = numeral_1 * n + roman
            elif n == 4:
                roman = numeral_1 + numeral_5 + roman
            elif 5 <= n <= 8:
                roman = numeral_5 + numeral_1 * (n - 5) + roman
            elif n == 9:
                roman = numeral_1 + numeral_10 + roman

            carry *= 10

        return roman