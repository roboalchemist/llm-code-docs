---
---
title: Console
description: "Capture console logs as breadcrumbs. (default)"
---

_Import name: `Sentry.consoleIntegration`_

This integration is enabled by default. If you'd like to modify your default integrations, read [this](./../#modifying-default-integrations).

The `consoleIntegration` generates breadcrumbs for console logs.

```JavaScript
Sentry.init({
  integrations: [Sentry.consoleIntegration()],
});
```
