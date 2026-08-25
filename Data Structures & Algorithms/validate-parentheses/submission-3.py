class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')','{':'}','[':']'}
        stack = []

        for i in s:
            if i in mapping:                 # it's an opener
                stack.append(i)
            else:                            # it's a closer
                if not stack or i != mapping[stack[-1]]:
                    return False             # nothing to match, or wrong match
                stack.pop()
        return len(stack) == 0