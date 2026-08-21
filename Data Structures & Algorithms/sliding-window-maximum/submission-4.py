from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()      # holds indices, values decreasing front→back
        result = []
        for r in range(len(nums)):
            # 1. pop smaller values from the back
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            # 2. add current index
            dq.append(r)
            # 3. remove front if out of window
            if dq[0] <= r - k:
                print(nums[dq[0]])
                dq.popleft()
            # 4. record max once first window is filled
            if r >= k - 1:
                result.append(nums[dq[0]])
        return result