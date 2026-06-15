class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result= {}
        for word in strs:
            temp = [0]*26
            for char in word:
                temp[ord(char)-ord("a")]+=1
            if result.get(tuple(temp),[]) == []:
                result[tuple(temp)] = [word]
            else:
                result[tuple(temp)].append(word)

        return list(result.values())