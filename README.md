# lemmAIngs - Spec-Driven Development, by Gaiotto

https://raw.githubusercontent.com/sergiogaiotto/lemmAIg/main/docs/assets/lemmaig_logo.jpeg

Aplicacao de **spec-driven development** com agentes de IA, onde especificacoes se tornam artefatos executaveis que geram implementacoes funcionais.

Inspirado no [spec-kit](https://github.com/github/spec-kit) do GitHub, construído com [deepagents](https://github.com/langchain-ai/deepagents) + LangGraph.

## Arquitetura

```
lemmAIngs/
├── app/
│   ├── agents/      # Agentes LangGraph (spec_agent.py)
│   ├── api/         # Rotas FastAPI
│   ├── core/        # Config, prompts
│   ├── models/      # Schemas Pydantic
│   ├── services/    # Logica de negocios
│   ├── templates/   # Frontend (default.html)
│   ├── static/      # Assets estaticos
│   └── main.py      # App FastAPI
├── specs/           # Projetos (ESPEC.md, DP.md, TASKS.md)
├── requirements.txt
├── .env
├── run.py
└── README.md
```

## Fluxo Spec-Driven

```
Descricao do usuario
        |
        v
   [1. Especificar]  -->  ESPEC.md (o que + por que)
        |
        v
   [2. Design Pattern]  -->  DP.md (como + stack)
        |
        v
   [3. Tarefas]  -->  TASKS.md (lista acionavel)
        |
        v
   [4. Implementar]  -->  Codigo gerado
```

Cada fase tem um checkpoint - voce nao avanca ate validar a saida atual.

## Setup

### 1. Instalar dependencias

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configurar .env

Edite o arquivo `.env` com sua API key:

```
OPENAI_API_KEY=sk-sua-chave-aqui
MODEL_NAME=gpt-4.1
```

### 3. Executar

```bash
python run.py
```

Acesse http://localhost:8000

## Endpoints da API

| Metodo | Rota                              | Descricao                            |
|--------|-----------------------------------|--------------------------------------|
| GET    | `/api/projects`                   | Lista todos os projetos              |
| GET    | `/api/projects/{name}`            | Status e artefatos de um projeto     |
| POST   | `/api/specify`                    | Gera ESPEC.md a partir de descricao  |
| POST   | `/api/plan`                       | Gera DP.md a partir de ESPEC + stack |
| POST   | `/api/tasks`                      | Gera TASKS.md a partir de ESPEC + DP |
| POST   | `/api/implement`                  | Gera codigo a partir dos artefatos   |
| PUT    | `/api/projects/{name}/{artifact}` | Edita um artefato manualmente        |

## Stack

- **Backend:** Python 3.11+ / FastAPI
- **AI:** LangGraph + LangChain + OpenAI (deepagents)
- **Frontend:** HTML / Tailwind CSS / Vanilla JS
- **Identidade Visual:** [falagaiotto.com.br](https://falagaiotto.com.br/)

## Conceito: ESPEC.md vs DP.md

| Artefato | Conteudo | Foco |
|--------------|--------------------------------|-----------------|
| **ESPEC.md** | Especificacao funcional        | O QUE e POR QUE |
| **DP.md**    | Design Pattern / Plano tecnico | COMO e COM QUE  |
| **TASKS.md** | Lista de tarefas               | O QUE FAZER     |
