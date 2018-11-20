class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        if len(s) == 0:
            return True
        i = 0
        j = len(s)-1
        while j > i :
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1 
            if s[i].isalnum() and s[j].isalnum():
                if s[i] == s[j] :                        
                    i += 1
                    j -= 1
                else:
                    return False
        return True

def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^a-zA-Z0-9]', '', s)
        return s.lower() == s[::-1].lower()
