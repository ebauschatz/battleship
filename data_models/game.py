from data_models.player import Player

class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()


    def run_game(self):
        self.player_one.place_all_ships()
        self.player_two.place_all_ships()