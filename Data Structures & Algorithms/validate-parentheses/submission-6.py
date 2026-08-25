class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')','{':'}','[':']'}
        stack = []

        for i in s:
            if i in mapping:
                stack.append(i)
                continue
            if stack and i in [')','}',']'] and i == mapping.get(stack[-1]) :
                stack.pop()
            else:
                return False
        return len(stack)==0
    