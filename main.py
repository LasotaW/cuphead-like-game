import pygame as pg 
import os

pg.init()
clock = pg.time.Clock()
FPS = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

path = os.path.join(os.getcwd(), 'images')

class Level:
    def __init__(self):
        self.scroll = 0
        self.bg_images = []
        for i in range(1, 6):
            self.bg_images.append(pg.image.load(path + f"\\background\\{i}.png").convert_alpha())

    def draw_bg(self):
        bg_width = self.bg_images[0].get_width()
        for x in range(3):
            speed = 1
            for i in self.bg_images:
                if self.scroll <= 0:
                     self.scroll = 0
                screen.blit(i, (x * bg_width - self.scroll * speed, 0))
                speed += 0.3
                   

    def draw_ground(self):
        pass

    def update(self):
        self.draw_bg()
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.scroll -= 5
        if key[pg.K_RIGHT]:
            self.scroll += 5


class Player(pg.sprite.Sprite):
    def __init__(self, images, state, x ,y):
        super().__init__()
        self.x = x
        self.y = y
        self.images = images
        self.state = state
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

    def _load_images(self, action, num_frames):
        images = []
        for i in range(1, num_frames+1):
            img = pg.image.load(f"{action}{i}.png").convert_alpha()
            images.append(img)
        return images

    def update(self):
        self.current_sprite += 0.3
        
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self.state = 'shoot'
        elif key[pg.K_UP] and not self.isJump:
            
            self.state = 'jump'
        elif key[pg.K_RIGHT]:
            self.state = 'run'
        elif key[pg.K_LEFT]:
            self.state = 'run'
        else:
            self.state = 'idle'

        if self.current_sprite >= len(self.animations[self.state]):
            self.current_sprite = 0
        
        self.image = self.animations[self.state][int(self.current_sprite)]


class Bullet:
    pass

class Enemy:
    pass

class Boss(Enemy):
    pass

player = Player(path + "\\player\\", 'idle', 100, 500)
l1 = Level()
moving_sprites = pg.sprite.Group()
moving_sprites.add(player)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
    #Render level
   
    l1.update()

    #Draw player
    player.update()
    #window update
    moving_sprites.draw(screen)
    clock.tick(FPS)
    pg.display.flip()

pg.quit()