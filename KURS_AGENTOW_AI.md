# Kompleksowy Kurs Pracy z Agentami AI (`agy`, `Claude Code`, `Codex`)
## Tworzenie AGENTS.md, Specyfikacji Technicznych oraz Metodyka AI-Driven TDD

Witaj w pełnym praktycznym przewodniku po pracy z **autonomicznymi agentami kodującymi** (zwanymi *Autonomous Coding Agents*), takimi jak **Google Antigravity (`agy`)**, **Anthropic `Claude Code`**, **OpenAI `Codex`** czy **Cursor**.

W przeciwieństwie do tradycyjnych asystentów AI (zwykłe układy chatu lub prostego autouzupełniania kodu), autonomiczny agent potrafi samoczynnie:
- Odczytywać i przeszukiwać strukturę całego repozytorium.
- Tworzyć, edytować i usuwać pliki w systemie operającym.
- Uruchamiać komendy w terminalu (lintery, kompilatory, suity testowe).
- Reagować na błędy wykonania i logi (Self-Correction / Feedback Loop).

Ta instrukcja nauczy Cię, jak opanować **trzy filary przewagi w pracy z agentami AI**:
1. **Konfigurację kontekstu i reguł w plikach `AGENTS.md` / `CLAUDE.md` / `.gemini/rules`.**
2. **Specyfikowanie wymagań metodą SDD (Specification-Driven Development).**
3. **Pętlę TDD sterowaną przez AI (AI-Driven Test-Driven Development).**

---

## SPIS TREŚCI
1. [Moduł 1: Ekosystem i Zasada Działania Agentów AI](#moduł-1-ekosystem-i-zasada-działania-agentów-ai)
2. [Moduł 2: Tworzenie i Struktura `AGENTS.md` / `CLAUDE.md`](#moduł-2-tworzenie-i-struktura-agentsmd--claudemd)
3. [Moduł 3: Specyfikacje Sterowane AI (Spec-Driven Development)](#moduł-3-specyfikacje-sterowane-ai-spec-driven-development)
4. [Moduł 4: Podejście AI-TDD (Test-Driven Development ze Wspomaganiem AI)](#moduł-4-podejście-ai-tdd-test-driven-development-ze-wspomaganiem-ai)
5. [Moduł 5: Warsztat Krok po Kroku – Przykładowy Workflow w Projekcie](#moduł-5-warsztat-krok-po-kroku--przykładowy-workflow-w-projekcie)
6. [Moduł 6: Dobra Praktyka i Najczęstsze Błędy (DOD & Troubleshooting)](#moduł-6-dobra-praktyka-i-najczęstsze-błędy-dod--troubleshooting)

---

## Moduł 1: Ekosystem i Zasada Działania Agentów AI

### 1.1 Jak działa agent terminalowy / IDE?
Zamiast jednorazowego pytania i odpowiedzi, agent działa w **pętli REPL (Read-Eval-Print Loop)**:
1. **Prompt / Wskazówka**: Użytkownik przekazuje cel (np. *"Zaimplementuj autoryzację JWT z testami"*).
2. **Planowanie**: Agent analizuje cel i pliki projektu.
3. **Wykonanie narzędzia (Tool Call)**: Agent wywołuje `view_file`, `grep_search`, `write_to_file` lub `run_command` (np. `npm test`).
4. **Odpowiedź środowiska**: Agent dostaje wynik narzędzia (np. błąd kompilacji TypeScript lub nieprzechodzący test).
5. **Korekta (Self-Correction)**: Agent analizuje ślad błędu (stack trace) i poprawia kod.
6. **Zakończenie**: Agent komunikuje wykonanie zadania po potwierdzeniu sukcesu w testach.

### 1.2 Porównanie narzędzi: `agy`, `Claude Code`, `Codex`
| Cecha | Google Antigravity (`agy`) | Anthropic Claude Code | OpenAI Codex / CLI / Cursor |
| :--- | :--- | :--- | :--- |
| **Plik Konfiguracji** | `AGENTS.md` / `.gemini/rules` / `SKILL.md` | `CLAUDE.md` | `AGENTS.md` / `.cursorrules` |
| **Wielowątkowość** | Tak (Subagenty, zadania w tle) | Głównie jedno-wątkowa pętla CLI | Głównie pętla konwersacyjna |
| **Pętla zwrotna (Tools)** | Komendy, Pliki, Przeglądarka, Artefakty | Zintegrowany Bash, Pliki | Zintegrowany Terminal / Editor |
| **Skupienie** | Pełne środowisko AI-First z architekturą zadań | Szybka praca w konsoli terminala | Asystowanie w edytorze / CLI |

---

## Moduł 2: Tworzenie i Struktura `AGENTS.md` / `CLAUDE.md`

Agent AI bez pliku instrukcji projektu jest jak programista pierwszego dnia w pracy: nie zna konwencji, nazw zmiennych ani tego, jak uruchomić testy.

Plik **`AGENTS.md`** (lub `CLAUDE.md` dla Claude Code) to plik tekstowy umieszczony w głównym katalogu projektu (`/AGENTS.md`), który jest **automatycznie wczytywany przy każdym uruchomieniu agenta**.

### 2.1 Struktura Idealnego Pliku `AGENTS.md`

Dobry plik `AGENTS.md` powinien zawierać 5 kluczowych sekcji:
1. **Tech Stack & Architecture**: Użyty język, frameworki, struktura katalogów.
2. **Commands (Kluczowe komendy)**: Jak budować, uruchamiać i testować projekt (dopisane wprost command lines).
3. **Coding Standards & Patterns**: Zasady nazewnictwa, zarządzanie błędami, typowanie.
4. **AI Workflow & Rules**: Zasady postępowania agenta (np. "Używaj TDD", "Nie modyfikuj istniejących testów", "Zawsze sprawdzaj linter").
5. **Definition of Done (DoD)**: Kiedy agent może uznać zadanie za skończone.

### 2.2 Przykład Pliku `AGENTS.md`

```markdown
# Instrukcje dla Agenta AI (AGENTS.md / CLAUDE.md)

## 1. Technologia i Architektura
- **Język**: TypeScript 5.x (Strict mode: true)
- **Runtime**: Node.js v20+ / Bun
- **Framework**: Express.js
- **Testy**: Vitest + Supertest
- **Struktura**:
  - `src/controllers/` - logika HTTP
  - `src/services/` - logika biznesowa
  - `src/models/` - struktury danych i schematy Zod
  - `tests/` - testy jednostkowe i integracyjne

## 2. Kluczowe Komendy
- **Uruchomienie testów**: `npm run test`
- **Testy w trybie watch**: `npm run test:watch`
- **Sprawdzenie typów i linting**: `npm run check` (wykonuje `tsc --noEmit && eslint`)
- **Budowanie**: `npm run build`

## 3. Metodyka i Wymagania Pracy z Kodem
- **Zasada AI-TDD**: ZAWSZE pisz lub edytuj testy NAJPIERW (Red), upewnij się, że nie przechodzą, a dopiero potem pisz kod źródłowy (Green).
- **Zero Halucynacji**: Zanim użyjesz nieznanej funkcji lub ścieżki, zobacz plik przy użyciu narzędzi czytania.
- **Bezpieczeństwo**: Nie zapisuj haseł ani kluczy w kodzie. Używaj `.env`.
- **Obsługa Błędów**: Wszystkie błędy domenowe wyliczaj w `src/errors/AppError.ts`. Nie używaj powszechnych `catch (e) {}` bez logowania.

## 4. Kryteria Zakończenia Zadania (Definition of Done)
1. Kod kompiluje się bez błędów TypeScript (`npm run check`).
2. Wszystkie testy jednostkowe i integracyjne przechodzą na zielono (`npm run test`).
3. Brak niepotrzebnych logów `console.log` w kodzie produkcyjnym.
```

---

## Moduł 3: Specyfikacje Sterowane AI (Spec-Driven Development)

Promptowanie w stylu: *"Stwórz mi sklep internetowy"* prowadzi do chaosu i porażki.
Przy złożonych funkcjonalnościach stosujemy **Specification-Driven Development (SDD)**.

### 3.1 Dwu-etapowy proces SDD z Agentem

#### Etap 1: Wywiad i Generowanie Specyfikacji (`docs/SPEC.md`)
Dajesz agentowi zarys i każesz mu napisać szczegółową specyfikację technologiczną.
Możesz poprosić agenta:
> *"Zadawaj mi pytania o szczegóły, aż uzyskasz pełen obraz, a następnie wygeneruj plik `docs/SPEC-auth.md` według naszego szablonu specyfikacji."*

#### Etap 2: Rozbicie na Atomowe Zadania (`docs/TASKS.md`)
Agent przekształca specyfikację w checklistę zadań (Task List), gdzie każde zadanie jest na tyle małe, że mieści się w jednym cyklu TDD.

### 3.2 Struktura pliku `SPEC.md`
- **Cel i Zakres (Scope)**: Co robimy, a czego NIE robimy.
- **Model Danych / API**: Kontrakty JSON, schematy bazy, typy.
- **Obsługa Przypadków Brzegowych (Edge Cases)**: Brak sieci, błędy walidacji, nieprawidłowy token.
- **Scenariusze Testowe**: Przykłady Given-When-Then.

---

## Moduł 4: Podejście AI-TDD (Test-Driven Development ze Wspomaganiem AI)

DLACZEGO TDD JEST KLUCZOWE DLA AGENTÓW AI?
Gdy każesz agentowi napisać sam kod, agent nie ma jak obiektywnie sprawdzić, czy kod działa prawidłowo.
Gdy każesz agentowi pracować w pętli **TDD (Red -> Green -> Refactor)**:
- Test staje się **obiektywną specyfikacją wykonawczą**.
- Agent sam uruchamia test w terminalu, widzi błąd i wie dokładnie, co poprawić!

```
┌─────────────────────────────────────────────────────────┐
│              CYKL AI-DRIVEN TDD                         │
│                                                         │
│   1. SPEC & TEST (RED)                                  │
│      Agent pisze test na podstawie SPEC.md              │
│      ├──> Exec: `npm test` -> FAILS (Red) ❌            │
│                                                         │
│   2. MINIMAL CODE (GREEN)                               │
│      Agent pisze minimalny kod źródłowy                │
│      ├──> Exec: `npm test` -> PASSES (Green) ✅        │
│                                                         │
│   3. REFACTOR & CHECK                                   │
│      Agent poprawia jakość kodu                         │
│      ├──> Exec: `npm run check` -> Success 🎉          │
└─────────────────────────────────────────────────────────┘
```

### Cykl AI-TDD krok po kroku:
1. **Faza RED (Test Najpierw)**:
   - Prompt dla agenta: *"Na podstawie `docs/SPEC-auth.md` zaimplementuj wyłącznie suite testowy w `tests/auth.test.ts`. Nie pisz jeszcze kodu usługi. Uruchom test i upewnij się, że nie przechodzi z powodu braku funkcji."*
2. **Faza GREEN (Minimalny Kod)**:
   - Prompt dla agenta: *"Teraz napisz minimalny kod w `src/services/auth.ts`, aby test `tests/auth.test.ts` przeszedł na zielono. Uruchom testy i pokaż wynik."*
3. **Faza REFACTOR (Czyszczenie)**:
   - Prompt dla agenta: *"Zrefaktoryzuj kod pod kątem czytelności i obsłuż wyjątki, dbając by testy cały czas przechodziły."*

---

## Moduł 5: Warsztat Krok po Kroku – Przykładowy Workflow w Projekcie

Przećwiczmy pełen proces od zera.

### Krok 1: Inicjalizacja Repozytorium i `AGENTS.md`
Stwórz plik `AGENTS.md` w korzeniu projektu z definicją komend i standardów (patrz Moduł 2).

### Krok 2: Generowanie Specyfikacji z Agentem
Wywołaj agenta (`agy`, `claude` lub `codex`):

```bash
# W konsoli / CLI agenta:
Napisz specyfikację techniczną dla modułu kalkulatora zniżek w e-commerce.
Zapisz wynik w pliku `docs/SPEC-discounts.md`. 
Uwzględnij:
- Zniżkę kwotową i procentową
- Zniżki nie łączą się ze sobą
- Przypadki brzegowe: wartość koszyka < 0, zniżka > 100%
```

### Krok 3: Wygenerowanie Listy Zadania `TASKS.md`
```bash
Na podstawie `docs/SPEC-discounts.md` stwórz listę atomowych zadań w `docs/TASKS.md` w formie checklisty Markdown `- [ ]`.
```

### Krok 4: Wykonanie Zadania w Pętli AI-TDD
```bash
Pobierz pierwsze zadanie z `docs/TASKS.md`.
1. Napisz testy w `tests/discounts.test.ts` pokrywające scenariusz z zadania 1.
2. Uruchom `npm test`, potwierdź błąd testu.
3. Zaimplementuj kod w `src/discounts.ts`.
4. Uruchom `npm test`, aż osiągniesz wynik pozytywny.
5. Zaznacz zadanie jako [x] w `docs/TASKS.md`.
```

---

## Moduł 6: Dobra Praktyka i Najczęstsze Błędy (DOD & Troubleshooting)

### Golden Rules (Złote Zasady Pracy z Agentami):
1. **Nigdy nie pozwalaj agentowi modyfikować testów po to, by "naprawić" błąd!**
   - Jeśli test nie przechodzi, problemem niemal zawsze jest kod źródłowy. Wyjątkiem jest zmiana specyfikacji.
2. **Krótkie i precyzyjne kroki (Context Management)**:
   - Nie dawaj agentowi 20 zadań naraz. Wykonuj 1-2 zadania z checklisty `TASKS.md` w jednej iteracji.
3. **Zawsze weryfikuj uruchomienie komend (Empirical Runtime Verification)**:
   - Nie wierz agentowi na słowo, że "kod działa". Agent MUSI uruchomić testy w terminalu i przeanalizować ich output.
4. **Używaj gałęzi Git (Git Feature Branches)**:
   - Przed zleceniem agentowi większego zadania zrób `git checkout -b feature/nowa-funkcja`. W razie niepowodzenia łatwo cofnie się zmiany.

---
*Plik wygenerowany w ramach kursu obsługi agentów AI (`agy`, `Claude Code`, `Codex`).*
