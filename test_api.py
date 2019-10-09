import unittest
from api import Api_acceso


class Test_api_acceso(unittest.TestCase):
    def setUp(self):
        self.api = Api_acceso()
        self.api_4 = Api_acceso(1, 4)
        self.board = self.api.get_new_board()
        self.board4 = self.api_4.get_new_board()

    def test_board4(self):
        self.assertEqual(len(self.board4), 4)

    def test_board_not_null(self):
        self.assertTrue(self.board)

    def test_board_has_numbers(self):
        for x in range(9):
            for y in range(9):
                if self.board[x][y] != 'x':
                    flag = True
                    break
        self.assertTrue(flag)

    def test_valid_rows(self):
        for y in range(9):
            row = []
            for x in range(9):
                if self.board[y][x] != 'x':
                    row.append(self.board[y][x])
            s = set(row)
            self.assertEqual(len(row), len(s))

    def test_valid_cols(self):
        for y in range(9):
            col = []
            for x in range(9):
                if self.board[x][y] != 'x':
                    col.append(self.board[x][y])
            s = set(col)
            self.assertEqual(len(col), len(s))

    def test_valid_blocks(self):
        pass


if __name__ == "__main__":
    unittest.main()
