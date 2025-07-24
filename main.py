import pgzrun
import math
import random
from pygame import Rect

WIDTH = 800
HEIGHT = 600
TITLE = "Breaking Hero"

MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"

game_state = MENU
music_enabled = True
sounds_enabled = True

current_wave = 1
max_waves = 3
enemies_spawned = False

def init_audio():
    global music_enabled
    if music_enabled:
        try:
            music.play('background_music')
            music.set_volume(0.5)
        except:
            pass

class Hero:
    def __init__(self):
        self.actor = Actor('hero')
        self.actor.pos = (100, 400)
        
        self.ground_level = 430
        self.actor.y = self.ground_level
        
        self.direction = 1
        self.velocity_y = 0
        self.on_ground = True
        self.gravity = 0.8
        self.jump_force = -15
        self.speed = 200
        
        self.health = 100
        self.max_health = 100
        self.is_dead = False
        self.attack_timer = 0
        self.attack_duration = 0.6
        
        self.state = 'idle'
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.15
        
        self.animations = {
            'idle': ['hero'],
            'walking': ['hero_walk', 'hero_walk2', 'hero_walk3', 'hero_walk4', 'hero_walk5', 'hero_walk6', 'hero_walk7'],
            'jumping': ['hero_jump', 'hero_jump2'],
            'attacking': ['hero_attack', 'hero_attack1', 'hero_attack2', 'hero_attack3'],
            'dead': ['hero_down2']
        }
        
        self.animations_left = {
            'idle': ['hero'],
            'walking': ['hero_walk_left', 'hero_walk2_left', 'hero_walk3_left', 'hero_walk4_left', 'hero_walk5_left', 'hero_walk6_left', 'hero_walk7_left'],
            'jumping': ['hero_jump_left', 'hero_jump2_left'],
            'attacking': ['hero_attack_left', 'hero_attack1_left', 'hero_attack2_left', 'hero_attack3_left'],
            'dead': ['hero_down2']
        }
        
    def update(self, dt):
        if self.is_dead:
            self.state = 'dead'
            if keyboard.r:
                self.revive()
            return
            
        self.animation_timer += dt
        self.attack_timer -= dt
        
        moving = False
        if keyboard.left:
            self.actor.x -= self.speed * dt
            self.direction = -1
            moving = True
        if keyboard.right:
            self.actor.x += self.speed * dt
            self.direction = 1
            moving = True

        if keyboard.space and self.on_ground:
            self.velocity_y = self.jump_force
            self.on_ground = False
            if sounds_enabled:
                try:
                    sounds.jump.play()
                except:
                    pass
            
        if keyboard.x and self.attack_timer <= 0:
            self.state = 'attacking'
            self.attack_timer = self.attack_duration
            if sounds_enabled:
                try:
                    sounds.attack.play()
                except:
                    pass
            
        if self.attack_timer > 0:
            self.state = 'attacking'
        elif not self.on_ground:
            self.state = 'jumping'
        elif moving:
            self.state = 'walking'
        else:
            self.state = 'idle'
            
        if not self.on_ground:
            self.velocity_y += self.gravity
            self.actor.y += self.velocity_y
            if self.actor.y >= self.ground_level:
                self.actor.y = self.ground_level
                self.velocity_y = 0
                self.on_ground = True
                
        self.actor.x = max(50, min(WIDTH - 50, self.actor.x))
        
        self.update_animation()
        
    def update_animation(self):
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            
            if self.direction == -1:
                current_animation = self.animations_left[self.state]
            else:
                current_animation = self.animations[self.state]
                
            if self.state != 'dead':
                self.animation_frame = (self.animation_frame + 1) % len(current_animation)
            self.actor.image = current_animation[self.animation_frame]
            
    def take_damage(self, damage):
        if not self.is_dead:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.is_dead = True
                
    def revive(self):
        self.is_dead = False
        self.health = self.max_health
        self.state = 'idle'
        
    def draw(self):
        self.actor.draw()

class Enemy:
    def __init__(self, x, y, enemy_type="normal"):
        self.actor = Actor('alienblue_stand')
        
        self.ground_level = 420
        self.actor.pos = (x, self.ground_level)
        
        self.enemy_type = enemy_type
        self.direction = 1
        self.start_x = x
        self.health = 30
        self.is_dead = False
        
        self.attack_timer = 0
        self.attack_duration = 0.8
        self.attack_range = 50
        
        if enemy_type == "fast":
            self.speed = 120
            self.patrol_range = 200
            self.detection_range = 150
            self.damage = 10
            self.attack_cooldown = 1.5
        else:
            self.speed = 60
            self.patrol_range = 150
            self.detection_range = 120
            self.damage = 15
            self.attack_cooldown = 2.0
            

        self.state = 'patrol'
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.2
        
        self.animations = {
            'patrol': ['alienblue_walk1', 'alienblue_walk2'],
            'chase': ['alienblue_swim1', 'alienblue_swim2'],
            'attack': ['alienblue_swim1', 'alienblue_swim2'],
            'dead': ['alienblue_hurt']
        }
        
        self.animations_left = {
            'patrol': ['alienblue_walk1_left', 'alienblue_walk2_left'],
            'chase': ['alienblue_swim1_left', 'alienblue_swim2_left'],
            'attack': ['alienblue_swim1_left', 'alienblue_swim2_left'],
            'dead': ['alienblue_hurt_left']
        }
        
    def update(self, dt, hero):
        if self.is_dead:
            self.state = 'dead'
            return
            
        self.animation_timer += dt
        self.attack_timer -= dt
        distance_to_hero = abs(self.actor.x - hero.actor.x)
        
        if (not hero.is_dead and distance_to_hero <= self.attack_range and 
            self.attack_timer <= 0):
            self.state = 'attack'
            self.attack_timer = self.attack_cooldown
            hero.take_damage(self.damage)
            if sounds_enabled:
                try:
                    sounds.enemy_attack.play()
                except:
                    pass

        elif (not hero.is_dead and distance_to_hero <= self.detection_range and
              distance_to_hero > self.attack_range):
            self.state = 'chase'
            if hero.actor.x < self.actor.x:
                self.direction = -1
                self.actor.x -= self.speed * dt
            else:
                self.direction = 1
                self.actor.x += self.speed * dt
                
        else:
            self.state = 'patrol'
            if self.actor.x <= self.start_x - self.patrol_range:
                self.direction = 1
            elif self.actor.x >= self.start_x + self.patrol_range:
                self.direction = -1
            self.actor.x += self.direction * self.speed * 0.5 * dt
            
        if (hero.state == 'attacking' and distance_to_hero <= 60 and not self.is_dead):
            self.take_damage(50)
            if sounds_enabled:
                try:
                    sounds.enemy_hurt.play()
                except:
                    pass
            
        self.actor.x = max(50, min(WIDTH - 50, self.actor.x))
        self.update_animation()
        
    def take_damage(self, damage):
        if not self.is_dead:
            self.health -= damage
            if self.health <= 0:
                self.is_dead = True
                
    def update_animation(self):
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            
            if self.direction == -1:
                current_animation = self.animations_left[self.state]
            else:
                current_animation = self.animations[self.state]
                
            if self.state != 'dead':
                self.animation_frame = (self.animation_frame + 1) % len(current_animation)
            self.actor.image = current_animation[self.animation_frame]
            
    def draw(self):
        self.actor.draw()
        if not self.is_dead and self.health < 30:
            bar_width = 30
            bar_height = 4
            bar_x = self.actor.x - bar_width // 2
            bar_y = self.actor.y - self.actor.height // 2 - 10
            
            screen.draw.filled_rect(Rect(bar_x, bar_y, bar_width, bar_height), (139, 0, 0))

            health_width = int((self.health / 30) * bar_width)
            screen.draw.filled_rect(Rect(bar_x, bar_y, health_width, bar_height), (0, 128, 0))

hero = Hero()
enemies = []

def spawn_wave(wave_number):
    """Spawna inimigos baseado no número da onda"""
    global enemies
    enemies = []
    
    if wave_number == 1:
        enemies.append(Enemy(400, 420, "normal"))
    elif wave_number == 2:
        enemies.append(Enemy(350, 420, "normal"))
        enemies.append(Enemy(450, 420, "fast"))
    elif wave_number == 3:
        enemies.append(Enemy(300, 420, "normal"))
        enemies.append(Enemy(400, 420, "fast"))
        enemies.append(Enemy(500, 420, "normal"))

def reset_game():
    global hero, enemies, current_wave, enemies_spawned
    hero = Hero()
    current_wave = 1
    enemies_spawned = False
    spawn_wave(current_wave)

def update(dt):
    global game_state, current_wave, enemies_spawned
    
    if game_state == MENU:
        pass
    elif game_state == PLAYING:
        if not enemies_spawned:
            spawn_wave(current_wave)
            enemies_spawned = True
            
        hero.update(dt)
        for enemy in enemies:
            enemy.update(dt, hero)
            
        if hero.is_dead:
            game_state = GAME_OVER
        if all(enemy.is_dead for enemy in enemies):
            if current_wave < max_waves:
                # Next wave
                current_wave += 1
                enemies_spawned = False
            else:
                game_state = GAME_OVER
            
    elif game_state == GAME_OVER:
        if keyboard.r:
            reset_game()
            game_state = PLAYING

def draw():
    screen.fill((135, 206, 235))
    
    if game_state == MENU:
        draw_menu()
    elif game_state == PLAYING:
        draw_game()
    elif game_state == GAME_OVER:
        draw_game_over()

def draw_menu():
    screen.draw.text("HERO BATTLE", center=(WIDTH//2, 150), fontsize=60, color="white")
    
    start_button = Rect(WIDTH//2 - 100, 250, 200, 50)
    music_button = Rect(WIDTH//2 - 100, 320, 200, 50)
    exit_button = Rect(WIDTH//2 - 100, 390, 200, 50)
    
    screen.draw.filled_rect(start_button, (0, 128, 0))
    screen.draw.filled_rect(music_button, (0, 0, 128))
    screen.draw.filled_rect(exit_button, (128, 0, 0))
    
    screen.draw.text("START GAME", center=start_button.center, fontsize=30, color="white")
    music_text = f"MUSIC: {'ON' if music_enabled else 'OFF'}"
    screen.draw.text(music_text, center=music_button.center, fontsize=30, color="white")
    screen.draw.text("EXIT", center=exit_button.center, fontsize=30, color="white")

def draw_game():
    screen.draw.filled_rect(Rect(0, 450, WIDTH, 150), (34, 139, 34))
    
    hero.draw()
    for enemy in enemies:
        enemy.draw()
    
    screen.draw.text("ARROWS: Move | SPACE: Jump | X: Attack", (10, 10), fontsize=20, color="white")
    screen.draw.text(f"Health: {hero.health}/100", (10, 40), fontsize=20, 
                    color="green" if hero.health > 50 else "red")
    
    alive_enemies = sum(1 for enemy in enemies if not enemy.is_dead)
    screen.draw.text(f"Enemies: {alive_enemies}", (WIDTH - 150, 10), fontsize=20, color="orange")

def draw_game_over():
    draw_game()
    
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (0, 0, 0, 128))
    
    if hero.is_dead:
        screen.draw.text("GAME OVER!", center=(WIDTH//2, HEIGHT//2 - 50), fontsize=48, color="red")
        screen.draw.text("Press R to restart", center=(WIDTH//2, HEIGHT//2), fontsize=24, color="white")
    else:
        screen.draw.text("VICTORY!", center=(WIDTH//2, HEIGHT//2 - 50), fontsize=48, color="gold")
        screen.draw.text("All enemies defeated!", center=(WIDTH//2, HEIGHT//2), fontsize=24, color="white")
        screen.draw.text("Press R to restart", center=(WIDTH//2, HEIGHT//2 + 30), fontsize=24, color="white")

def on_mouse_down(pos):
    global game_state, music_enabled
    
    if game_state == MENU:
        start_button = Rect(WIDTH//2 - 100, 250, 200, 50)
        music_button = Rect(WIDTH//2 - 100, 320, 200, 50)
        exit_button = Rect(WIDTH//2 - 100, 390, 200, 50)
        
        if start_button.collidepoint(pos):
            game_state = PLAYING
            reset_game()
            if music_enabled:
                try:
                    music.play('background_music')
                    music.set_volume(0.5)
                except:
                    pass
        elif music_button.collidepoint(pos):
            music_enabled = not music_enabled
            if music_enabled:
                try:
                    music.play('background_music')
                    music.set_volume(0.5)
                except:
                    pass
            else:
                try:
                    music.stop()
                except:
                    pass
        elif exit_button.collidepoint(pos):
            exit()
pgzrun.go()