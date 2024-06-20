import pygame as pg 

from Menu import Menu

from settings import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.clock = pg.time.Clock()
        self.state = 'menu'

    def run(self):
        run = True
        
        while run:
            if self.state == "menu":
                menu = Menu()
                menu.start()
            if self.state == "running":
                    #Render level
                l1.update()
                enemy.draw()
                #Draw player
                player.update()
                enemy.update()   
                #window update
                moving_sprites.draw(screen)
                
                if player.isDead:
                    self.state = "gameover"
            
            if self.state == "gameover":
                menu = Menu()
                menu.end()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.MOUSEBUTTONDOWN and self.state == "menu":
                    if menu.exit_btn.rect.collidepoint(pg.mouse.get_pos()):
                        run = False
                    if menu.start_btn.rect.collidepoint(pg.mouse.get_pos()):
                        self.state = "running"
                if event.type == pg.MOUSEBUTTONDOWN and self.state == "gameover" or self.state == "win":
                    if menu.exit_btn.rect.collidepoint(pg.mouse.get_pos()):
                        run = False
            self.clock.tick(FPS)
            pg.display.flip()

        pg.quit()
