class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        try:
            for i in s:
                if i == '(' or i == '[' or i == '{':
                    stack.append(i)
                if i == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
                if i == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(i)
                if i == '}':
                    if stack[-1] == '{':
                        stack.pop()   
                    else:
                        stack.append(i)
            return not stack
        except:
            return bool(0)
        
class Solution_better:
    def isValid(self, s):
        stack = []
        dic = {')':'(', ']':'[', '}':'{'}
        for i, v in enumerate(s):
            if v in ['(','[','{']:
                stack.append(v)
            elif v in dic:
                if len(stack) > 0 and dic[v] == stack[-1]:
                    stack.pop()
                else:
                    return False # Closing wihle no parenthesis was open
        if stack != []:
            return False # Mismatch
        else:
            return True
