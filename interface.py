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
        return (self.format_board(self.game.place_number(str(number), X, Y)),
                self.game.game_is_over())

    def get_board(self):
        return self.format_board(self.game.board)

    def formatted_line(self, line, lines):
        new_board_line = []
        for idx, val in enumerate(line):
            x = val if val != 'x' else '_'
            new_board_line.append(x + " ")
            if idx in lines:
                new_board_line.append("| ")
        return "".join(new_board_line)

    def X_coords(self, board, lines):
        coor_X = "\n     "
        for val in range(len(board)):
            coor_X += str(val + 1) + " "
            if val in lines:
                coor_X += "  "
        return coor_X + " X"

    def format_board(self, board):
        new_board = ["Y"]
        lines = [2, 5] if len(board) == 9 else [1]
        for row_index, line in enumerate(board):
            new_board.append(str(str(len(board) - row_index) + "    " +
                             self.formatted_line(line, lines)))
            if row_index in lines:
                new_line = '    -'
                for __ in range(len(board) + lines[0]):
                    new_line += "--"
                new_board.append(new_line)
        new_board.append(self.X_coords(board, lines))
        return new_board
