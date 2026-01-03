---
---
title: BrowserWindowSession
description: "Captures sessions linked to the focus of Electron BrowserWindows."
---

Requires `@sentry/electron` version `4.11.0` or higher.

Captures sessions linked to the focus of Electron `BrowserWindow`s. Capturing
sessions makes it possible to show [release health](/product/releases/health/)
statistics in Sentry.

Adding this integration disables the MainProcessSession
session integration.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.browserWindowSessionIntegration()],
});
```

By default, sessions are ended when no window has had focus for 30
seconds. You can adjust this timeout via the `backgroundTimeoutSeconds` option:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.browserWindowSessionIntegration({
      backgroundTimeoutSeconds: 120,
    }),
  ],
});
```
