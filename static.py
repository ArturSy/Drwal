import pgzrun
from pgzero.builtins import Actor, keyboard, Rect, animate, sounds
from pgzero.screen import Screen
import pygame
import random
screen: Screen
keys: keyboard
from screeninfo import get_monitors

monitor = get_monitors()[0]


FULLSCREEN = False
WIDTH = 800
HEIGHT = 450

BASE_WIDTH = 1920
BASE_HEIGHT = 1080

FULLSCREEN_WIDTH = monitor.width
FULLSCREEN_HEIGHT = monitor.height

base_kx = WIDTH/BASE_WIDTH
base_ky = HEIGHT/BASE_HEIGHT

def chanege_fullscreen():
    global FULLSCREEN
    FULLSCREEN = not FULLSCREEN

def is_fullscreen():
    return FULLSCREEN


background = Actor('background', pos=(0,0), anchor=(0,0))
bee = Actor('bee_01', pos=(WIDTH-100, HEIGHT/2), anchor=(0,0))
clouds = [Actor(f'chmurka_0{i}', pos=(0,0), anchor= (0,0)) for i in range(1,5)]

trunk_unused = Actor('pien_solo',)
trunk = Actor('pien_solo', pos=(WIDTH/2, 0), anchor=(trunk_unused.width/2, 0))

trunk_base_unused = Actor('pien_podstawa')
trunk_base = Actor('pien_podstawa', pos=(trunk.x+1.5, base_ky*trunk.height), anchor=(trunk_base_unused.width/2, 0))

tree_unused = Actor('pien_caly')
tree = Actor('pien_caly', pos=(WIDTH/2+2, HEIGHT+11), anchor=(tree_unused.width/2, tree_unused.height))

slice_wood_scale = 375/HEIGHT
slice_wood_unused=Actor('plaster_drewna')
slice_wood=Actor('plaster_drewna', pos=(trunk.x, HEIGHT*slice_wood_scale), anchor=(slice_wood_unused.width / 2, 0))
slice_wood_origin=Actor('plaster_drewna', pos=(trunk.x, HEIGHT*slice_wood_scale), anchor=(slice_wood_unused.width/2, 0))

lumberjack_scale = 1040/1080

lumberjack_ready_unused = Actor('drwal_01')
lumberjack_ready = Actor('drwal_01', pos=(trunk.x - trunk.width, HEIGHT*lumberjack_scale), anchor=(0, lumberjack_ready_unused.height))

lumberjack_hit_unused = Actor('drwal_02')
lumberjack_hit = Actor('drwal_02', pos=(trunk.x - trunk.width + 16, HEIGHT*lumberjack_scale), anchor=(0, lumberjack_hit_unused.height))

rip = Actor('rip', pos=(WIDTH/4, HEIGHT*(2/3)), anchor=(0,0))

SCALABLE = [background, bee, trunk, trunk_base, tree, slice_wood, slice_wood_origin, lumberjack_ready, lumberjack_hit, rip] + clouds

cloud_speed = [random.uniform(0.01, 1) for _ in range(4)] 




BLACK = 0,0,0
ORANGE = 255, 125, 0
RED = 255, 0, 0