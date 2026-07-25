# SPEC-001: [Nazwa Funkcjonalności]

## 1. Przegląd i Cel (Overview & Goals)
- **Problem**: [Opisz jaki problem rozwiązujemy]
- **Cel**: [Opisz oczekiwany rezultat biznesowy/techniczny]
- **Poza Zakresem (Out of Scope)**: [Czego NIE robimy w tej iteracji]

## 2. Architektura i Kontrakty Danych (Data Contracts & API)
### 2.1 Struktury Danych / Typy
```typescript
export interface UserPayload {
  id: string;
  email: string;
  role: 'admin' | 'user';
}
```

### 2.2 Punkty Endpoints / Metody
- **Metoda / Funkcja**: `POST /api/v1/auth/login`
- **Wejście (Request Body)**: `{ email: string, pass: string }`
- **Wyjście Ok (200 OK)**: `{ token: string, user: UserPayload }`
- **Błędy (400 / 401)**: `{ error: string, code: string }`

## 3. Scenariusze Testowe (Given-When-Then)
1. **Scenariusz Sukcesu**:
   - **Given**: Prawidłowy email i hasło zarejestrowanego użytkownika.
   - **When**: Wywołujemy funkcję logowania.
   - **Then**: Otrzymujemy poprawny JWT token oraz dane użytkownika.
2. **Scenariusz Błędu Walidacji**:
   - **Given**: Niepoprawny format adresu email.
   - **When**: Wywołujemy funkcję logowania.
   - **Then**: Otrzymujemy błąd HTTP 400 z kodem `INVALID_EMAIL`.

## 4. Przypadki Brzegowe (Edge Cases)
- Wygaśnięcie tokenu w trakcie zapytania.
- Próba logowania przy zablokowanym koncie.
- Atak typu Brute-Force (przekroczenie rate-limitera).
