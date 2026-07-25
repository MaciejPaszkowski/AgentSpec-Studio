import pytest
from app.generator import generate_agent_artifacts

def test_generate_agent_artifacts_basic():
    spec_data = {
        "title": "E-Commerce Discount Service",
        "description": "System obliczania zniżek w sklepie internetowym",
        "agent_type": "agy",
        "languages": ["python", "typescript"],
        "backend_frameworks": ["fastapi", "node-express"],
        "frontend_frameworks": ["angular"],
        "databases": ["postgres", "redis"],
        "testing_frameworks": ["pytest", "vitest"],
        "custom_rules": "Używaj wzorca Repository oraz DTO dla każdego zapytania.",
        "enforce_tdd": True
    }

    result = generate_agent_artifacts(spec_data)

    assert "agents_md" in result
    assert "spec_md" in result
    assert "tasks_md" in result

    # Check content of AGENTS.md
    assert "AGENTS.md" in result["agents_md"] or "Instrukcje" in result["agents_md"]
    assert "python" in result["agents_md"].lower()
    assert "fastapi" in result["agents_md"].lower()
    assert "angular" in result["agents_md"].lower()
    assert "pytest" in result["agents_md"].lower()
    assert "Wzorca Repository" in result["agents_md"] or "custom_rules" in result["agents_md"] or "Repository" in result["agents_md"]
    assert "TDD" in result["agents_md"]

    # Check content of SPEC.md
    assert "E-Commerce Discount Service" in result["spec_md"]
    assert "postgres" in result["spec_md"].lower()

    # Check content of TASKS.md
    assert "TASKS" in result["tasks_md"]
    assert "[ ]" in result["tasks_md"]
