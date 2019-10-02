class Sudoku:
    def __init__(self, board):
        self.original_board = board[:]
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

    def place_number(self, number, X, Y):
        number = str(number)
        X = int(X)
        Y = int(Y)

        # comprobar si el lugar esta disponible
        if self.original_board[Y][X] != 'x':
            return self.board

        # comprobar si se repite en el bloque
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
        for y in range(block_Y, block_Y + 3):
            for x in range(block_X, block_X + 3):
                if self.board[y][x] == number:
                    return self.board

        # comprobar si se repite en la fila/columna
        for x in range(8):
            if self.board[Y][x] == number or self.board[x][X] == number:
                return self.board

        # colocar el numero
        f = list(self.board[Y])
        f[X] = number
        s = ''.join(f)
        self.board[Y] = s

        self.check_full_board()

        return self.board
