import unittest
from unittest.mock import MagicMock
from api import Api_acceso


class Test_api_acceso(unittest.TestCase):
    def setUp(self):
        self.api = Api_acceso()
        self.api4 = Api_acceso(1, 4)
        self.mock = MagicMock()
        self.mock.json = MagicMock(
            return_value={'response': True, 'size': '9', 'squares': [
                {'x': 0, 'y': 1, 'value': 1}, {'x': 0, 'y': 2, 'value': 6},
                {'x': 0, 'y': 4, 'value': 7}, {'x': 0, 'y': 6, 'value': 5},
                {'x': 0, 'y': 8, 'value': 2}, {'x': 1, 'y': 0, 'value': 3},
                {'x': 1, 'y': 1, 'value': 5}, {'x': 1, 'y': 5, 'value': 2},
                {'x': 1, 'y': 7, 'value': 6}, {'x': 1, 'y': 8, 'value': 7},
                {'x': 2, 'y': 2, 'value': 2}, {'x': 2, 'y': 3, 'value': 6},
                {'x': 2, 'y': 4, 'value': 3}, {'x': 2, 'y': 5, 'value': 5},
                {'x': 2, 'y': 6, 'value': 1}, {'x': 2, 'y': 8, 'value': 8},
                {'x': 3, 'y': 0, 'value': 5}, {'x': 3, 'y': 1, 'value': 3},
                {'x': 3, 'y': 3, 'value': 1}, {'x': 3, 'y': 7, 'value': 8},
                {'x': 4, 'y': 2, 'value': 1}, {'x': 4, 'y': 4, 'value': 6},
                {'x': 4, 'y': 6, 'value': 9}, {'x': 5, 'y': 1, 'value': 9},
                {'x': 5, 'y': 3, 'value': 5}, {'x': 5, 'y': 7, 'value': 1},
                {'x': 5, 'y': 8, 'value': 3}, {'x': 6, 'y': 0, 'value': 4},
                {'x': 6, 'y': 2, 'value': 3}, {'x': 6, 'y': 3, 'value': 2},
                {'x': 6, 'y': 5, 'value': 1}, {'x': 6, 'y': 6, 'value': 8},
                {'x': 7, 'y': 1, 'value': 7}, {'x': 7, 'y': 3, 'value': 9},
                {'x': 7, 'y': 4, 'value': 4}, {'x': 7, 'y': 7, 'value': 2},
                {'x': 8, 'y': 2, 'value': 5}, {'x': 8, 'y': 4, 'value': 8},
                {'x': 8, 'y': 6, 'value': 3}, {'x': 8, 'y': 8, 'value': 1}]
            })
        self.mock4 = MagicMock()
        self.mock4.json = MagicMock(
            return_value={'response': True, 'size': '4', 'squares': [
                {'x': 0, 'y': 0, 'value': 2}, {'x': 0, 'y': 3, 'value': 4},
                {'x': 1, 'y': 2, 'value': 2}, {'x': 2, 'y': 1, 'value': 2},
                {'x': 2, 'y': 3, 'value': 3}, {'x': 3, 'y': 0, 'value': 4},
                {'x': 3, 'y': 1, 'value': 3}, {'x': 3, 'y': 3, 'value': 2}]})

    def test_board4(self):
        board = self.api4.get_new_board(self.mock4)
        self.assertEqual(board, [['2', 'x', 'x', '4'],
                                 ['x', 'x', '2', 'x'],
                                 ['x', '2', 'x', '3'],
                                 ['4', '3', 'x', '2']])

    def test_board(self):
        board = self.api.get_new_board(self.mock)
        self.assertEqual(board, [['x', '1', '6', 'x', '7', 'x', '5', 'x', '2'],
                                 ['3', '5', 'x', 'x', 'x', '2', 'x', '6', '7'],
                                 ['x', 'x', '2', '6', '3', '5', '1', 'x', '8'],
                                 ['5', '3', 'x', '1', 'x', 'x', 'x', '8', 'x'],
                                 ['x', 'x', '1', 'x', '6', 'x', '9', 'x', 'x'],
                                 ['x', '9', 'x', '5', 'x', 'x', 'x', '1', '3'],
                                 ['4', 'x', '3', '2', 'x', '1', '8', 'x', 'x'],
                                 ['x', '7', 'x', '9', '4', 'x', 'x', '2', 'x'],
                                 ['x', 'x', '5', 'x', '8', 'x', '3', 'x', '1']]
                         )


if __name__ == "__main__":
    unittest.main()
