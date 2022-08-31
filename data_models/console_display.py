from data_models.hit_type import HitType

class ConsoleDisplay:
    @staticmethod
    def display_board(board, row_labels, column_labels):
        ConsoleDisplay.display_board_headers(column_labels)
        for row_index, row_label in enumerate(row_labels):
            output_text = row_label
            board_row = board[row_index]
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
            if space.hit_type == HitType.UNGUESSED:
                output += '⚫'
            elif space.hit_type == HitType.HIT:
                output += '🔴'
            elif space.hit_type == HitType.MISS:
                output += '⚪'
            elif space.hit_type == HitType.SHIP:
                output += '🚢'
        return output

    @staticmethod
    def display_board_type(board_type):
        print(f'\nBelow is your {board_type} board:')

    @staticmethod
    def display_ship_placement_message(name, size):
        print(f'\nPlace your {name}! This ship is {size} spaces long.')