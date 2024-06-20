import pygame as pg

from Button import Button
from Text import Text

from settings import SCREEN_HEIGHT, SCREEN_WIDTH, screen, path

BLACK = pg.color.THECOLORS["black"]
WHITE = pg.color.THECOLORS["white"]

class Menu:
    def __init__(self):
        self.bg_image = pg.image.load(path + "\\background\\bg.png")
        self.bg_image = pg.transform.scale_by(self.bg_image, 0.5)
        self.start_btn = Button("START", BLACK, WHITE, 200, 100, SCREEN_WIDTH//2, SCREEN_HEIGHT//2-100, 36, "Arial")
        self.exit_btn = Button("WYJŚCIE", BLACK, WHITE, 200, 100, SCREEN_WIDTH//2, SCREEN_HEIGHT//2+100, 36, "Arial")

    def start(self):
        screen.blit(self.bg_image, (0,0))
        self.start_btn.draw(screen)
        self.exit_btn.draw(screen)

    def end(self):
        text = Text("PRZEGRANA", WHITE, SCREEN_WIDTH//2, SCREEN_HEIGHT//2-100, 36, "Arial")
        text.draw(screen)
        self.exit_btn.draw(screen)

  
