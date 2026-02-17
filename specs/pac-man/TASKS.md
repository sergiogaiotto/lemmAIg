```markdown
# TASKS.md

## Lista de Tarefas

---

### 1. Setup Inicial e Infraestrutura

#### T001 - Estruturar Repositório e Diretórios
- **Descrição**: Criar a estrutura de diretórios conforme especificado em DP.md, incluindo backend/app, frontend/src, assets, styles, etc.
- **Dependências**: Nenhuma
- **Critério de Aceite**: Estrutura de pastas criada no repositório, conforme diagrama apresentado.
- **Estimativa**: P

#### T002 - Configurar Ambiente Backend com FastAPI
- **Descrição**: Inicializar projeto Python com Poetry, instalar FastAPI, Uvicorn e criar app/main.py básico.
- **Dependências**: T001
- **Critério de Aceite**: Backend roda localmente com endpoint raiz (`/`) respondendo "OK".
- **Estimativa**: P

#### T003 - Configurar Ambiente Frontend com Webpack e Vanilla JS
- **Descrição**: Inicializar projeto frontend, configurar Webpack para empacotamento, ESLint, Prettier e estrutura básica de arquivos JS/CSS.
- **Dependências**: T001
- **Critério de Aceite**: Frontend compila e serve bundle.js e styles.css.
- **Estimativa**: P

---

### 2. Assets e Recursos Visuais/Sonoros

#### T004 - Adicionar Sprites, Sons e Fontes 8 bits Otimizados
- **Descrição**: Adicionar e otimizar sprites, sons e fontes em estilo 8 bits nas pastas de assets.
- **Dependências**: T001
- **Critério de Aceite**: Todos os arquivos de assets disponíveis e otimizados (<3s carregamento).
- **Estimativa**: M

---

### 3. Backend: Servir Arquivos Estáticos

#### T005 - Configurar Servidor de Arquivos Estáticos no FastAPI
- **Descrição**: Configurar FastAPI para servir index.html, bundle.js, styles.css, sprites, sons e fontes.
- **Dependências**: T002, T003, T004
- **Critério de Aceite**: Todos os arquivos estáticos acessíveis via navegador.
- **Estimativa**: P

---

### 4. Frontend: UI e Estados do Jogo

#### T006 - Implementar Tela Inicial (Logo, Instruções, Botão Jogar)
- **Descrição**: Criar tela inicial com logo, instruções resumidas e botão "Jogar" (RF01).
- **Dependências**: T003, T004
- **Critério de Aceite**: Tela inicial exibida ao acessar o site, botão "Jogar" funcional.
- **Estimativa**: P

#### T007 - Implementar Tela de Jogo (Canvas, HUD: Pontuação, Vidas, Nível)
- **Descrição**: Criar tela principal do jogo com canvas para labirinto, HUD mostrando pontuação, vidas e nível (RF02, RF03, RF04).
- **Dependências**: T006
- **Critério de Aceite**: Tela de jogo renderiza labirinto e HUD corretamente.
- **Estimativa**: M

#### T008 - Implementar Tela de Game Over e Compartilhamento
- **Descrição**: Criar tela de fim de jogo com pontuação final, botões "Jogar Novamente" e "Compartilhar" (RF05, RF16).
- **Dependências**: T007
- **Critério de Aceite**: Tela de game over exibida corretamente, botões funcionais.
- **Estimativa**: P

#### T009 - Implementar Responsividade e Acessibilidade Básica
- **Descrição**: Garantir responsividade para desktop/mobile, contraste adequado e textos alternativos (RNF02, RNF07).
- **Dependências**: T006, T007, T008
- **Critério de Aceite**: Interface funcional e acessível em diferentes dispositivos.
- **Estimativa**: M

---

### 5. Frontend: Engine e Mecânicas do Jogo

#### T010 - Implementar State Machine para Estados do Jogo
- **Descrição**: Criar máquina de estados para controlar transições (inicial, jogando, game over, compartilhando).
- **Dependências**: T006, T007, T008
- **Critério de Aceite**: Estados do jogo transitam corretamente conforme ações do usuário.
- **Estimativa**: P

#### T011 - Implementar Renderização do Labirinto e Entidades
- **Descrição**: Renderizar labirinto clássico, Pac-Man, fantasmas e pontos no canvas (RF02, RF03).
- **Dependências**: T007, T004
- **Critério de Aceite**: Labirinto e personagens exibidos fielmente em 8 bits.
- **Estimativa**: M

#### T012 - Implementar Controles de Teclado e Touch (Input)
- **Descrição**: Permitir movimentação do Pac-Man via setas do teclado e swipe em mobile (RF06, RF07).
- **Dependências**: T011
- **Critério de Aceite**: Pac-Man responde instantaneamente a comandos de teclado e touch.
- **Estimativa**: M

#### T013 - Implementar Lógica de Movimentação do Pac-Man
- **Descrição**: Implementar movimentação do Pac-Man nas quatro direções, respeitando colisões com paredes.
- **Dependências**: T012
- **Critério de Aceite**: Pac-Man se move corretamente e não atravessa paredes.
- **Estimativa**: P

#### T014 - Implementar IA dos Fantasmas (Strategy Pattern)
- **Descrição**: Implementar IA básica dos quatro fantasmas, cada um com padrão distinto (RF08).
- **Dependências**: T011
- **Critério de Aceite**: Fantasmas se movem autonomamente, cada um com comportamento próprio.
- **Estimativa**: M

#### T015 - Implementar Coleta de Pontos e Power-Pellets
- **Descrição**: Lógica para coletar pontos normais e power-pellets, ativando modo de comer fantasmas (RF09).
- **Dependências**: T013
- **Critério de Aceite**: Pontos e power-pellets podem ser coletados, modo especial ativado corretamente.
- **Estimativa**: P

#### T016 - Implementar Lógica de Colisão (Pac-Man x Fantasmas)
- **Descrição**: Detectar colisão entre Pac-Man e fantasmas, com perda de vida ou comer fantasma (RF10).
- **Dependências**: T014, T015
- **Critério de Aceite**: Colisões tratadas conforme regras do jogo.
- **Estimativa**: P

#### T017 - Implementar Reinício de Posições ao Perder Vida
- **Descrição**: Reiniciar posições de Pac-Man e fantasmas ao perder vida (RF11).
- **Dependências**: T016
- **Critério de Aceite**: Posições reiniciam corretamente após perda de vida.
- **Estimativa**: P

#### T018 - Implementar Avanço de Nível e Dificuldade Progressiva
- **Descrição**: Avançar para próximo nível ao limpar todos os pontos, aumentando dificuldade (RF12, RF13).
- **Dependências**: T015, T016
- **Critério de Aceite**: Nível avança e dificuldade aumenta conforme esperado.
- **Estimativa**: P

#### T019 - Implementar Reinício de Partida sem Recarregar Página
- **Descrição**: Permitir reiniciar o jogo a partir da tela de game over sem reload (CA07).
- **Dependências**: T010, T017, T018
- **Critério de Aceite**: Jogo reinicia corretamente sem recarregar a página.
- **Estimativa**: P

---

### 6. Frontend: Áudio

#### T020 - Implementar Efeitos Sonoros e Música de Fundo (Web Audio API)
- **Descrição**: Adicionar sons de coleta, morte, power-up e música de fundo (RF14, RF15).
- **Dependências**: T011, T015, T016
- **Critério de Aceite**: Áudio toca nos eventos corretos, estilo 8 bits.
- **Estimativa**: P

#### T021 - Implementar Controle de Áudio (On/Off)
- **Descrição**: Adicionar botão para ativar/desativar áudio, persistindo preferência do usuário (RNF06).
- **Dependências**: T020
- **Critério de Aceite**: Usuário pode ligar/desligar áudio a qualquer momento.
- **Estimativa**: P

---

### 7. Backend: Compartilhamento

#### T022 - Implementar Endpoint POST /api/v1/share
- **Descrição**: Criar endpoint no FastAPI para receber pontuação/nivel e retornar link de compartilhamento.
- **Dependências**: T002
- **Critério de Aceite**: Endpoint retorna URL válida para dados recebidos.
- **Estimativa**: P

#### T023 - Implementar Endpoint GET /share/{share_id}
- **Descrição**: Criar endpoint para exibir tela de compartilhamento com pontuação.
- **Dependências**: T022
- **Critério de Aceite**: Acesso ao link exibe HTML com pontuação compartilhada.
- **Estimativa**: P

#### T024 - Implementar Geração Segura de Links Temporários
- **Descrição**: Garantir que links de compartilhamento não exponham dados sensíveis e expirem após tempo configurável.
- **Dependências**: T022
- **Critério de Aceite**: Links são seguros, não expõem dados pessoais e expiram corretamente.
- **Estimativa**: P

---

### 8. Frontend: Integração de Compartilhamento

#### T025 - Implementar Integração Frontend com API de Compartilhamento
- **Descrição**: Ao clicar em "Compartilhar", enviar pontuação para backend e exibir link/modal para copiar ou compartilhar.
- **Dependências**: T008, T022
- **Critério de Aceite**: Compartilhamento funciona e exibe link ao usuário.
- **Estimativa**: P

---

### 9. Testes Automatizados

#### T026 - Implementar Testes Unitários Backend (Pytest)
- **Descrição**: Testar endpoints de compartilhamento, payloads válidos/ inválidos.
- **Dependências**: T022, T023, T024
- **Critério de Aceite**: Cobertura 95%+ dos endpoints de backend.
- **Estimativa**: P

#### T027 - Implementar Testes Unitários Frontend (Jest)
- **Descrição**: Testar lógica de engine, IA dos fantasmas, detecção de colisão.
- **Dependências**: T010, T013, T014, T016
- **Critério de Aceite**: Cobertura 80%+ da lógica de frontend.
- **Estimativa**: M

#### T028 - Implementar Testes E2E (Cypress)
- **Descrição**: Testar jornadas principais: iniciar jogo, jogar, perder, compartilhar, responsividade.
- **Dependências**: T019, T025
- **Critério de Aceite**: Testes E2E cobrem jornadas principais em diferentes dispositivos.
- **Estimativa**: M

---

### 10. Performance, Segurança e Acessibilidade

#### T029 - Otimizar Performance de Carregamento (<3s)
- **Descrição**: Minimizar assets, lazy loading, otimizar bundle para garantir carregamento rápido (RNF01).
- **Dependências**: T004, T005, T003
- **Critério de Aceite**: Jogo carrega em até 3 segundos em banda larga.
- **Estimativa**: P

#### T030 - Garantir Segurança e Ausência de Dados Pessoais
- **Descrição**: Revisar código para garantir que nenhum dado pessoal é coletado ou exposto (RNF04, CA10).
- **Dependências**: T022, T024, T025
- **Critério de Aceite**: Nenhum dado pessoal é coletado, transmitido ou exposto.
- **Estimativa**: P

#### T031 - Garantir Acessibilidade Avançada
- **Descrição**: Adicionar navegação por teclado, textos alternativos, ARIA labels e testes de contraste (RNF07).
- **Dependências**: T009
- **Critério de Aceite**: Interface aprovada em testes de acessibilidade automatizados.
- **Estimativa**: P

---

## Resumo de Dependências

- **T001** → T002, T003, T004
- **T002, T003, T004** → T005
- **T003, T004** → T006
- **T006** → T007
- **T007** → T008, T011
- **T008** → T009, T025
- **T009** → T031
- **T011** → T012, T014, T020
- **T012** → T013
- **T013** → T015
- **T014** → T016
- **T015** → T016, T018
- **T016** → T017, T018
- **T017, T018, T010** → T019
- **T020** → T021
- **T022** → T023, T024, T025
- **T023, T024** → T026
- **T010, T013, T014, T016** → T027
- **T019, T025** → T028
- **T004, T005, T003** → T029
- **T022, T024, T025** → T030

---

## Fim das Tarefas
```