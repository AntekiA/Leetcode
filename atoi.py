class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """ 
        str = str.strip()
        if len(str) == 0:
            return 0
        min = -2147483648        
        max = 2147483647
        chars='+-0123456789'
        i = 0
        if str[0] not in chars:
            return 0
        if str[0] == '-' or str[0] == '+':
            i = 1
        while i < len(str) and str[i] in chars[2:]:
            i += 1
        try:
            res = int(str[:i])
            if min <= res <= max:
                return res
            elif res < min:
                return min
            else: 
                return max
        except:
            return 0 
        
