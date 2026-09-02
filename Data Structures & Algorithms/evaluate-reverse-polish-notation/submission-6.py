class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ('+', '-', '*', '/'):
                stack.append(int(t))        # push numbers as ints
            else:
                b = stack.pop()             # second operand (top)
                a = stack.pop()             # first operand
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:                       # division
                    stack.append(int(a / b))
        return stack[0]