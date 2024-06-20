import pygame as pg

from EnemyBullet import EnemyBullet

import settings

class Enemy(pg.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pg.image.load(image)
        self.image = pg.transform.scale_by(self.image, 8)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

        self.health = 100
        self.isDead = False
        self.isHit = False
        self.tick = pg.time.get_ticks()

    def draw(self):
        settings.screen.blit(self.image, self.rect)

    def attack(self):
        current_tick = pg.time.get_ticks()
        if current_tick - self.tick >= 1000:
            self.tick = current_tick
            settings.l1.bullets.add(
                EnemyBullet(settings.path + "\\enemy\\bullet.png", self.rect.x+50, self.rect.y+52, 30, settings.player)    
                )    


    def update(self):
        if self.isDead:
            self.image = pg.image.load(settings.path + "\\enemy\\dead.png")
            self.image = pg.transform.scale_by(self.image, 8)
            self.rect.centery = self.y+140