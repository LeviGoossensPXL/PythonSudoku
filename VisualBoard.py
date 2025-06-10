import math

import pygame as pg
from pygame import Surface

from LogicBoard import LogicBoard

CELL_SIZE = 40

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
            offset = (CELL_SIZE * i) + 1.5
            length = (CELL_SIZE * self.lb.row_and_col_length) + 2
            pg.draw.line(surface, "black", (0, offset), (length, offset), width)
            pg.draw.line(surface, "black", (offset, 0), (offset, length), width)
        return surface

    def draw_numbers(self, surf: Surface):
        """function for drawing the numbers on the board"""
        font = pg.font.SysFont("ubuntu", 35)
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
        return surf

    def draw_selection(self, surf: Surface):
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