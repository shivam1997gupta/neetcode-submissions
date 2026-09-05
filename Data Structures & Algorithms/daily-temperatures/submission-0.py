class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0]*len(temperatures)
        stack = [] #pair of temperature,index
        for index, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                result[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
            stack.append([t,index])

        return result