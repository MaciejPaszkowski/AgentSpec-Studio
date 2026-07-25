import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import engine, Base

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_get_options():
    response = client.get("/api/v1/options")
    assert response.status_code == 200
    data = response.json()
    assert "deployments" in data
    assert "output_languages" in data
    assert "architectures" in data
    assert "security" in data
    assert "protocols" in data
    assert "mcp_skills" in data
    assert "ci_cd_presets" in data
    assert "project_presets" in data
    assert "languages" in data
    assert "backend_frameworks" in data
    assert "frontend_frameworks" in data
    assert "databases" in data
    assert "testing_frameworks" in data

def test_create_and_get_spec():
    payload = {
        "title": "Moja Aplikacja Testowa v2",
        "description": "Opis aplikacji w Rust i Angular",
        "agent_type": "agy",
        "deployment_mode": "docker-compose",
        "architecture_pattern": "clean",
        "language_output": "pl",
        "security_standards": ["owasp", "jwt"],
        "api_protocols": ["rest"],
        "mcp_integrations": ["db-mcp"],
        "git_ci_cd": "github-actions",
        "preset_template": "saas-fullstack",
        "languages": ["rust", "typescript"],
        "backend_frameworks": ["actix-web"],
        "frontend_frameworks": ["angular"],
        "databases": ["postgres"],
        "testing_frameworks": ["cargo-test"],
        "custom_rules": "Używaj zasady TDD i bezwzględnie dbaj o typowanie.",
        "enforce_tdd": True,
        "enforce_spec_compliance_check": True,
        "generate_unit_tests": True,
        "generate_integration_tests": True,
        "generate_functional_tests": True
    }
    
    # Create
    res_create = client.post("/api/v1/specs", json=payload)
    assert res_create.status_code == 201
    created_data = res_create.json()
    assert "id" in created_data
    spec_id = created_data["id"]

    # Get single
    res_get = client.get(f"/api/v1/specs/{spec_id}")
    assert res_get.status_code == 200
    spec_detail = res_get.json()
    assert spec_detail["title"] == "Moja Aplikacja Testowa v2"
    assert "agents_md" in spec_detail
    assert "spec_md" in spec_detail
    assert "tasks_md" in spec_detail
    assert "zgodności" in spec_detail["agents_md"].lower()
    assert "weryfikacja" in spec_detail["tasks_md"].lower()
    assert "mermaid" in spec_detail["spec_md"].lower()

    # List all
    res_list = client.get("/api/v1/specs")
    assert res_list.status_code == 200
    specs_list = res_list.json()
    assert len(specs_list) >= 1

    # Delete
    res_del = client.delete(f"/api/v1/specs/{spec_id}")
    assert res_del.status_code == 200
