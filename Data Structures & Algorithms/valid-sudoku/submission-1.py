class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        allowed = set("123456789")
        for row in board:
            nums = [x for x in row if x != "."]
            if len(nums) != len(set(nums)) or not set(nums).issubset(allowed):
                return False
        
        for col in zip(*board):
            nums = [x for x in col if x != "."]
            if len(nums) != len(set(nums)) or not set(nums).issubset(allowed):
                return False
        

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                nums = []

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if board[r][c] != ".":
                            nums.append(board[r][c])

                if len(nums) != len(set(nums)):
                    return False
        
        return True
        