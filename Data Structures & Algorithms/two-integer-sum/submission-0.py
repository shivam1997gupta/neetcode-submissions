class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1,-1,-1):
                if i==j:
                    continue
                else:
                    if nums[i]+nums[j] == target:
                        if i<j:
                            return [i,j]
                        else:
                            return [j,i]