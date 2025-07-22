import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "Hero Smash"

from pgzero.actor import Actor
from pygame import Rect
import random
import math

player = Actor('character_maleadventurer_idle', (400, 300))  # Começar no meio da tela
player.vx = 0
player.vy = 0
player.on_ground = False
player.animation_frame = 0
player.animation_timer = 0
player.state = "idle"
player.health = 100
player.attacking = False
player.attack_timer = 0

# Sistema de pontuação
score = 0
enemies_defeated = 0

# Lista de inimigos
enemies = []

platforms = []

ground = Actor('platform', (400, 590))
platforms.append(ground)

def create_enemy(x, y):
    """Cria um novo inimigo robô"""
    # Temporariamente usando sprite do herói, depois você substitui por robô
    enemy = Actor('character_maleadventurer_idle', (x, y))
    enemy.vx = 0
    enemy.vy = 0
    enemy.on_ground = False
    enemy.health = 50
    enemy.direction = 1  # 1 = direita, -1 = esquerda
    enemy.move_timer = 0
    enemy.state = "idle"
    enemy.animation_frame = 0
    enemy.animation_timer = 0
    enemy.is_enemy = True
    return enemy

# Criar alguns inimigos iniciais
enemies.append(create_enemy(600, 300))
enemies.append(create_enemy(200, 300))

def draw():
    screen.clear()
    screen.fill((135, 206, 235))
    
    # Desenhar plataformas
    for platform in platforms:
        platform.draw()
    
    # Desenhar inimigos
    for enemy in enemies:
        enemy.draw()
        # Barra de vida do inimigo
        bar_width = 40
        bar_height = 5
        health_percent = enemy.health / 50
        screen.draw.filled_rect(
            Rect(enemy.x - bar_width//2, enemy.y - 40, bar_width, bar_height), 
            (255, 0, 0)
        )
        screen.draw.filled_rect(
            Rect(enemy.x - bar_width//2, enemy.y - 40, bar_width * health_percent, bar_height), 
            (0, 255, 0)
        )
    
    # Desenhar player
    player.draw()
    
    # Interface do jogo
    screen.draw.text(f"Pontuação: {score}", (10, 10), color="white", fontsize=30)
    screen.draw.text(f"Robôs Derrotados: {enemies_defeated}", (10, 50), color="white", fontsize=25)
    screen.draw.text(f"Vida: {player.health}", (10, 90), color="white", fontsize=25)
    screen.draw.text(f"Inimigos Restantes: {len(enemies)}", (10, 130), color="white", fontsize=25)
    
    # Instruções
    screen.draw.text("CONTROLES:", (WIDTH - 200, 10), color="yellow", fontsize=20)
    screen.draw.text("Z = Atacar", (WIDTH - 200, 35), color="white", fontsize=18)
    screen.draw.text("Setas = Mover", (WIDTH - 200, 60), color="white", fontsize=18)
    screen.draw.text("Shift + Setas = Correr", (WIDTH - 200, 85), color="white", fontsize=18)

def update():
    global score, enemies_defeated
    
    # Atualizar player
    gravity = 0.5
    player.vy += gravity
    player.x += player.vx
    player.y += player.vy

    # Atualizar timer de ataque
    if player.attacking:
        player.attack_timer -= 1
        if player.attack_timer <= 0:
            player.attacking = False

    # Colisão do player com plataformas
    player.on_ground = False
    for platform in platforms:
        if player.colliderect(platform) and player.vy >= 0:
            player.bottom = platform.top
            player.vy = 0
            player.on_ground = True
            break

    # Atualizar inimigos
    for enemy in enemies[:]:  # [:] faz uma cópia da lista
        # Física do inimigo
        enemy.vy += gravity
        enemy.x += enemy.vx
        enemy.y += enemy.vy
        
        # Colisão do inimigo com plataformas
        enemy.on_ground = False
        for platform in platforms:
            if enemy.colliderect(platform) and enemy.vy >= 0:
                enemy.bottom = platform.top
                enemy.vy = 0
                enemy.on_ground = True
                break
        
        # IA simples do inimigo
        enemy.move_timer += 1
        if enemy.move_timer >= 60:  # Muda direção a cada 60 frames (1 segundo)
            enemy.direction *= -1
            enemy.move_timer = 0
        
        enemy.vx = enemy.direction * 1  # Velocidade lenta
        
        # Impedir que inimigo saia da tela
        if enemy.left < 0 or enemy.right > WIDTH:
            enemy.direction *= -1
        
        # Verificar colisão com ataque do player
        if player.attacking and player.colliderect(enemy):
            enemy.health -= 25
            if enemy.health <= 0:
                enemies.remove(enemy)
                score += 100
                enemies_defeated += 1
                # Criar novo inimigo após um tempo
                if len(enemies) < 3:  # Máximo 3 inimigos na tela
                    import random
                    new_x = random.randint(100, WIDTH - 100)
                    enemies.append(create_enemy(new_x, 300))

    # Impedir que o player saia da tela
    if player.left < 0:
        player.left = 0
    elif player.right > WIDTH:
        player.right = WIDTH

    # Determinar estado do player
    if player.attacking:
        player.state = "attacking"
    elif not player.on_ground:
        player.state = "jumping"
    elif keyboard.down:
        player.state = "crouching"
    elif abs(player.vx) > 0:
        if abs(player.vx) >= 5:
            player.state = "running"
        else:
            player.state = "walking"
    else:
        player.state = "idle"

    update_player_animation()
    update_enemies_animation()

def update_player_animation():
    """Atualiza a animação do player baseado no seu estado"""
    player.animation_timer += 1
    
    if player.state == "attacking":
        # Animação de ataque - alternar entre os 3 sprites de ataque
        if player.animation_timer >= 5:
            player.animation_frame = (player.animation_frame + 1) % 3
            player.animation_timer = 0
        player.image = f"character_maleadventurer_attack{player.animation_frame}"
    
    elif player.state == "idle":
        player.image = "character_maleadventurer_idle"
    
    elif player.state == "walking":
        if player.animation_timer >= 8:
            player.animation_frame = (player.animation_frame + 1) % 8
            player.animation_timer = 0
        player.image = f"character_maleadventurer_walk{player.animation_frame}"
    
    elif player.state == "running":
        if player.animation_timer >= 5:
            player.animation_frame = (player.animation_frame + 1) % 3  
            player.animation_timer = 0
        player.image = f"character_maleadventurer_run{player.animation_frame}"
    
    elif player.state == "jumping":
        if player.vy < 0:
            player.image = "character_maleadventurer_jump"
        else:
            player.image = "character_maleadventurer_fall"
    
    elif player.state == "crouching":
        player.image = "character_maleadventurer_duck"

def update_enemies_animation():
    """Atualiza a animação dos inimigos"""
    for enemy in enemies:
        enemy.animation_timer += 1
        
        if abs(enemy.vx) > 0:  # Se está se movendo
            if enemy.animation_timer >= 10:
                enemy.animation_frame = (enemy.animation_frame + 1) % 8
                enemy.animation_timer = 0
            enemy.image = f"character_maleadventurer_walk{enemy.animation_frame}"
        else:
            enemy.image = "character_maleadventurer_idle"

def on_key_down(key):
    if key == keys.LEFT:
        if keyboard.lshift or keyboard.rshift:
            player.vx = -5
        else:
            player.vx = -3
    elif key == keys.RIGHT:
        if keyboard.lshift or keyboard.rshift:
            player.vx = 5
        else:
            player.vx = 3
    elif key == keys.SPACE and player.on_ground:
        player.vy = -10
    elif key == keys.DOWN:
        pass
    elif key == keys.Z:  # Tecla de ataque
        if not player.attacking:
            player.attacking = True
            player.attack_timer = 15  # Duração do ataque em frames

def on_key_up(key):
    if key == keys.LEFT or key == keys.RIGHT:
        player.vx = 0

pgzrun.go()