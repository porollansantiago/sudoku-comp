from sudoku import Sudoku


class Interface:
    def __init__(self, board):
        self.game = Sudoku(board)

    def play(self, number, X, Y):

        try:
            number, X, Y = int(number), int(X), int(Y)
        except ValueError:
            return "Solo se pueden ingresar numeros", self.game.game_is_over()

        if number not in range(1, 10):
            return "El numero va desde 1 a 9", self.game.game_is_over()
        if X not in range(0, 9) or Y not in range(0, 9):
            return "Las coordenadas van del 0 al 8", self.game.game_is_over()

        return (self.game.place_number(str(number), str(X), str(Y)),
                self.game.game_is_over())
