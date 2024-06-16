import pygame as pg 

from settings import *

pg.init()
clock = pg.time.Clock()

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
    #Render level
   
    l1.update()

    #Draw player
    player.update()
    #window update
    moving_sprites.draw(screen)
    clock.tick(FPS)
    pg.display.flip()

pg.quit()