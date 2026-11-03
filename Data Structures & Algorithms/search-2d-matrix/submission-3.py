class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // cols][mid % cols]

            if val == target:
                return True
            elif val < target:
                l=mid+1
            else:
                r=mid-1
            
            # same three cases as your binary search:
            # equal → True, too small → l = mid + 1, too big → r = mid - 1

        return False

