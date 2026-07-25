from typing import Dict, Any, List

COMMAND_MAP = {
    "python": "python3 -m pytest && mypy .",
    "rust": "cargo test && cargo clippy",
    "go": "go test ./... && go vet ./...",
    "dlang": "dub test",
    "javascript": "npm test",
    "typescript": "npx tsc --noEmit && npm test",
    "cpp": "cmake -B build && cmake --build build && ctest --test-dir build",
    "csharp": "dotnet test",
    "elixir": "mix test",
    "kotlin": "gradle test",
    "java": "mvn test",
    "zig": "zig test src/main.zig",
    "php": "vendor/bin/phpunit",
    "ruby": "bundle exec rspec",
    "fastapi": "pytest",
    "flask": "pytest",
    "django": "python manage.py test",
    "falcon": "pytest",
    "blacksheep": "pytest",
    "starlite": "pytest",
    "node-express": "npm test",
    "nestjs": "npm run test",
    "angular": "ng test --watch=false",
    "react": "npm test",
    "vue": "npm run test:unit",
    "pytest": "pytest -v",
    "vitest": "npx vitest run",
    "jest": "npx jest",
    "cargo-test": "cargo test",
    "go-test": "go test ./...",
    "dub-test": "dub test"
}

TRANSLATIONS = {
    "pl": {
        "agents_title": "Instrukcje dla Agenta AI",
        "arch_section": "1. Architektura i Stos Techniczny",
        "project": "Projekt",
        "arch_pattern": "Wzorzec Architektoniczny",
        "deployment": "Środowisko Uruchomieniowe",
        "api_proto": "Protokoły API",
        "languages": "Języki",
        "backend": "Backend",
        "frontend": "Frontend",
        "database": "Baza Danych",
        "git_commits": "Konwencja Commitów Git",
        "env_cmd_section": "2. Kluczowe Komendy Środowiskowe",
        "cmd_intro": "Przed zgłoszeniem zakończenia zadania MUSISZ uruchomić komendy i zweryfikować wynik:",
        "sec_section": "3. Standardy Bezpieczeństwa & Zgodności",
        "mcp_section": "4. Integracje MCP & AI Skills",
        "rules_section": "5. Zasady Metodyki i Pracy z Kodem",
        "tdd_rule": "- **Wymóg AI-TDD**: ZAWSZE twórz lub modyfikuj testy NAJPIERW (Red), upewnij się w terminalu że nie przechodzą, a dopiero potem pisz minimalny kod produkcyjny (Green).",
        "non_tdd_rule": "- **Testy**: Twórz testy pokrywające kluczowe scenariusze biznesowe.",
        "required_tests": "Wymagane Testy",
        "zero_hallucination": "- **Zero Halucynacji**: Odczytuj pliki repozytorium przy użyciu narzędzi czytania zanim użyjesz ścieżek czy typów.",
        "compliance_audit": "- **Audyt Zgodności**: Po zrealizowaniu zadań wykonaj weryfikację ze specyfikacją docs/SPEC.md.",
        "custom_rules_section": "6. Dedykowane Wymagania Użytkownika (Custom Rules)",
        "dod_section": "7. Kryteria Zakończenia Zadania (Definition of Done)",
        "dod_1": "1. Kod kompiluje się bez błędów Lintera i kompilatora.",
        "dod_2": "2. Pełny pakiet testów ({tests}) wykonuje się z wynikiem 100% PASS.",
        "dod_3": "3. Plik docs/TASKS.md zawiera zaktualizowane statusy kroków [x].",

        "spec_title": "SPEC: {title}",
        "spec_overview": "1. Przegląd i Cel Projektu",
        "spec_stack": "Użyty Stos Techniczny i Wzorce:",
        "spec_diagram": "2. Diagram Architektury Systemu (Mermaid.js)",
        "spec_sec": "3. Standardy Bezpieczeństwa & Zgodności",
        "spec_domain": "4. Dodatkowe Wymagania Domenowe",
        "spec_scenarios": "5. Scenariusze Testowe (Given-When-Then)",

        "tasks_title": "TASKS: Lista Zadań dla Agenta AI - {title}",
        "tasks_hints": "Wskazówki dla Agenta AI:\n1. Wykonuj zadania sekwencyjnie po jednym punkcie.\n2. Stosuj zasadę Conventional Commits (feat:, fix:, test:).\n3. Dla każdego punktu stosuj cykl TDD (Red -> Green -> Refactor).",
        "step_1": "Krok 1: Przygotowanie Struktury Architektonicznej",
        "step_2": "Krok 2: Zestaw Testów",
        "step_3": "Krok 3: Implementacja Logiki Domenowej i Serwisów",
        "step_4": "Krok 4: Punkty Endpoints i Interfejs Użytkownika",
        "step_5": "Krok 5: Weryfikacja Zgodności ze SPEC.md"
    },
    "en": {
        "agents_title": "AI Agent Instructions",
        "arch_section": "1. Architecture & Tech Stack",
        "project": "Project",
        "arch_pattern": "Architecture Pattern",
        "deployment": "Runtime Environment",
        "api_proto": "API Protocols",
        "languages": "Languages",
        "backend": "Backend",
        "frontend": "Frontend",
        "database": "Database",
        "git_commits": "Git Commit Convention",
        "env_cmd_section": "2. Key Environment Commands",
        "cmd_intro": "Before reporting task completion, you MUST run these commands and verify output:",
        "sec_section": "3. Security & Compliance Standards",
        "mcp_section": "4. MCP & AI Skills Integrations",
        "rules_section": "5. Methodology & Coding Rules",
        "tdd_rule": "- **AI-TDD Requirement**: ALWAYS create or modify tests FIRST (Red), ensure they fail in terminal, and only then write minimal production code (Green).",
        "non_tdd_rule": "- **Testing**: Write tests covering key business scenarios.",
        "required_tests": "Required Tests",
        "zero_hallucination": "- **Zero Hallucination**: Inspect repository files using file reading tools before referencing symbols or paths.",
        "compliance_audit": "- **Compliance Audit**: After completing tasks, perform a full verification against docs/SPEC.md.",
        "custom_rules_section": "6. Custom User Requirements",
        "dod_section": "7. Definition of Done",
        "dod_1": "1. Code compiles without linter or compiler errors.",
        "dod_2": "2. Full test suite ({tests}) passes with 100% PASS result.",
        "dod_3": "3. File docs/TASKS.md contains updated step statuses [x].",

        "spec_title": "SPEC: {title}",
        "spec_overview": "1. Project Overview & Goal",
        "spec_stack": "Tech Stack & Design Patterns:",
        "spec_diagram": "2. System Architecture Diagram (Mermaid.js)",
        "spec_sec": "3. Security & Compliance Standards",
        "spec_domain": "4. Additional Domain Requirements",
        "spec_scenarios": "5. Test Scenarios (Given-When-Then)",

        "tasks_title": "TASKS: AI Agent Task Checklist - {title}",
        "tasks_hints": "Guidelines for AI Agent:\n1. Execute tasks sequentially, one item at a time.\n2. Follow Conventional Commits (feat:, fix:, test:).\n3. Apply TDD cycle (Red -> Green -> Refactor) for each step.",
        "step_1": "Step 1: Architectural Structure Setup",
        "step_2": "Step 2: Test Suite Setup",
        "step_3": "Step 3: Domain Logic & Services Implementation",
        "step_4": "Step 4: Endpoints & User Interface",
        "step_5": "Step 5: Compliance Audit against SPEC.md"
    },
    "de": {
        "agents_title": "Anweisungen für KI-Agenten",
        "arch_section": "1. Architektur & Tech-Stack",
        "project": "Projekt",
        "arch_pattern": "Architekturmuster",
        "deployment": "Laufzeitumgebung",
        "api_proto": "API-Protokolle",
        "languages": "Sprachen",
        "backend": "Backend",
        "frontend": "Frontend",
        "database": "Datenbank",
        "git_commits": "Git-Commit-Konvention",
        "env_cmd_section": "2. Wichtige Umgebungsbefehle",
        "cmd_intro": "Vor der Aufgabenerledigung MÜSSEN Sie diese Befehle ausführen und das Ergebnis überprüfen:",
        "sec_section": "3. Sicherheits- & Compliance-Standards",
        "mcp_section": "4. MCP- & KI-Skills-Integrationen",
        "rules_section": "5. Methodik & Code-Regeln",
        "tdd_rule": "- **KI-TDD Anforderung**: Erstellen Sie Tests IMMER ZUERST (Red), prüfen Sie Fehlschlag im Terminal und schreiben Sie erst dann Produktionscode (Green).",
        "non_tdd_rule": "- **Testing**: Schreiben Sie Tests für wichtige Geschäftsszenarien.",
        "required_tests": "Erforderliche Tests",
        "zero_hallucination": "- **Keine Halluzinationen**: Lesen Sie Repository-Dateien vor der Verwendung von Pfaden.",
        "compliance_audit": "- **Compliance-Audit**: Führen Sie nach Abschluss der Aufgaben eine Prüfung gegen docs/SPEC.md durch.",
        "custom_rules_section": "6. Benutzerdefinierte Anforderungen",
        "dod_section": "7. Definition of Done",
        "dod_1": "1. Code kompiliert ohne Linter- oder Compilerfehler.",
        "dod_2": "2. Gesamte Testsuite ({tests}) verläuft zu 100% erfolgreich.",
        "dod_3": "3. Datei docs/TASKS.md enthält aktualisierte Statuswerte [x].",

        "spec_title": "SPEC: {title}",
        "spec_overview": "1. Projektübersicht & Ziel",
        "spec_stack": "Tech-Stack & Entwurfsmuster:",
        "spec_diagram": "2. Systemarchitektur-Diagramm (Mermaid.js)",
        "spec_sec": "3. Sicherheits- & Compliance-Standards",
        "spec_domain": "4. Zusätzliche Domänenanforderungen",
        "spec_scenarios": "5. Testszenerien (Given-When-Then)",

        "tasks_title": "TASKS: Aufgabenliste für KI-Agenten - {title}",
        "tasks_hints": "Richtlinien für den KI-Agenten:\n1. Führen Sie Aufgaben sequentiell aus.\n2. Verwenden Sie Conventional Commits (feat:, fix:).\n3. Wenden Sie TDD an (Red -> Green -> Refactor).",
        "step_1": "Schritt 1: Einrichtung der Architekturstruktur",
        "step_2": "Schritt 2: Einrichtung der Testsuite",
        "step_3": "Schritt 3: Implementierung der Domänenlogik",
        "step_4": "Schritt 4: Endpunkte & Benutzeroberfläche",
        "step_5": "Schritt 5: Compliance-Prüfung gegen SPEC.md"
    },
    "fr": {
        "agents_title": "Instructions pour l'Agent IA",
        "arch_section": "1. Architecture et Stack Technique",
        "project": "Projet",
        "arch_pattern": "Modèle d'Architecture",
        "deployment": "Environnement d'Exécution",
        "api_proto": "Protocoles API",
        "languages": "Langages",
        "backend": "Backend",
        "frontend": "Frontend",
        "database": "Base de Données",
        "git_commits": "Convention de Commit Git",
        "env_cmd_section": "2. Commandes d'Environnement Clés",
        "cmd_intro": "Avant de signaler la fin de la tâche, vous DEVEZ exécuter ces commandes et vérifier le résultat :",
        "sec_section": "3. Normes de Sécurité & Conformité",
        "mcp_section": "4. Intégrations MCP et Compétences IA",
        "rules_section": "5. Méthodologie et Règles de Code",
        "tdd_rule": "- **Exigence AI-TDD**: Créez TOUJOURS les tests EN PREMIER (Rouge), vérifiez l'échec en terminal, puis écrivez le code de production (Vert).",
        "non_tdd_rule": "- **Tests**: Écrivez des tests couvrant les scénarios clés.",
        "required_tests": "Tests Requis",
        "zero_hallucination": "- **Zéro Hallucination**: Inspectez les fichiers du dépôt avant d'utiliser des chemins.",
        "compliance_audit": "- **Audit de Conformité**: Effectuez une vérification complète par rapport à docs/SPEC.md.",
        "custom_rules_section": "6. Exigences Personnalisées",
        "dod_section": "7. Définition de Terminé (Definition of Done)",
        "dod_1": "1. Le code compile sans erreurs de linter ni de compilateur.",
        "dod_2": "2. La suite de tests ({tests}) passe à 100%.",
        "dod_3": "3. Le fichier docs/TASKS.md contient les statuts mis à jour [x].",

        "spec_title": "SPEC: {title}",
        "spec_overview": "1. Aperçu et Objectif du Projet",
        "spec_stack": "Stack Technique & Modèles d'Architecture :",
        "spec_diagram": "2. Diagramme d'Architecture Système (Mermaid.js)",
        "spec_sec": "3. Normes de Sécurité & Conformité",
        "spec_domain": "4. Exigences Métier Supplémentaires",
        "spec_scenarios": "5. Scénarios de Test (Given-When-Then)",

        "tasks_title": "TASKS: Liste de Tâches pour l'Agent IA - {title}",
        "tasks_hints": "Directives pour l'Agent IA :\n1. Exécutez les tâches séquentiellement.\n2. Suivez la convention Conventional Commits (feat:, fix:).\n3. Appliquez le cycle TDD (Rouge -> Vert -> Refactor).",
        "step_1": "Étape 1: Structure Architectural",
        "step_2": "Étape 2: Suite de Tests",
        "step_3": "Étape 3: Logique Métier",
        "step_4": "Étape 4: Points d'Accès et Interface",
        "step_5": "Étape 5: Audit de Conformité avec SPEC.md"
    },
    "es": {
        "agents_title": "Instrucciones para el Agente IA",
        "arch_section": "1. Arquitectura y Stack Técnico",
        "project": "Proyecto",
        "arch_pattern": "Patrón de Arquitectura",
        "deployment": "Entorno de Ejecución",
        "api_proto": "Protocolos API",
        "languages": "Lenguajes",
        "backend": "Backend",
        "frontend": "Frontend",
        "database": "Base de Datos",
        "git_commits": "Convención de Commits de Git",
        "env_cmd_section": "2. Comandos Clave del Entorno",
        "cmd_intro": "Antes de informar la finalización de la tarea, DEBES ejecutar estos comandos y verificar el resultado:",
        "sec_section": "3. Estándares de Seguridad y Cumplimiento",
        "mcp_section": "4. Integraciones MCP y Habilidades IA",
        "rules_section": "5. Metodología y Reglas de Código",
        "tdd_rule": "- **Requisito AI-TDD**: Crea SIEMPRE las pruebas PRIMERO (Rojo), verifica el fallo en la terminal y luego escribe el código de producción (Verde).",
        "non_tdd_rule": "- **Pruebas**: Escribe pruebas que cubran los escenarios clave del negocio.",
        "required_tests": "Pruebas Requeridas",
        "zero_hallucination": "- **Cero Alucinaciones**: Inspecciona los archivos del repositorio antes de usar rutas.",
        "compliance_audit": "- **Auditoría de Cumplimiento**: Realiza una verificación completa con docs/SPEC.md.",
        "custom_rules_section": "6. Requisitos Personalizados",
        "dod_section": "7. Definición de Hecho (Definition of Done)",
        "dod_1": "1. El código se compila sin errores de linter ni de compilador.",
        "dod_2": "2. El conjunto de pruebas ({tests}) se ejecuta con un 100% de éxito.",
        "dod_3": "3. El archivo docs/TASKS.md contiene los estados actualizados [x].",

        "spec_title": "SPEC: {title}",
        "spec_overview": "1. Descripción y Objetivo del Proyecto",
        "spec_stack": "Stack Técnico y Patrones de Diseño:",
        "spec_diagram": "2. Diagrama de Arquitectura del Sistema (Mermaid.js)",
        "spec_sec": "3. Estándares de Seguridad y Cumplimiento",
        "spec_domain": "4. Requisitos Adicionales del Dominio",
        "spec_scenarios": "5. Escenarios de Prueba (Given-When-Then)",

        "tasks_title": "TASKS: Lista de Tareas para el Agente IA - {title}",
        "tasks_hints": "Directrices para el Agente IA:\n1. Ejecuta las tareas secuencialmente.\n2. Usa Conventional Commits (feat:, fix:).\n3. Aplica el ciclo TDD (Rojo -> Verde -> Refactor).",
        "step_1": "Paso 1: Configuración de la Estructura Arquitectónica",
        "step_2": "Paso 2: Configuración del Conjunto de Pruebas",
        "step_3": "Paso 3: Implementación de la Lógica del Dominio",
        "step_4": "Paso 4: Puntos de Acceso e Interfaz de Usuario",
        "step_5": "Paso 5: Auditoría de Cumplimiento con SPEC.md"
    },
    "ru": {
        "agents_title": "Инструкции для ИИ-Агента",
        "arch_section": "1. Архитектура и Технический Стек",
        "project": "Проект",
        "arch_pattern": "Архитектурный Шаблон",
        "deployment": "Среда Выполнения",
        "api_proto": "Протоколы API",
        "languages": "Языки",
        "backend": "Бэкенд",
        "frontend": "Фронтенд",
        "database": "База Данных",
        "git_commits": "Соглашение о Коммитах Git",
        "env_cmd_section": "2. Ключевые Команды Окружения",
        "cmd_intro": "Перед отчетом о завершении задачи вы ДОЛЖНЫ выполнить эти команды и проверить результат:",
        "sec_section": "3. Стандарты Безопасности и Соответствия",
        "mcp_section": "4. Интеграции MCP и Навыки ИИ",
        "rules_section": "5. Методология и Правила Кода",
        "tdd_rule": "- **Требование AI-TDD**: ВСЕГДА создавайте тесты СНАЧАЛА (Red), убедитесь в сбое в терминале и только затем пишите продуктовый код (Green).",
        "non_tdd_rule": "- **Тестирование**: Пишите тесты, покрывающие ключевые бизнес-сценарии.",
        "required_tests": "Обязательные Тесты",
        "zero_hallucination": "- **Ноль Галлюцинаций**: Читайте файлы репозитория перед использованием путей.",
        "compliance_audit": "- **Аудит Соответствия**: Проведите полную проверку с docs/SPEC.md.",
        "custom_rules_section": "6. Пользовательские Требования",
        "dod_section": "7. Критерии Завершения (Definition of Done)",
        "dod_1": "1. Код компилируется без ошибок линтера и компилятора.",
        "dod_2": "2. Полный набор тестов ({tests}) проходит на 100%.",
        "dod_3": "3. Файл docs/TASKS.md содержит обновленные статусы [x].",

        "spec_title": "SPEC: {title}",
        "spec_overview": "1. Обзор и Цель Проекта",
        "spec_stack": "Технический Стек и Шаблоны Проектирования:",
        "spec_diagram": "2. Диаграмма Архитектуры Системы (Mermaid.js)",
        "spec_sec": "3. Стандарты Безопасности и Соответствия",
        "spec_domain": "4. Дополнительные Доменные Требования",
        "spec_scenarios": "5. Тестовые Сценарии (Given-When-Then)",

        "tasks_title": "TASKS: Список Задач для ИИ-Агента - {title}",
        "tasks_hints": "Рекомендации для ИИ-Агента:\n1. Выполняйте задачи последовательно.\n2. Используйте Conventional Commits (feat:, fix:).\n3. Применяйте цикл TDD (Красный -> Зеленый -> Рефакторинг).",
        "step_1": "Шаг 1: Подготовка Архитектурной Структуры",
        "step_2": "Шаг 2: Подготовка Набора Тестов",
        "step_3": "Шаг 3: Реализация Доменной Логики",
        "step_4": "Шаг 4: Эндпоинты и Пользовательский Интерфейс",
        "step_5": "Шаг 5: Проверка Соответствия с SPEC.md"
    }
}

def generate_agent_artifacts(spec: Dict[str, Any]) -> Dict[str, Any]:
    title = spec.get("title", "Bez tytułu")
    description = spec.get("description", "")
    agent_type = spec.get("agent_type", "universal")
    deployment_mode = spec.get("deployment_mode", "docker-compose")
    arch_pattern = spec.get("architecture_pattern", "clean")
    lang_out = spec.get("language_output", "pl")
    if lang_out not in TRANSLATIONS:
        lang_out = "pl"
    t = TRANSLATIONS[lang_out]

    security_stds = spec.get("security_standards", ["owasp", "jwt"])
    api_protocols = spec.get("api_protocols", ["rest"])
    mcp_integrations = spec.get("mcp_integrations", ["db-mcp"])
    git_ci_cd = spec.get("git_ci_cd", "github-actions")

    languages = spec.get("languages", [])
    backend_frameworks = spec.get("backend_frameworks", [])
    frontend_frameworks = spec.get("frontend_frameworks", [])
    databases = spec.get("databases", [])
    testing_frameworks = spec.get("testing_frameworks", [])
    custom_rules = spec.get("custom_rules", "")
    enforce_tdd = spec.get("enforce_tdd", True)
    enforce_spec_compliance = spec.get("enforce_spec_compliance_check", True)
    gen_unit = spec.get("generate_unit_tests", True)
    gen_integration = spec.get("generate_integration_tests", True)
    gen_functional = spec.get("generate_functional_tests", False)

    dep_label = "Docker Compose" if deployment_mode == "docker-compose" else ("Native System Environment" if deployment_mode == "native" else "Kubernetes K8s")

    # Collect commands
    commands: List[str] = []
    if deployment_mode == "docker-compose":
        commands.append("- **Docker Compose Build & Run**: `docker-compose up -d --build`")
        commands.append("- **Logs**: `docker-compose logs -f`")
    elif deployment_mode == "native":
        commands.append("- **Native Run**: Activate environment and start server scripts")

    all_techs = languages + backend_frameworks + frontend_frameworks + testing_frameworks
    for tech in all_techs:
        t_low = tech.lower()
        if t_low in COMMAND_MAP and COMMAND_MAP[t_low] not in commands:
            commands.append(f"- **{tech}**: `{COMMAND_MAP[t_low]}`")

    # Test types list
    test_types = []
    if gen_unit: test_types.append("Unit Tests")
    if gen_integration: test_types.append("Integration Tests")
    if gen_functional: test_types.append("Functional/E2E Tests")

    # Mermaid diagram generation
    be_label = backend_frameworks[0] if backend_frameworks else "Backend API"
    fe_label = frontend_frameworks[0] if frontend_frameworks else "Frontend UI"
    db_label = databases[0] if databases else "Database"
    
    mermaid_diagram = f"""```mermaid
graph TD
    Client["📱 Client / Browser"] -->|{', '.join(api_protocols).upper()}| Frontend["🎨 {fe_label}"]
    Frontend -->|HTTP / API| Backend["⚙️ {be_label}"]
    Backend -->|ORM / SQL| DB[("🗄️ {db_label}")]
```"""

    # Build AGENTS.md / CLAUDE.md
    filename_agent = 'CLAUDE.md' if agent_type == 'claude-code' else 'AGENTS.md'
    agents_md = f"""# {t['agents_title']} ({filename_agent})

## {t['arch_section']}
- **{t['project']}**: {title}
- **{t['arch_pattern']}**: {arch_pattern.upper()}
- **{t['deployment']}**: {dep_label}
- **{t['api_proto']}**: {', '.join(api_protocols).upper()}
- **{t['languages']}**: {', '.join(languages) if languages else 'N/A'}
- **{t['backend']}**: {', '.join(backend_frameworks) if backend_frameworks else 'N/A'}
- **{t['frontend']}**: {', '.join(frontend_frameworks) if frontend_frameworks else 'N/A'}
- **{t['database']}**: {', '.join(databases) if databases else 'N/A'}
- **{t['git_commits']}**: Conventional Commits (`feat:`, `fix:`, `refactor:`, `test:`, `docs:`)

## {t['env_cmd_section']}
{t['cmd_intro']}
{chr(10).join(commands)}

## {t['sec_section']}
{chr(10).join(['- Standard: ' + s for s in security_stds])}

## {t['mcp_section']}
{chr(10).join(['- Skill: ' + m for m in mcp_integrations])}

## {t['rules_section']}
{t['tdd_rule'] if enforce_tdd else t['non_tdd_rule']}
- **{t['required_tests']}**: {', '.join(test_types)}.
{t['zero_hallucination']}
{t['compliance_audit'] if enforce_spec_compliance else ''}

## {t['custom_rules_section']}
{custom_rules if custom_rules.strip() else "N/A"}

## {t['dod_section']}
{t['dod_1']}
{t['dod_2'].format(tests=', '.join(test_types))}
{t['dod_3']}
"""

    # Build SPEC.md
    spec_md = f"""# {t['spec_title'].format(title=title)}

## {t['spec_overview']}
{description if description else title}

### {t['spec_stack']}
- **{t['arch_pattern']}**: {arch_pattern.upper()}
- **{t['deployment']}**: {dep_label}
- **{t['api_proto']}**: {', '.join(api_protocols).upper()}
- **{t['languages']}**: {', '.join(languages)}
- **{t['backend']} / {t['frontend']}**: {', '.join(backend_frameworks)} / {', '.join(frontend_frameworks)}
- **{t['database']}**: {', '.join(databases)}

## {t['spec_diagram']}
{mermaid_diagram}

## {t['spec_sec']}
{chr(10).join(['- Standard: ' + s for s in security_stds])}

## {t['spec_domain']}
{custom_rules if custom_rules.strip() else "N/A"}

## {t['spec_scenarios']}
1. **Happy Path**:
   - **Given**: Valid input data.
   - **When**: Request is processed via {', '.join(api_protocols).upper()}.
   - **Then**: 200 OK with expected payload.
2. **Edge Case**:
   - **Given**: Invalid payload or missing auth headers.
   - **When**: Request reaches server.
   - **Then**: Server returns error status with detailed reason.
"""

    # Build TASKS.md
    tasks_md = f"""# {t['tasks_title'].format(title=title)}

Spec: `docs/SPEC.md`

{t['tasks_hints']}

---

## Task Checklist:

- [ ] **{t['step_1']} ({arch_pattern.upper()})**
  - [ ] Initialize directory structure & models

- [ ] **{t['step_2']} ({', '.join(test_types)})**
  - [ ] Write unit & integration test suites (Red)

- [ ] **{t['step_3']}**
  - [ ] Implement domain logic (Green)

- [ ] **{t['step_4']}**
  - [ ] Create API controllers & UI components

- [ ] **{t['step_5']}**
  - [ ] Audit implementation against docs/SPEC.md & mark tasks [x]
"""

    ci_workflow = f"""name: CI Workflow

on:
  push:
    branches: [ main, master, dev ]
  pull_request:
    branches: [ main, master ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Tests
        run: echo "Testing {title}..."
""" if git_ci_cd == "github-actions" else None

    return {
        "agents_md": agents_md,
        "spec_md": spec_md,
        "tasks_md": tasks_md,
        "ci_workflow": ci_workflow
    }
