from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        for r in range(len(nums)):
            while dq and nums[r] >= nums[dq[-1]] :
                dq.pop()
            dq.append(r)
            if dq[0] <= r-k:
                dq.popleft()
            if r>=k-1:
                result.append(nums[dq[0]])
        return result
