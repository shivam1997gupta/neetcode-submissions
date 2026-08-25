class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')','{':'}','[':']'}
        stack = []

        for i in s:
            if i in mapping:                 # opener → push, done
                stack.append(i)
            else:                            # closer → must match
                if not stack or i != mapping[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0
    