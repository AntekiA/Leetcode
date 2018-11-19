class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

class Solution_KMP(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        return self.kmp(haystack,needle)
        
    def makeNext(self,P):
        next = [0] * len(P)
        
        q = 1 # cursor in P, starting from 1
        k = 0 # k is the length of maximum common suffix and prefix
        
        while q < len(P):
            while k > 0 and P[q] != P[k]:
                k = next[k-1]
            if P[q] == P[k]:
                k+=1
            next[q] = k
            q +=1
        
        return next
            
    
    def kmp(self,T,P):
        
        next = self.makeNext(P)
        
        i = 0 #cursor in T
        q = 0 #cursor in P
        while i < len(T):
            while q > 0 and P[q] != T[i]:
                q = next[q-1]
            
            if T[i] == P[q]:
                q += 1
            
            if q == len(P):
                return i - len(P) + 1
            i+=1
        
        return -1

    
class Solution:
    """KMP solution"""
    def getNext(self, needle):
        length = len(needle)
        result = [-1]*length
        j, t = 0, -1
        while j < length-1:
            if t < 0 or needle[t] == needle[j]:
                j += 1
                t += 1
                result[j] = t
            else:
                t = result[t]
        return result
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nextTable = self.getNext(needle)
        hlength, nlength = len(haystack), len(needle)
        i, j, temp = 0, 0, None
        if hlength == 0 and nlength == 0:
            return 0
        while i < hlength and j < nlength:
            if needle[j] == haystack[i]:
                if temp == None:
                    temp = i
                i += 1
                j += 1
            else:
                if temp != None:
                    i = temp
                    temp = None
                i += (j - nextTable[j])
                j = 0
        if j == nlength:
            return i-nlength
        else:
            return -1
