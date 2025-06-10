import math


class LogicBoard:
    """class for managing the logic, data and implementation of the sudoku board"""
    def __init__(self, board: list[list[int]]):
        self.b = board
        self._block_length = 3

    @property
    def block_length(self):
        return self._block_length

    @property
    def row_and_col_length(self):
        return int(math.pow(self._block_length, 2))

    def get_board_row(self, x: int):
        """function for getting a row at x coordinate"""
        return self.b[x]

    def get_board_col(self, y: int):
        """function for getting a column at y coordinate"""
        col_list = []
        for row in self.b:
            col_list.append(row[y])
        return col_list

    def get_board_block(self, x: int, y: int):
        """function for getting a block around x and y coordinates"""
        block_list = []
        x = math.floor(x / self.block_length)
        y = math.floor(y / self.block_length)
        for x1 in range(x * self.block_length, (x + 1) * self.block_length):
            for y1 in range(y * self.block_length, (y + 1) * self.block_length):
                block_list.append(self.b[x1][y1])
        return block_list

    def is_cell_correct(self, x: int, y: int):
        """function for checking if cell at x and y coordinates is correct"""
        unit = self.b[x][y]
        if unit == 0: # TODO: move or refactor for more easier to read code
            return True
        #     if check_if_emtpy:
        #         return False
        #     else:
        #         # print("cell is zero (empty)")
        #         return True
        if self.get_board_block(x, y).count(unit) > 1:
            # print("fout block")
            return False
        if self.get_board_row(x).count(unit) > 1:
            # print("fout row")
            return False
        if self.get_board_col(y).count(unit) > 1:
            # print("fout col")
            return False
        return True

    def get_all_mistakes(self):
        mistake_list = []
        for i in range(self.row_and_col_length):
            for j in range(self.row_and_col_length):
                if not self.is_cell_correct(i, j):
                    mistake_list.append((i, j))
        return mistake_list

    def modify_number(self, number: int, pos1: int, pos2: int):
        """function for modifying number at x and y coordinate"""
        if not (0 <= pos1 < self.row_and_col_length and 0 <= pos2 < self.row_and_col_length):
            return
        row = self.b[pos2]
        row[pos1] = number
