import pygame as pg

def draw_visual_board():
    surface = pg.Surface(((40*9)+3, (40*9)+3))
    surface.fill("white")
    for i in range(10):
        width = 1
        if i % 3 == 0:
            width = 3
        pg.draw.line(surface, "black", (0, (40*i)+1.5), ((40*9)+2, (40*i)+1.5), width)
        pg.draw.line(surface, "black", ((40*i)+1.5, 0), ((40*i)+1.5, (40*9)+2), width)
    return surface

pg.init()

screen = pg.display.set_mode((1280*1.5,720*1.5))
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("white")
    screen.blit(draw_visual_board(), (50, 50))
    pg.display.flip()

pg.quit()