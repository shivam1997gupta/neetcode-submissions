class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        l ,r = 0, len(matrix[0]) - 1
        for i in matrix:
            
            if target<=i[-1]:
                while l<=r:
                    mid = (r+l)//2
                    if i[mid] == target:
                        return True
                    elif i[mid]<target:
                        l=mid+1
                    else:
                        r=mid-1
                l ,r = 0,len(matrix[0]) - 1
        return False

