---
---
title: Anr
description: "Capture events when the event loop is blocked and the application is no longer responding."
---

**Deprecated**: This integration is deprecated. Please use the [`eventLoopBlockIntegration`](./event-loop-block) instead for better performance and more comprehensive monitoring.

This integration only works in the Node.js runtime.

_Import name: `Sentry.anrIntegration`_

The `anrIntegration` captures Application Not Responding (ANR)/Event Loop Stall errors and reports them as Sentry events. For more details, see the documentation on [Event Loop Block Detection](../../event-loop-block).

```JavaScript
Sentry.init({
  integrations: [Sentry.anrIntegration({ captureStackTrace: true })],
});
```
