import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "Hero Smash"

from pgzero.actor import Actor
from pygame import Rect
import random
import math

player = Actor('hero', (100, 500))
player.vx = 0
player.vy = 0
player.on_ground = False

# criando plataformas
platforms = [Rect((0, 580),(800, 20)), Rect((200, 450), (150, 20))]

def draw():
    screen.clear()
    screen.fill((135, 206, 235)) # céu azul
    for platform in platforms:
        screen.draw.filled_rect(platform, (139, 69, 19)) # plataforma marrom (terra)
        player.draw()

def update():
    gravity = 0.5
    player.vy += gravity
    player.x += player.vx
    player.y += player.vy

    player.on_ground = False
    for plat in platforms:
        if player.colliderect(plat) and player.vy >= 0:
            player.y = plat.top
            player.vy = 0
            player.on_ground = True

def on_key_down(key):
    if key == keys.LEFT:
        player.vx = -3
    elif key == keys.RIGHT:
        player.vx = 3
    elif key == keys.SPACE and player.on_ground:
        player.vy = -10 # pulo

def on_key_up(key):
    if key == keys.LEFT or key == keys.RIGHT:
        player.vx = 0  # parar movimento horizontal ao soltar as teclas




pgzrun.go()