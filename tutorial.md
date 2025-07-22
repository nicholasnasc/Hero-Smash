# Hero Smash - Tutorial Completo 🎮⚔️

Um jogo de luta 2D desenvolvido em Python usando a biblioteca Pygame Zero. Controle um aventureiro e derrote robôs inimigos para ganhar pontos!

![Game Preview](https://img.shields.io/badge/Status-Funcional-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Pygame Zero](https://img.shields.io/badge/Pygame%20Zero-1.2+-orange)

## 📖 Índice
- [Sobre o Pygame Zero](#sobre-o-pygame-zero)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Funciona](#como-funciona)
- [Tutorial de Desenvolvimento](#tutorial-de-desenvolvimento)
- [Controles do Jogo](#controles-do-jogo)
- [Como Executar](#como-executar)
- [Conceitos Aprendidos](#conceitos-aprendidos)

## 🎯 Sobre o Pygame Zero

**Pygame Zero** é uma biblioteca Python que simplifica a criação de jogos 2D. É uma versão mais simples do Pygame tradicional, criada especificamente para iniciantes.

### Por que Pygame Zero?
- ✅ **Sintaxe simples**: Não precisa de classes complexas ou gerenciamento manual de eventos
- ✅ **Funcionalidades automáticas**: Carregamento automático de sprites, sons e música
- ✅ **Estrutura pré-definida**: Funções `draw()`, `update()` e eventos já organizados
- ✅ **Ideal para aprender**: Foca na lógica do jogo, não na programação complexa

### Diferenças do Pygame tradicional:
```python
# Pygame tradicional (complexo)
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
# ... muito mais código

# Pygame Zero (simples)
WIDTH = 800
HEIGHT = 600
def draw():
    screen.fill((0, 0, 0))
```

## 📁 Estrutura do Projeto

```
Hero-Smash/
├── main.py                    # Arquivo principal do jogo
├── images/                    # Pasta de sprites
│   ├── character_maleadventurer_idle.png
│   ├── character_maleadventurer_walk0.png
│   ├── character_maleadventurer_walk1.png
│   ├── character_maleadventurer_walk2.png
│   ├── character_maleadventurer_walk3.png
│   ├── character_maleadventurer_walk4.png
│   ├── character_maleadventurer_walk5.png
│   ├── character_maleadventurer_walk6.png
│   ├── character_maleadventurer_walk7.png
│   ├── character_maleadventurer_run0.png
│   ├── character_maleadventurer_run1.png
│   ├── character_maleadventurer_run2.png
│   ├── character_maleadventurer_jump.png
│   ├── character_maleadventurer_fall.png
│   ├── character_maleadventurer_duck.png
│   ├── character_maleadventurer_attack0.png
│   ├── character_maleadventurer_attack1.png
│   ├── character_maleadventurer_attack2.png
│   └── platform.png
└── README.md                  # Este arquivo
```

## 🎮 Como Funciona

### 1. **Inicialização do Jogo**
```python
import pgzrun
WIDTH = 800
HEIGHT = 600
TITLE = "Hero Smash"
```
- Define o tamanho da janela (800x600 pixels)
- Define o título da janela
- `pgzrun` é necessário no final para executar o jogo

### 2. **Criação do Personagem Principal**
```python
player = Actor('character_maleadventurer_idle', (400, 300))
player.vx = 0  # velocidade horizontal
player.vy = 0  # velocidade vertical
player.on_ground = False  # está no chão?
player.state = "idle"  # estado atual (parado, andando, etc.)
```

**Por que usar Actor?**
- `Actor` é a classe principal do Pygame Zero para sprites
- Automaticamente carrega a imagem da pasta `images/`
- Tem propriedades úteis como `.x`, `.y`, `.left`, `.right`, `.top`, `.bottom`
- Tem métodos como `.draw()` e `.colliderect()`

### 3. **Sistema de Animação**
```python
def update_player_animation():
    if player.state == "walking":
        # Alterna entre walk0, walk1, walk2... walk7
        player.image = f"character_maleadventurer_walk{player.animation_frame}"
```

**Como funciona:**
- Cada estado (idle, walking, running, jumping) tem sprites diferentes
- Um timer controla quando trocar de frame
- `player.animation_frame` controla qual sprite mostrar

### 4. **Sistema de Física**
```python
def update():
    gravity = 0.5
    player.vy += gravity  # Aplica gravidade
    player.x += player.vx  # Move horizontalmente
    player.y += player.vy  # Move verticalmente
```

**Conceitos físicos:**
- **Gravidade**: Puxa o personagem para baixo constantemente
- **Velocidade horizontal (vx)**: Controla movimento esquerda/direita
- **Velocidade vertical (vy)**: Controla pulos e quedas

### 5. **Sistema de Colisão**
```python
for platform in platforms:
    if player.colliderect(platform) and player.vy >= 0:
        player.bottom = platform.top  # Põe o player em cima da plataforma
        player.vy = 0  # Para a queda
        player.on_ground = True  # Marca que está no chão
```

**Por que `player.bottom = platform.top`?**
- `player.bottom`: A parte inferior do sprite do player
- `platform.top`: A parte superior da plataforma
- Isso garante que o player fique exatamente em cima da plataforma

### 6. **Sistema de Inimigos com IA**
```python
def create_enemy(x, y):
    enemy = Actor('character_maleadventurer_idle', (x, y))
    enemy.direction = 1  # 1 = direita, -1 = esquerda
    enemy.move_timer = 0
    enemy.health = 50
    return enemy
```

**IA Simples:**
- Inimigos se movem automaticamente
- Mudam de direção a cada 60 frames (1 segundo)
- Não saem da tela (invertem direção nas bordas)

### 7. **Sistema de Combate**
```python
if player.attacking and player.colliderect(enemy):
    enemy.health -= 25  # Causa dano
    if enemy.health <= 0:
        enemies.remove(enemy)  # Remove inimigo morto
        score += 100  # Adiciona pontos
```

## 🎯 Tutorial de Desenvolvimento

### Passo 1: Configuração Básica
```python
import pgzrun
WIDTH = 800
HEIGHT = 600
TITLE = "Hero Smash"

from pgzero.actor import Actor
from pygame import Rect
```

### Passo 2: Criando o Player
```python
player = Actor('character_maleadventurer_idle', (400, 300))
player.vx = 0
player.vy = 0
player.on_ground = False
```

### Passo 3: Função de Desenho
```python
def draw():
    screen.clear()
    screen.fill((135, 206, 235))  # Cor azul céu
    player.draw()
```

### Passo 4: Física e Movimento
```python
def update():
    # Aplicar gravidade
    gravity = 0.5
    player.vy += gravity
    
    # Aplicar movimento
    player.x += player.vx
    player.y += player.vy
```

### Passo 5: Controles
```python
def on_key_down(key):
    if key == keys.LEFT:
        player.vx = -3
    elif key == keys.RIGHT:
        player.vx = 3
    elif key == keys.SPACE and player.on_ground:
        player.vy = -10  # Pulo
```

### Passo 6: Adicionando Plataformas
```python
platforms = []
ground = Actor('platform', (400, 590))
platforms.append(ground)

# Na função update():
for platform in platforms:
    if player.colliderect(platform):
        player.bottom = platform.top
        player.vy = 0
        player.on_ground = True
```

### Passo 7: Sistema de Animação
```python
def update_player_animation():
    if player.state == "walking":
        if player.animation_timer >= 8:
            player.animation_frame = (player.animation_frame + 1) % 8
            player.animation_timer = 0
        player.image = f"character_maleadventurer_walk{player.animation_frame}"
```

### Passo 8: Inimigos e Combate
```python
enemies = []

def create_enemy(x, y):
    enemy = Actor('character_maleadventurer_idle', (x, y))
    enemy.health = 50
    return enemy

enemies.append(create_enemy(600, 300))
```

## 🎮 Controles do Jogo

| Tecla | Ação |
|-------|------|
| ←/→ | Mover para esquerda/direita |
| Shift + ←/→ | Correr |
| Espaço | Pular |
| ↓ | Agachar |
| Z | Atacar |

## 🚀 Como Executar

### Pré-requisitos:
```bash
pip install pgzero
```

### Executar o jogo:
```bash
python main.py
```

ou

```bash
pgzrun main.py
```

## 📚 Conceitos Aprendidos

### 1. **Programação Orientada a Objetos**
- **Actors**: Objetos que representam sprites
- **Propriedades**: `.x`, `.y`, `.vx`, `.vy`, `.health`
- **Métodos**: `.draw()`, `.colliderect()`

### 2. **Física de Jogos**
- **Gravidade**: Força constante que puxa objetos para baixo
- **Velocidade**: Taxa de mudança de posição
- **Colisão**: Detecção quando dois objetos se tocam

### 3. **Animação**
- **Frames**: Imagens individuais de uma animação
- **Frame Rate**: Velocidade de troca entre frames
- **Estados**: Diferentes animações para diferentes ações

### 4. **Estruturas de Dados**
- **Listas**: Para armazenar inimigos e plataformas
- **Dicionários implícitos**: Propriedades dos Actors

### 5. **Lógica de Jogo**
- **Game Loop**: Ciclo contínuo de atualizar e desenhar
- **Estados de Jogo**: idle, walking, jumping, attacking
- **Sistema de Pontuação**: Feedback para o jogador

### 6. **Controle de Input**
- **Eventos de Teclado**: `on_key_down()`, `on_key_up()`
- **Estados de Teclas**: `keyboard.left`, `keyboard.shift`

## 🎯 Funcionalidades do Jogo

### ✅ Implementadas:
- Movimento completo (andar, correr, pular, agachar)
- Sistema de animação com 8 frames de caminhada
- Física realista com gravidade
- Sistema de combate
- Inimigos com IA básica
- Sistema de pontuação
- Interface visual completa
- Colisão com plataformas

### 🚧 Possíveis Melhorias:
- Sons e música
- Diferentes tipos de inimigos
- Power-ups
- Múltiplos níveis
- Menu principal
- Sistema de vidas
- Efeitos visuais (partículas)
- Sprites de robô para inimigos

## 🎓 Por que Este Projeto é Educativo?

1. **Introduz conceitos fundamentais** de desenvolvimento de jogos
2. **Demonstra física básica** de forma visual e interativa
3. **Ensina estruturas de dados** de forma prática
4. **Mostra programação orientada a objetos** de forma simples
5. **Desenvolve lógica de programação** através de mecânicas de jogo
6. **Introduz conceitos de animação** e sprites
7. **Ensina gerenciamento de estado** (diferentes estados do player)

## 🏆 Conclusão

Este projeto demonstra como o **Pygame Zero** torna o desenvolvimento de jogos acessível para iniciantes, permitindo foco na lógica e criatividade ao invés de código complexo. O jogo implementa conceitos fundamentais como física, animação, colisão e IA de forma educativa e divertida.

**Hero Smash** serve como base sólida para projetos mais complexos e demonstra que jogos podem ser uma ferramenta poderosa para aprender programação! 🎮✨

---

*Desenvolvido como projeto educacional usando Python e Pygame Zero*