# ESPEC.md

## 1. Visão Geral

O objetivo deste projeto é desenvolver uma versão jogável do clássico jogo Pac-Man, com visual e sons em estilo 8 bits, para ser executado em navegadores web modernos. O sistema deve proporcionar uma experiência nostálgica, fiel à jogabilidade original, com controles simples, interface responsiva e placar de pontuação. O foco é diversão casual, acessível a qualquer usuário sem necessidade de cadastro ou instalação.

---

## 2. Personas

- **Jogador Casual**  
  Idade: 10-60 anos  
  Perfil: Busca entretenimento rápido e nostálgico, aprecia jogos retrô, não possui conhecimento técnico avançado, utiliza computador ou dispositivo móvel.

- **Entusiasta de Jogos Retrô**  
  Idade: 18-45 anos  
  Perfil: Fã de jogos clássicos, valoriza fidelidade visual e sonora ao original, pode jogar por períodos mais longos, gosta de comparar pontuações.

---

## 3. Jornadas do Usuário

### Jornada 1: Jogar uma Partida Rápida

1. O usuário acessa o site do Pac-Man.
2. Visualiza a tela inicial com o logo do jogo, instruções básicas e botão "Jogar".
3. Clica em "Jogar".
4. O jogo inicia, exibindo o labirinto clássico, Pac-Man, fantasmas e pontos.
5. O usuário controla o Pac-Man usando as setas do teclado (ou controles touch em dispositivos móveis).
6. O usuário coleta pontos, evita fantasmas e utiliza power-ups para comer fantasmas.
7. Ao perder todas as vidas, o jogo exibe a pontuação final e opção de reiniciar.

### Jornada 2: Visualizar e Compartilhar Pontuação

1. Ao final da partida, o usuário vê sua pontuação total.
2. Tem a opção de compartilhar a pontuação em redes sociais (ex: copiar link ou compartilhar no Twitter).
3. Pode clicar em "Jogar Novamente" para reiniciar.

---

## 4. Requisitos Funcionais

### 4.1. Interface e Experiência

- RF01: Exibir tela inicial com logo, instruções resumidas e botão "Jogar".
- RF02: Exibir o labirinto clássico do Pac-Man em estilo 8 bits.
- RF03: Exibir Pac-Man, quatro fantasmas (Blinky, Pinky, Inky, Clyde) e pontos no labirinto.
- RF04: Exibir pontuação atual e número de vidas restantes durante o jogo.
- RF05: Exibir tela de fim de jogo com pontuação final e opções de reiniciar ou compartilhar.
- RF06: Adaptar controles para teclado (setas) e touch (swipe) em dispositivos móveis.

### 4.2. Jogabilidade

- RF07: Permitir movimentação do Pac-Man em quatro direções (cima, baixo, esquerda, direita).
- RF08: Implementar IA básica para movimentação dos fantasmas, com padrões distintos.
- RF09: Implementar coleta de pontos e power-pellets (pontos grandes que permitem comer fantasmas).
- RF10: Implementar lógica de colisão entre Pac-Man e fantasmas (perda de vida ou comer fantasma).
- RF11: Reiniciar posição dos personagens ao perder vida.
- RF12: Avançar para próximo nível ao limpar todos os pontos do labirinto.
- RF13: Aumentar dificuldade progressivamente (velocidade dos fantasmas, etc).

### 4.3. Áudio e Visual

- RF14: Utilizar sprites, fontes e efeitos sonoros em estilo 8 bits.
- RF15: Tocar música de fundo e efeitos de coleta, morte e power-up.

### 4.4. Compartilhamento

- RF16: Permitir compartilhar a pontuação final via link ou redes sociais.

---

## 5. Requisitos Não-Funcionais

- RNF01: O jogo deve carregar completamente em até 3 segundos em conexões banda larga (>10Mbps).
- RNF02: O sistema deve funcionar em navegadores modernos (Chrome, Firefox, Edge, Safari) e ser responsivo para desktop e mobile.
- RNF03: O sistema não deve exigir cadastro ou login.
- RNF04: O código-fonte deve ser seguro, sem exposição de dados sensíveis.
- RNF05: O sistema deve suportar pelo menos 100 usuários simultâneos sem degradação perceptível de performance.
- RNF06: O áudio deve ser opcional e controlável pelo usuário (ligar/desligar).
- RNF07: O sistema deve ser acessível, com contraste adequado e textos alternativos para elementos visuais.

---

## 6. Critérios de Aceite

- CA01: O usuário consegue iniciar o jogo a partir da tela inicial em qualquer navegador suportado.
- CA02: O labirinto, personagens e pontos são exibidos em estilo 8 bits, fiel ao original.
- CA03: O Pac-Man responde instantaneamente aos comandos de teclado ou touch.
- CA04: Os fantasmas se movem de forma autônoma e apresentam padrões distintos.
- CA05: Ao coletar todos os pontos, o usuário avança de nível e a dificuldade aumenta.
- CA06: Ao perder todas as vidas, a pontuação final é exibida e pode ser compartilhada.
- CA07: O jogo pode ser reiniciado sem recarregar a página.
- CA08: O áudio pode ser ativado ou desativado pelo usuário.
- CA09: O sistema funciona em dispositivos móveis e desktops, mantendo jogabilidade adequada.
- CA10: O sistema não solicita ou armazena dados pessoais do usuário.

---

## 7. Fora de Escopo

- Implementação de rankings globais ou armazenamento de pontuação em servidores.
- Modo multiplayer (local ou online).
- Personalização de personagens, labirintos ou skins.
- Suporte a plugins, mods ou extensões de terceiros.
- Integração com sistemas de pagamento ou microtransações.
- Suporte a navegadores obsoletos (ex: Internet Explorer).
- Tradução para outros idiomas além do português brasileiro.
- Implementação de fases ou labirintos customizados além do clássico.

---