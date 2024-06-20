import pygame as pg

import settings

class Obstacle(pg.sprite.Sprite):
    def __init__(self, image, x):
        super().__init__()
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale2x(self.image)
        self.x = x
        self.y = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = self.x, 576-self.y//2

    def draw(self):
        settings.screen.blit(self.image, self.rect)

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.rect.x += 12
        if key[pg.K_RIGHT]:
           self.rect.x -= 12