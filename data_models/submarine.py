from data_models.ship import Ship

class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'submarine'
        self.space_size = 3