class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        chars = {'(':')','{':'}', '[':']'}
        
        for i in s:
            if i in chars:
                stack.insert(0,i)
            elif stack and chars[stack[0]] == i:
                    stack.pop(0)
            else:
                return False
        return not stack
