class Solution:
    def trap(self, height: List[int]) -> int:
        # vol = 0
        # result = {}
        # lmax= []
        # rmax = []
        # for i in range(len(height)):
        #     if i ==0 or i == (len(height)-1):
        #         lmax.append(0)
        #         rmax.append(0)
        #     for j in range(i):
        #         if height[j]>=height[i]:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n

     
        for i in range(n):
            if i == 0:
                maxLeft[i] = height[i]
            else:
                maxLeft[i] = max(height[i],maxLeft[i-1])
        for i in range(n-1,-1,-1):
            if i == n-1:
                maxRight[i] = height[i]
            else:
                maxRight[i] = max(height[i],maxRight[i+1])

        print(maxLeft)
        print(maxRight)
   
        vol = 0
        for i in range(n):
            vol += min(maxLeft[i], maxRight[i]) - height[i]
        return vol