class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0 
        ans = 0
        mostf = 0 
        n = len(s)
        for r in range(n):
            count[s[r]] = 1 + count.get(s[r],0)
            mostf = max(mostf, count[s[r]])
            while (r-l+1) - mostf > k:
                count[s[l]] -= 1
                l+=1
            ans = max(ans, r-l+1)

        return ans