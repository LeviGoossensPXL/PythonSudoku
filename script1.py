import math

import pygame as pg

CELL_SIZE = 40

board = [[6, 8, 2, 4, 3, 5, 1, 7, 9], # < x // 0
         [7, 1, 5, 2, 9, 6, 3, 8, 4], # < x // 1
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

def get_board_row(x):
    return board[x]

def get_board_col(y):
    col_list = []
    for row in board:
        col_list.append(row[y])
    return col_list

def get_board_block(x, y):
    block_list = []
    x = math.floor(x/3)
    y = math.floor(y/3)
    for x1 in range(x*3, (x+1)*3):
        for y1 in range(y*3, (y+1)*3):
            block_list.append(board[x1][y1])
    return block_list

def is_cell_correct(x, y):
    unit = board[x][y]
    if get_board_block(x, y).count(unit) > 1:
        print("fout block")
        return False
    if get_board_row(x).count(unit) > 1:
        print("fout row")
        return False
    if get_board_col(y).count(unit) > 1:
        print("fout col")
        return False
    return True

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
    print("XX")
    for i in range(9):
        for j in range(9):
            color = "black"
            if not is_cell_correct(i,j): #TODO: mark only new cell if wrong
                color = "red"
            font_surface = font.render(str(board[i][j]), True, color)
            font_rect = font_surface.get_rect(center=((CELL_SIZE * j) + (CELL_SIZE / 2), (CELL_SIZE * i) + (CELL_SIZE / 2)))
            surf.blit(font_surface, font_rect)
    print("XX")
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