# DP.md - Design Pattern / Plano Tecnico

> **Projeto:** [NOME_DO_PROJETO]
> **Versao:** 1.0
> **Data:** [DATA]
> **Arquiteto:** [AUTOR]

---

## 1. Arquitetura

### 1.1 Padrao Arquitetural
[ex: Clean Architecture, Hexagonal, Vertical Slice]

### 1.2 Justificativa
[Por que este padrao foi escolhido]

### 1.3 Diagrama
```
[Diagrama ASCII ou descricao da arquitetura]
```

---

## 2. Stack Tecnologica

| Camada | Tecnologia | Versao | Justificativa |
|--------|-----------|--------|---------------|
| Backend | [ex: Python/FastAPI] | [versao] | [motivo] |
| Frontend | [ex: HTML/Tailwind] | [versao] | [motivo] |
| Database | [ex: PostgreSQL] | [versao] | [motivo] |
| AI/ML | [ex: LangGraph/OpenAI] | [versao] | [motivo] |

---

## 3. Estrutura de Diretorios

```
projeto/
├── app/
│   ├── api/          # Endpoints e rotas
│   ├── core/         # Configuracao e constantes
│   ├── models/       # Schemas e entidades
│   ├── services/     # Logica de negocio
│   └── agents/       # Agentes de IA
├── templates/        # Templates HTML
├── static/           # Arquivos estaticos
├── tests/            # Testes
└── specs/            # Especificacoes
```

---

## 4. Design Patterns

| Pattern | Onde | Justificativa |
|---------|------|---------------|
| [ex: Repository] | [Camada de dados] | [motivo] |
| [ex: Strategy] | [Agentes] | [motivo] |
| [ex: Observer] | [Eventos] | [motivo] |

---

## 5. Modelagem de Dados

### Entidade: [Nome]
| Campo | Tipo | Descricao |
|-------|------|-----------|
| id | UUID | Identificador unico |
| [campo] | [tipo] | [descricao] |

---

## 6. APIs / Interfaces

### POST /api/[endpoint]
- **Descricao:** [o que faz]
- **Request Body:**
```json
{
  "campo": "valor"
}
```
- **Response:**
```json
{
  "resultado": "valor"
}
```

---

## 7. Fluxo de Dados

```
Usuario -> Frontend -> API -> Service -> Agent -> LLM
                                           |
                                           v
                                     Artefatos (.md)
```

---

## 8. Estrategia de Testes

| Tipo | Cobertura | Ferramenta |
|------|-----------|------------|
| Unitario | Services, Models | pytest |
| Integracao | API endpoints | pytest + httpx |
| E2E | Fluxo completo | playwright |

---

## 9. Constraints e Decisoes

| Decisao | Alternativas | Escolha | Motivo |
|---------|-------------|---------|--------|
| [Decisao 1] | [Op A, Op B] | [Escolha] | [Motivo] |
