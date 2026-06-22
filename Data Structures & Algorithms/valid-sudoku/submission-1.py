class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in range(9):
            temp = []
            for j in range(9):
                if board[i][j].isdigit():
                    temp.append(board[i][j])
            if len(set(temp)) != len(temp):
                return False
        for i in range(9):
            temp = []
            for j in range(9):
                if board[j][i].isdigit():
                    temp.append(board[j][i])
            if len(set(temp)) != len(temp):
                return False
        
        # print(temp)
        for maj in range(9):
            temp = []
            for i in range(3):
                for j in range(3):
                    row = (maj//3) * 3 + i
                    col = (maj%3) * 3 + j
                    if board[row][col].isdigit():
                        temp.append(board[row][col])
            if len(set(temp)) != len(temp):
                return False
        return True
                
                