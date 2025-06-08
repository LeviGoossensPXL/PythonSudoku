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

board3x3_unsolved = [[0, 8, 2, 4, 3, 5, 1, 7, 9],  # < x // 0
                     [0, 1, 5, 2, 9, 6, 3, 8, 4],  # < x // 1
                     [9, 4, 3, 8, 7, 1, 6, 2, 5],

                     [2, 7, 1, 6, 8, 9, 5, 4, 3],
                     [4, 6, 9, 3, 5, 7, 8, 1, 2],
                     [0, 3, 8, 1, 4, 2, 9, 6, 7],

                     [8, 2, 7, 0, 0, 3, 0, 0, 1],
                     [3, 5, 4, 0, 1, 0, 2, 9, 0],
                     [0, 9, 6, 0, 2, 4, 7, 0, 0]]
                     #^  ^
                     #y  y
                     #// //
                     #0  1

class LogicBoard:
    """class for managing the logic, data and implementation of the sudoku board"""
    def __init__(self, board: list[list[int]]):
        self.b = board

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
        x = math.floor(x/3)
        y = math.floor(y/3)
        for x1 in range(x*3, (x+1)*3):
            for y1 in range(y*3, (y+1)*3):
                block_list.append(self.b[x1][y1])
        return block_list

    def is_cell_correct(self, x, y):
        """function for checking if cell at x and y coordinates is correct"""
        unit = self.b[x][y]
        if unit == 0:
            print("cell is zero (empty)")
            return False
        if self.get_board_block(x, y).count(unit) > 1:
            print("fout block")
            return False
        if self.get_board_row(x).count(unit) > 1:
            print("fout row")
            return False
        if self.get_board_col(y).count(unit) > 1:
            print("fout col")
            return False
        return True

    def modify_number(self, number, pos1, pos2):
        """function for modifying number at x and y coordinate"""
        if not (0 <= pos1 < 9 and 0 <= pos2 < 9):
            return
        row = self.b[pos2]
        row[pos1] = int(number)

class VisualBoard:
    """class for managing the visual representation of the logic board"""
    def __init__(self, logic_board: LogicBoard):
        self.lb = logic_board

    def draw_visual_board(self):
        """function for drawing visual lines of the board"""
        surface = pg.Surface(((CELL_SIZE * 9) + 3, (CELL_SIZE * 9) + 3))
        surface.fill("white")
        for i in range(10):
            width = 1
            if i % 3 == 0:
                width = 3
            pg.draw.line(surface, "black", (0, (CELL_SIZE * i) + 1.5), ((CELL_SIZE * 9) + 2, (CELL_SIZE * i) + 1.5),
                         width)
            pg.draw.line(surface, "black", ((CELL_SIZE * i) + 1.5, 0), ((CELL_SIZE * i) + 1.5, (CELL_SIZE * 9) + 2),
                         width)
        return surface

    def draw_numbers(self, surf):
        """function for drawing the numbers on the board"""
        font = pg.font.SysFont("ubuntu", 40)
        print("XX")
        for i in range(9):
            for j in range(9):
                color = "black"
                if not self.lb.is_cell_correct(i, j):  # TODO: mark only new cell if wrong
                    color = "red"
                if self.lb.b[i][j] == 0:
                    continue
                font_surface = font.render(str(self.lb.b[i][j]), True, color)
                font_rect = font_surface.get_rect(
                    center=((CELL_SIZE * j) + (CELL_SIZE / 2), (CELL_SIZE * i) + (CELL_SIZE / 2)))
                surf.blit(font_surface, font_rect)
        print("XX")
        return surf

    def draw_selection(self, surf):
        """function for drawing the selected row and column"""
        pos = pg.mouse.get_pos()
        pos1 = math.floor((pos[0] - 50)/CELL_SIZE)
        pos2 = math.floor((pos[1] - 50)/CELL_SIZE)

        if not (0 <= pos1 < 9 and 0 <= pos2 < 9):
            return
        shape_surf = pg.Surface((CELL_SIZE, CELL_SIZE*9), pg.SRCALPHA)
        pg.draw.rect(shape_surf, (0, 0, 255, 127), shape_surf.get_rect())
        surf.blit(shape_surf, (CELL_SIZE*pos1, 0))

        shape_surf = pg.Surface((CELL_SIZE*9, CELL_SIZE), pg.SRCALPHA)
        pg.draw.rect(shape_surf, (0, 0, 255, 127), shape_surf.get_rect())
        surf.blit(shape_surf, (0, CELL_SIZE*pos2))









pg.init()

screen = pg.display.set_mode((1280*1.5,720*1.5))
running = True

lb = LogicBoard(board3x3_solved)
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



    screen.blit(surf1, (50, 50))
    pg.display.flip()

pg.quit()