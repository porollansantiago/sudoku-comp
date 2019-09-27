import unittest
from sudoku import Sudoku


class Test_sudoku(unittest.TestCase):
    def setUp(self):
        self.game = Sudoku(["53xx7xxxx",
                            "6xx195xxx",
                            "x98xxxx6x",
                            "8xxx6xxx3",
                            "4xx8x3xx1",
                            "7xxx2xxx6",
                            "x6xxxx28x",
                            "xxx419xx5",
                            "xxxx8xx79"])

    def test_place_invalid_number1(self):
        number, X, Y = 1, 0, 0
        new_board = self.game.place_number(number, X, Y)
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
        number, X, Y = 1, 3, 0
        new_board = self.game.place_number(number, X, Y)
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
        number, X, Y = 5, 0, 2
        new_board = self.game.place_number(number, X, Y)
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
        number, X, Y = 8, 7, 7
        new_board = self.game.place_number(number, X, Y)
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
        number, X, Y = 6, 3, 3
        new_board = self.game.place_number(number, X, Y)
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
        number, X, Y = 8, 7, 0
        new_board = self.game.place_number(number, X, Y)
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
        number, X, Y = 8, 8, 2
        new_board = self.game.place_number(number, X, Y)
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
        number, X, Y = 3, 0, 8
        new_board = self.game.place_number(number, X, Y)
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_valid_number2(self):
        number, X, Y = 4, 8, 0
        new_board = self.game.place_number(number, X, Y)
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_place_valid_number3(self):
        number, X, Y = 1, 0, 2
        new_board = self.game.place_number(number, X, Y)
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "198xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_game_not_over(self):
        over = self.game.game_is_over()
        self.assertFalse(over)

    def test_game_not_over_after_play(self):
        number, X, Y = 1, 0, 2
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
        number, X, Y = 9, 8, 8
        full_board.place_number(number, X, Y)
        over = full_board.game_is_over()
        self.assertTrue(over)

    def test_replace_placed_number(self):
        number, X, Y = 7, 6, 2
        new_board = self.game.place_number(number, X, Y)
        number, X, Y = 5, 6, 2
        new_board = self.game.place_number(number, X, Y)
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxx56x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])


if __name__ == "__main__":
    unittest.main()
