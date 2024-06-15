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
        self.bg_images = []
        for i in range(1, 6):
            self.bg_images.append(pg.image.load(path + f"\\background\{i}.png").convert_alpha())

    def draw_bg(self):
        bg_width = self.bg_images[0].get_width()
        for x in range(10):
            speed = 1
            for i in self.bg_images:
                screen.blit(i, (x * bg_width - scroll * speed, 0))
                speed += 0.3
    def draw_ground():
        pass

class Player(pg.sprite.Sprite):
    def __init__(self, image, cx, cy):
        super().__init__()
        self.image = image
        self.image
        self.rect = self.image.get_rect()
        self.rect.center = cx, cy

    def draw_player(self, surface):
        surface.blit(self.image, self.rect)

player_img = pg.image.load(path + "\player\player.png").convert_alpha()
print(path + "\player.png")
player = Player(player_img, 100, 500)

scroll = 0
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
    #Render level
    l1 = Level()
    l1.draw_bg()
    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
        scroll -= 5
    if key[pg.K_RIGHT]:
        scroll += 5

    #Draw player
    player.draw_player(screen)

    clock.tick(FPS)
    pg.display.flip()

pg.quit()