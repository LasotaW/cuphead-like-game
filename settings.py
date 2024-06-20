import pygame as pg
import os

from Player import Player
from Level import Level
from Enemy import Enemy

FPS = 30
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
path = os.path.join(os.getcwd(), 'images')
music_path = os.path.join(os.getcwd(), 'sounds')

pg.mixer.init()
jump_sound = pg.mixer.Sound(music_path + "\\jump.ogg")
hit_sound = pg.mixer.Sound(music_path + "\\hit.ogg")
death_sound = pg.mixer.Sound(music_path + "\\death.ogg")
shot_sound = pg.mixer.Sound(music_path + "\\shot.ogg")
damage_sound = pg.mixer.Sound(music_path + "\\damage.ogg")
enemy_shot_sound = pg.mixer.Sound(music_path + "\\enemy_shot.ogg")

player = Player(path + "\\player\\", 100, 500)
l1 = Level(path, screen)
enemy = Enemy(path + "\\enemy\\idle1.png", 3500, 470)
moving_sprites = pg.sprite.Group()
moving_sprites.add(player)