import pygame as pg 
import os

pg.init()
clock = pg.time.Clock()
FPS = 60

SCREEN_WIDTH = 1280 
SCREEN_HEIGHT = 720

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

path = os.path.join(os.getcwd(), 'images')
print(path + "\background")


class Level:
    def __init__(self):
        self.bg_images = []
        for i in range(1, 6):
            self.bg_images.append(pg.image.load(path + f"\\background\{i}.png").convert_alpha())

    def draw_bg(self):
        for i in self.bg_images:
            screen.blit(i, (0, 0))

run = True
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
    #Render level
    l1 = Level()
    l1.draw_bg()

    pg.display.update()

pg.quit()