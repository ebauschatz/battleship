from data_models.space_marker import SpaceMarker

class Ship:
    def __init__(self):
        self.is_sunk = False
        self.name = ''
        self.space_size = 0
        self.current_spaces = []

    def check_if_sunk(self):
        if len([space for space in self.current_spaces if space.space_marker != SpaceMarker.HIT]) == 0:
            self.is_sunk = True