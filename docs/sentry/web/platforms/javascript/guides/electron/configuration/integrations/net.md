---
---
title: ElectronNet
description: "Captures breadcrumbs and tracing spans for Electrons `net` module. (default)"
---

This integration captures breadcrumbs and tracing spans for Electron's `net` module. Breadcrumbs and tracing spans are enabled by default, while `sentry-trace` headers are added to requests for all origins.

The integration can be configured with the following options:

```typescript
interface NetOptions {
  /**
   * Whether breadcrumbs should be captured for net requests
   *
   * Defaults to: true
   */
  breadcrumbs: boolean;
  /**
   * Whether to capture transaction spans for net requests
   *
   * Defaults to: true
   */
  tracing: boolean | (method: string, url: string) => boolean;
}
```

Here's a code example of how to disable breadcrumb capture and add `sentry-trace` headers to only capture spans for `POST` requests:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.electronNetIntegration({
      breadcrumbs: false,
      tracing: (method) => method == "POST",
    }),
  ],
});
```
