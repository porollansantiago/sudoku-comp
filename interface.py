from sudoku import Sudoku


class Interface:
    def __init__(self):
        self.game = Sudoku(["53xx7xxxx",
                            "6xx195xxx",
                            "x98xxxx6x",
                            "8xxx6xxx3",
                            "4xx8x3xx1",
                            "7xxx2xxx6",
                            "x6xxxx28x",
                            "xxx419xx5",
                            "xxxx8xx79"])

    def play(self, number, X, Y):

        try:
            number, X, Y = int(number), int(X), int(Y)
        except ValueError:
            return "Solo se pueden ingresar numeros"

        if number not in range(1, 10):
            return "El numero va desde 1 a 9"
        if X not in range(0, 9) or Y not in range(0, 9):
            return "Las coordenadas van del 0 al 8"

        return self.game.place_number(str(number), str(X), str(Y))
