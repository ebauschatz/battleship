from data_models.board import Board

class OpponentBoard(Board):
    def __init__(self):
        super().__init__()

    def display_board(self):
        print('display guesses about opponents board')