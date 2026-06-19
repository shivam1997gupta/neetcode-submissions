class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lenword = []
        for word in strs:
            lenword.append(str(len(word)))
            lenword.append(",")
        lenword.append("#")
        lenword.extend(strs)
        print(''.join(lenword))
        return ''.join(lenword)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        nums = []
        while s[i]!='#':
            j=i
            while s[j]!=',':
                j+=1
            if s[i:j]:
                nums.append(int(s[i:j]))
            i=j+1
        
            
        onlywords = s[j+2:]
        print(onlywords)
        print(nums)
        result = []
        start=0
        end = 0
        for index in nums:
            start = end
            end = end + index
            # print(start,end)
            result.append(onlywords[start:end])

        return result

        