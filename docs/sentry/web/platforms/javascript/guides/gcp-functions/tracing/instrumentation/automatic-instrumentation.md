---
---
title: Automatic Instrumentation
description: "Learn what transactions are captured after tracing is enabled."
---

When performance is enabled through `tracesSampleRate` or a `tracesSampler` function, the Sentry SDK will automatically capture spans for incoming, and outgoing HTTP requests.

Database instrumentation can be manually enabled by adding the corresponding integration to the `integrations` array in the `init` method. The following packages are supported:

- `mysql`
- `mysql2`
- `pg`
- `graphql` (including Apollo Server)
- `mongo`
- `mongoose`
- `ioredis`
- `prisma` (requires additional configuration - see Prisma Integration)

You can add the integrations as follows:

```javascript
const Sentry = require("@sentry/google-cloud-serverless");

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 1.0,
  integrations: [
    Sentry.mysqlIntegration(),
    Sentry.mysql2Integration(),
    Sentry.pgIntegration(),
    Sentry.graphqlIntegration(),
    Sentry.mongoIntegration(),
    Sentry.mongooseIntegration(),
    Sentry.ioredisIntegration(),
  ],
});
```
