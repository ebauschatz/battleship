from data_models.space import Space
from data_models.hit_type import HitType

class Board:
    def __init__(self):
        self.grid_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.grid_columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        new_grid = []
        for row in self.grid_rows:
            new_grid.append([Space(row, column) for column in self.grid_columns])
        return new_grid

    def display_board_headers(self):
        header_text = '\n  '
        for column in self.grid_columns:
            header_text += str(column) + ' '
        print(header_text)

    def display_board(self):
        self.display_board_headers()
        for row_index in range(len(self.grid_rows)):
            output_text = str(self.grid_rows[row_index])
            board_row = self.grid[row_index]
            output_text += self.translate_grid_spaces(board_row)
            print(output_text)

    def translate_grid_spaces(self, grid_row):
        output = ''
        for space in grid_row:
            if space.hit_type == HitType.UNGUESSED:
                output += '⚫'
            elif space.hit_type == HitType.HIT:
                output += '🔴'
            elif space.hit_type == HitType.MISS:
                output += '⚪'
            elif space.hit_type == HitType.SHIP:
                output += '🚢'
        return output