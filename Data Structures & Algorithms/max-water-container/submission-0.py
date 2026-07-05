class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l = len(heights)
        # half = l//2
        # print(half)
        res = []
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                # print(i,j)
                width = j-i
                # print(width)
                length = min(heights[i],heights[j])
                vol = length * width
                res.append(vol)
        return max(res)