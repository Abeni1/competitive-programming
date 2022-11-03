class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.insert(0,i)
            elif s[i] == ")":
                c = stack.pop(0)
                s = s[:c] + s[i-1: c:-1]+ s[i+1:]
                i -= 2
            i += 1
        return s
                
