import math

import pygame as pg

CELL_SIZE = 40

board = [[9, 9, 9, 9, 9, 9, 9, 9, 9],
         [9, 4, 9, 9, 9, 9, 9, 9, 9],
         [9, 9, 9, 9, 9, 9, 9, 9, 9],

         [9, 5, 9, 9, 9, 9, 9, 9, 9],
         [9, 9, 9, 9, 9, 9, 9, 9, 9],
         [9, 9, 9, 9, 9, 9, 9, 9, 9],

         [9, 9, 9, 9, 9, 9, 9, 9, 9],
         [9, 9, 9, 9, 9, 9, 9, 9, 9],
         [9, 9, 9, 9, 9, 9, 9, 9, 9]]

def draw_visual_board():
    surface = pg.Surface(((CELL_SIZE * 9) + 3, (CELL_SIZE * 9) + 3))
    surface.fill("white")
    for i in range(10):
        width = 1
        if i % 3 == 0:
            width = 3
        pg.draw.line(surface, "black", (0, (CELL_SIZE * i) + 1.5), ((CELL_SIZE * 9) + 2, (CELL_SIZE * i) + 1.5), width)
        pg.draw.line(surface, "black", ((CELL_SIZE * i) + 1.5, 0), ((CELL_SIZE * i) + 1.5, (CELL_SIZE * 9) + 2), width)
    return surface

def draw_numbers(surf):
    font = pg.font.SysFont("ubuntu", 40)
    for i in range(9):
        for j in range(9):
            font_surface = font.render("9", True, "black")
            font_rect = font_surface.get_rect(center=((CELL_SIZE * i) + (CELL_SIZE / 2), (CELL_SIZE * j) + (CELL_SIZE / 2)))
            surf.blit(font_surface, font_rect)
    return surf

def draw_selection(surf):
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

def modify_number(number):
    pos = pg.mouse.get_pos()
    pos1 = math.floor((pos[0] - 50)/CELL_SIZE)
    pos2 = math.floor((pos[1] - 50)/CELL_SIZE)
    if not (0 <= pos1 < 9 and 0 <= pos2 < 9):
        return
    row = board[pos2]
    row[pos1] = int(number)

pg.init()

screen = pg.display.set_mode((1280*1.5,720*1.5))
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            try:
                if 1 <= int(event.unicode) <= 9:
                    modify_number(event.unicode)
            except:
                pass

    screen.fill("white")
    surf1 = draw_visual_board()
    draw_numbers(surf1)
    draw_selection(surf1)
    screen.blit(surf1, (50, 50))
    pg.display.flip()

pg.quit()