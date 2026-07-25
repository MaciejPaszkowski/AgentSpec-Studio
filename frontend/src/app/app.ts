import { Component, OnInit, signal, WritableSignal, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SpecService } from './services/spec.service';
import { OptionsResponse, SpecResponse } from './models/spec.model';

export const DEFAULT_TEXTS: Record<string, { title: string; description: string; customRules: string }> = {
  pl: {
    title: 'Mój Nowy Projekt AI',
    description: 'Złożony system w Python 3.12, Postgres i Angular',
    customRules: 'Wykorzystuj wzorzec Repository, ścisłe typowanie oraz obsługę błędów w osobnym module.'
  },
  en: {
    title: 'My New AI Project',
    description: 'Complex system in Python 3.12, Postgres and Angular',
    customRules: 'Use Repository pattern, strict typing, and error handling in a dedicated module.'
  },
  de: {
    title: 'Mein Neues KI-Projekt',
    description: 'Komplexes System in Python 3.12, Postgres und Angular',
    customRules: 'Verwenden Sie das Repository-Muster, strikte Typisierung und Fehlerbehandlung in einem separaten Modul.'
  },
  fr: {
    title: 'Mon Nouveau Projet IA',
    description: 'Système complexe en Python 3.12, Postgres et Angular',
    customRules: 'Utilisez le modèle Repository, le typage strict et la gestion des erreurs dans un module dédié.'
  },
  es: {
    title: 'Mi Nuevo Proyecto IA',
    description: 'Sistema complejo en Python 3.12, Postgres y Angular',
    customRules: 'Utilice el patrón Repository, tipado estricto y gestión de errores en un módulo dedicado.'
  },
  ru: {
    title: 'Мой Новый ИИ-Проект',
    description: 'Сложная система на Python 3.12, Postgres и Angular',
    customRules: 'Используйте паттерн Repository, строгую типизацию и обработку ошибок в отдельном модуле.'
  }
};

export const PRESET_TRANSLATIONS: Record<string, Record<string, { title: string; description: string }>> = {
  'saas-fullstack': {
    pl: { title: 'SaaS Fullstack Platform', description: 'Aplikacja SaaS z autoryzacją JWT, FastAPI backendem i Angular frontendem w Dockerze.' },
    en: { title: 'SaaS Fullstack Platform', description: 'SaaS application with JWT authorization, FastAPI backend, and Angular frontend in Docker.' },
    de: { title: 'SaaS-Fullstack-Plattform', description: 'SaaS-Anwendung mit JWT-Autorisierung, FastAPI-Backend und Angular-Frontend in Docker.' },
    fr: { title: 'Plateforme Fullstack SaaS', description: 'Application SaaS avec autorisation JWT, backend FastAPI et frontend Angular dans Docker.' },
    es: { title: 'Plataforma Fullstack SaaS', description: 'Aplicación SaaS con autorización JWT, backend FastAPI y frontend Angular en Docker.' },
    ru: { title: 'Полностековая SaaS-Платформа', description: 'SaaS-приложение с JWT-авторизацией, бэкендом FastAPI и фронтендом Angular в Docker.' }
  },
  'ai-rag': {
    pl: { title: 'AI RAG Knowledge Agent', description: 'System wyszukiwania semantycznego z wektorową bazą Qdrant i silnikiem LangChain.' },
    en: { title: 'AI RAG Knowledge Agent', description: 'Semantic search system with Qdrant vector database and LangChain engine.' },
    de: { title: 'KI-RAG Wissensagent', description: 'Semantisches Suchsystem mit Qdrant-Vektordatenbank und LangChain-Engine.' },
    fr: { title: 'Agent de Connaissances IA RAG', description: 'Système de recherche sémantique avec base vectorielle Qdrant et moteur LangChain.' },
    es: { title: 'Agente de Conocimiento IA RAG', description: 'Sistema de búsqueda semántica con base de datos vectorial Qdrant y motor LangChain.' },
    ru: { title: 'Агент Знаний ИИ RAG', description: 'Система семантического поиска с векторной базой данных Qdrant и движком LangChain.' }
  },
  'rust-microservice': {
    pl: { title: 'High-Performance Microservice', description: 'Wysokowydajny mikroserwis w języku Rust z gRPC i PostgreSQL.' },
    en: { title: 'High-Performance Microservice', description: 'High-performance microservice in Rust with gRPC and PostgreSQL.' },
    de: { title: 'Hochleistungs-Mikrodienst', description: 'Hochleistungs-Microservice in Rust mit gRPC und PostgreSQL.' },
    fr: { title: 'Microservice Haute Performance', description: 'Microservice haute performance en Rust avec gRPC et PostgreSQL.' },
    es: { title: 'Microservicio de Alto Rendimiento', description: 'Microservicio de alto rendimiento en Rust con gRPC y PostgreSQL.' },
    ru: { title: 'Высокопроизводительный Микросервис', description: 'Высокопроизводительный микросервис на Rust с gRPC и PostgreSQL.' }
  },
  'web-ssr': {
    pl: { title: 'Modern Web App SSR', description: 'Nowoczesny portal internetowy w Next.js z integracją Supabase.' },
    en: { title: 'Modern Web App SSR', description: 'Modern web portal in Next.js with Supabase integration.' },
    de: { title: 'Moderne Web-App-SSR', description: 'Modernes Webportal in Next.js mit Supabase-Integration.' },
    fr: { title: 'Application Web SSR Moderne', description: 'Portail web moderne en Next.js avec intégration Supabase.' },
    es: { title: 'Aplicación Web SSR Moderna', description: 'Portal web moderno en Next.js con integración Supabase.' },
    ru: { title: 'Современное Веб-Приложение SSR', description: 'Современный веб-портал на Next.js с интеграцией Supabase.' }
  }
};

export const UI_TRANSLATIONS: Record<string, Record<string, string>> = {
  pl: {
    headerTitle: 'AgentSpec Studio',
    headerSubtitle: 'Zaawansowany Generator Specyfikacji, Reguł AGENTS.md, Diagramów Mermaid i Metodyki AI-TDD',
    langLabel: '🌐 Język Interfejsu (UI Language):',
    aiInterviewBtn: '🤖 Wywiad ze Specyfikacją (Prompt AI)',
    hideAiInterviewBtn: '🤖 Ukryj Wywiad AI',
    refreshDbBtn: '🔄 Odśwież Bazę',
    aiInterviewTitle: '🤖 Prompt do Przeprowadzenia Wywiadu ze Specyfikacją z Agentem AI',
    aiInterviewSub: 'Skopiuj poniższy prompt i wklej go do swojego agenta (agy, Claude Code, Codex), aby przeprowadzony został z Tobą krótki wywiad precyzujący cel biznesowy:',
    quickStartTitle: '🚀 Szybki Start - Gotowe Presety Projektowe 1-Kliknięciem:',
    formTitle: '📝 Konfiguracja Projektu i Technologii',
    projNameLabel: 'Nazwa Projektu / Funkcjonalności',
    projNamePlaceholder: 'np. System Rozliczeń E-commerce',
    projDescLabel: 'Opis i Cel Biznesowy',
    projDescPlaceholder: 'np. Moduł obliczający zniżki i generujący faktury',
    agentLabel: '🤖 Agent AI',
    envLabel: '⚙️ Środowisko',
    outLangLabel: '🌐 Język Wyjściowy Dokumentów (SPEC.md, AGENTS.md)',
    archLabel: '🏗️ Wzorzec Architektury Systemu (Architecture Pattern)',
    securityLabel: '🛡️ Standardy Bezpieczeństwa & Zgodności (Security & Compliance)',
    protocolsLabel: '🔌 Protokoły Komunikacji API',
    mcpLabel: '🧰 Integracje MCP & AI Skills',
    cicdLabel: '🌿 CI/CD Pipeline & GitHub Actions Generator',
    langLabelForm: 'Języki Programowania',
    selectFromList: '(wybierz z listy)',
    backendLabel: 'Frameworki Backendowe',
    frontendLabel: 'Frameworki Frontendowe',
    dbLabel: 'Bazy Danych i Przechowywanie',
    customRulesLabel: '✍️ Ręcznie Wpisane Zasady i Wymagania Architektoniczne',
    customRulesPlaceholder: 'Tutaj możesz dopisać ręcznie specyficzne zasady, wzorce projektowe...',
    workflowHeader: '🛠️ Opcje Procesowe i Testowanie dla Agenta AI',
    enforceTdd: '🔴🟢 Wymuszaj metodykę AI-TDD (Red-Green-Refactor)',
    enforceCompliance: '🛡️ Zadanie Końcowe: Obowiązkowy Audyt Zgodności ze SPEC.md przed Oddaniem Zadania',
    testTypesHeader: 'Rodzaje Testów Do Wygenerowania przez Agenta:',
    unitTests: '🧪 Testy Jednostkowe (Unit Tests)',
    integrationTests: '🔗 Testy Integracyjne (Integration Tests)',
    functionalTests: '🌐 Testy Funkcyjne / E2E (End-to-End Tests)',
    generateBtn: '🚀 Wygeneruj Specyfikację i Reguły Agenta',
    generating: 'Generowanie...',
    previewTitle: '📄 Podgląd Artefaktów Agenta AI',
    copyBtn: '📋 Kopiuj Plik',
    downloadZipBtn: '📦 Pobierz Paczkę ZIP (z CI/CD)',
    copySuccess: 'Skopiowano do schowka!',
    emptyPreview: 'Skonfiguruj stos po lewej stronie i kliknij Wygeneruj Specyfikację, aby zobaczyć wygenerowane pliki.',
    historyTitle: '🗄️ Zapisane Specyfikacje w Bazie PostgreSQL',
    deleteBtn: 'Usuń',
    emptyHistory: 'Brak zapisanych specyfikacji w bazie. Wygeneruj pierwszą powyżej!',
    autoTranslateBtn: '🌐 Przetłumacz pola formularza'
  },
  en: {
    headerTitle: 'AgentSpec Studio',
    headerSubtitle: 'Advanced Specification Generator, AGENTS.md Rules, Mermaid Diagrams & AI-TDD Methodology',
    langLabel: '🌐 UI Interface Language:',
    aiInterviewBtn: '🤖 Spec Interview (AI Prompt)',
    hideAiInterviewBtn: '🤖 Hide AI Interview',
    refreshDbBtn: '🔄 Refresh DB',
    aiInterviewTitle: '🤖 AI Agent Specification Interview Prompt',
    aiInterviewSub: 'Copy the prompt below and paste it into your AI agent (agy, Claude Code, Codex) to conduct an interactive spec interview:',
    quickStartTitle: '🚀 Quick Start - 1-Click Project Presets:',
    formTitle: '📝 Project & Tech Stack Configuration',
    projNameLabel: 'Project / Feature Name',
    projNamePlaceholder: 'e.g. E-commerce Billing System',
    projDescLabel: 'Description & Business Goal',
    projDescPlaceholder: 'e.g. Module calculating discounts and generating invoices',
    agentLabel: '🤖 Target AI Agent',
    envLabel: '⚙️ Environment',
    outLangLabel: '🌐 Generated Output Document Language (SPEC.md, AGENTS.md)',
    archLabel: '🏗️ System Architecture Pattern',
    securityLabel: '🛡️ Security & Compliance Standards',
    protocolsLabel: '🔌 API Communication Protocols',
    mcpLabel: '🧰 MCP Integrations & AI Skills',
    cicdLabel: '🌿 CI/CD Pipeline & GitHub Actions Generator',
    langLabelForm: 'Programming Languages',
    selectFromList: '(select from list)',
    backendLabel: 'Backend Frameworks',
    frontendLabel: 'Frontend Frameworks',
    dbLabel: 'Databases & Storage',
    customRulesLabel: '✍️ Custom Architecture Rules & Requirements',
    customRulesPlaceholder: 'Write custom design patterns, security constraints, or domain rules here...',
    workflowHeader: '🛠️ Process Options & AI Testing',
    enforceTdd: '🔴🟢 Enforce AI-TDD Methodology (Red-Green-Refactor)',
    enforceCompliance: '🛡️ Final Step: Mandatory Compliance Audit against SPEC.md',
    testTypesHeader: 'Test Types for AI Agent to Generate:',
    unitTests: '🧪 Unit Tests',
    integrationTests: '🔗 Integration Tests',
    functionalTests: '🌐 Functional / E2E Tests',
    generateBtn: '🚀 Generate Specification & Agent Rules',
    generating: 'Generating...',
    previewTitle: '📄 AI Agent Artifacts Preview',
    copyBtn: '📋 Copy File',
    downloadZipBtn: '📦 Download ZIP Bundle (with CI/CD)',
    copySuccess: 'Copied to clipboard!',
    emptyPreview: 'Configure stack on the left and click Generate Specification to preview files.',
    historyTitle: '🗄️ Saved Specifications in PostgreSQL DB',
    deleteBtn: 'Delete',
    emptyHistory: 'No saved specifications found. Generate your first one above!',
    autoTranslateBtn: '🌐 Auto-Translate Form Fields'
  },
  de: {
    headerTitle: 'AgentSpec Studio',
    headerSubtitle: 'Erweiterter Spezifikations-Generator, AGENTS.md-Regeln, Mermaid-Diagramme & KI-TDD-Methodik',
    langLabel: '🌐 UI-Benutzeroberflächensprache:',
    aiInterviewBtn: '🤖 Spezifikations-Interview (KI-Prompt)',
    hideAiInterviewBtn: '🤖 Interview Ausblenden',
    refreshDbBtn: '🔄 DB Aktualisieren',
    aiInterviewTitle: '🤖 KI-Agent Spezifikations-Interview-Prompt',
    aiInterviewSub: 'Kopieren Sie den folgenden Prompt in Ihren KI-Agenten (agy, Claude Code, Codex) für ein interaktives Interview:',
    quickStartTitle: '🚀 Schnellstart - 1-Klick-Projektvorlagen:',
    formTitle: '📝 Projekt- & Tech-Stack-Konfiguration',
    projNameLabel: 'Projekt- / Funktionsname',
    projNamePlaceholder: 'z.B. E-Commerce Abrechnungssystem',
    projDescLabel: 'Beschreibung & Geschäftsziel',
    projDescPlaceholder: 'z.B. Modul zur Rabattberechnung und Rechnungserstellung',
    agentLabel: '🤖 Ziel-KI-Agent',
    envLabel: '⚙️ Umgebung',
    outLangLabel: '🌐 Ausgabesprache für Dokumente (SPEC.md, AGENTS.md)',
    archLabel: '🏗️ Systemarchitektur-Muster',
    securityLabel: '🛡️ Sicherheits- & Compliance-Standards',
    protocolsLabel: '🔌 API-Kommunikationsprotokolle',
    mcpLabel: '🧰 MCP-Integrationen & KI-Skills',
    cicdLabel: '🌿 CI/CD-Pipeline & GitHub Actions Generator',
    langLabelForm: 'Programmiersprachen',
    selectFromList: '(aus Liste auswählen)',
    backendLabel: 'Backend-Frameworks',
    frontendLabel: 'Frontend-Frameworks',
    dbLabel: 'Datenbanken & Speicher',
    customRulesLabel: '✍️ Benutzerdefinierte Architekturregeln',
    customRulesPlaceholder: 'Schreiben Sie benutzerdefinierte Entwurfsmuster oder Sicherheitsregeln hier...',
    workflowHeader: '🛠️ Prozessoptionen & KI-Testing',
    enforceTdd: '🔴🟢 KI-TDD-Methodik erzwingen (Red-Green-Refactor)',
    enforceCompliance: '🛡️ Letzter Schritt: Obligatorisches Compliance-Audit gegen SPEC.md',
    testTypesHeader: 'Zu generierende Testarten:',
    unitTests: '🧪 Unit-Tests',
    integrationTests: '🔗 Integrationstests',
    functionalTests: '🌐 Funktionstests / E2E-Tests',
    generateBtn: '🚀 Spezifikation & Agentenregeln Generieren',
    generating: 'Generierung...',
    previewTitle: '📄 Vorschau der KI-Agenten-Artefakte',
    copyBtn: '📋 Datei Kopieren',
    downloadZipBtn: '📦 ZIP-Paket Herunterladen (mit CI/CD)',
    copySuccess: 'In Zwischenablage kopiert!',
    emptyPreview: 'Konfigurieren Sie den Stack links und klicken Sie auf Spezifikation Generieren.',
    historyTitle: '🗄️ Gespeicherte Spezifikationen in PostgreSQL-DB',
    deleteBtn: 'Löschen',
    emptyHistory: 'Keine gespeicherten Spezifikationen vorhanden.',
    autoTranslateBtn: '🌐 Formularfelder Automatisch Übersetzen'
  },
  fr: {
    headerTitle: 'AgentSpec Studio',
    headerSubtitle: 'Générateur Avancé de Spécifications, Règles AGENTS.md, Diagrammes Mermaid et Méthodologie AI-TDD',
    langLabel: '🌐 Langue de l\'Interface (UI):',
    aiInterviewBtn: '🤖 Interview de Spécification (Prompt IA)',
    hideAiInterviewBtn: '🤖 Masquer l\'Interview',
    refreshDbBtn: '🔄 Rafraîchir BD',
    aiInterviewTitle: '🤖 Prompt d\'Interview de Spécification IA',
    aiInterviewSub: 'Copiez le prompt ci-dessous dans votre agent IA pour mener une interview de spécification :',
    quickStartTitle: '🚀 Démarrage Rapide - Préréglages en 1 Clic:',
    formTitle: '📝 Configuration du Projet & Stack Technique',
    projNameLabel: 'Nom du Projet / Fonctionnalité',
    projNamePlaceholder: 'ex. Système de Facturation E-commerce',
    projDescLabel: 'Description & Objectif Métier',
    projDescPlaceholder: 'ex. Module calculant les remises et générant les factures',
    agentLabel: '🤖 Agent IA Cible',
    envLabel: '⚙️ Environnement',
    outLangLabel: '🌐 Langue des Documents Générés (SPEC.md, AGENTS.md)',
    archLabel: '🏗️ Modèle d\'Architecture Système',
    securityLabel: '🛡️ Normes de Sécurité & Conformité',
    protocolsLabel: '🔌 Protocoles de Communication API',
    mcpLabel: '🧰 Intégrations MCP & Compétences IA',
    cicdLabel: '🌿 Pipeline CI/CD & Générateur GitHub Actions',
    langLabelForm: 'Langages de Programmation',
    selectFromList: '(sélectionnez dans la liste)',
    backendLabel: 'Frameworks Backend',
    frontendLabel: 'Frameworks Frontend',
    dbLabel: 'Bases de Données & Stockage',
    customRulesLabel: '✍️ Règles Personnalisées d\'Architecture',
    customRulesPlaceholder: 'Écrivez ici vos règles métier ou contraintes de sécurité...',
    workflowHeader: '🛠️ Options de Processus & Tests IA',
    enforceTdd: '🔴🟢 Appliquer la méthodologie AI-TDD (Red-Green-Refactor)',
    enforceCompliance: '🛡️ Étape Finale: Audit de Conformité Obligatoire avec SPEC.md',
    testTypesHeader: 'Types de Tests à Générer:',
    unitTests: '🧪 Tests Unitaires',
    integrationTests: '🔗 Tests d\'Intégration',
    functionalTests: '🌐 Tests Fonctionnels / E2E',
    generateBtn: '🚀 Générer la Spécification & Règles de l\'Agent',
    generating: 'Génération...',
    previewTitle: '📄 Aperçu des Artefacts de l\'Agent IA',
    copyBtn: '📋 Copier le Fichier',
    downloadZipBtn: '📦 Télécharger l\'Archive ZIP (avec CI/CD)',
    copySuccess: 'Copié dans le presse-papier !',
    emptyPreview: 'Configurez la stack à gauche et cliquez sur Générer la Spécification.',
    historyTitle: '🗄️ Spécifications Enregistrées dans PostgreSQL',
    deleteBtn: 'Supprimer',
    emptyHistory: 'Aucune spécification enregistrée.',
    autoTranslateBtn: '🌐 Traduire Automatiquement les Champs'
  },
  es: {
    headerTitle: 'AgentSpec Studio',
    headerSubtitle: 'Generador Avanzado de Especificaciones, Reglas AGENTS.md, Diagramas Mermaid y Metodología AI-TDD',
    langLabel: '🌐 Idioma de Interfaz (UI):',
    aiInterviewBtn: '🤖 Entrevista de Especificación (Prompt IA)',
    hideAiInterviewBtn: '🤖 Ocultar Entrevista',
    refreshDbBtn: '🔄 Actualizar BD',
    aiInterviewTitle: '🤖 Prompt de Entrevista de Especificación IA',
    aiInterviewSub: 'Copia el siguiente prompt en tu agente IA para realizar una entrevista interactiva:',
    quickStartTitle: '🚀 Inicio Rápido - Plantillas en 1 Clic:',
    formTitle: '📝 Configuración del Proyecto y Stack Técnico',
    projNameLabel: 'Nombre del Proyecto / Funcionalidad',
    projNamePlaceholder: 'ej. Sistema de Facturación E-commerce',
    projDescLabel: 'Descripción y Objetivo de Negocio',
    projDescPlaceholder: 'ej. Módulo que calcula descuentos y genera facturas',
    agentLabel: '🤖 Agente IA Objetivo',
    envLabel: '⚙️ Entorno',
    outLangLabel: '🌐 Idioma de los Documentos Generados (SPEC.md, AGENTS.md)',
    archLabel: '🏗️ Patrón de Arquitectura del Sistema',
    securityLabel: '🛡️ Estándares de Seguridad y Cumplimiento',
    protocolsLabel: '🔌 Protocolos de Comunicación API',
    mcpLabel: '🧰 Integraciones MCP y Habilidades IA',
    cicdLabel: '🌿 Pipeline CI/CD y Generador GitHub Actions',
    langLabelForm: 'Lenguajes de Programación',
    selectFromList: '(seleccionar de la lista)',
    backendLabel: 'Frameworks Backend',
    frontendLabel: 'Frameworks Frontend',
    dbLabel: 'Bases de Datos y Almacenamiento',
    customRulesLabel: '✍️ Reglas de Arquitectura Personalizadas',
    customRulesPlaceholder: 'Escribe patrones de diseño o reglas de seguridad aquí...',
    workflowHeader: '🛠️ Opciones de Proceso y Pruebas IA',
    enforceTdd: '🔴🟢 Forzar metodología AI-TDD (Red-Green-Refactor)',
    enforceCompliance: '🛡️ Paso Final: Auditoría Obligatoria de Cumplimiento con SPEC.md',
    testTypesHeader: 'Tipos de Pruebas a Generar:',
    unitTests: '🧪 Pruebas Unitarias',
    integrationTests: '🔗 Pruebas de Integración',
    functionalTests: '🌐 Pruebas Funcionales / E2E',
    generateBtn: '🚀 Generar Especificación y Reglas del Agente',
    generating: 'Generando...',
    previewTitle: '📄 Vista Previa de Artefactos del Agente IA',
    copyBtn: '📋 Copiar Archivo',
    downloadZipBtn: '📦 Descargar Paquete ZIP (con CI/CD)',
    copySuccess: '¡Copiado al portapapeles!',
    emptyPreview: 'Configura el stack a la izquierda y haz clic en Generar Especificación.',
    historyTitle: '🗄️ Especificaciones Guardadas en PostgreSQL',
    deleteBtn: 'Eliminar',
    emptyHistory: 'No hay especificaciones guardadas.',
    autoTranslateBtn: '🌐 Traducir Campos Automáticamente'
  },
  ru: {
    headerTitle: 'AgentSpec Studio',
    headerSubtitle: 'Продвинутый Генератор Спецификаций, Правил AGENTS.md, Диаграмм Mermaid и Методологии AI-TDD',
    langLabel: '🌐 Язык Интерфейса (UI):',
    aiInterviewBtn: '🤖 Интервью по Спецификации (ИИ-Промпт)',
    hideAiInterviewBtn: '🤖 Скрыть Интервью',
    refreshDbBtn: '🔄 Обновить БД',
    aiInterviewTitle: '🤖 Промпт для Интервью по Спецификации с ИИ-Агентом',
    aiInterviewSub: 'Скопируйте промпт ниже и вставьте его вашему ИИ-агенту (agy, Claude Code, Codex) для проведения интервью:',
    quickStartTitle: '🚀 Быстрый Старт - Пресеты Проектов в 1 Клик:',
    formTitle: '📝 Конфигурация Проекта и Технического Стека',
    projNameLabel: 'Название Проекта / Функционала',
    projNamePlaceholder: 'например, Система Биллинга E-commerce',
    projDescLabel: 'Описание и Бизнес-Цель',
    projDescPlaceholder: 'например, Модуль расчета скидок и генерации счетов',
    agentLabel: '🤖 Целевой ИИ-Агент',
    envLabel: '⚙️ Среда',
    outLangLabel: '🌐 Язык Сгенерированных Документов (SPEC.md, AGENTS.md)',
    archLabel: '🏗️ Архитектурный Шаблон Системы',
    securityLabel: '🛡️ Стандарты Безопасности и Соответствия',
    protocolsLabel: '🔌 Протоколы Коммуникации API',
    mcpLabel: '🧰 Интеграции MCP и Навыки ИИ',
    cicdLabel: '🌿 CI/CD Пайплайн и Генератор GitHub Actions',
    langLabelForm: 'Языки Программирования',
    selectFromList: '(выберите из списка)',
    backendLabel: 'Бэкенд Фреймворки',
    frontendLabel: 'Фронтенд Фреймворки',
    dbLabel: 'Базы Данных и Хранилища',
    customRulesLabel: '✍️ Пользовательские Правила Архитектуры',
    customRulesPlaceholder: 'Запишите здесь паттерны проектирования или ограничения безопасности...',
    workflowHeader: '🛠️ Опции Процесса и Тестирование ИИ',
    enforceTdd: '🔴🟢 Принудительная методология AI-TDD (Red-Green-Refactor)',
    enforceCompliance: '🛡️ Финальный Шаг: Обязательный Аудит Соответствия с SPEC.md',
    testTypesHeader: 'Типы Тестов для Генерации:',
    unitTests: '🧪 Юнит-Тесты',
    integrationTests: '🔗 Интеграционные Тесты',
    functionalTests: '🌐 Функциональные / E2E Тесты',
    generateBtn: '🚀 Сгенерировать Спецификацию и Правила Агента',
    generating: 'Генерация...',
    previewTitle: '📄 Предпросмотр Артефактов ИИ-Агента',
    copyBtn: '📋 Копировать Файл',
    downloadZipBtn: '📦 Скачать ZIP Архив (с CI/CD)',
    copySuccess: 'Скопировано в буфер обмена!',
    emptyPreview: 'Настройте стек слева и нажмите Сгенерировать Спецификацию.',
    historyTitle: '🗄️ Сохраненные Спецификации в PostgreSQL',
    deleteBtn: 'Удалить',
    emptyHistory: 'Нет сохраненных спецификаций.',
    autoTranslateBtn: '🌐 Автоматически Перевести Поля'
  }
};

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.css'
})
export class AppComponent implements OnInit {
  private specService = inject(SpecService);

  // Options loaded from backend
  options = signal<OptionsResponse | null>(null);

  // UI Language Signal (controls interface text)
  uiLanguage = signal<string>('pl');

  // Document Output Language Signal (controls generated SPEC.md, AGENTS.md, TASKS.md language)
  languageOutput = signal<string>('pl');

  // Form State
  title = signal<string>(DEFAULT_TEXTS['pl'].title);
  description = signal<string>(DEFAULT_TEXTS['pl'].description);
  agentType = signal<string>('agy');
  deploymentMode = signal<string>('docker-compose');
  architecturePattern = signal<string>('clean');
  gitCiCd = signal<string>('github-actions');
  presetTemplate = signal<string>('custom');

  // Selected technology chips
  selectedSecurity = signal<string[]>(['owasp', 'jwt']);
  selectedProtocols = signal<string[]>(['rest']);
  selectedMcp = signal<string[]>(['db-mcp']);

  selectedLanguages = signal<string[]>(['python', 'typescript']);
  selectedBackend = signal<string[]>(['fastapi']);
  selectedFrontend = signal<string[]>(['angular']);
  selectedDatabases = signal<string[]>(['postgres']);
  selectedTesting = signal<string[]>(['pytest', 'vitest']);

  customRules = signal<string>(DEFAULT_TEXTS['pl'].customRules);
  
  // Workflow & Testing Toggles
  enforceTdd = signal<boolean>(true);
  enforceSpecCompliance = signal<boolean>(true);
  generateUnitTests = signal<boolean>(true);
  generateIntegrationTests = signal<boolean>(true);
  generateFunctionalTests = signal<boolean>(false);

  // Results State
  currentSpec = signal<SpecResponse | null>(null);
  activeTab = signal<'agents' | 'spec' | 'tasks'>('agents');

  // History State
  savedSpecs = signal<SpecResponse[]>([]);
  isLoading = signal<boolean>(false);
  isTranslating = signal<boolean>(false);
  copyNotification = signal<string | null>(null);
  showAiInterviewPrompt = signal<boolean>(false);

  ngOnInit() {
    this.loadOptions();
    this.loadHistory();
  }

  // Helper method for calling free translation API (MyMemory API)
  async translateText(text: string, fromLang: string, toLang: string): Promise<string | null> {
    if (!text || fromLang === toLang) return text;
    try {
      const url = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=${fromLang}|${toLang}`;
      const res = await fetch(url);
      const data = await res.json();
      if (data?.responseData?.translatedText && data.responseData.translatedText !== text) {
        return data.responseData.translatedText;
      }
    } catch (e) {
      console.warn('Translation API failed:', e);
    }
    return null;
  }

  // Set UI language and translate custom or default fields instantly
  async setUiLanguage(lang: string) {
    const oldLang = this.uiLanguage();
    if (oldLang === lang) return;

    this.uiLanguage.set(lang);

    const currentTitle = this.title().trim();
    const currentDesc = this.description().trim();
    const currentRules = this.customRules().trim();

    // First check preset dictionary for instant response
    const currentPreset = this.presetTemplate();
    if (currentPreset && PRESET_TRANSLATIONS[currentPreset]) {
      const presetData = PRESET_TRANSLATIONS[currentPreset][lang] || PRESET_TRANSLATIONS[currentPreset]['pl'];
      this.title.set(presetData.title);
      this.description.set(presetData.description);
      return;
    }

    // Check if title, description, or customRules are standard defaults
    const isDefaultTitle = Object.values(DEFAULT_TEXTS).some(d => d.title === currentTitle);
    const isDefaultDesc = Object.values(DEFAULT_TEXTS).some(d => d.description === currentDesc);
    const isDefaultRules = Object.values(DEFAULT_TEXTS).some(d => d.customRules === currentRules);

    if (isDefaultTitle) {
      this.title.set(DEFAULT_TEXTS[lang]?.title || DEFAULT_TEXTS['pl'].title);
    }
    if (isDefaultDesc) {
      this.description.set(DEFAULT_TEXTS[lang]?.description || DEFAULT_TEXTS['pl'].description);
    }
    if (isDefaultRules) {
      this.customRules.set(DEFAULT_TEXTS[lang]?.customRules || DEFAULT_TEXTS['pl'].customRules);
    }

    // If user typed custom text in title, description or customRules, translate them via API!
    if (!isDefaultTitle || !isDefaultDesc || !isDefaultRules) {
      this.isTranslating.set(true);

      const tasks: Promise<void>[] = [];

      if (!isDefaultTitle && currentTitle) {
        tasks.push(
          this.translateText(currentTitle, oldLang, lang).then(txt => {
            if (txt) this.title.set(txt);
          })
        );
      }

      if (!isDefaultDesc && currentDesc) {
        tasks.push(
          this.translateText(currentDesc, oldLang, lang).then(txt => {
            if (txt) this.description.set(txt);
          })
        );
      }

      if (!isDefaultRules && currentRules) {
        tasks.push(
          this.translateText(currentRules, oldLang, lang).then(txt => {
            if (txt) this.customRules.set(txt);
          })
        );
      }

      await Promise.all(tasks);
      this.isTranslating.set(false);
    }
  }

  // Translation helper (uses uiLanguage)
  t(key: string): string {
    const lang = this.uiLanguage();
    const dict = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS['pl'];
    return dict[key] || UI_TRANSLATIONS['pl'][key] || key;
  }

  loadOptions() {
    this.specService.getOptions().subscribe({
      next: (data) => this.options.set(data),
      error: (err) => console.error('Błąd pobierania opcji:', err)
    });
  }

  loadHistory() {
    this.specService.getSpecs().subscribe({
      next: (data) => this.savedSpecs.set(data),
      error: (err) => console.error('Błąd pobierania historii:', err)
    });
  }

  applyPreset(presetId: string) {
    this.presetTemplate.set(presetId);
    const lang = this.uiLanguage();

    if (PRESET_TRANSLATIONS[presetId]) {
      const presetData = PRESET_TRANSLATIONS[presetId][lang] || PRESET_TRANSLATIONS[presetId]['pl'];
      this.title.set(presetData.title);
      this.description.set(presetData.description);
    }

    if (presetId === 'saas-fullstack') {
      this.architecturePattern.set('clean');
      this.selectedLanguages.set(['python', 'typescript']);
      this.selectedBackend.set(['fastapi']);
      this.selectedFrontend.set(['angular']);
      this.selectedDatabases.set(['postgres', 'redis']);
      this.selectedTesting.set(['pytest', 'vitest']);
      this.selectedSecurity.set(['owasp', 'jwt', 'gdpr']);
      this.selectedProtocols.set(['rest']);
    } else if (presetId === 'ai-rag') {
      this.architecturePattern.set('ddd');
      this.selectedLanguages.set(['python']);
      this.selectedBackend.set(['fastapi']);
      this.selectedFrontend.set([]);
      this.selectedDatabases.set(['qdrant', 'redis']);
      this.selectedTesting.set(['pytest']);
      this.selectedSecurity.set(['owasp', 'api-keys']);
      this.selectedMcp.set(['db-mcp', 'browser-mcp']);
    } else if (presetId === 'rust-microservice') {
      this.architecturePattern.set('event-driven');
      this.selectedLanguages.set(['rust']);
      this.selectedBackend.set(['axum']);
      this.selectedFrontend.set([]);
      this.selectedDatabases.set(['postgres', 'redis']);
      this.selectedTesting.set(['cargo-test']);
      this.selectedProtocols.set(['grpc', 'rest']);
    } else if (presetId === 'web-ssr') {
      this.architecturePattern.set('modular');
      this.selectedLanguages.set(['typescript']);
      this.selectedBackend.set(['nestjs']);
      this.selectedFrontend.set(['nextjs']);
      this.selectedDatabases.set(['supabase', 'postgres']);
      this.selectedTesting.set(['vitest']);
    }
  }

  toggleChip(list: WritableSignal<string[]>, id: string) {
    const current = list();
    if (current.includes(id)) {
      list.set(current.filter((item: string) => item !== id));
    } else {
      list.set([...current, id]);
    }
  }

  isSelected(list: WritableSignal<string[]>, id: string): boolean {
    return list().includes(id);
  }

  generate() {
    if (!this.title().trim()) {
      alert(this.t('projNameLabel'));
      return;
    }

    this.isLoading.set(true);
    const payload = {
      title: this.title(),
      description: this.description(),
      agent_type: this.agentType(),
      deployment_mode: this.deploymentMode(),
      architecture_pattern: this.architecturePattern(),
      language_output: this.languageOutput(),
      security_standards: this.selectedSecurity(),
      api_protocols: this.selectedProtocols(),
      mcp_integrations: this.selectedMcp(),
      git_ci_cd: this.gitCiCd(),
      preset_template: this.presetTemplate(),
      languages: this.selectedLanguages(),
      backend_frameworks: this.selectedBackend(),
      frontend_frameworks: this.selectedFrontend(),
      databases: this.selectedDatabases(),
      testing_frameworks: this.selectedTesting(),
      custom_rules: this.customRules(),
      enforce_tdd: this.enforceTdd(),
      enforce_spec_compliance_check: this.enforceSpecCompliance(),
      generate_unit_tests: this.generateUnitTests(),
      generate_integration_tests: this.generateIntegrationTests(),
      generate_functional_tests: this.generateFunctionalTests()
    };

    this.specService.createSpec(payload).subscribe({
      next: (spec) => {
        this.currentSpec.set(spec);
        this.isLoading.set(false);
        this.loadHistory();
      },
      error: (err) => {
        console.error('Błąd generowania specyfikacji:', err);
        this.isLoading.set(false);
        alert('Error / Błąd');
      }
    });
  }

  selectSpec(spec: SpecResponse) {
    this.currentSpec.set(spec);
  }

  deleteSpec(id: string, event: Event) {
    event.stopPropagation();
    if (confirm(this.t('deleteBtn') + '?')) {
      this.specService.deleteSpec(id).subscribe({
        next: () => {
          if (this.currentSpec()?.id === id) {
            this.currentSpec.set(null);
          }
          this.loadHistory();
        }
      });
    }
  }

  get activeContent(): string {
    const spec = this.currentSpec();
    if (!spec) return '';
    if (this.activeTab() === 'agents') return spec.agents_md || '';
    if (this.activeTab() === 'spec') return spec.spec_md || '';
    return spec.tasks_md || '';
  }

  copyContent() {
    const text = this.activeContent;
    if (text) {
      navigator.clipboard.writeText(text).then(() => {
        this.copyNotification.set(this.t('copySuccess'));
        setTimeout(() => this.copyNotification.set(null), 2500);
      });
    }
  }

  downloadZip() {
    const spec = this.currentSpec();
    if (spec) {
      window.open(this.specService.getExportZipUrl(spec.id), '_blank');
    }
  }

  get aiInterviewPrompt(): string {
    const lang = this.uiLanguage();
    const docLang = this.languageOutput().toUpperCase();
    const title = this.title();
    const desc = this.description();
    const techs = `${this.selectedLanguages().join(', ')} / ${this.selectedBackend().join(', ')} / ${this.selectedFrontend().join(', ')}`;

    if (lang === 'pl') {
      return `Napisz specyfikację techniczną dla mojego projektu "${title}".\nOpis biznesowy: "${desc}".\nWybrane technologie: ${techs}.\nPrzeprowadź ze mną krótki wywiad (zadaj mi 3 pytania doprecyzowujące), a następnie wygeneruj pliki SPEC.md, AGENTS.md oraz TASKS.md w języku ${docLang} w metodyce TDD.`;
    } else if (lang === 'de') {
      return `Schreiben Sie eine technische Spezifikation für mein Projekt "${title}".\nGeschäftsbeschreibung: "${desc}".\nTech-Stack: ${techs}.\nFühren Sie ein kurzes Interview mit mir (stellen Sie mir 3 klärende Fragen) und generieren Sie dann SPEC.md-, AGENTS.md- und TASKS.md-Dateien in der Sprache ${docLang} unter Verwendung der TDD-Methodik.`;
    } else if (lang === 'fr') {
      return `Rédigez une spécification technique pour mon projet "${title}".\nDescription métier : "${desc}".\nStack technique : ${techs}.\nMenez une courte interview avec moi (posez-moi 3 questions de clarification), puis générez les fichiers SPEC.md, AGENTS.md et TASKS.md en langue ${docLang} en suivant la méthodologie TDD.`;
    } else if (lang === 'es') {
      return `Escribe una especificación técnica para mi proyecto "${title}".\nDescripción del negocio: "${desc}".\nStack técnico: ${techs}.\nRealiza una breve entrevista conmigo (hazme 3 preguntas aclaratorias) y luego genera los archivos SPEC.md, AGENTS.md y TASKS.md en idioma ${docLang} siguiendo la metodología TDD.`;
    } else if (lang === 'ru') {
      return `Напишите техническую спецификацию для моего проекта "${title}".\nБизнес-описание: "${desc}".\nСтек технологий: ${techs}.\nПроведите со мной короткое интервью (задайте мне 3 уточняющих вопроса), а затем сгенерируйте файлы SPEC.md, AGENTS.md и TASKS.md на языке ${docLang} по методологии TDD.`;
    } else {
      return `Write a technical specification for my project "${title}".\nBusiness description: "${desc}".\nTech stack: ${techs}.\nConduct a short interview with me (ask me 3 clarifying questions), then generate SPEC.md, AGENTS.md, and TASKS.md files in ${docLang} language following TDD methodology.`;
    }
  }
}
