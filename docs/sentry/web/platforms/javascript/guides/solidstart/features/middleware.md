---
---
title: Solid Middleware
description: "Learn about Sentry's middleware for better instrumentation."
---

The Sentry middleware enhances the data collected by Sentry on the server side by enabling distributed tracing between the client and server.

Add the Sentry middleware to your `middleware.ts` file. If you don't have a `middleware.ts` file yet, create one:

```typescript {filename:middleware.ts}
export default createMiddleware({
  onBeforeResponse: [
    sentryBeforeResponseMiddleware(),
    // Add your other middleware handlers after `sentryBeforeResponseMiddleware`
  ],
});
```

And specify `middleware.ts` in `app.config.ts`:

```typescript {filename:app.config.ts}
export default defineConfig({
  // ...
  middleware: './src/middleware.ts',
});
```
