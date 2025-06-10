import math

import pygame as pg

CELL_SIZE = 40

board3x3_solved = [[6, 8, 2, 4, 3, 5, 1, 7, 9],  # < x // 0
                   [7, 1, 5, 2, 9, 6, 3, 8, 4],  # < x // 1
                   [9, 4, 3, 8, 7, 1, 6, 2, 5],

                   [2, 7, 1, 6, 8, 9, 5, 4, 3],
                   [4, 6, 9, 3, 5, 7, 8, 1, 2],
                   [5, 3, 8, 1, 4, 2, 9, 6, 7],

                   [8, 2, 7, 9, 6, 3, 4, 5, 1],
                   [3, 5, 4, 7, 1, 8, 2, 9, 6],
                   [1, 9, 6, 5, 2, 4, 7, 3, 8]]
                   #^  ^
                   #y  y
                   #// //
                   #0  1

board3x3_unsolved = [[0, 8, 0, 0, 0, 5, 1, 7, 9],  # < x // 0
                     [0, 0, 0, 2, 0, 6, 0, 8, 4],  # < x // 1
                     [9, 0, 3, 0, 0, 0, 6, 0, 0],

                     [2, 7, 0, 0, 8, 0, 5, 0, 3],
                     [4, 0, 0, 0, 5, 0, 8, 1, 2],
                     [0, 0, 8, 0, 4, 2, 0, 0, 7],

                     [8, 0, 0, 0, 0, 3, 0, 0, 1],
                     [3, 5, 4, 0, 1, 0, 0, 9, 0],
                     [0, 9, 6, 0, 2, 4, 7, 0, 0]]
                     #^  ^
                     #y  y
                     #// //
                     #0  1

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

    def get_board_row(self, x):
        """function for getting a row at x coordinate"""
        return self.b[x]

    def get_board_col(self, y):
        """function for getting a column at y coordinate"""
        col_list = []
        for row in self.b:
            col_list.append(row[y])
        return col_list

    def get_board_block(self, x, y):
        """function for getting a block around x and y coordinates"""
        block_list = []
        x = math.floor(x / self.block_length)
        y = math.floor(y / self.block_length)
        for x1 in range(x*self.block_length, (x + 1) * self.block_length):
            for y1 in range(y*self.block_length, (y + 1) * self.block_length):
                block_list.append(self.b[x1][y1])
        return block_list

    def is_cell_correct(self, x, y, check_if_emtpy=False):
        """function for checking if cell at x and y coordinates is correct"""
        unit = self.b[x][y]
        if unit == 0: # TODO: move or refactor for more easier to read code
            if not check_if_emtpy:
                return True
            else:
                # print("cell is zero (empty)")
                return False
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

    def modify_number(self, number, pos1, pos2):
        """function for modifying number at x and y coordinate"""
        if not (0 <= pos1 < self.row_and_col_length and 0 <= pos2 < self.row_and_col_length):
            return
        row = self.b[pos2]
        row[pos1] = int(number)

class VisualBoard:
    """class for managing the visual representation of the logic board"""
    def __init__(self, logic_board: LogicBoard):
        self.lb = logic_board

    def draw_visual_board(self):
        """function for drawing visual lines of the board"""
        surface = pg.Surface(((CELL_SIZE * self.lb.row_and_col_length) + 3, (CELL_SIZE * self.lb.row_and_col_length) + 3))
        surface.fill("white")
        for i in range(self.lb.row_and_col_length+1):
            width = 1
            if i % self.lb.block_length == 0:
                width = 3
            pg.draw.line(surface, "black", (0, (CELL_SIZE * i) + 1.5), ((CELL_SIZE * self.lb.row_and_col_length) + 2, (CELL_SIZE * i) + 1.5),
                         width)
            pg.draw.line(surface, "black", ((CELL_SIZE * i) + 1.5, 0), ((CELL_SIZE * i) + 1.5, (CELL_SIZE * self.lb.row_and_col_length) + 2),
                         width)
        return surface

    def draw_numbers(self, surf):
        """function for drawing the numbers on the board"""
        font = pg.font.SysFont("ubuntu", 35)
        # print("XX")
        for i in range(self.lb.row_and_col_length):
            for j in range(self.lb.row_and_col_length):
                color = "black"
                if not self.lb.is_cell_correct(i, j):  # TODO: mark only new cell if wrong
                    color = "red"
                if self.lb.b[i][j] == 0:
                    continue
                font_surface = font.render(str(self.lb.b[i][j]), True, color)
                font_rect = font_surface.get_rect(center=((CELL_SIZE * j) + (CELL_SIZE / 2), (CELL_SIZE * i) + (CELL_SIZE / 2)))
                surf.blit(font_surface, font_rect)
        # print("XX")
        return surf

    def draw_selection(self, surf):
        """function for drawing the selected row and column"""
        pos = pg.mouse.get_pos()
        pos1 = math.floor((pos[0] - 50)/CELL_SIZE)
        pos2 = math.floor((pos[1] - 50)/CELL_SIZE)

        if not (0 <= pos1 < self.lb.row_and_col_length and 0 <= pos2 < self.lb.row_and_col_length):
            return
        shape_surf = pg.Surface((CELL_SIZE, CELL_SIZE*self.lb.row_and_col_length), pg.SRCALPHA)
        pg.draw.rect(shape_surf, (0, 0, 255, 127), shape_surf.get_rect())
        surf.blit(shape_surf, (CELL_SIZE*pos1, 0))

        shape_surf = pg.Surface((CELL_SIZE*self.lb.row_and_col_length, CELL_SIZE), pg.SRCALPHA)
        pg.draw.rect(shape_surf, (0, 0, 255, 127), shape_surf.get_rect())
        surf.blit(shape_surf, (0, CELL_SIZE*pos2))

def dd():

    pass


pg.init()

screen = pg.display.set_mode((1280*1.5,720*1.5))
running = True

lb = LogicBoard(board3x3_unsolved)
vb = VisualBoard(lb)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            try:
                if 1 <= int(event.unicode) <= 9:
                    pos = pg.mouse.get_pos()
                    pos1 = math.floor((pos[0] - 50) / CELL_SIZE)
                    pos2 = math.floor((pos[1] - 50) / CELL_SIZE)
                    lb.modify_number(event.unicode, pos1, pos2)
            except:
                pass

    screen.fill("white")
    surf1 = vb.draw_visual_board()
    vb.draw_numbers(surf1)
    vb.draw_selection(surf1)
    print(lb.get_all_mistakes())



    screen.blit(surf1, (50, 50))
    pg.display.flip()

pg.quit()