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
