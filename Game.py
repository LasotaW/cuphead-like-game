import pygame as pg 

from settings import *
from Menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.state = 'menu'

    def run(self):
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if menu.exit_btn.rect.collidepoint(pg.mouse.get_pos()):
                        run = False
                    if menu.start_btn.rect.collidepoint(pg.mouse.get_pos()):
                        self.state = "running"



            if self.state == "menu":
                        menu = Menu()
                        menu.update()
            if self.state == "running":
                #Render level
                l1.update()
                enemy.draw()
                #Draw player
                player.update()
                enemy.update()   
                #window update
                moving_sprites.draw(screen)
            if self.state == "paused":
                print("PAUSED")


            self.clock.tick(FPS)
            pg.display.flip()

        pg.quit()
