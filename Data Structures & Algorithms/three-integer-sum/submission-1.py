class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a>0:
                break
            if i>0 and nums[i-1]==a:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                cumsum = a + nums[l] + nums [r]
                if cumsum>0:
                    r-=1
                elif cumsum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1

                   
        print(res)
        return res