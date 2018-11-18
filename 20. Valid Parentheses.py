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
