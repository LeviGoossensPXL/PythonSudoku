import pygame as pg

def draw_visual_board(surface):
    for i in range(1, 11):
        width = 1
        if (i-1) % 3 == 0:
            width = 3
        pg.draw.line(surface, "black", (40, 40*i), (40+(40*9), 40*i), width)
        pg.draw.line(surface, "black", (40*i, 40), (40*i, 40+(40*9)), width)

pg.init()

screen = pg.display.set_mode((1280*1.5,720*1.5))
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("white")
    draw_visual_board(screen)
    pg.display.flip()

pg.quit()


