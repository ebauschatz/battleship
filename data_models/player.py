from data_models.boards.personal_board import PersonalBoard
from data_models.boards.opponent_board import OpponentBoard
from data_models.ships.destroyer import Destroyer
from data_models.ships.submarine import Submarine
from data_models.enums.space_marker import SpaceMarker
from data_models.enums.alignment import Alignment
from data_models.console_display import ConsoleDisplay

class Player:
    def __init__(self, name):
        self.name = name
        self.personal_board = PersonalBoard()
        self.opponent_board = OpponentBoard()
        self.ships = self.__generate_all_ships()

    def __generate_all_ships(self):
        return [Destroyer(), Submarine()]

    def pass_turn(self):
        ConsoleDisplay.display_turn_pass_message()
        ConsoleDisplay.clear_console()

    def place_all_ships(self):
        self.ship_placement_setup()
        for ship in self.ships:
            self.place_single_ship(ship)
            self.personal_board.display_board()
        self.pass_turn()

    def ship_placement_setup(self):
        ConsoleDisplay.display_turn_indicator(self.name)
        ConsoleDisplay.display_ship_placement_rules()
        self.personal_board.display_board()

    def place_single_ship(self, ship):
        ConsoleDisplay.display_ship_placement_message(ship.name, ship.space_size)
        valid_boundaries_found = False
        while valid_boundaries_found is False:
            start_row_label, start_column_label, end_row_label, end_column_label = self.get_ship_boundary_labels(ship.name)
            aligned, alignment = self.validate_boundary_alignment(start_row_label, start_column_label, end_row_label, end_column_label)
            if aligned is False:
                ConsoleDisplay.display_text('Ship alignment must be either horizontal or vertical, please try again.')
                continue
            if self.validate_ships_do_not_collide() is False:
                continue
            valid_boundaries_found = True
        if alignment == Alignment.HORIZONTAL:
            self.place_ship_in_row(ship, start_row_label, start_column_label, end_column_label)
        elif alignment == Alignment.VERTICAL:
            self.place_ship_in_column(ship, start_column_label, start_row_label, end_row_label)

    def get_ship_boundary_labels(self, ship_name):
        start_row = ConsoleDisplay.get_single_grid_coordinate(f'Please enter the starting row for your {ship_name}: ', self.personal_board.row_labels)
        start_column = ConsoleDisplay.get_single_grid_coordinate(f'Please enter the starting column for your {ship_name}: ', self.personal_board.column_labels)
        end_row = ConsoleDisplay.get_single_grid_coordinate(f'Please enter the ending row for your {ship_name}: ', self.personal_board.row_labels)
        end_column = ConsoleDisplay.get_single_grid_coordinate(f'Please enter the ending column for your {ship_name}: ', self.personal_board.column_labels)
        return start_row, start_column, end_row, end_column

    def validate_boundary_alignment(self, start_row_label, start_column_label, end_row_label, end_column_label):
        if start_row_label == end_row_label:
            return (True, Alignment.HORIZONTAL)
        elif start_column_label == end_column_label:
            return (True, Alignment.VERTICAL)
        else:
            return (False, None)

    def validate_ships_do_not_collide(self):
        pass

    def place_ship_in_row(self, ship, row, start_column, end_column):
        row_index = self.personal_board.row_labels.index(row)
        ship.current_spaces = self.personal_board.grid[row_index][int(start_column) - 1 : int(end_column)]
        for space in ship.current_spaces:
            space.space_marker = SpaceMarker.SHIP

    def place_ship_in_column(self, ship, column, start_row, end_row):
        column = int(column) - 1
        start_row_index = self.personal_board.row_labels.index(start_row)
        end_row_index = self.personal_board.row_labels.index(end_row)
        for row_index in range(start_row_index, end_row_index + 1):
            ship.current_spaces.append(self.personal_board.grid[row_index][column])
        for space in ship.current_spaces:
            space.space_marker = SpaceMarker.SHIP