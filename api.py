import requests


class Api_acceso():
    def __init__(self):
        self.board = [['x' for _ in range(9)] for _ in range(9)]

    def get_new_board(self):
        res = requests.get(
            "http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=9")
        res = res.json()
        for val in res["squares"]:
            x = val['x']
            y = val['y']
            value = val['value']
            self.board[x][y] = str(value)
        return self.board
