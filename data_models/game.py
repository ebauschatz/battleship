from data_models.console_display import ConsoleDisplay
from data_models.player import Player
from data_models.space_marker import SpaceMarker

class Game:
    def __init__(self):
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')

    def run_game(self):
        self.player_one.place_all_ships()
        self.player_two.place_all_ships()
        self.run_rounds()
        self.determine_winner()

    def run_rounds(self):
        all_ships_sunk = False
        while all_ships_sunk is False:
            self.make_guess(self.player_one, self.player_two)
            if self.all_ships_are_sunk(self.player_two):
                all_ships_sunk = True
                break
            self.make_guess(self.player_two, self.player_one)
            if self.all_ships_are_sunk(self.player_one):
                all_ships_sunk = True
                break

    def make_guess(self, guesser, opponent):
        guess_row = input('Please enter a guess row: ')
        guess_column = input('Please enter a guess column: ')

        guess_row_index = opponent.personal_board.grid_rows.index(guess_row)
        opponent_personal_board_guess_space = opponent.personal_board.grid[guess_row_index][int(guess_column) - 1]
        guesser_opponent_board_guess_space = guesser.opponent_board.grid[guess_row_index][int(guess_column) - 1]

        if opponent_personal_board_guess_space.space_marker == SpaceMarker.SHIP:
            self.register_guess_result(guesser_opponent_board_guess_space, opponent_personal_board_guess_space, SpaceMarker.HIT, 'a hit')
            opponent_ship = self.find_ship_from_space(opponent.ships, opponent_personal_board_guess_space)
            opponent_ship.check_if_sunk()
        else:
            self.register_guess_result(guesser_opponent_board_guess_space, opponent_personal_board_guess_space, SpaceMarker.MISS, 'a miss')

        guesser.opponent_board.display_board()

    def register_guess_result(self, player_space, opponent_space, space_marker, space_marker_text):
        player_space.register_guess_result(space_marker)
        opponent_space.register_guess_result(space_marker)
        ConsoleDisplay.display_guess_result(space_marker_text)

    def find_ship_from_space(self, ships, space):
        for ship in ships:
            if space in ship.current_spaces:
                return ship

    def determine_winner(self):
        if self.all_ships_are_sunk(self.player_one):
            ConsoleDisplay.display_game_winner(self.player_two.name)
        else:
            ConsoleDisplay.display_game_winner(self.player_one.name)

    def all_ships_are_sunk(self, player):
        unsunk_ships = [ship for ship in player.ships if ship.is_sunk is False]
        if len(unsunk_ships) > 0:
            return False
        else:
            return True