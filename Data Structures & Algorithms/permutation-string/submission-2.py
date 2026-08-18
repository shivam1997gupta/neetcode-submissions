class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        print(s1Count)
        print(s2Count)
        
        if s1Count == s2Count:
            return True
        
        for r in range(len(s1),len(s2)):
            index = ord(s2[r]) - ord('a')
            leftindex = ord(s2[r-len(s1)]) - ord('a')
            s2Count[index]+=1
            s2Count[leftindex]-=1
            if s1Count==s2Count:
                return True
        return False 


        # l=0
        # n = len(s2)
        # resultlong= 0
        # for r in range(n):
        #     if s2[r] not in s1:
        #         l=r
        #     else:
        #         resultlong = max(resultlong,r-l+1)
        # print(resultlong)
        # if resultlong>len(s1):
        #     return True
        # else:
        #     return False
        #     # while s2[r] not in s1:
        #     #     l+=1
                
        
        