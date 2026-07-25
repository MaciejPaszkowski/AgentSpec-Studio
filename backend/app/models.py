import uuid
import datetime
from sqlalchemy import Column, String, Text, Boolean, DateTime, JSON
from app.database import Base

class SpecificationModel(Base):
    __tablename__ = "specifications"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    agent_type = Column(String(50), nullable=False, default="agy")
    deployment_mode = Column(String(50), nullable=False, default="docker-compose")
    architecture_pattern = Column(String(50), nullable=False, default="clean")
    language_output = Column(String(10), nullable=False, default="pl")
    security_standards = Column(JSON, nullable=False, default=list)
    api_protocols = Column(JSON, nullable=False, default=list)
    mcp_integrations = Column(JSON, nullable=False, default=list)
    git_ci_cd = Column(String(50), nullable=False, default="github-actions")
    preset_template = Column(String(50), nullable=False, default="custom")

    languages = Column(JSON, nullable=False, default=list)
    backend_frameworks = Column(JSON, nullable=False, default=list)
    frontend_frameworks = Column(JSON, nullable=False, default=list)
    databases = Column(JSON, nullable=False, default=list)
    testing_frameworks = Column(JSON, nullable=False, default=list)
    custom_rules = Column(Text, nullable=True, default="")
    enforce_tdd = Column(Boolean, nullable=False, default=True)
    enforce_spec_compliance_check = Column(Boolean, nullable=False, default=True)
    generate_unit_tests = Column(Boolean, nullable=False, default=True)
    generate_integration_tests = Column(Boolean, nullable=False, default=True)
    generate_functional_tests = Column(Boolean, nullable=False, default=False)
    split_modular_artifacts = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
