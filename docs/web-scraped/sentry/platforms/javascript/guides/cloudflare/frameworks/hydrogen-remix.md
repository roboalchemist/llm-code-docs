---
---
title: Hydrogen with Remix (Legacy)
description: Learn how to use the Sentry Remix SDK to instrument your Hydrogen app (versions before 2025.5.0).
---

This guide applies to Hydrogen versions **before 2025.5.0** that use Remix v2. For newer versions of Hydrogen (2025.5.0+) that use React Router 7, see the [React Router guide](/platforms/javascript/guides/cloudflare/frameworks/hydrogen-react-router/).

If you're using Shopify's Hydrogen framework with Remix v2, you can use the Sentry Remix SDK to add Sentry instrumentation to your app.

## Installing Sentry Remix and Cloudflare SDKs

First, install the Sentry Remix and Cloudflare SDKs with your package manager:

```bash {tabTitle:npm}
npm install @sentry/remix @sentry/cloudflare --save
```

```bash {tabTitle:yarn}
yarn add @sentry/remix @sentry/cloudflare
```

```bash {tabTitle:pnpm}
pnpm add @sentry/remix @sentry/cloudflare
```

## Instrumenting Your Server

Update your `server.ts` file to use the `wrapRequestHandler` method from `@sentry/cloudflare/request` and `instrumentBuild` from `@sentry/remix/cloudflare`:

```ts {filename:server.ts}
// Virtual entry point for the app
/**
 * Export a fetch handler in module format.
 */
export default {
  async fetch(
    request: Request,
    env: Env,
    executionContext: ExecutionContext
  ): Promise {
    return wrapRequestHandler(
      {
        options: {
          dsn: "YOUR_DSN_HERE",
          tracesSampleRate: 1.0,
        },
        // Need to cast to any because this is not on cloudflare
        request: request as any,
        context: executionContext,
      },
      async () => {
        // Instrument your server build with Sentry
        // and use the instrumented build inside the fetch handler
        const instrumentedBuild = instrumentBuild(remixBuild);

        const handleRequest = createRequestHandler({
          build: instrumentedBuild,
          mode: process.env.NODE_ENV,
          getLoadContext: (): AppLoadContext => ({
            // your load context
          }),
        });

        return handleRequest(request);
      }
    );
  },
};
```

## Instrumenting Your Client

Wrap your Remix root component using `withSentry`:

```tsx {filename:app/root.tsx}
function App() {
  return (
    // Your app content
  );
}

// Pass `useEffect`, `useLocation` and `useMatches` hooks to `withSentry`
export default Sentry.withSentry(App, useEffect, useLocation, useMatches);
```

Finally, update your `entry.client.tsx` file to initialize Sentry SDK on the client:

```tsx {filename:app/entry.client.tsx}
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.browserTracingIntegration({
      useEffect,
      useLocation,
      useMatches,
    }),
    // Replay is only available in the client
    Sentry.replayIntegration(),
  ],

  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for tracing.
  // We recommend adjusting this value in production
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/configuration/options/#traces-sample-rate
  tracesSampleRate: 1.0,

  // Set `tracePropagationTargets` to control for which URLs distributed tracing should be enabled
  tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],

  // Capture Replay for 10% of all sessions,
  // plus for 100% of sessions with an error
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/session-replay/configuration/#general-integration-configuration
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```
