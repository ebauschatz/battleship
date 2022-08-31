from data_models.space import Space

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

    def display_board(self):
        pass