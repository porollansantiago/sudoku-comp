import copy


class Sudoku:
    def __init__(self, board):
        if type(board[0]) is str:
            for val in range(len(board[0])):
                board[val] = list(board[val])
        self.original_board = copy.deepcopy(board)
        self.board = board
        self.over = False

    def game_is_over(self):
        return self.over

    def check_full_board(self):
        for x in range(len(self.board[0])):
            for y in range(len(self.board[0])):
                if self.board[x][y] == "x":
                    self.over = False
                    return
        self.over = True

    def get_block_number(self, X, Y, blocks):
        block_X = X // blocks
        block_Y = Y // blocks
        if block_X == 1:
            block_X += blocks - 1
        elif block_X == 2:
            block_X += ((blocks - 1) * 2)
        if block_Y == 1:
            block_Y += blocks - 1
        elif block_Y == 2:
            block_Y += ((blocks - 1) * 2)
        return block_Y, block_X

    def place_number(self, number, X, Y):
        # comprobar si el lugar esta disponible
        if self.original_board[Y][X] != 'x':
            return self.board

        # comprobar si se repite en el bloque
        blocks = 3 if len(self.board[0]) == 9 else 2
        block_Y, block_X = self.get_block_number(X, Y, blocks)
        for y in range(block_Y, block_Y + blocks):
            for x in range(block_X, block_X + blocks):
                if self.board[y][x] == number:
                    return self.board

        # comprobar si se repite en la fila/columna
        for x in range(len(self.board)):
            if self.board[Y][x] == number or self.board[x][X] == number:
                return self.board

        # colocar el numero
        self.board[Y][X] = number

        self.check_full_board()
        return self.board
