import imp
from data_models.personal_board import PersonalBoard
from data_models.opponent_board import OpponentBoard
from data_models.destroyer import Destroyer
from data_models.submarine import Submarine
from data_models.hit_type import HitType
from data_models.console_display import ConsoleDisplay

class Player:
    def __init__(self, name):
        self.name = name
        self.personal_board = PersonalBoard()
        self.opponent_board = OpponentBoard()
        self.ships = self.__generate_all_ships()

    def __generate_all_ships(self):
        return [Destroyer(), Submarine()]

    def place_all_ships(self):
        for ship in self.ships:
            ConsoleDisplay.display_ship_placement_message(ship.name, ship.space_size)
            start_row = input(f'Please enter the starting row for your {ship.name}: ')
            start_column = input(f'Please enter the starting column for your {ship.name}: ')
            end_row = input(f'Please enter the ending row for your {ship.name}: ')
            end_column = input(f'Please enter the ending column for your {ship.name}: ')

            if start_row == end_row:
                self.place_ship_in_row(ship, start_row, start_column, end_column)
            else:
                self.place_ship_in_column(ship, start_column, start_row, end_row)

        self.personal_board.display_board()

    def place_ship_in_row(self, ship, row, start_column, end_column):
        row_index = self.personal_board.grid_rows.index(row)
        ship.current_spaces = self.personal_board.grid[row_index][int(start_column) - 1 : int(end_column)]
        for space in ship.current_spaces:
            space.hit_type = HitType.SHIP

    def place_ship_in_column(self, ship, column, start_row, end_row):
        column = int(column) - 1
        start_row_index = self.personal_board.grid_rows.index(start_row)
        end_row_index = self.personal_board.grid_rows.index(end_row)
        for row_index in range(start_row_index, end_row_index + 1):
            ship.current_spaces.append(self.personal_board.grid[row_index][column])
        for space in ship.current_spaces:
            space.hit_type = HitType.SHIP