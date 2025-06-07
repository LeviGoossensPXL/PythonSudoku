import pygame as pg

CELL_SIZE = 40

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

pg.init()

screen = pg.display.set_mode((1280*1.5,720*1.5))
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("white")
    surf1 = draw_visual_board()
    draw_numbers(surf1)
    screen.blit(surf1, (50, 50))
    pg.display.flip()

pg.quit()