import os
from data_models.enums.space_marker import SpaceMarker

class ConsoleDisplay:
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else "clear")
    
    @staticmethod
    def display_text(text):
        print(text)

    @staticmethod
    def display_turn_pass_message():
        input('\nPress enter to pass the turn to the next player')

    @staticmethod
    def display_ship_placement_rules():
        print('''\nTo place your ships, you will be prompted for a starting and ending row and column.
        > Ships cannot be placed diagonally, they must be either horizontal or vertical.
            - To place a ship vertically, enter the same starting and ending column.
            - To place a ship horizontally, enter the same starting and ending row.
        > Ships cannot overlap or intersect.
        > The number of spaces spanned by a ship must be exactly equal to the length of the ship.''')

    @staticmethod
    def display_ship_placement_message(name, size):
        print(f'\nPlace your {name}! This ship is {size} spaces long.')

    @staticmethod
    def get_single_grid_coordinate(display_message, coordinate_options):
        selection = (False, None)
        while selection[0] is False:
            user_input = input(display_message)
            selection = ConsoleDisplay.validate_selection_in_options(coordinate_options, user_input)
        return selection[1]

    @staticmethod
    def validate_selection_in_options(options, selection):
        options_dict = {}
        for option in options:
            options_dict[option] = (True, option)
        return options_dict.get(selection, (False, None))

    @staticmethod
    def display_board(board):
        ConsoleDisplay.display_board_headers(board.column_labels)
        for row_index, row_label in enumerate(board.row_labels):
            output_text = row_label
            board_row = board.grid[row_index]
            output_text += ConsoleDisplay.translate_board_spaces(board_row)
            print(output_text)

    @staticmethod
    def display_board_headers(board_columns):
        header_text = '\n  '
        for column in board_columns:
            header_text += str(column) + ' '
        print(header_text)

    @staticmethod
    def translate_board_spaces(grid_row):
        output = ''
        for space in grid_row:
            if space.space_marker == SpaceMarker.UNGUESSED:
                output += '⚫'
            elif space.space_marker == SpaceMarker.HIT:
                output += '🔴'
            elif space.space_marker == SpaceMarker.MISS:
                output += '⚪'
            elif space.space_marker == SpaceMarker.SHIP:
                output += '🚢'
        return output

    @staticmethod
    def display_board_type(board_type):
        print(f'\nBelow is your {board_type} board:')

    @staticmethod
    def display_guess_result(result_text):
        print(f'\nThat guess resulted in {result_text}!')

    @staticmethod
    def display_game_winner(player_name):
        print(f'{player_name} has won!')

    @staticmethod
    def display_turn_indicator(player_name):
        print(f'\nIt is now {player_name}\'s turn')

    @staticmethod
    def display_game_welcome():
        ConsoleDisplay.clear_console()
        print('''                                     |__
                                     |\/
                                     ---
                                     / | [
                              !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____               /\\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--          \/   _
 __..._____--==/___]_|__|_____________________________[___\==--___,-----' .7
|                                                                         /
 \_______________________________________________________________________|
 Artist credit: Matthew Bace''')
        print('\n\t\t\tWelcome to Battleship!')
        input('\n\t\tPress enter to begin the game')