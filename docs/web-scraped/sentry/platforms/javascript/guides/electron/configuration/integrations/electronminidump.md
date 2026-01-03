---
---
title: ElectronMinidump
description: "Captures and sends minidumps via Electrons built in `crashReporter` uploader."
---

Captures and sends minidumps via Electrons built in `crashReporter` uploader. Renderer and GPU crashes will only include minimal context because of limitations of the `crashReporter` uploader . For full context, you should prefer the default `SentryMinidump` integration .

If you add the `ElectronMinidump` integration, the `SentryMinidump` integration will be automatically removed to avoid duplicate crashes being reported.

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [Sentry.electronMinidumpIntegration()],
});
```
