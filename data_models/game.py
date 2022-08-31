import imp
from data_models.player import Player
from data_models.hit_type import HitType

class Game:
    def __init__(self):
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')

    def run_game(self):
        self.player_one.place_all_ships()
        self.player_two.place_all_ships()
        self.make_guess(self.player_one, self.player_two)

    def make_guess(self, guesser, opponent):
        guess_row = input('Please enter a guess row: ')
        guess_column = input('Please enter a guess column: ')

        guess_row_index = opponent.personal_board.grid_rows.index(guess_row)
        opponent_personal_board_guess_space = opponent.personal_board.grid[guess_row_index][int(guess_column) - 1]
        guesser_opponent_board_guess_space = guesser.opponent_board.grid[guess_row_index][int(guess_column) - 1]
        if opponent_personal_board_guess_space.hit_type == HitType.SHIP:
            opponent_personal_board_guess_space.hit_type = HitType.HIT
            guesser_opponent_board_guess_space.hit_type = HitType.HIT
        else:
            opponent_personal_board_guess_space.hit_type = HitType.MISS
            guesser_opponent_board_guess_space.hit_type = HitType.MISS

        guesser.opponent_board.display_board()