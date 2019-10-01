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
        number, Y, X = 0, 0, 0
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "El numero va desde 1 a 9")

    def test_number_not_in_range2(self):
        number, Y, X = 10, 0, 0
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "El numero va desde 1 a 9")

    def test_number_not_in_range3(self):
        number, Y, X = -1, 0, 0
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "El numero va desde 1 a 9")

    def test_XY_not_in_range1(self):
        number, Y,  X = 1, 9, 0
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Las coordenadas van del 0 al 8")

    def test_XY_not_in_range2(self):
        number, Y,  X = 1, 0, 9
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Las coordenadas van del 0 al 8")

    def test_XY_not_in_range3(self):
        number, Y,  X = 1, 55, 55
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Las coordenadas van del 0 al 8")

    def test_XY_not_in_range4(self):
        number, Y,  X = 1, -43, 55
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, "Las coordenadas van del 0 al 8")

    def test_number_placed1(self):
        number, Y, X = 3, 0, 8
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, ["53xx7xxxx",
                                "6xx195xxx",
                                "x98xxxx6x",
                                "8xxx6xxx3",
                                "4xx8x3xx1",
                                "7xxx2xxx6",
                                "x6xxxx28x",
                                "xxx419xx5",
                                "xxxx8xx79"])

    def test_number_placed2(self):
        number, Y, X = 4, 8, 0
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, ["53xx7xxxx",
                                "6xx195xxx",
                                "x98xxxx6x",
                                "8xxx6xxx3",
                                "4xx8x3xx1",
                                "7xxx2xxx6",
                                "x6xxxx28x",
                                "xxx419xx5",
                                "xxxx8xx79"])

    def test_place_valid_number3(self):
        number, Y, X = 1, 2, 0
        play, is_over = self.interface.play(number, X, Y)
        self.assertEqual(play, ["53xx7xxxx",
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
