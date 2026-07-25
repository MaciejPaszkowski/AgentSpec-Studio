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
