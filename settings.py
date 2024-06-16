import pygame as pg
import os

from Player import Player
from Level import Level

FPS = 30
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
path = os.path.join(os.getcwd(), 'images')

player = Player(path + "\\player\\", 100, 500)
l1 = Level(path, screen)
moving_sprites = pg.sprite.Group()
moving_sprites.add(player)