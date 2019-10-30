import unittest
from sudoku import Sudoku
from parameterized import parameterized


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
        self.orig_board_44 = (["x2xx",
                               "3xx1",
                               "x32x",
                               "4xxx"])
        self.game = Sudoku(self.orig_board)
        self.game44 = Sudoku(self.orig_board_44)

    @parameterized.expand([
        ("1", 0, 0),
        ("1", 3, 0),
        ("8", 1, 1),
        ("2", 7, 7),
        ("2", 3, 3),
        ("6", 8, 2),
        ("6", 0, 6),
    ])
    def test_place_invalid_number_block(self, number, Y, X):
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

    @parameterized.expand([
        ("1", 3, 3),
        ("9", 4, 4),
        ("6", 7, 7),
        ("5", 6, 0),
        ("7", 6, 0),
        ("5", 8, 0),
        ("8", 7, 0)
    ])
    def test_place_invalid_number_col(self, number, Y, X):
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

    @parameterized.expand([
        ("9", 1, 1),
        ("4", 4, 4),
        ("4", 7, 7),
        ("5", 0, 7),
        ("3", 0, 7),
        ("7", 0, 6),
        ("7", 0, 8),
    ])
    def test_place_invalid_number_row(self, number, Y, X):
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

    @parameterized.expand([
        ("2", 1, 1, ["53xx7xxxx",
                     "62x195xxx",
                     "x98xxxx6x",
                     "8xxx6xxx3",
                     "4xx8x3xx1",
                     "7xxx2xxx6",
                     "x6xxxx28x",
                     "xxx419xx5",
                     "xxxx8xx79"]),
        ("5", 4, 4, ["53xx7xxxx",
                     "6xx195xxx",
                     "x98xxxx6x",
                     "8xxx6xxx3",
                     "4xx853xx1",
                     "7xxx2xxx6",
                     "x6xxxx28x",
                     "xxx419xx5",
                     "xxxx8xx79"]),
        ("3", 7, 7, ["53xx7xxxx",
                     "6xx195xxx",
                     "x98xxxx6x",
                     "8xxx6xxx3",
                     "4xx8x3xx1",
                     "7xxx2xxx6",
                     "x6xxxx28x",
                     "xxx419x35",
                     "xxxx8xx79"]),
        ("2", 0, 8, ["53xx7xxx2",
                     "6xx195xxx",
                     "x98xxxx6x",
                     "8xxx6xxx3",
                     "4xx8x3xx1",
                     "7xxx2xxx6",
                     "x6xxxx28x",
                     "xxx419xx5",
                     "xxxx8xx79"]),
        ("2", 8, 0, ["53xx7xxxx",
                     "6xx195xxx",
                     "x98xxxx6x",
                     "8xxx6xxx3",
                     "4xx8x3xx1",
                     "7xxx2xxx6",
                     "x6xxxx28x",
                     "xxx419xx5",
                     "2xxx8xx79"]),
    ])
    def test_place_valid_number(self, number, Y, X, expected):
        board = self.game.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, expected)

    def test_game_not_over(self):
        over = self.game.game_is_over()
        self.assertFalse(over)

    def test_game_not_over_after_play(self):
        number, Y, X = "1", 0, 2
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
        number, Y, X = "9", 8, 8
        full_board.place_number(number, X, Y)
        over = full_board.game_is_over()
        self.assertTrue(over)

    def test_replace_placed_number1(self):
        number, Y, X = "7", 2, 6
        board = self.game.place_number(number, X, Y)
        number, Y, X = "5", 2, 6
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
        number, Y, X = "2", 3, 5
        board = self.game.place_number(number, X, Y)
        number, Y, X = "1", 3, 5
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
        number, Y, X = "5", 8, 1
        new_board = self.game.place_number(number, X, Y)
        number, Y, X = "4", 8, 1
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

    def test_place_invalid_number_block41(self):
        number, Y, X = "2", 3, 3
        board = self.game44.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["x2xx",
                                     "3xx1",
                                     "x32x",
                                     "4xxx"])

    def test_place_invalid_number_row41(self):
        number, Y, X = "1", 1, 1
        board = self.game44.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["x2xx",
                                     "3xx1",
                                     "x32x",
                                     "4xxx"])

    def test_place_valid_number41(self):
        number, Y, X = "1", 0, 0
        board = self.game44.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["12xx",
                                     "3xx1",
                                     "x32x",
                                     "4xxx"])

    def test_place_valid_number42(self):
        number, Y, X = "3", 0, 2
        board = self.game44.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["x23x",
                                     "3xx1",
                                     "x32x",
                                     "4xxx"])

    def test_place_valid_number4(self):
        number, Y, X = "3", 3, 3
        board = self.game44.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["x2xx",
                                     "3xx1",
                                     "x32x",
                                     "4xx3"])

    def test_game_not_over4(self):
        over = self.game44.game_is_over()
        self.assertFalse(over)

    def test_game_not_over_after_play4(self):
        number, Y, X = "3", 3, 3
        self.game44.place_number(number, X, Y)
        over = self.game.game_is_over()
        self.assertFalse(over)

    def test_game_over_after_play4(self):
        full_board = Sudoku(["2134",
                             "3421",
                             "1342",
                             "421x"])
        number, Y, X = "3", 3, 3
        full_board.place_number(number, X, Y)
        over = full_board.game_is_over()
        self.assertTrue(over)

    def test_replace_placed_number41(self):
        number, Y, X = "3", 0, 2
        board = self.game44.place_number(number, X, Y)
        number, Y, X = "4", 0, 2
        board = self.game44.place_number(number, X, Y)
        new_board = []
        for val in board:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["x24x",
                                     "3xx1",
                                     "x32x",
                                     "4xxx"])


if __name__ == "__main__":
    unittest.main()
