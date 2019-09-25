class Sudoku:
    def __init__(self, board):
        self.original_board = board
        self.board = board
        self.over = False
        
    
    def game_is_over(self):
        self.over = True
        for x in range(len(self.board[0])):
            for y in range(len(self.board[0])):
                 if self.board[x][y] == "x":
                     self.over = False
                     break
        return self.over

    def place_number(self, number, X, Y):
        number = str(number)
        if self.original_board[X][Y] != 'x':
            return False

        block_X = X // 3
        block_Y = Y // 3
        if block_X == 1:
            block_X += 2
        if block_Y == 1:
            block_Y += 2
        if block_X == 2:
            block_X += 4
        if block_Y == 2:
            block_Y += 4
        
        for x in range(block_X, block_X + 3):
            for y in range(block_Y, block_Y + 3):
                if self.board[x][y] == number:
                    return False

        f = list(self.board[X])
        f[Y] = number
        s = ''.join(f)
        self.board[X] = s

        return True
            


