import pygame as pg

from Bullet import Bullet
import settings

class Player(pg.sprite.Sprite):
    def __init__(self, images, x ,y):
        super().__init__()
        self.x = x
        self.y = y
        self.images = images
        self.state = 'idle'
        self.isJump = False
        self.jumpCount = 10
        self.current_sprite = 0
        self.health = 100
        self.animations = {
            'idle': self._load_images(self.images + 'idle', 2),
            'run': self._load_images(self.images + 'run', 2),
            'shoot': self._load_images(self.images + 'shoot', 2),
            'jump': self._load_images(self.images + 'jump', 1)
        }
        self.image = self.animations[self.state][self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

        self.tick = pg.time.get_ticks()
        self.vel_y = 0
        self.gravity = 0.8

    def _load_images(self, action, num_frames):
        images = []
        for i in range(1, num_frames+1):
            img = pg.image.load(f"{action}{i}.png").convert_alpha()
            images.append(img)
        return images

    def shoot(self, fire_rate):
        current_tick = pg.time.get_ticks()
        if current_tick - self.tick >= fire_rate:
            self.tick = current_tick
            b = Bullet(settings.path + "\\bullet.png", self.rect.x+105, self.rect.y+105, 15)
            settings.l1.bullets.add(b)

    def jump(self):
        if not self.isJump:
            self.isJump = True
            self.vel_y = -15

    def apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        if self.rect.bottom >= 576:  
            self.rect.bottom = 576
            self.vel_y = 0
            self.isJump = False
        
    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_UP]:
            self.state = 'jump'
            self.jump()
        elif key[pg.K_SPACE]:
            self.state = 'shoot'
            self.shoot(250)
        elif key[pg.K_RIGHT]:
            self.state = 'run'
        elif key[pg.K_LEFT]:
            self.state = 'run'
        else:
            self.state = 'idle'

        self.current_sprite += 0.3
        if self.current_sprite >= len(self.animations[self.state]):
            self.current_sprite = 0
        self.image = self.animations[self.state][int(self.current_sprite)]
        
        self.apply_gravity()
        
        