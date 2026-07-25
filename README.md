# ⚡ AgentSpec Studio (v0.2.0)

**AgentSpec Studio** is an advanced specification and AI agent rule generator designed for modern software development. It creates production-ready technical specifications (`SPEC.md`), tailored AI agent instruction files (`AGENTS.md` / `CLAUDE.md`), step-by-step task checklists (`TASKS.md`), and automated CI/CD workflows.

The application features **6 output languages** (🇵🇱 PL, 🇬🇧 EN, 🇩🇪 DE, 🇫🇷 FR, 🇪🇸 ES, 🇷🇺 RU), real-time UI auto-translation, **Mermaid.js** architectural diagrams, **hierarchical monorepo artifact splitting**, and strict **AI-TDD (Red-Green-Refactor)** enforcement.

---

## 🛠️ Architecture & Tech Stack

- **Backend**: Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic v2, PyTest, PostgreSQL 16
- **Frontend**: Angular 19+ (Standalone Components, Signals, Zoneless Change Detection)
- **Infrastructure**: Docker Compose & Nginx

---

## 🚀 Quick Start (Docker Compose)

The project is fully pre-configured for instant deployment using Docker Compose:

```bash
# 1. Clone repository
git clone https://github.com/MaciejPaszkowski/AgentSpec-Studio.git
cd AgentSpec-Studio

# 2. Build & launch containers
docker-compose up -d --build
```

### 🌐 System Ports & Services:
- **Frontend App (Angular 19 / Nginx)**: [http://localhost:4200](http://localhost:4200)
- **Backend API (FastAPI Swagger Docs)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **PostgreSQL Database**: `localhost:5436` (User: `postgres`, DB: `agentspec_db`)

---

## ✨ Key Features

1. **Target AI Agent Selection**: Google Antigravity (`AGY` / `agy`), Anthropic Claude Code (`CLAUDE.md`), OpenAI Codex, Cursor AI (`.cursorrules`), and Universal Agent.
2. **Hierarchical Monorepo Splitting**: Option to generate master root instruction files alongside layer-specific files (`backend/AGENTS.md`, `frontend/AGENTS.md`, `backend/SPEC.md`, `frontend/SPEC.md`).
3. **8 Advanced Architecture Modules**:
   - **Architectural Patterns**: Clean Architecture / Hexagonal, Modular Monolith, Event-Driven, DDD, Classic Monolith.
   - **Security & Compliance**: OWASP Top 10, GDPR/RODO, JWT Tokens, OAuth2/OIDC, API Keys.
   - **API Protocols**: REST (OpenAPI 3.1), GraphQL, gRPC Proto3, WebSockets / SSE.
   - **MCP Integrations & AI Skills**: Database MCP, Browser Automation (Playwright), Document Generator.
   - **CI/CD Pipeline Generator**: GitHub Actions (`.github/workflows/ci.yml`), GitLab CI.
   - **Auto Mermaid.js Diagrams**: Real-time rendering of client-frontend-backend-database architecture flows.
   - **1-Click Presets**: SaaS Fullstack, AI RAG Agent, Rust Microservice, Web SSR.
4. **Multi-language Support**: Independent UI interface language selection and output document target language selection across 6 languages with real-time translation.
5. **Project Management & Persistence**: Integrated PostgreSQL project storage with 1-click **New Project**, **Save Project**, and **Load Project** functionality, plus 1-click ZIP bundle exports.

---

## 🧪 Testing & Verification

```bash
# Run backend test suite
PYTHONPATH=backend pytest backend/tests

# Verify Angular production build
cd frontend && npx ng build --configuration production
```

---

## 📜 License
MIT License © 2026 AgentSpec Studio.
