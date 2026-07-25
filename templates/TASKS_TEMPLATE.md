# Lista Zadań Wykonawczych (TASKS) - [Nazwa Funkcjonalności]

Specyfikacja źródłowa: [SPEC-001](SPEC_TEMPLATE.md)

## Instrukcja dla Agenta AI:
1. Przetwarzaj zadania sekwencyjnie po JEDNYM punkcie.
2. Dla każdego zadania zastosuj pętlę TDD: 
   a. Napisz/Zaktualizuj test (Red)
   b. Zaimplementuj kod (Green)
   c. Zweryfikuj zestaw testów
3. Po zrealizowaniu zadania zmień status z `[ ]` na `[x]`.

---

## Lista Zadań:

- [ ] **Zadanie 1: Przygotowanie struktur i typów danych**
  - [ ] Utworzenie interfejsów TypeScript w `src/types/auth.ts`
  - [ ] Wygenerowanie testu sprawdzającego walidację typu schema Zod

- [ ] **Zadanie 2: Implementacja walidacji danych wejściowych**
  - [ ] Napisanie testu w `tests/validation.test.ts` dla niepoprawnego adresu email (Red)
  - [ ] Implementacja funkcji walidującej w `src/utils/validation.ts` (Green)

- [ ] **Zadanie 3: Implementacja logiki biznesowej / serwisu**
  - [ ] Napisanie testów jednostkowych w `tests/authService.test.ts` (Red)
  - [ ] Implementacja metody `login()` w `src/services/authService.ts` (Green)
  - [ ] Weryfikacja przechodzenia wszystkich testów

- [ ] **Zadanie 4: Integracja HTTP / Controller**
  - [ ] Napisanie testów integracyjnych w `tests/authController.test.ts` z użyciem Supertest (Red)
  - [ ] Utworzenie endpointu w `src/controllers/authController.ts` (Green)
