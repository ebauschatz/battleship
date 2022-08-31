from data_models.board import Board
from data_models.console_display import ConsoleDisplay

class OpponentBoard(Board):
    def __init__(self):
        super().__init__()

    def display_board(self):
        ConsoleDisplay.display_board_type('opponent\'s')
        ConsoleDisplay.display_board(self.grid, self.grid_rows, self.grid_columns)