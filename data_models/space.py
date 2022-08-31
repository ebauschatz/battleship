from data_models.hit_type import HitType

class Space:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.guess_type = HitType.UNGUESSED