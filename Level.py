import pygame as pg
import random

import settings

from EnemyBullet import EnemyBullet
from Obstacle import Obstacle

class Level:
    def __init__(self, path, surface):
        self.scroll = 0
        self.surface = surface
        self.bg_images = []
        for i in range(1, 6):
            self.bg_images.append(pg.image.load(path + f"\\background\\{i}.png").convert_alpha())
        self.bullets = pg.sprite.Group()
        self.obstacles = pg.sprite.Group()

        for i in range(5):
            rand_obstacle = random.randint(1,5)
            o = Obstacle(path + f"\\obstacle\\{rand_obstacle}.png",i * 1.5 *(random.randint(500,800)))
            self.obstacles.add(o)

    def draw_bg(self):
        bg_width = self.bg_images[0].get_width()
        for x in range(5):
            speed = 1
            for i in self.bg_images:
                if self.scroll < 0:
                     self.scroll = 0
                elif self.scroll > bg_width * 1.5:
                    self.scroll = bg_width * 1.5
                self.surface.blit(i, (x * bg_width - self.scroll * speed, 0))
                speed += 0.3

        self.bullets.draw(self.surface)
        

    def update(self):
        self.bullets.update()

        self.draw_bg()
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            if self.scroll > 0:
                self.scroll -= 5
                settings.enemy.rect.centerx += 12
        if key[pg.K_RIGHT]:
            self.scroll += 5
            settings.enemy.rect.centerx -= 12

        bullet_hit = pg.sprite.spritecollideany(settings.enemy, self.bullets)
        if bullet_hit and not isinstance(bullet_hit,EnemyBullet) and not settings.enemy.isDead:
            settings.hit_sound.play()
            bullet_hit.kill()
            settings.enemy.isHit = True
            settings.enemy.health -= bullet_hit.damage
            if settings.enemy.health <= 0:
                pg.mixer.quit()
                pg.mixer.init()
                settings.death_sound.play()
                settings.enemy.isDead = True


        if settings.enemy.x - self.scroll * 2.5 <= 750 and not settings.enemy.isDead:
            settings.enemy.attack()

        enemy_bullet_hit = pg.sprite.spritecollideany(settings.player, self.bullets)
        if enemy_bullet_hit and isinstance(enemy_bullet_hit, EnemyBullet):
            enemy_bullet_hit.kill()
            settings.player.health -= enemy_bullet_hit.damage
            if settings.player.health <= 0:
                settings.player.isDead = True

        
                