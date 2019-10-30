import unittest
from interface import Interface
from parameterized import parameterized


class Test_interface(unittest.TestCase):
    def setUp(self):
        self.interface = Interface(["53xx7xxxx",
                                    "6xx195xxx",
                                    "x98xxxx6x",
                                    "8xxx6xxx3",
                                    "4xx8x3xx1",
                                    "7xxx2xxx6",
                                    "x6xxxx28x",
                                    "xxx419xx5",
                                    "xxxx8xx79"])

    @parameterized.expand([
        (0, 1, 1),
        (10, 1, 1),
        (-1, 1, 1),
        (10000, 4, 4),
        (-1234, 1, 3),
    ])
    def test_number_not_in_range(self, number, Y, X):
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "El numero va desde 1 a 9")

    @parameterized.expand([
        (1, 10, 0),
        (1, 0, 10),
        (1, 55, 55),
        (1, -43, 55),
    ])
    def test_XY_not_in_range(self, number, Y, X):
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Las coordenadas van del 1 al 9")

    @parameterized.expand([
        (2, 9, 9, [
            "Y",
            "9    5 3 _ | _ 7 _ | _ _ 2 ",
            "8    6 _ _ | 1 9 5 | _ _ _ ",
            "7    _ 9 8 | _ _ _ | _ 6 _ ",
            "    -----------------------",
            "6    8 _ _ | _ 6 _ | _ _ 3 ",
            "5    4 _ _ | 8 _ 3 | _ _ 1 ",
            "4    7 _ _ | _ 2 _ | _ _ 6 ",
            "    -----------------------",
            "3    _ 6 _ | _ _ _ | 2 8 _ ",
            "2    _ _ _ | 4 1 9 | _ _ 5 ",
            "1    _ _ _ | _ 8 _ | _ 7 9 ",
            "\n     1 2 3   4 5 6   7 8 9  X"]),
        (2, 1, 1, [
            "Y",
            "9    5 3 _ | _ 7 _ | _ _ _ ",
            "8    6 _ _ | 1 9 5 | _ _ _ ",
            "7    _ 9 8 | _ _ _ | _ 6 _ ",
            "    -----------------------",
            "6    8 _ _ | _ 6 _ | _ _ 3 ",
            "5    4 _ _ | 8 _ 3 | _ _ 1 ",
            "4    7 _ _ | _ 2 _ | _ _ 6 ",
            "    -----------------------",
            "3    _ 6 _ | _ _ _ | 2 8 _ ",
            "2    _ _ _ | 4 1 9 | _ _ 5 ",
            "1    2 _ _ | _ 8 _ | _ 7 9 ",
            "\n     1 2 3   4 5 6   7 8 9  X"]),
        (1, 7, 1, [
            "Y",
            "9    5 3 _ | _ 7 _ | _ _ _ ",
            "8    6 _ _ | 1 9 5 | _ _ _ ",
            "7    1 9 8 | _ _ _ | _ 6 _ ",
            "    -----------------------",
            "6    8 _ _ | _ 6 _ | _ _ 3 ",
            "5    4 _ _ | 8 _ 3 | _ _ 1 ",
            "4    7 _ _ | _ 2 _ | _ _ 6 ",
            "    -----------------------",
            "3    _ 6 _ | _ _ _ | 2 8 _ ",
            "2    _ _ _ | 4 1 9 | _ _ 5 ",
            "1    _ _ _ | _ 8 _ | _ 7 9 ",
            "\n     1 2 3   4 5 6   7 8 9  X"]),

    ])
    def test_number_placed(self, number, Y, X, expected):
        play, is_over = self.interface.play(number, X, Y)
        new_board = []
        for val in play:
            new_board.append("".join(val))
        self.assertEqual(new_board, expected)

    @parameterized.expand([
        (1, 2, 'X'),
        (1, 'X', 0),
        ('X', 2, 0),
    ])
    def test_letters(self, number, Y, X):
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Solo se pueden ingresar numeros")


if __name__ == "__main__":
    unittest.main()
