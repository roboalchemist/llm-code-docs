---
---
title: AdditionalContext
description: "Adds additional device context to events. (default)"
---

Adds additional device context to events.

```typescript
interface AdditionalContextOptions {
  /**
   * Capture dimensions and resolution of the primary display
   * @default true
   */
  screen: boolean;
  /**
   * Capture device model and manufacturer.
   * No supported on Linux.
   * @default false
   */
  deviceModelManufacturer: boolean;
}
```

To disable specific context items, set them as `false`:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.additionalContextIntegration({
      screen: false,
    }),
  ],
});
```
