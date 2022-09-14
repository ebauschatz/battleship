from data_models.enums.space_marker import SpaceMarker
from data_models.boards.coordinate import Coordinate

class Space:
    def __init__(self):
        self.space_marker = SpaceMarker.UNGUESSED

    def register_guess_result(self, space_marker):
        self.space_marker = space_marker