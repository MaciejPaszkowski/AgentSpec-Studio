export interface TechOption {
  id: string;
  name: string;
  category: string;
  icon?: string;
}

export interface OptionsResponse {
  agents: TechOption[];
  deployments: TechOption[];
  output_languages: TechOption[];
  architectures: TechOption[];
  security: TechOption[];
  protocols: TechOption[];
  mcp_skills: TechOption[];
  ci_cd_presets: TechOption[];
  project_presets: TechOption[];
  languages: TechOption[];
  backend_frameworks: TechOption[];
  frontend_frameworks: TechOption[];
  databases: TechOption[];
  testing_frameworks: TechOption[];
}

export interface SpecCreateRequest {
  title: string;
  description?: string;
  agent_type: string;
  deployment_mode: string;
  architecture_pattern: string;
  language_output: string;
  security_standards: string[];
  api_protocols: string[];
  mcp_integrations: string[];
  git_ci_cd: string;
  preset_template: string;
  languages: string[];
  backend_frameworks: string[];
  frontend_frameworks: string[];
  databases: string[];
  testing_frameworks: string[];
  custom_rules?: string;
  enforce_tdd: boolean;
  enforce_spec_compliance_check: boolean;
  generate_unit_tests: boolean;
  generate_integration_tests: boolean;
  generate_functional_tests: boolean;
  split_modular_artifacts?: boolean;
}

export interface SpecResponse extends SpecCreateRequest {
  id: string;
  created_at: string;
  updated_at: string;
  agents_md?: string;
  spec_md?: string;
  tasks_md?: string;

  backend_agents_md?: string;
  backend_spec_md?: string;
  backend_tasks_md?: string;

  frontend_agents_md?: string;
  frontend_spec_md?: string;
  frontend_tasks_md?: string;
}
