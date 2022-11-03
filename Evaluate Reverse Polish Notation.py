class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.insert(0,int(i))
            else:
                b, a = stack.pop(0), stack.pop(0)
                if i == "+":
                    stack.insert(0,a+b)
                elif i == "-":
                    stack.insert(0,a-b)
                elif i == "*":
                    stack.insert(0,a*b)
                else:
                    stack.insert(0,int(float(a)/b))
        return stack.pop(0)
