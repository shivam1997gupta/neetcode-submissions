class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT={}
        if not t or not s:
            return ""

        for i in t:
            countT[i] = 1 + countT.get(i,0)
        # print(countT)
        have, need = 0, len(countT)
        l = 0
        resStart = 0
        reslen=float("inf")
        window = {}
        for r in range(len(s)):
            item = s[r]
            window[item] = 1 + window.get(item,0)
            if item in countT and window[item] == countT[item]:
                have+=1
            while have==need:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    resStart = l

                leftitem = s[l]
                window[leftitem] -=1
                if leftitem in countT and window[leftitem]<countT[leftitem]:
                    have-=1
                l+=1
        return s[resStart : resStart + reslen] if reslen != float("inf") else ""

