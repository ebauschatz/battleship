import imp
from data_models.board import Board
from data_models.console_display import ConsoleDisplay

class PersonalBoard(Board):
    def __init__(self):
        super().__init__()

    def display_board(self):
        ConsoleDisplay.display_board_type('personal')
        ConsoleDisplay.display_board(self.grid, self.grid_rows, self.grid_columns)