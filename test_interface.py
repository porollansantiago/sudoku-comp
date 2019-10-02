import unittest
from interface import Interface


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

    def test_number_not_in_range1(self):
        number, Y, X = 0, 1, 1
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "El numero va desde 1 a 9")

    def test_number_not_in_range2(self):
        number, Y, X = 10, 1, 1
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "El numero va desde 1 a 9")

    def test_number_not_in_range3(self):
        number, Y, X = -1, 1, 1
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "El numero va desde 1 a 9")

    def test_XY_not_in_range1(self):
        number, Y,  X = 1, 10, 0
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Las coordenadas van del 1 al 9")

    def test_XY_not_in_range2(self):
        number, Y,  X = 1, 0, 10
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Las coordenadas van del 1 al 9")

    def test_XY_not_in_range3(self):
        number, Y,  X = 1, 55, 55
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Las coordenadas van del 1 al 9")

    def test_XY_not_in_range4(self):
        number, Y,  X = 1, -43, 55
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Las coordenadas van del 1 al 9")

    def test_number_placed1(self):
        number, Y, X = 2, 9, 9
        play, is_over = self.interface.play(number, X, Y)
        new_board = []
        for val in play:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxx2",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_number_placed2(self):
        number, Y, X = 2, 1, 1
        play, is_over = self.interface.play(number, X, Y)
        new_board = []
        for val in play:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "x98xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "2xxx8xx79"])

    def test_place_valid_number3(self):
        number, Y, X = 1, 7, 1
        play, is_over = self.interface.play(number, X, Y)
        new_board = []
        for val in play:
            new_board.append("".join(val))
        self.assertEqual(new_board, ["53xx7xxxx",
                                     "6xx195xxx",
                                     "198xxxx6x",
                                     "8xxx6xxx3",
                                     "4xx8x3xx1",
                                     "7xxx2xxx6",
                                     "x6xxxx28x",
                                     "xxx419xx5",
                                     "xxxx8xx79"])

    def test_letters1(self):
        number, Y, X = 1, 2, 'X'
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Solo se pueden ingresar numeros")

    def test_letters2(self):
        number, Y, X = 1, 'X', 0
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Solo se pueden ingresar numeros")

    def test_letters3(self):
        number, Y, X = 'X', 2, 0
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Solo se pueden ingresar numeros")


if __name__ == "__main__":
    unittest.main()
