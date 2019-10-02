import requests


class Api_acceso():
    def __init__(self, difficulty=1):
        self.board = [['x' for _ in range(9)] for _ in range(9)]
        if difficulty not in [1, 2, 3]:
            difficulty = 1
        url = "http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=" + str(
            difficulty) + "&size=9"
        self.res = requests.get(url)

    def get_new_board(self):

        if self.res.status_code == 200:
            res = self.res.json()
            for val in res["squares"]:
                x = val['x']
                y = val['y']
                value = val['value']
                self.board[x][y] = str(value)
            return self.board
        else:
            return "no se pudo conseguir el tablero"
