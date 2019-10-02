import unittest
from sudoku import Sudoku


class Test_sudoku(unittest.TestCase):
    def setUp(self):
        self.orig_board = (["53xx7xxxx",
                            "6xx195xxx",
                            "x98xxxx6x",
                            "8xxx6xxx3",
                            "4xx8x3xx1",
                            "7xxx2xxx6",
                            "x6xxxx28x",
                            "xxx419xx5",
                            "xxxx8xx79"])
        self.game = Sudoku(self.orig_board)

    def test_place_invalid_number1(self):
        number, Y, X = 1, 0, 0
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_block(self):
        number, Y, X = 1, 3, 0
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_block2(self):
        number, Y, X = 8, 1, 1
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_block3(self):
        number, Y, X = 2, 7, 7
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))        
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_block4(self):
        number, Y, X = 2, 3, 3
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_col(self):
        number, Y, X = 1, 3, 3
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_col1(self):
        number, Y, X = 9, 4, 4
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_col2(self):
        number, Y, X = 6, 7, 7
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_row(self):
        number, Y, X = 9, 1, 1
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))        
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_row1(self):
        number, Y, X = 4, 4, 4
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_invalid_number_row2(self):
        number, Y, X = 4, 7, 7
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_valid_number1(self):
        number, Y, X = 2, 1, 1
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "62x195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_valid_number2(self):
        number, Y, X = 5, 4, 4
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx853xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_valid_number3(self):
        number, Y, X = 3, 7, 7
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419x35",
                                     "xxxx8xx79"])

    def test_game_not_over(self):
        over = self.game.game_is_over()
        self.assertFalse(over)

    def test_game_not_over_after_play(self):
        number, Y, X = 1, 0, 2
        self.game.place_number(number, X, Y)
        over = self.game.game_is_over()
        self.assertFalse(over)

    def test_game_over_after_play(self):
        full_board = Sudoku(["534678912",
                             "672195348",
                             "198342567",
                             "859761423",
                             "426853791",
                             "713924856",
                             "961537284",
                             "287419635",
                             "34528617x"])
        number, Y, X = 9, 8, 8
        full_board.place_number(number, X, Y)
        over = full_board.game_is_over()
        self.assertTrue(over)

    def test_replace_placed_number1(self):
        number, Y, X = 7, 2, 6
        board = self.game.place_number(number, X, Y)
        number, Y, X = 5, 2, 6
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxx56x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_replace_placed_number2(self):
        number, Y, X = 2, 3, 5
        board = self.game.place_number(number, X, Y)
        number, Y, X = 1, 3, 5
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx61xx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_replace_placed_number3(self):
        number, Y, X = 5, 8, 1
        new_board = self.game.place_number(number, X, Y)
        number, Y, X = 4, 8, 1
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "x4xx8xx79"])


if __name__ == "__main__":
    unittest.main()
