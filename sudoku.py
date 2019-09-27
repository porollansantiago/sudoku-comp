class Sudoku:
    def __init__(self, board):
        self.original_board = board
        self.board = board

    def game_is_over(self):
        self.over = True
        for x in range(len(self.board[0])):
            for y in range(len(self.board[0])):
                if self.board[x][y] == "x":
                    return False
        return True

    def place_number(self, number, X, Y):
        number = str(number)

        # comprobar si el lugar esta disponible
        if self.original_board[X][Y] != 'x':
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
        for x in range(block_X, block_X + 3):
            for y in range(block_Y, block_Y + 3):
                if self.board[x][y] == number:
                    return self.board

        # comprobar si se repite en la fila/columna
        for x in range(len(self.board[0])):
            if self.board[X][x] == number or self.board[x][Y] == number:
                return self.board

        # colocar el numero
        f = list(self.board[Y])
        f[X] = number
        s = ''.join(f)
        self.board[Y] = s

        return self.board
