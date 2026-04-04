---
---
title: BunServer
description: "Instruments Bun.serve to automatically create transactions and capture errors. (default)"
---

This integration only works in the Bun runtime.

_Import name: `Sentry.bunServerIntegration`_

This integration is enabled by default. If you'd like to modify your default integrations, read [this](./../#modifying-default-integrations).

The `bunServerIntegration` instruments [`Bun.serve` API](https://bun.sh/docs/api/http) to automatically create transactions and capture errors.

```JavaScript
Sentry.init({
  integrations: [Sentry.bunServerIntegration()],
});
```
