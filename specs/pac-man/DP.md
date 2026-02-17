```markdown
# DP.md

## 1. Arquitetura

### Padrão Arquitetural Escolhido: **Frontend SPA + Backend API REST**

#### Justificativa
- **Frontend SPA (Single Page Application)**: A lógica e renderização do jogo Pac-Man, incluindo gráficos, controles e áudio, serão executadas no navegador do usuário para garantir responsividade, baixa latência e experiência fluida.
- **Backend API REST**: O backend, implementado com Python e FastAPI, será responsável apenas por funcionalidades auxiliares, como geração de links de compartilhamento, registro de logs de uso (sem dados pessoais), e servir arquivos estáticos (sprites, sons, HTML, JS, CSS).
- **Separação de responsabilidades**: Mantém o frontend desacoplado do backend, facilitando manutenção, testes e futuras evoluções.
- **Escalabilidade**: Atende facilmente à demanda de 100+ usuários simultâneos, pois a maior parte do processamento ocorre no cliente.

---

## 2. Stack Tecnológica

- **Backend**
  - Linguagem: Python 3.11+
  - Framework: FastAPI 0.110+
  - Servidor ASGI: Uvicorn 0.29+
  - Gerenciador de dependências: Poetry 1.8+
- **Frontend**
  - Linguagem: JavaScript (ES2021+)
  - Framework: Nenhum (vanilla JS para performance e footprint reduzido)
  - Canvas API (para renderização do jogo)
  - Web Audio API (para sons 8 bits)
  - Responsividade: CSS3 Flexbox/Grid + Media Queries
- **Build/Dev Tools**
  - Webpack 5+ (empacotamento frontend)
  - ESLint (lint JS)
  - Prettier (formatação)
- **Testes**
  - Backend: Pytest 8+
  - Frontend: Jest 29+ (testes unitários JS)
  - Cypress 13+ (testes E2E)

---

## 3. Estrutura de Diretórios

```
pacman/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── share.py
│   │   ├── core/
│   │   │   └── config.py
│   │   └── static/
│   │       ├── index.html
│   │       ├── assets/
│   │       │   ├── sprites/
│   │       │   ├── sounds/
│   │       │   └── fonts/
│   │       └── dist/
│   │           ├── bundle.js
│   │           └── styles.css
│   └── tests/
│       ├── test_share.py
│       └── ...
├── frontend/
│   ├── src/
│   │   ├── index.js
│   │   ├── game/
│   │   │   ├── engine.js
│   │   │   ├── entities.js
│   │   │   ├── ai.js
│   │   │   ├── audio.js
│   │   │   ├── renderer.js
│   │   │   └── input.js
│   │   ├── ui/
│   │   │   ├── screens.js
│   │   │   └── controls.js
│   │   └── utils/
│   │       └── helpers.js
│   ├── assets/
│   │   ├── sprites/
│   │   ├── sounds/
│   │   └── fonts/
│   └── styles/
│       └── main.css
├── .env
├── README.md
├── pyproject.toml
└── package.json
```

---

## 4. Design Patterns

### Backend (FastAPI)
- **Factory Pattern**: Inicialização da aplicação FastAPI e injeção de dependências.
- **Router Pattern**: Organização modular dos endpoints via APIRouter.
- **Adapter Pattern**: Adaptação de dados para compartilhamento de pontuação (ex: geração de links).

### Frontend (JS)
- **State Machine**: Gerenciamento dos estados do jogo (inicial, jogando, game over, compartilhando).
- **Observer Pattern**: Notificação de mudanças de estado (ex: atualização de pontuação, vidas).
- **Strategy Pattern**: Implementação dos diferentes comportamentos de IA dos fantasmas.
- **Module Pattern**: Organização do código JS em módulos autocontidos (engine, renderer, audio, etc).
- **Command Pattern**: Mapeamento de entradas do usuário (teclado/touch) para ações do jogo.

---

## 5. Modelagem de Dados

### Entidades Principais (Frontend)

- **GameState**
  - estado: [inicial, jogando, game_over, compartilhando]
  - pontuacao: int
  - vidas: int
  - nivel: int
  - labirinto: matriz[int]
  - pacman: {posicao: (x, y), direcao, status}
  - fantasmas: [{nome, posicao, direcao, modo}]
  - pontos: [{posicao, tipo}]
  - power_pellets: [{posicao, ativo}]
  - audio_on: bool

### Backend

- **ShareRequest**
  - pontuacao: int
  - nivel: int
  - timestamp: datetime

- **ShareResponse**
  - url: str

**Relacionamentos**: O backend não armazena dados persistentes, apenas gera links temporários para compartilhamento.

---

## 6. APIs / Interfaces

### Backend

#### `POST /api/v1/share`
- **Descrição**: Gera um link de compartilhamento de pontuação.
- **Request Body**:
  ```json
  {
    "pontuacao": 12345,
    "nivel": 5
  }
  ```
- **Response**:
  ```json
  {
    "url": "https://pacman.exemplo.com/share/abc123"
  }
  ```
- **Status**: 200 OK

#### `GET /share/{share_id}`
- **Descrição**: Redireciona para tela de compartilhamento com pontuação.
- **Response**: HTML com dados da pontuação.

#### `GET /static/*`
- **Descrição**: Servir arquivos estáticos (frontend, sprites, sons).

### Frontend

- **Interface de Usuário**
  - Tela Inicial: Logo, instruções, botão "Jogar"
  - Tela de Jogo: Canvas do labirinto, HUD (pontuação, vidas, nível), botão áudio on/off
  - Tela de Game Over: Pontuação final, botões "Jogar Novamente" e "Compartilhar"
  - Compartilhamento: Modal/link para copiar ou compartilhar em redes sociais

---

## 7. Fluxo de Dados

1. **Carregamento**
   - Usuário acessa `/` → FastAPI serve `index.html` e assets.
   - Frontend carrega sprites, sons e inicializa engine JS.

2. **Jogo**
   - Usuário inicia partida → engine JS gerencia estados, renderiza canvas, processa entradas.
   - Toda lógica de jogo, IA, pontuação e áudio ocorre no frontend.

3. **Compartilhamento**
   - Ao fim do jogo, usuário clica em "Compartilhar".
   - Frontend envia `POST /api/v1/share` com pontuação.
   - Backend retorna URL de compartilhamento.
   - Frontend exibe link e opções de copiar/compartilhar.

4. **Acessibilidade**
   - Frontend aplica contraste, textos alternativos e controles acessíveis.

---

## 8. Estratégia de Testes

### Backend
- **Testes Unitários**: Pytest para rotas, validação de payloads, geração de links.
- **Testes de Integração**: Testes de endpoints REST com dados válidos e inválidos.
- **Cobertura Esperada**: 95%+ do backend.

### Frontend
- **Testes Unitários**: Jest para lógica de engine, IA dos fantasmas, detecção de colisão.
- **Testes de Interface**: Cypress para jornadas principais (iniciar jogo, jogar, game over, compartilhar).
- **Testes de Responsividade**: Cypress em diferentes viewports.
- **Cobertura Esperada**: 80%+ do frontend.

---

## 9. Constraints e Decisões

- **Sem persistência de dados**: Não haverá banco de dados, nem armazenamento de pontuações no servidor (apenas geração de links temporários).
- **Sem autenticação**: Não haverá login/cadastro.
- **Performance**: Todo processamento do jogo ocorre no cliente, garantindo baixa latência e alta escalabilidade.
- **Acessibilidade**: Interface com contraste adequado, textos alternativos e controles acessíveis.
- **Compatibilidade**: Suporte garantido apenas para navegadores modernos (Chrome, Firefox, Edge, Safari).
- **Assets**: Sprites, sons e fontes 8 bits devem ser otimizados para carregamento rápido (<3s).
- **Áudio opcional**: Controle de áudio implementado no frontend, sem dependência do backend.
- **Internacionalização**: Apenas português brasileiro.
- **Segurança**: Sem coleta ou exposição de dados pessoais; links de compartilhamento não expõem informações sensíveis.

---
```