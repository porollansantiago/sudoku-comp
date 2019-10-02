from interface import Interface


def main():

    interface_sudoku = Interface()
    show_board(interface_sudoku.get_board())
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
