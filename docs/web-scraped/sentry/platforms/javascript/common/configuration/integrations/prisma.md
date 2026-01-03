---
---
title: Prisma
description: "Adds instrumentation for Prisma. (default)"
---

This integration only works in the Node.js and Bun runtimes.

_Import name: `Sentry.prismaIntegration`_

Sentry supports tracing [Prisma ORM](https://www.prisma.io/) queries with the Prisma integration.

The Prisma Integrations creates a spans for each query and reports to Sentry with relevant details inside the`description` if available.

This integration is enabled by default and supports Prisma versions 5 & 6. In Prisma v5, you need to follow the instructions below to enable tracing.

If you'd like to learn how to modify your default integrations, visit the docs on Modifying Default Integrations.

## Prisma Version >=6

To use the integration with Prisma version >=6, no configuration is required - tracing in Prisma v6 is enabled by default.

```javascript {3}
Sentry.init({
  tracesSampleRate: 1.0,
  integrations: [Sentry.prismaIntegration()],
});
```

## Prisma Version 5

To configure the integration for Prisma version 5, first add the `tracing` feature flag to the `generator` block of your Prisma schema:

```txt {tabTitle: Prisma Schema} {filename: schema.prisma} {3}
generator client {
  provider        = "prisma-client-js"
  previewFeatures = ["tracing"]
}
```

Then, the `prismaIntegration` will automatically capture spans for Prisma queries.

```javascript {3}
Sentry.init({
  tracesSampleRate: 1.0,
  integrations: [Sentry.prismaIntegration()],
});
```

## Supported Versions

- `prisma`: `>=5`
