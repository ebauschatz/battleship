from data_models.boards.board import Board
from data_models.console_display import ConsoleDisplay

class PersonalBoard(Board):
    def __init__(self):
        super().__init__()

    def display_board(self):
        ConsoleDisplay.display_board_type('personal')
        ConsoleDisplay.display_board(self)