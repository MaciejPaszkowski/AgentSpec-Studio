import io
import zipfile
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import engine, Base, get_db
from app.models import SpecificationModel
from app.schemas import SpecCreateSchema, SpecResponseSchema, OptionsResponse, TechOption
from app.generator import generate_agent_artifacts

# Create tables & auto-migrate missing columns for existing PostgreSQL DBs
Base.metadata.create_all(bind=engine)

def auto_migrate_columns():
    try:
        with engine.connect() as conn:
            conn.execute(text("""
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS deployment_mode VARCHAR DEFAULT 'docker-compose';
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS architecture_pattern VARCHAR DEFAULT 'clean';
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS language_output VARCHAR DEFAULT 'pl';
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS security_standards JSON DEFAULT '[]';
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS api_protocols JSON DEFAULT '[]';
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS mcp_integrations JSON DEFAULT '[]';
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS git_ci_cd VARCHAR DEFAULT 'github-actions';
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS preset_template VARCHAR DEFAULT 'custom';
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS enforce_spec_compliance_check BOOLEAN DEFAULT TRUE;
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS generate_unit_tests BOOLEAN DEFAULT TRUE;
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS generate_integration_tests BOOLEAN DEFAULT TRUE;
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS generate_functional_tests BOOLEAN DEFAULT FALSE;
                ALTER TABLE specifications ADD COLUMN IF NOT EXISTS split_modular_artifacts BOOLEAN DEFAULT FALSE;
            """))
            conn.commit()
    except Exception as e:
        print("Auto-migration notice:", e)

auto_migrate_columns()

app = FastAPI(
    title="AgentSpec Studio API",
    description="API do zbierania specyfikacji i generowania reguł dla agentów AI z obsługą 6 języków wyjściowych i hierarchicznego podziału plików",
    version="0.1.0"
)

# Enable CORS for Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRESET_OPTIONS = OptionsResponse(
    agents=[
        TechOption(id="agy", name="Google Antigravity (AGY / agy)", category="agent"),
        TechOption(id="claude-code", name="Anthropic Claude Code (CLAUDE.md)", category="agent"),
        TechOption(id="codex", name="OpenAI Codex / Copilot CLI", category="agent"),
        TechOption(id="cursor", name="Cursor AI (.cursorrules)", category="agent"),
        TechOption(id="universal", name="Uniwersalny Agent AI", category="agent"),
    ],
    deployments=[
        TechOption(id="docker-compose", name="🐳 Docker Compose (Konteneryzacja)", category="deployment"),
        TechOption(id="native", name="💻 Natywne / Lokalne Środowisko Systemowe", category="deployment"),
        TechOption(id="kubernetes", name="☸️ Kubernetes (K8s Manifests)", category="deployment"),
    ],
    output_languages=[
        TechOption(id="pl", name="🇵🇱 Polski (Polish)", category="language_output"),
        TechOption(id="en", name="🇬🇧 English", category="language_output"),
        TechOption(id="de", name="🇩🇪 Deutsch (German)", category="language_output"),
        TechOption(id="fr", name="🇫🇷 Français (French)", category="language_output"),
        TechOption(id="es", name="🇪🇸 Español (Spanish)", category="language_output"),
        TechOption(id="ru", name="🇷🇺 Русский (Russian)", category="language_output"),
    ],
    architectures=[
        TechOption(id="clean", name="🏗️ Clean Architecture / Hexagonal (Ports & Adapters)", category="architecture"),
        TechOption(id="modular", name="📦 Modular Monolith (Domenowe Bounded Contexts)", category="architecture"),
        TechOption(id="event-driven", name="⚡ Event-Driven Architecture (Pub/Sub, Event Bus)", category="architecture"),
        TechOption(id="ddd", name="🎯 Domain-Driven Design (Aggregates, Entities, Repositories)", category="architecture"),
        TechOption(id="monolith", name="🏛️ Klasyczny Monolith (Controllers / Services)", category="architecture"),
    ],
    security=[
        TechOption(id="owasp", name="🛡️ OWASP Top 10 Safeguards (Input Sanitization, CORS/CSP)", category="security"),
        TechOption(id="gdpr", name="🔒 RODO / GDPR Compliance (Anonimizacja Logów PII)", category="security"),
        TechOption(id="jwt", name="🔑 Autentykacja JWT (Access + Refresh Tokens)", category="security"),
        TechOption(id="oauth2", name="🌐 OAuth2 / OIDC (Authorization Code with PKCE)", category="security"),
        TechOption(id="api-keys", name="🗝️ API Keys Authentication", category="security"),
    ],
    protocols=[
        TechOption(id="rest", name="🔌 REST API (OpenAPI 3.1 / JSON)", category="protocol"),
        TechOption(id="graphql", name="🕸️ GraphQL (Schema-First)", category="protocol"),
        TechOption(id="grpc", name="⚡ gRPC / Protocol Buffers (Proto3)", category="protocol"),
        TechOption(id="websockets", name="🔄 WebSockets / Server-Sent Events (SSE)", category="protocol"),
    ],
    mcp_skills=[
        TechOption(id="db-mcp", name="🗄️ Database MCP / Sidecar (Direct DB Inspection)", category="mcp"),
        TechOption(id="browser-mcp", name="🎭 Browser Automation MCP (Playwright UI Verification)", category="mcp"),
        TechOption(id="docs-mcp", name="📄 Document Generator Skill (DOCX/PDF Reports)", category="mcp"),
    ],
    ci_cd_presets=[
        TechOption(id="github-actions", name="🐙 GitHub Actions (.github/workflows/ci.yml)", category="cicd"),
        TechOption(id="gitlab-ci", name="🦊 GitLab CI (.gitlab-ci.yml)", category="cicd"),
        TechOption(id="none", name="🚫 Brak CI/CD", category="cicd"),
    ],
    project_presets=[
        TechOption(id="custom", name="⚙️ Własna Konfiguracja (Custom)", category="preset"),
        TechOption(id="saas-fullstack", name="🚀 SaaS Fullstack (FastAPI + Postgres + Angular + JWT)", category="preset"),
        TechOption(id="ai-rag", name="🧠 AI RAG Agent (Python + Qdrant + PyTest + LangChain)", category="preset"),
        TechOption(id="rust-microservice", name="🦀 High-Perf Microservice (Rust Axum + Postgres)", category="preset"),
        TechOption(id="web-ssr", name="🌐 Web App SSR (Next.js / Nuxt 3 + Supabase)", category="preset"),
    ],
    languages=[
        TechOption(id="python", name="Python 3.12+", category="language"),
        TechOption(id="rust", name="Rust", category="language"),
        TechOption(id="go", name="Go (Golang)", category="language"),
        TechOption(id="dlang", name="D (Dlang)", category="language"),
        TechOption(id="javascript", name="JavaScript (ESNext)", category="language"),
        TechOption(id="typescript", name="TypeScript 5.x", category="language"),
        TechOption(id="cpp", name="C++ 20/23", category="language"),
        TechOption(id="csharp", name="C# / .NET 8/9", category="language"),
        TechOption(id="java", name="Java 21+", category="language"),
        TechOption(id="kotlin", name="Kotlin", category="language"),
        TechOption(id="elixir", name="Elixir", category="language"),
        TechOption(id="zig", name="Zig", category="language"),
        TechOption(id="swift", name="Swift", category="language"),
        TechOption(id="php", name="PHP 8.3+", category="language"),
        TechOption(id="ruby", name="Ruby 3.3+", category="language"),
        TechOption(id="haskell", name="Haskell", category="language"),
        TechOption(id="scala", name="Scala 3", category="language"),
        TechOption(id="julia", name="Julia", category="language"),
        TechOption(id="nim", name="Nim", category="language"),
    ],
    backend_frameworks=[
        TechOption(id="fastapi", name="FastAPI (Python)", category="backend"),
        TechOption(id="falcon", name="Falcon 3.0 (Python)", category="backend"),
        TechOption(id="blacksheep", name="BlackSheep (Python)", category="backend"),
        TechOption(id="starlite", name="Starlite / Litestar (Python)", category="backend"),
        TechOption(id="flask", name="Flask (Python)", category="backend"),
        TechOption(id="django", name="Django (Python)", category="backend"),
        TechOption(id="actix-web", name="Actix-web (Rust)", category="backend"),
        TechOption(id="axum", name="Axum (Rust)", category="backend"),
        TechOption(id="gin", name="Gin (Go)", category="backend"),
        TechOption(id="node-express", name="Node.js + Express", category="backend"),
        TechOption(id="nestjs", name="NestJS (TypeScript)", category="backend"),
        TechOption(id="spring-boot", name="Spring Boot 3 (Java/Kotlin)", category="backend"),
        TechOption(id="aspnet-core", name="ASP.NET Core Web API (.NET)", category="backend"),
    ],
    frontend_frameworks=[
        TechOption(id="angular", name="Angular 18/19+", category="frontend"),
        TechOption(id="react", name="React 18/19", category="frontend"),
        TechOption(id="vue", name="Vue.js 3", category="frontend"),
        TechOption(id="svelte", name="Svelte 5 / SvelteKit", category="frontend"),
        TechOption(id="nextjs", name="Next.js (React)", category="frontend"),
        TechOption(id="nuxt", name="Nuxt 3 (Vue)", category="frontend"),
    ],
    databases=[
        TechOption(id="postgres", name="PostgreSQL 16", category="database"),
        TechOption(id="sqlite", name="SQLite 3", category="database"),
        TechOption(id="mysql", name="MySQL / MariaDB", category="database"),
        TechOption(id="redis", name="Redis (Cache/KV)", category="database"),
        TechOption(id="mongodb", name="MongoDB", category="database"),
        TechOption(id="qdrant", name="Qdrant (Vector DB)", category="database"),
    ],
    testing_frameworks=[
        TechOption(id="pytest", name="PyTest (Python)", category="testing"),
        TechOption(id="vitest", name="Vitest (TS/JS)", category="testing"),
        TechOption(id="jest", name="Jest (TS/JS)", category="testing"),
        TechOption(id="cargo-test", name="Cargo Test (Rust)", category="testing"),
        TechOption(id="go-test", name="Go Test (Go)", category="testing"),
    ]
)

@app.get("/api/v1/options", response_model=OptionsResponse)
def get_preset_options():
    return PRESET_OPTIONS

@app.post("/api/v1/specs", response_model=SpecResponseSchema, status_code=status.HTTP_201_CREATED)
def create_specification(spec_in: SpecCreateSchema, db: Session = Depends(get_db)):
    db_spec = SpecificationModel(
        title=spec_in.title,
        description=spec_in.description,
        agent_type=spec_in.agent_type,
        deployment_mode=spec_in.deployment_mode,
        architecture_pattern=spec_in.architecture_pattern,
        language_output=spec_in.language_output,
        security_standards=spec_in.security_standards,
        api_protocols=spec_in.api_protocols,
        mcp_integrations=spec_in.mcp_integrations,
        git_ci_cd=spec_in.git_ci_cd,
        preset_template=spec_in.preset_template,
        languages=spec_in.languages,
        backend_frameworks=spec_in.backend_frameworks,
        frontend_frameworks=spec_in.frontend_frameworks,
        databases=spec_in.databases,
        testing_frameworks=spec_in.testing_frameworks,
        custom_rules=spec_in.custom_rules,
        enforce_tdd=spec_in.enforce_tdd,
        enforce_spec_compliance_check=spec_in.enforce_spec_compliance_check,
        generate_unit_tests=spec_in.generate_unit_tests,
        generate_integration_tests=spec_in.generate_integration_tests,
        generate_functional_tests=spec_in.generate_functional_tests,
        split_modular_artifacts=spec_in.split_modular_artifacts
    )
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)

    artifacts = generate_agent_artifacts(spec_in.model_dump())
    res = SpecResponseSchema.model_validate(db_spec)
    res.agents_md = artifacts["agents_md"]
    res.spec_md = artifacts["spec_md"]
    res.tasks_md = artifacts["tasks_md"]
    return res

@app.get("/api/v1/specs", response_model=List[SpecResponseSchema])
def list_specifications(db: Session = Depends(get_db)):
    specs = db.query(SpecificationModel).order_by(SpecificationModel.created_at.desc()).all()
    results = []
    for s in specs:
        artifacts = generate_agent_artifacts({
            "title": s.title,
            "description": s.description,
            "agent_type": s.agent_type,
            "deployment_mode": getattr(s, "deployment_mode", "docker-compose"),
            "architecture_pattern": getattr(s, "architecture_pattern", "clean"),
            "language_output": getattr(s, "language_output", "pl"),
            "security_standards": getattr(s, "security_standards", ["owasp", "jwt"]),
            "api_protocols": getattr(s, "api_protocols", ["rest"]),
            "mcp_integrations": getattr(s, "mcp_integrations", ["db-mcp"]),
            "git_ci_cd": getattr(s, "git_ci_cd", "github-actions"),
            "preset_template": getattr(s, "preset_template", "custom"),
            "languages": s.languages,
            "backend_frameworks": s.backend_frameworks,
            "frontend_frameworks": s.frontend_frameworks,
            "databases": s.databases,
            "testing_frameworks": s.testing_frameworks,
            "custom_rules": s.custom_rules,
            "enforce_tdd": s.enforce_tdd,
            "enforce_spec_compliance_check": getattr(s, "enforce_spec_compliance_check", True),
            "generate_unit_tests": getattr(s, "generate_unit_tests", True),
            "generate_integration_tests": getattr(s, "generate_integration_tests", True),
            "generate_functional_tests": getattr(s, "generate_functional_tests", False),
            "split_modular_artifacts": getattr(s, "split_modular_artifacts", False)
        })
        res = SpecResponseSchema.model_validate(s)
        res.agents_md = artifacts["agents_md"]
        res.spec_md = artifacts["spec_md"]
        res.tasks_md = artifacts["tasks_md"]
        results.append(res)
    return results

@app.get("/api/v1/specs/{spec_id}", response_model=SpecResponseSchema)
def get_specification(spec_id: str, db: Session = Depends(get_db)):
    s = db.query(SpecificationModel).filter(SpecificationModel.id == spec_id).first()
    if not s:
        raise HTTPException(status_code=404, detail="Specyfikacja nie istnieje.")
    
    artifacts = generate_agent_artifacts({
        "title": s.title,
        "description": s.description,
        "agent_type": s.agent_type,
        "deployment_mode": getattr(s, "deployment_mode", "docker-compose"),
        "architecture_pattern": getattr(s, "architecture_pattern", "clean"),
        "language_output": getattr(s, "language_output", "pl"),
        "security_standards": getattr(s, "security_standards", ["owasp", "jwt"]),
        "api_protocols": getattr(s, "api_protocols", ["rest"]),
        "mcp_integrations": getattr(s, "mcp_integrations", ["db-mcp"]),
        "git_ci_cd": getattr(s, "git_ci_cd", "github-actions"),
        "preset_template": getattr(s, "preset_template", "custom"),
        "languages": s.languages,
        "backend_frameworks": s.backend_frameworks,
        "frontend_frameworks": s.frontend_frameworks,
        "databases": s.databases,
        "testing_frameworks": s.testing_frameworks,
        "custom_rules": s.custom_rules,
        "enforce_tdd": s.enforce_tdd,
        "enforce_spec_compliance_check": getattr(s, "enforce_spec_compliance_check", True),
        "generate_unit_tests": getattr(s, "generate_unit_tests", True),
        "generate_integration_tests": getattr(s, "generate_integration_tests", True),
        "generate_functional_tests": getattr(s, "generate_functional_tests", False),
        "split_modular_artifacts": getattr(s, "split_modular_artifacts", False)
    })
    res = SpecResponseSchema.model_validate(s)
    res.agents_md = artifacts["agents_md"]
    res.spec_md = artifacts["spec_md"]
    res.tasks_md = artifacts["tasks_md"]
    return res

@app.delete("/api/v1/specs/{spec_id}")
def delete_specification(spec_id: str, db: Session = Depends(get_db)):
    s = db.query(SpecificationModel).filter(SpecificationModel.id == spec_id).first()
    if not s:
        raise HTTPException(status_code=404, detail="Specyfikacja nie istnieje.")
    db.delete(s)
    db.commit()
    return {"message": "Specyfikacja usunięta pomyślnie."}

@app.get("/api/v1/specs/{spec_id}/export/zip")
def export_spec_zip(spec_id: str, db: Session = Depends(get_db)):
    s = db.query(SpecificationModel).filter(SpecificationModel.id == spec_id).first()
    if not s:
        raise HTTPException(status_code=404, detail="Specyfikacja nie istnieje.")
    
    artifacts = generate_agent_artifacts({
        "title": s.title,
        "description": s.description,
        "agent_type": s.agent_type,
        "deployment_mode": getattr(s, "deployment_mode", "docker-compose"),
        "architecture_pattern": getattr(s, "architecture_pattern", "clean"),
        "language_output": getattr(s, "language_output", "pl"),
        "security_standards": getattr(s, "security_standards", ["owasp", "jwt"]),
        "api_protocols": getattr(s, "api_protocols", ["rest"]),
        "mcp_integrations": getattr(s, "mcp_integrations", ["db-mcp"]),
        "git_ci_cd": getattr(s, "git_ci_cd", "github-actions"),
        "preset_template": getattr(s, "preset_template", "custom"),
        "languages": s.languages,
        "backend_frameworks": s.backend_frameworks,
        "frontend_frameworks": s.frontend_frameworks,
        "databases": s.databases,
        "testing_frameworks": s.testing_frameworks,
        "custom_rules": s.custom_rules,
        "enforce_tdd": s.enforce_tdd,
        "enforce_spec_compliance_check": getattr(s, "enforce_spec_compliance_check", True),
        "generate_unit_tests": getattr(s, "generate_unit_tests", True),
        "generate_integration_tests": getattr(s, "generate_integration_tests", True),
        "generate_functional_tests": getattr(s, "generate_functional_tests", False),
        "split_modular_artifacts": getattr(s, "split_modular_artifacts", False)
    })

    zip_buffer = io.BytesIO()
    filename_agent = "CLAUDE.md" if s.agent_type == "claude-code" else "AGENTS.md"
    split_modular = getattr(s, "split_modular_artifacts", False)

    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        # Master Root files
        zip_file.writestr(filename_agent, artifacts["agents_md"])
        zip_file.writestr("docs/SPEC.md", artifacts["spec_md"])
        zip_file.writestr("docs/TASKS.md", artifacts["tasks_md"])

        # Dedicated Sub-module files for Monorepo
        if split_modular:
            if artifacts.get("backend_agents_md"):
                zip_file.writestr(f"backend/{filename_agent}", artifacts["backend_agents_md"])
                zip_file.writestr("backend/SPEC.md", artifacts["backend_spec_md"])
                zip_file.writestr("backend/TASKS.md", artifacts["backend_tasks_md"])
            if artifacts.get("frontend_agents_md"):
                zip_file.writestr(f"frontend/{filename_agent}", artifacts["frontend_agents_md"])
                zip_file.writestr("frontend/SPEC.md", artifacts["frontend_spec_md"])
                zip_file.writestr("frontend/TASKS.md", artifacts["frontend_tasks_md"])

        if artifacts.get("ci_workflow"):
            zip_file.writestr(".github/workflows/ci.yml", artifacts["ci_workflow"])

    zip_buffer.seek(0)
    safe_title = "".join([c if c.isalnum() else "_" for c in s.title])
    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename=agent_spec_{safe_title}.zip"}
    )
