# Sprawdzona Konfiguracja Angular 19 dla Agentów AI

## 1. Wymagania Środowiskowe
- **Node.js**: `v24.x` (Obraz Docker: `node:24-alpine`)
- **Angular CLI**: `22.x` / `19.x`
- **Serwowanie produkcyjne**: `nginx:alpine` (`/usr/share/nginx/html`)

## 2. Kluczowe Ustawienia Kodu

### 2.1 `app.config.ts` (Bezpośrednia zmiana stanu bez Zone.js)
```typescript
import { ApplicationConfig, provideZonelessChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZonelessChangeDetection(),
    provideRouter(routes),
    provideHttpClient()
  ]
};
```

### 2.2 Rejestracja Błędów w `main.ts`
```typescript
import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => {
    console.error('ANGULAR BOOTSTRAP ERROR:', err);
    document.body.innerHTML = `
      <div style="padding: 2rem; color: #f87171; background: #0f172a; font-family: sans-serif;">
        <h2>Wystąpił błąd uruchamiania aplikacji Angular</h2>
        <pre style="background: #1e293b; padding: 1rem; border-radius: 8px; overflow-x: auto; color: #f1f5f9;">${err?.stack || err}</pre>
      </div>
    `;
  });
```

### 2.3 Reguły Konstrukcji Szablonów HTML
- **Pętla po opcjach w `<select>`**:
```html
<select class="form-control" [ngModel]="agentType()" (ngModelChange)="agentType.set($event)">
  @for (agent of (options()?.agents || []); track agent.id) {
    <option [value]="agent.id">{{ agent.name }}</option>
  }
</select>
```
- **Zasada**: Nie wstawiać sztucznych węzłów blokowych (`@if`, `<div>`) bezpośrednio wewnątrz elementu `<select>`, aby nie powodować błędów parsowania DOM w przeglądarkach.
