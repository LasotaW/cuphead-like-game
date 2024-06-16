import pygame as pg

import settings

class Bullet(pg.sprite.Sprite):
    def __init__(self, image, x, y, vel_x):
        super().__init__()
        self.image = pg.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def update(self):
        self.rect.centerx += self.vel_x
        if self.rect.centerx > settings.SCREEN_WIDTH:
            self.kill()