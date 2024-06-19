import pygame as pg

from Button import Button

from settings import SCREEN_HEIGHT, SCREEN_WIDTH, screen

BLACK = pg.color.THECOLORS["black"]
WHITE = pg.color.THECOLORS["white"]

class Menu:
    def __init__(self):
        self.start_btn = Button("START", BLACK, WHITE, 200, 100, SCREEN_WIDTH//2, SCREEN_HEIGHT//2-100, 36, "Arial")
        self.exit_btn = Button("WYJŚCIE", BLACK, WHITE, 200, 100, SCREEN_WIDTH//2, SCREEN_HEIGHT//2+100, 36, "Arial")

    def update(self):
        self.start_btn.draw(screen)
        self.exit_btn.draw(screen)