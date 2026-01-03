---
---
title: trpcMiddleware
description: "Capture spans & errors for tRPC handlers."
---

This integration only works inside server environments (Node.js, Bun, Deno).

_Import name: `Sentry.trpcMiddleware`_

The Sentry tRPC middleware creates spans for you and improves error capturing for tRPC handlers.

The `trpcMiddleware` is not a traditional SDK integration in the sense that your are **not** supposed to add it to the `integrations` option.
Instead, add it as a middleware to your tRPC router.

```javascript
const t = initTRPC.context().create();

const sentryMiddleware = t.middleware(
  Sentry.trpcMiddleware({
    attachRpcInput: true,
  })
);

const sentrifiedProcedure = t.procedure.use(sentryMiddleware);
```

## Options

### `attachRpcInput`

_Type: `boolean`_

Defaults to `false`. If enabled, the RPC input will be captured in error events as `trpc` context.

If you observe nested objects in the `trpc` context being truncated with "`[Object]`", you can define a `normalizeDepth` value to allow for more deeply nested objects in context.
Note that the default depth for `trpc` context is 5.

