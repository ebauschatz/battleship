from data_models.boards.space import Space

class Board:
    def __init__(self):
        self.row_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.column_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        new_grid = []
        for _ in self.row_labels:
            new_grid.append([Space() for _ in self.column_labels])
        return new_grid