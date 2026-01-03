---
---
title: Hono
description: Learn how to manually set up Sentry in your Hono app and capture your first errors.
---

  This guide focuses on the **Node.js runtime** for Hono. For other runtimes, see the links below. 
  If you are using the `@sentry/cloudflare` middleware, see the [Hono on Cloudflare guide](/platforms/javascript/guides/cloudflare/frameworks/hono/).

## Runtime Support

Hono works across multiple JavaScript runtimes. Choose the appropriate Sentry SDK for your environment:

- **Node.js**: Use `@sentry/node` (this guide)
- **Cloudflare Workers**: Use `@sentry/cloudflare` - see our [Hono on Cloudflare guide](/platforms/javascript/guides/cloudflare/frameworks/hono/)
- **Deno**: Use `@sentry/deno` - see our [Deno guide](/platforms/javascript/guides/deno/) (Beta)
- **Bun**: Use `@sentry/bun` - see our [Bun guide](/platforms/javascript/guides/bun/)

  The community middleware `@hono/sentry` has been deprecated in favor of using Sentry's official 
  packages, which provide better performance and more features. If you're currently using `@hono/sentry` middleware, you'll need to migrate to `@sentry/cloudflare`. 

## Runtime-Specific Setup

### Node.js Runtime (This Guide)

This guide focuses on Node.js. The setup uses `@sentry/node` and follows standard Node.js patterns.

### Other Runtimes

For other runtimes, use the appropriate Sentry SDK:

```javascript
// For Deno, use @sentry/deno (currently in Beta)
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 1.0,
});

const app = new Hono();
// Your Hono app setup...
```

```javascript
// For Bun, use @sentry/bun
// Initialize Sentry before importing other modules
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  tracesSampleRate: 1.0,
});

const app = new Hono();
// Your Hono app setup...
```

```javascript
// For Cloudflare Workers, use @sentry/cloudflare
const app = new Hono();

export default Sentry.withSentry(
  (env: Env) => ({
    dsn: "___PUBLIC_DSN___",
    tracesSampleRate: 1.0,
  }),
  app
);
```

