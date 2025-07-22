# 🦸‍♂️ Hero Smash

Um jogo de plataforma 2D educativo desenvolvido em Python usando PyZero (Pygame Zero), criado como projeto demonstrativo para a Kodland - plataforma de aprendizado de programação online.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte de um teste prático para posição de professor de Python na **Kodland**. O objetivo foi criar um jogo simples e educativo que demonstra conceitos fundamentais de programação e desenvolvimento de jogos, sendo ideal para ensinar Python de forma prática e divertida.

## 🎮 Descrição do Jogo

Hero Smash é um jogo de plataforma onde o jogador controla um herói que pode:
- Mover-se horizontalmente pelas plataformas
- Pular entre diferentes níveis
- Interagir com física realista (gravidade e colisão)

### Mecânicas Implementadas
- **Movimento horizontal**: Teclas direcionais esquerda/direita
- **Sistema de pulo**: Barra de espaço (apenas quando no chão)
- **Física de gravidade**: Movimentação vertical realista
- **Detecção de colisão**: Interação com plataformas
- **Sistema de plataformas**: Múltiplos níveis para exploração

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **PyZero (Pygame Zero)** - Framework simplificado para desenvolvimento de jogos
- **Pygame** - Biblioteca base para gráficos e input

## 📁 Estrutura do Projeto

```
Hero-Smash/
├── main.py          # Código principal do jogo
├── images/          # Assets visuais
│   ├── hero.png     # Sprite do personagem principal
│   ├── hero_1.png   # Variação do sprite
│   └── hero_2.png   # Variação do sprite
├── sounds/          # Assets de áudio
├── LICENSE          # Licença do projeto
└── README.md        # Este arquivo
```

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install pgzero
```

### Execução
```bash
python main.py
```

Ou usando o comando direto do PyZero:
```bash
pgzrun main.py
```

## 🎯 Controles

- **← →** (Setas): Mover o herói horizontalmente
- **Espaço**: Pular (apenas quando o herói estiver no chão)

## 🎓 Conceitos de Programação Demonstrados

Este projeto serve como exemplo prático para ensinar diversos conceitos importantes:

### Fundamentos de Python
- Importação e uso de módulos
- Variáveis e constantes
- Estruturas de dados (listas, tuplas)
- Funções e event handlers

### Conceitos de Programação de Jogos
- **Game Loop**: Ciclo principal de atualização do jogo
- **Sprites e Atores**: Representação de objetos no jogo
- **Física básica**: Implementação de gravidade e movimento
- **Detecção de colisão**: Interação entre objetos
- **Input handling**: Captura e processamento de entrada do usuário

### Programação Orientada a Eventos
- Tratamento de eventos de teclado (`on_key_down`, `on_key_up`)
- Loop de atualização (`update`)
- Loop de renderização (`draw`)

## 📚 Valor Educativo

Este projeto é ideal para:
- **Iniciantes em Python**: Demonstra sintaxe e estruturas básicas
- **Introdução a jogos**: Conceitos fundamentais sem complexidade excessiva
- **Programação visual**: Feedback imediato das mudanças no código
- **Lógica de programação**: Estruturas condicionais e loops em contexto prático

## 🎨 Características Técnicas

- **Resolução**: 800x600 pixels
- **Taxa de atualização**: 60 FPS (padrão PyZero)
- **Física**: Sistema de gravidade simples (0.5 unidades/frame)
- **Movimento**: Velocidade horizontal de 3 unidades/frame
- **Pulo**: Impulso inicial de -10 unidades (direção para cima)

## 🔮 Possíveis Expansões

Este projeto pode ser expandido para demonstrar conceitos mais avançados:
- Sistema de pontuação
- Inimigos e obstáculos
- Power-ups e coleta de itens
- Múltiplas fases
- Sistema de vidas
- Efeitos sonoros e música
- Animações de sprites
- Menu principal e game over

## 🏫 Sobre a Kodland

A Kodland é uma plataforma inovadora de ensino de programação online, focada em tornar o aprendizado de código acessível e divertido para todas as idades. Este projeto demonstra como conceitos de programação podem ser ensinados através de projetos práticos e envolventes.

## 📄 Licença

Este projeto está licenciado sob os termos da licença especificada no arquivo LICENSE.

---

**Desenvolvido por**: Nicholas Nascimento
**Propósito**: Teste prático para professor de Python - Kodland  
**Data**: Julho 2025  
**Framework**: PyZero (Pygame Zero)
