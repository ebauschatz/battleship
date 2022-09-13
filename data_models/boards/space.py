from data_models.enums.space_marker import SpaceMarker

class Space:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.space_marker = SpaceMarker.UNGUESSED

    def register_guess_result(self, space_marker):
        self.space_marker = space_marker