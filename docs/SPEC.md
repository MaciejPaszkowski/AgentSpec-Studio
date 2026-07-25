# SPEC-003: AgentSpec Studio v2 - Zaawansowane Funkcje Specyfikacji i Reguł AI

## 1. Cel i Rozszerzenie Systemu
System AgentSpec Studio v2 zostaje rozbudowany o 8 zaawansowanych modułów inżynieryjnych:
1. **Wzorce Architektoniczne** (Clean Architecture, Modular Monolith, Event-Driven, DDD).
2. **Standardy Bezpieczeństwa** (OWASP Top 10, RODO/GDPR, JWT/OAuth2).
3. **Protokoły API** (REST API, GraphQL, gRPC, WebSockets/SSE).
4. **Integracje MCP & AI Skills** (Database MCP, Browser Automation, Office Skills).
5. **Wywiad i Prompting Asystenta AI** (Wbudowane szablony wywiadu ze specyfikacją).
6. **Konwencje Git & CI/CD** (Conventional Commits, Generowanie GitHub Actions `.github/workflows/ci.yml`).
7. **Diagramy Architektury Mermaid.js** (Dynamicznie generowane diagramy przepływu w `SPEC.md`).
8. **Gotowe Presety Projektowe (1-Click Presets)** (SaaS Fullstack, AI RAG Agent, Microservice Rust, Web App SSR).

---

## 2. Rozszerzona Architektura Danych (SQLAlchemy & Pydantic)

### 2.1 Nowe Pola w `SpecificationModel` i `SpecCreateSchema`:
- `architecture_pattern`: String (clean, modular, event-driven, ddd, monolith)
- `security_standards`: JSON Array (owasp, gdpr, jwt, oauth2)
- `api_protocols`: JSON Array (rest, graphql, grpc, websockets)
- `mcp_integrations`: JSON Array (db-mcp, browser-mcp, docs-mcp)
- `git_ci_cd`: String (none, github-actions, gitlab-ci)
- `preset_template`: String (custom, saas-fullstack, ai-rag, rust-microservice, web-ssr)

---

## 3. Nowe Opcje REST API (`/api/v1/options`)
- Extended options including `architectures`, `security`, `protocols`, `mcp_skills`, `ci_cd_presets`, `project_presets`.

---

## 4. Wzmocnienie Generatora Artefaktów (`generator.py`)
- Generowanie reguł architektonicznych w `AGENTS.md`.
- Wygenerowanie bloku Mermaid.js w `SPEC.md`.
- Generowanie zadania CI/CD oraz pliku `.github/workflows/ci.yml` w paczce ZIP.
