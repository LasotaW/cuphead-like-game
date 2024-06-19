import pygame as pg

class Text:
    def __init__(self, text, text_color, x, y, font_size = 36, font_type = None):
        self.text = str(text)
        self.text_color = text_color
        self.font_size = font_size
        self.font_type = font_type
        self.font = pg.font.SysFont(self.font_type, self.font_size)
        self.x = x
        self.y = y
        self.update()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y