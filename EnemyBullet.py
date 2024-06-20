import pygame as pg
import random
import math

from Bullet import Bullet

class EnemyBullet(Bullet):
    def __init__(self, image, x, y, vel_x, target):
        super().__init__(image, x, y, vel_x)
        self.damage = 34


        random_target_y = random.uniform(target.rect.y - target.image.get_height() / 2, target.rect.y + target.image.get_height() / 2)

        direction_x = target.rect.x - x
        direction_y = random_target_y - y
        angle = math.atan2(direction_y, direction_x)
        self.image = pg.transform.rotate(self.image, angle)
    
        self.vel_x = vel_x * math.cos(angle) 
        self.vel_y = vel_x * math.sin(angle)

    def update(self):
        key = pg.key.get_pressed()
        self.rect.x += self.vel_x - 5
        self.rect.y += self.vel_y
        if key[pg.K_RIGHT]:
             self.rect.centerx -= self.vel_x + 20
        elif key[pg.K_LEFT]:
            self.rect.centerx -= self.vel_x 
        else:
            self.rect.centerx -= self.vel_x + 10
        
        #if self.rect.centerx < 0:
           # self.kill()
        if self.rect.right < 0 or self.rect.left > pg.display.get_surface().get_width() or self.rect.bottom < 0 or self.rect.top > pg.display.get_surface().get_height():
            self.kill()