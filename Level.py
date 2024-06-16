import pygame as pg

class Level:
    def __init__(self, path, surface):
        self.scroll = 0
        self.surface = surface
        self.bg_images = []
        for i in range(1, 6):
            self.bg_images.append(pg.image.load(path + f"\\background\\{i}.png").convert_alpha())
        self.bullets = pg.sprite.Group()

    def draw_bg(self):
        bg_width = self.bg_images[0].get_width()
        for x in range(3):
            speed = 1
            for i in self.bg_images:
                if self.scroll < 0:
                     self.scroll = 0
                self.surface.blit(i, (x * bg_width - self.scroll * speed, 0))
                speed += 0.3

        self.bullets.draw(self.surface)

    def draw_ground(self):
        pass

    def update(self):
        self.bullets.update()

        self.draw_bg()
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.scroll -= 5
        if key[pg.K_RIGHT]:
            self.scroll += 5