# ⚡ AgentSpec Studio (v0.2.0)

**AgentSpec Studio** to zaawansowany generator specyfikacji technicznych (`SPEC.md`), reguł dla agentów AI (`AGENTS.md` / `CLAUDE.md`), harmonogramów zadań (`TASKS.md`) oraz automatycznych przepływów CI/CD.

Aplikacja wspiera **6 języków wyjściowych** (🇵🇱 PL, 🇬🇧 EN, 🇩🇪 DE, 🇫🇷 FR, 🇪🇸 ES, 🇷🇺 RU), dynamiczny interfejs użytkownika z automatycznym tłumaczeniem na żywo, diagramy architektoniczne **Mermaid.js** oraz automatyczną metodykę **AI-TDD (Red-Green-Refactor)**.

---

## 🛠️ Architektura i Stos Technologiczny

- **Backend**: Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic v2, PyTest
- **Frontend**: Angular 19+ (Standalone Components, Signals, Zoneless Change Detection)
- **Baza Danych**: PostgreSQL 16 (z mapowaniem portów dla środowiska Docker)
- **Infrastruktura**: Docker Compose & Nginx

---

## 🚀 Szybkie Uruchomienie (Docker Compose)

Projekt jest fabrycznie skonfigurowany do natychmiastowego uruchomienia w **Docker Compose**.

```bash
# 1. Klonowanie repozytorium
git clone https://github.com/MaciejPaszkowski/AgentSpec-Studio.git
cd AgentSpec-Studio

# 2. Uruchomienie kontenerów w tle
docker-compose up -d --build
```

### 🌐 Dostępne Porty Systemowe:
- **Frontend App (Angular 19 / Nginx)**: [http://localhost:4200](http://localhost:4200)
- **Backend API (FastAPI Swagger Docs)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Baza Danych PostgreSQL**: `localhost:5436` (użytkownik: `postgres`, baza: `agentspec_db`)

---

## ✨ Główne Funkcje

1. **Wybór Agenta AI**: Google Antigravity (`AGY` / `agy`), Anthropic Claude Code (`CLAUDE.md`), OpenAI Codex, Cursor AI (`.cursorrules`).
2. **Tryby Wdrożenia**: Docker Compose, Natywne/Lokalne, Kubernetes (K8s).
3. **8 Zaawansowanych Modułów Architektury**:
   - Wzorce Architektoniczne (Clean Architecture, Modular Monolith, Event-Driven, DDD).
   - Standardy Bezpieczeństwa (OWASP Top 10, GDPR/RODO, JWT, OAuth2, API Keys).
   - Protokoły API (REST, GraphQL, gRPC Proto3, WebSockets/SSE).
   - Integracje MCP & AI Skills (Database MCP, Browser Automation Playwright, Document Generator).
   - Wywiad AI Prompt w wybranym języku.
   - Generator GitHub Actions CI Workflow (`.github/workflows/ci.yml`).
   - Auto-Diagramy Mermaid.js.
   - Gotowe Presety 1-Kliknięciem (SaaS Fullstack, AI RAG Agent, Microservice, Web SSR).
4. **Wielojęzyczność**: Pełny wybór 6 języków dla interfejsu (UI) oraz niezależny wybór języka dokumentów wyjściowych.
5. **Eksport Paczek ZIP**: Pobieranie kompletu wygenerowanych plików projektowych jednym kliknięciem.

---

## 🧪 Testowanie i Weryfikacja

```bash
# Uruchomienie testów backendu
PYTHONPATH=backend pytest backend/tests

# Weryfikacja kompilacji produkcyjnej Angulara
cd frontend && npx ng build --configuration production
```

---

## 📜 Licencja
MIT License © 2026 AgentSpec Studio.
