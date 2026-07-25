# AGENTS.md / CLAUDE.md - Uniwersalne Instrukcje dla Agenta AI

## 1. Kontekst Projektu i Stos Techniczny
- **Projekt**: [Wpisz nazwę projektu]
- **Język**: TypeScript / Python / Go [wybierz właściwy]
- **Framework**: Express / NestJS / FastAPI / React
- **Baza Danych**: PostgreSQL / MongoDB / SQLite
- **Test Runner**: Vitest / Jest / PyTest

## 2. Dostępne Komendy Środowiskowe
Zanim zgłosisz zakończenie zadania, MUSISZ zweryfikować kod za pomocą poniższych komend:
- **Testy**: `npm test` (lub `pytest`)
- **Lint / Typecheck**: `npm run check` (lub `mypy .`)
- **Budowanie**: `npm run build`

## 3. Zasady Inżynieryjne i Konwencje Kodu
- **Metodyka AI-TDD**:
  1. Wszystkie nowe funkcjonalności MUSZĄ być rozwijane w cyklu Red-Green-Refactor.
  2. Najpierw generujesz/edytujesz plik testowy (`.test.ts` / `test_*.py`).
  3. Uruchamiasz komendę testową i weryfikujesz, że test nie przechodzi (Red).
  4. Dopiero wtedy piszesz minimalną implementację w kodzie produkcyjnym (Green).
  5. Uruchamiasz testy ponownie aż do uzyskania statusu powodzenia.
- **Bezpieczeństwo Testów**: Niewolno edytować istniejących testów w celu "ukrycia" błędu w kodzie produkcyjnym.
- **Zasada Czystego Kodu**: Usuwaj nieużywane importy, unikaj wartości wpisanych na sztywno (magic numbers/strings).
- **Struktura Katalogów**:
  - `src/` - Kod źródłowy
  - `tests/` - Pliki testowe
  - `docs/` - Specyfikacje (`SPEC.md`) i zadania (`TASKS.md`)

## 4. Kryteria Zakończenia Zadania (Definition of Done)
1. Sprawdzenie typów kompilatora przebiega bez błędów.
2. Pełny zestaw testów wykonuje się z wynikiem pozytywnym.
3. Plik `docs/TASKS.md` zawiera zaktualizowany status wykonanych kroków.
