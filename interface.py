from sudoku import Sudoku


class Interface:
    def __init__(self, board):
        self.board = board
        self.game = Sudoku(self.board)

    def play(self, number, X, Y):
        try:
            number, X, Y = int(number), int(X), int(Y)
        except ValueError:
            return "Solo se pueden ingresar numeros", self.game.game_is_over()
        Y = len(self.board) - Y
        X = X - 1
        if number not in range(1, len(self.board) + 1):
            return "El numero va desde 1 a 9", self.game.game_is_over()
        if X not in range(0, len(self.board)) or Y not in range(0, len(self.board)):
            return "Las coordenadas van del 1 al 9", self.game.game_is_over()
        return (self.game.place_number(str(number), str(X), str(Y)),
                self.game.game_is_over())

    def get_board(self):
        return self.game.board
