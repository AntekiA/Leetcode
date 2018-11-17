import re        

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        min = -2147483648        
        max = 2147483647 
        chars='+-0123456789'
        str = str.strip()
        
        if not re.match(r'^(\-|\+)?\d+', str):
            return 0   
        
        
        i=1 if str[0] in chars[0:2] else 0
        
        while i < len(str) and str[i] in chars[2:]:
            i+=1
        
        res = int(str[:i])
        if min <= res <= max:
            return res
        elif res < min:
            return min
        else: 
            return max
