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
    def getnext(self, N):
        p = 1
        k = 0
        n = [0] * len(N)
        while p < len(N):
            while k > 0 and N[p] != N[k]:
                k = n[k - 1]
            if N[p] == N[k]:
                k += 1
            n[p] = k
            p += 1
        return n
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        next_ = self.getnext(needle)
        p = 0
        k = 0
        while p < len(haystack):
            while k > 0 and needle[k] != haystack[p]:
                k = next_[k - 1]
            if needle[k] == haystack[p]:
                k += 1
            if k == len(needle):
                return p - k + 1
            p += 1
        return -1 
