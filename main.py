from interface import Interface
from api import Api_acceso


def main():
    board_flag = input("Usar el tablero predeterminado?, si, no: ")
    if board_flag == "si":
        board = ["53xx7xxxx",
                 "6xx195xxx",
                 "x98xxxx6x",
                 "8xxx6xxx3",
                 "4xx8x3xx1",
                 "7xxx2xxx6",
                 "x6xxxx28x",
                 "xxx419xx5",
                 "xxxx8xx79"]
    elif board_flag == "no":
        difficulty = input("Dificultad: 1, 2, 3: ")
        size = input("Tamaño: 4, 9: ")
        api = Api_acceso(difficulty, size)
        board = api.get_new_board()

    interface_sudoku = Interface(board)
    show_board(interface_sudoku.get_board())
    over = False

    while not over:
        number = input("number: ")
        Y = input("Y: ")
        X = input("X: ")
        board, over = interface_sudoku.play(number, X, Y)
        show_board(board)
    print("Felicidades, ha completado el juego")


def show_board(board):
    lines = [2, 5] if len(board) == 9 else [1]
    if len(board) == 9 or len(board) == 4:
        print_board(board, lines)
        print_X_coord(board, lines)
    else:
        print(board)


def print_X_coord(board, lines):
    coor_X = "\n     "
    for val in range(len(board)):
        coor_X += str(val + 1) + " "
        if val in lines:
            coor_X += "  "
    print(coor_X + " X")


def print_board(board, lines):
    print("Y")
    for index in range(len(board)):
        print(len(board) - index, "  ", formatted(board[index], lines))
        if index in lines:
            line = '    -'
            for __ in range(len(board) + lines[0]):
                line += "--"
            print(line)


def formatted(board_line, lines):
    new_board_line = []
    for idx, val in enumerate(board_line):
        x = val if val != 'x' else '_'
        new_board_line.append(x + " ")
        if idx in lines:
            new_board_line.append("| ")
    return "".join(new_board_line)


main()
