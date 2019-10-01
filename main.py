from interface import Interface


def main():
    board = ["53xx7xxxx",
             "6xx195xxx",
             "x98xxxx6x",
             "8xxx6xxx3",
             "4xx8x3xx1",
             "7xxx2xxx6",
             "x6xxxx28x",
             "xxx419xx5",
             "xxxx8xx79"]

    interface_sudoku = Interface(board)
    show_board(board)
    over = False

    while not over:
        number = input("number: ")
        Y = input("Y: ")
        X = input("X: ")
        board, over = interface_sudoku.play(number, X, Y)
        show_board(board)


def show_board(board):
    if len(board) == 9:
        for line in board:
            print(line)
    else:
        print(board)


main()
