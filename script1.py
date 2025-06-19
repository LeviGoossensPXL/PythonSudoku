import math
import random
import time

import pygame as pg

from LogicBoard import LogicBoard
from VisualBoard import VisualBoard

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

board3x3_unsolved1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],  # < x // 0
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],  # < x // 1
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],

                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],

                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                     #^  ^
                     #y  y
                     #// //
                     #0  1


def algo1(board_su: LogicBoard):
    """solve sudoku brute force at random
     plus: /
     negative: changes original sudoku if algorithm makes any mistakes, gets stuck sometimes mostly when starting from empty, no method or memory for solving"""
    for cell in board_su.get_all_mistakes():
        board_su.modify_number(0, cell[1], cell[0])

    for i in range(board_su.row_and_col_length):
        for j in range(board_su.row_and_col_length):
            if board_su.b[i][j] == 0:
                wrong_list = set()
                correct = False
                while not correct:
                    r = random.randint(1, 9)
                    board_su.b[i][j] = r
                    if len(board_su.get_all_mistakes()) == 0:
                        correct = True
                    else:
                        wrong_list.add(r)
                    if len(wrong_list) == 9:
                        break
                return # for visible algorithm

def algo2(board_su: LogicBoard):
    #use while loop because the pointer to the sudoku grid moves froward and backward at random

    # go list off
    # if cell is empty:
    # if solution(s) can be found for cell
    # then pick a random solution for cell
    # if solution is found for a cell
    # then go back to previous solution of cell
    # if previous cell has only 1 solution make it empty
    # Do till you find a cell with minimum 2 solutions
    # if cell has minimum 2 solutions
    # then mark the one already in the cell as wrong and pick one of the others
    # begin from this cell again
    # find previous cell with min 2 solution

    pass

pg.init()

screen = pg.display.set_mode((1280*1.5,720*1.5))
running = True

lb = LogicBoard(board3x3_unsolved.copy())
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
                    lb.modify_number(int(event.unicode), pos1, pos2)
            except:
                pass

    screen.fill("white")
    surf1 = vb.draw_visual_board()
    vb.draw_numbers(surf1)
    vb.draw_selection(surf1)
    # algo1(lb)
    # time.sleep(0.5)
    print(lb.get_all_mistakes())
    # for cell in lb.get_all_mistakes(): #allows self healing when user messes sudoku up again after it is solved
    #     lb.modify_number(0, cell[1], cell[0])


    screen.blit(surf1, (50, 50))
    pg.display.flip()

pg.quit()