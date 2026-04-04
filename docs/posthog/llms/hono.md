# Source: https://posthog.com/docs/error-tracking/installation/hono.md

# Source: https://posthog.com/docs/libraries/hono.md

# Hono - Docs

PostHog makes it easy to get data about usage of your [Hono](https://hono.dev/) app. Integrating PostHog into your app enables analytics, custom events capture, feature flags, and more.

This guide walks you through integrating PostHog with your Hono app running on the [Node.js](https://hono.dev/docs/getting-started/nodejs) runtime, but has also been tested with Cloudflare Workers, Vercel, and Bun. You can hook into the same middleware and `onError` for other runtimes to capture events.

## Prerequisites

To follow this guide along, you need:

1.  A PostHog instance (either [Cloud](https://app.posthog.com/signup) or [self-hosted](/docs/self-host.md))
2.  A Hono application. We suggest trying first with a fresh [Hono Node.js starter template](https://hono.dev/docs/getting-started/nodejs#_1-setup).

## Installation

Start by installing the `posthog-node` package using your package manager.

Terminal

PostHog AI

```bash
npm install --save posthog-node
```

Then, create a [middleware](https://hono.dev/docs/guides/middleware) to capture events for your routes. Remember to **export** your [project token](https://us.posthog.com/settings/project#variables) as an environment variable.

index.ts

PostHog AI

```javascript
import { env } from 'hono/adapter'
import { createMiddleware } from 'hono/factory'
import { PostHog } from 'posthog-node'
const posthog = new PostHog(process.env.POSTHOG_PUBLIC_KEY, { host: 'https://us.i.posthog.com' })
const posthogServerMiddleware = createMiddleware(async (c, next) => {
  posthog.capture({
      distinctId: 'distinct_id_of_user', // Their user id or email
      event: 'user_did_something',
  })
  await next()
  await posthog.flush()
})
```

**Shutdown**

Make sure to always call `posthog.shutdown()` after capturing events from the server-side. PostHog queues events into larger batches. This call forces all batched events to be flushed immediately.

Next, apply this middleware to your app. This middleware will be called on every request handled by Hono, denoted by the wildcard `*`.

index.ts

PostHog AI

```typescript
// use the middleware on all (*) routes.
app.use('*', posthogServerMiddleware)
```

In your routes, you can pass information to be captured by your middleware using [context `set()` and `get()` pair](https://hono.dev/docs/api/context#set-get)

**Cloudflare Pages**

Cloudflare Pages uses its own middleware system that is different from Hono's middleware. Follow the [Hono documentation on Cloudflare Pages](https://hono.dev/docs/getting-started/cloudflare-pages#cloudflare-pages-middleware) to handle middleware.

## Error tracking

Hono uses [`app.onError`](https://hono.dev/docs/api/exception#handling-httpexception) for root-level error handling. You can take advantage of this for [Error tracking](/docs/error-tracking.md).

index.ts

PostHog AI

```typescript
import { PostHog } from 'posthog-node'
const posthog = new PostHog(process.env.POSTHOG_PUBLIC_KEY, { host: 'https://us.i.posthog.com' })
app.onError(async (err, c) => {
  posthog.captureException(err, 'user_distinct_id_with_err_rethrow', {
    path: c.req.path,
    method: c.req.method,
    url: c.req.url,
    headers: c.req.header(),
    // ... other properties
  })
  await posthog.flush()
  // other error handling logic
  return c.text('Internal Server Error', 500)
})
```

## Next steps

To read more about how to integrate specific PostHog features into Hono, have a look at our [Node SDK docs](/docs/libraries/node.md) for concepts such as:

-   [Capturing custom events, setting properties, and more.](/docs/libraries/node.md#capturing-events)
-   [Setting up feature flags including variants and payloads.](/docs/libraries/node.md#feature-flags)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better