class Solution:
    def noe(self, stk, pf, nf, df, ef, e_f):
        cha_1 = r'e+-.'
        if len(stk) == 1:
            for i in stk:
                if i in cha_1:
                    return False
        if pf + nf > 1:
            return False
        elif df > 1:
            return False
        elif pf == 1 and stk[0] != '+':
            return False
        elif nf == 1 and stk[0] != '-':
            return False
        elif ef == 1 and df == 1 and e_f == 0:
            return False
        else:
            return True
        
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cha = r'0123456789e+-.'
        e_idx = -1
        pf = 0
        nf = 0
        df = 0
        pfe = 0
        nfe = 0
        dfe = 0
        stk = []
        s = s.split()
        if len(s) > 1 or len(s) == 0:
            return False
        if len(s[0]) == 1 and not s[0].isdigit():
            return False
        for i in s[0]:
            if i in cha:
                stk.append(i)
                if i == 'e':
                    if e_idx == -1:
                        e_idx = s[0].index('e')
                    else:
                        return False
                    if e_idx == 0 or e_idx == len(s[0])-1:
                        return False
                if i == '+':
                    if e_idx == -1:
                        pf += 1
                    else:
                        pfe += 1
                if i == '-':
                    if e_idx == -1:
                        nf += 1
                    else:
                        nfe += 1
                if i == '.':
                    if e_idx == -1:
                        df += 1
                    else:
                        dfe += 1
            else:
                return False
        # print(stk)
        if e_idx == -1:
            if pf + nf + df == len(stk):
                return False
            else:
                return self.noe(stk, pf, nf, df, ef=0, e_f=-1)
        else:
            if pf + nf + df + pfe + nfe + dfe + 1 == len(stk):
                return False
            else:
                return self.noe(stk[0:e_idx], pf, nf, df, ef=1, e_f=1) and \
                       self.noe(stk[e_idx+1:len(stk)], pfe, nfe, dfe, ef=1, e_f=0)
