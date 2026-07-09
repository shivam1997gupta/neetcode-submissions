class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        l = 0
        best = 0
        for r in range(n):
            while s[r] in seen:      # duplicate → shrink from left
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best = max(best, r - l + 1)   # measure EVERY step
        return best
