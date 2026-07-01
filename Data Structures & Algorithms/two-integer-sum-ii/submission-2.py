class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        start = 0
        end = len(numbers)-1

        while (numbers[start]+numbers[end])!=target:
            sum2 = numbers[start]+numbers[end]
            if sum2<target:
                start+=1
            elif sum2>target:
                end-=1
            else:
                return [start+1,end+1] 
        return [start+1,end+1]