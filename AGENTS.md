# Instrukcje dla Agenta AI (AGENTS.md) - AgentSpec Studio

## 1. Technologia i Architektura Projektu
- **Backend**: Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic v2, PostgreSQL 16.
- **Frontend**: Angular 19+ (Standalone Components, Signals, Zoneless Change Detection).
- **Infrastruktura**: Docker Compose (`postgres` port 5436:5432, `backend` 8000, `frontend` 4200).

## 2. Sprawdzona i Działająca Konfiguracja Angular 19 (VERY IMPORTANT)

### A. Konfiguracja Aplikacji (`frontend/src/app/app.config.ts`)
```typescript
import { ApplicationConfig, provideZonelessChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZonelessChangeDetection(), // ZAWSZE używaj Zoneless dla wersji 18/19 bez zależności zone.js w Dockerze
    provideRouter(routes),
    provideHttpClient()
  ]
};
```

### B. Obraz Docker (`frontend/Dockerfile`)
```dockerfile
FROM node:24-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build -- --configuration production

FROM nginx:alpine
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### C. Zasady Szablonów HTML w Angular 19
1. Stosuj wbudowane bloki kontroli przepływu `@if` oraz `@for`.
2. **NIGDY nie umieszczaj bloków `@if` / `@for` bezpośrednio wewnątrz znacznika `<select>`**. Stosuj `@for` bezpośrednio na elemencie `<option>` (np. `@for (opt of options; track opt.id) { <option [value]="opt.id">{{ opt.name }}</option> }`).

## 3. Komendy Testowania i Weryfikacji
- **Testy Backendu**: `PYTHONPATH=backend ./backend/venv/bin/pytest backend/tests`
- **Build Frontendu**: `npx ng build --configuration production` w `frontend/`
- **Docker Compose**: `docker-compose up -d --build` (PostgreSQL na porcie `5436`, Frontend `4200`, Backend `8000`).
