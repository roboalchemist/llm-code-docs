---
---
title: Postgres
description: "Adds instrumentation for Postgres. (default)"
---

This integration only works in the Node.js and Bun runtimes.

_Import name: `Sentry.postgresIntegration`_

This integration is enabled by default when performance monitoring is enabled. If you'd like to modify your default integrations, read [this](./../#modifying-default-integrations).

The `postgresIntegration` adds instrumentation for the `pg` library to capture spans using [`@opentelemetry/instrumentation-pg`](https://www.npmjs.com/package/@opentelemetry/instrumentation-pg).

```JavaScript
Sentry.init({
  integrations: [Sentry.postgresIntegration()],
});
```

## Supported Versions

- `pg`: `>=8 <9`
