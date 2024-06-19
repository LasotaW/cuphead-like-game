import pygame as pg

from Text import Text

class Button:
    def __init__(self, text, text_color, bg_color, width, height,
                x, y, font_size=36, font_type=None):
        self.bg_color = bg_color
        self.width = width
        self.height = height
        self.text = Text(text, text_color, x, y, font_size, font_type)
        self.rect = pg.Rect(0,0, self.width, self.height)
        self.rect.center = self.text.rect.center

    def draw(self, surface):
        surface.fill(self.bg_color, self.rect)
        self.text.update()
        self.text.draw(surface)

