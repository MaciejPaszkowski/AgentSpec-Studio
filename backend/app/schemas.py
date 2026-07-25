from typing import List, Optional
from pydantic import BaseModel, Field
import datetime

class SpecCreateSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = ""
    agent_type: str = Field(default="agy") # agy, claude-code, codex, cursor, universal
    deployment_mode: str = Field(default="docker-compose") # docker-compose, native, kubernetes
    architecture_pattern: str = Field(default="clean") # clean, modular, event-driven, ddd, monolith
    language_output: str = Field(default="pl") # pl, en, de, fr, es, ru
    security_standards: List[str] = Field(default_factory=lambda: ["owasp", "jwt"]) # owasp, gdpr, jwt, oauth2, api-keys
    api_protocols: List[str] = Field(default_factory=lambda: ["rest"]) # rest, graphql, grpc, websockets
    mcp_integrations: List[str] = Field(default_factory=lambda: ["db-mcp"]) # db-mcp, browser-mcp, docs-mcp
    git_ci_cd: str = Field(default="github-actions") # github-actions, gitlab-ci, none
    preset_template: str = Field(default="custom") # custom, saas-fullstack, ai-rag, rust-microservice, web-ssr

    languages: List[str] = Field(default_factory=list)
    backend_frameworks: List[str] = Field(default_factory=list)
    frontend_frameworks: List[str] = Field(default_factory=list)
    databases: List[str] = Field(default_factory=list)
    testing_frameworks: List[str] = Field(default_factory=list)
    custom_rules: Optional[str] = ""
    enforce_tdd: bool = True
    enforce_spec_compliance_check: bool = True
    generate_unit_tests: bool = True
    generate_integration_tests: bool = True
    generate_functional_tests: bool = False
    split_modular_artifacts: bool = False

class SpecResponseSchema(SpecCreateSchema):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    agents_md: Optional[str] = None
    spec_md: Optional[str] = None
    tasks_md: Optional[str] = None

    backend_agents_md: Optional[str] = None
    backend_spec_md: Optional[str] = None
    backend_tasks_md: Optional[str] = None

    frontend_agents_md: Optional[str] = None
    frontend_spec_md: Optional[str] = None
    frontend_tasks_md: Optional[str] = None

    class Config:
        from_attributes = True

class TechOption(BaseModel):
    id: str
    name: str
    category: str
    icon: Optional[str] = None

class OptionsResponse(BaseModel):
    agents: List[TechOption]
    deployments: List[TechOption]
    output_languages: List[TechOption]
    architectures: List[TechOption]
    security: List[TechOption]
    protocols: List[TechOption]
    mcp_skills: List[TechOption]
    ci_cd_presets: List[TechOption]
    project_presets: List[TechOption]
    languages: List[TechOption]
    backend_frameworks: List[TechOption]
    frontend_frameworks: List[TechOption]
    databases: List[TechOption]
    testing_frameworks: List[TechOption]
