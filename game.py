import pgzrun # Importar a biblioteca pygame para iniciar o jogo

WIDTH = 800 # Largura da janela do jogo
HEIGHT = 600 # Altura da janela do jogo
TITLE = "Hero Smash" # Título da janela do jogo

# Vamos importar as classes e funções necessárias

from pgzero.actor import Actor # importar a classe de sprite
from pygame import Rect # importar a classe de retangulos do PYGAME (OBS: FOI PERMITIDO PELAS DOCS)
import random # Importar biblioteca para gravidade // colisão
import math # importar biblioteca para gravidade // colisão


# agora vamos trabalhar com o player
player = Actor('hero', (0, 0)) # posição do sprite + import do sprie
player.vx = 0 # velocidade horizontal que ele vai andar
player.vy = 0 # velocidade na vertical que ele vai pular
player.on_ground = True # Se o player está no chão
player.animation_frame = 0 # Frame da animação do player
player.animation_timer = 0 # Timer da animação do player
player.state = "idle" # definir estado do player (INICIAL)

# trabalhar com as plataformas
platforms = [] # Lista de plataformas
ground = Actor('platform', (400, 590))  # sprite de plataforma do chão
ground.width = 800  # definir largura da plataforma do chão
ground.height = 20  # definir altura da plataforma do chão
