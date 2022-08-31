from data_models.hit_type import HitType

class Space:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.hit_type = HitType.UNGUESSED