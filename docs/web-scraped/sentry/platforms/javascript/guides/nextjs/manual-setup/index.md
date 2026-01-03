---
---
title: "Manual Setup"
description: "Learn how to set up and configure Sentry in your Next.js application, capture your first errors, logs and traces and view them in Sentry."
---

  For the fastest setup, we recommend using the [wizard
  installer](/platforms/javascript/guides/nextjs).

This guide covers manual setup for **Next.js 15+ with Turbopack and App Router**. For other setups, see:

- [Pages Router Setup](/platforms/javascript/guides/nextjs/manual-setup/pages-router/) - For applications using the Pages Router
- [Webpack Setup](/platforms/javascript/guides/nextjs/manual-setup/webpack-setup/) - For applications not using Turbopack

Choose the features you want to configure:

**How this guide works:**

1. **Install** - Add the Sentry SDK to your project
2. **Configure** - Set up SDK initialization files and Next.js configuration
3. **Verify** - Test error monitoring and any additional features you enabled

## Install

### Install the Sentry SDK

Run the command for your preferred package manager to add the Sentry SDK to your application.

```bash {tabTitle:npm}
npm install @sentry/nextjs --save
```

```bash {tabTitle:yarn}
yarn add @sentry/nextjs
```

```bash {tabTitle:pnpm}
pnpm add @sentry/nextjs
```

## Configure

### Apply Instrumentation to Your App

Extend your app's default Next.js options by adding `withSentryConfig` into your `next.config.ts` file.

```typescript {filename:next.config.ts}
const nextConfig: NextConfig = {
  // Your existing Next.js configuration
};

export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",

  // Only print logs for uploading source maps in CI
  silent: !process.env.CI,
});
```

### Initialize Sentry SDKs

Create the following files in your application's root directory (or `src` folder if you have one):

- `instrumentation-client.ts` - Client-side SDK initialization
- `sentry.server.config.ts` - Server-side SDK initialization
- `sentry.edge.config.ts` - Edge runtime SDK initialization

  Include your DSN directly in these files, or use a _public_ environment
  variable like `NEXT_PUBLIC_SENTRY_DSN`.

```typescript {tabTitle:Client} {filename:instrumentation-client.ts}
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance

  // Capture 100% in dev, 10% in production
  // Adjust based on your traffic volume
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
  // ___PRODUCT_OPTION_END___ performance
  integrations: [
    // ___PRODUCT_OPTION_START___ session-replay
    Sentry.replayIntegration(),
    // ___PRODUCT_OPTION_END___ session-replay
    // ___PRODUCT_OPTION_START___ user-feedback
    Sentry.feedbackIntegration({
      colorScheme: "system",
    }),
    // ___PRODUCT_OPTION_END___ user-feedback
  ],
  // ___PRODUCT_OPTION_START___ session-replay

  // Capture Replay for 10% of all sessions,
  // plus for 100% of sessions with an error
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ session-replay
  // ___PRODUCT_OPTION_START___ logs

  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
});

// ___PRODUCT_OPTION_START___ performance
// This export will instrument router navigations
export const onRouterTransitionStart = Sentry.captureRouterTransitionStart;
// ___PRODUCT_OPTION_END___ performance
```

```typescript {tabTitle:Server} {filename:sentry.server.config.ts}
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance

  // Capture 100% in dev, 10% in production
  // Adjust based on your traffic volume
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ logs

  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
});
```

```typescript {tabTitle:Edge} {filename:sentry.edge.config.ts}
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance

  // Capture 100% in dev, 10% in production
  // Adjust based on your traffic volume
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ logs

  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
});
```

The example above samples 100% of traces in development and 10% in production. Monitor your [usage stats](https://sentry.io/orgredirect/organizations/:orgslug/settings/stats/?dataCategory=spans) and adjust `tracesSampleRate` based on your traffic volume. Learn more about [sampling configuration](/platforms/javascript/guides/nextjs/configuration/sampling/).

### Register Server-Side SDK

Create a [Next.js Instrumentation file](https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation) named `instrumentation.ts` in your project root (or `src` folder). This file imports your server and edge configurations and exports `onRequestError` to capture server-side errors.

  The `onRequestError` hook requires `@sentry/nextjs` version `8.28.0` or higher
  and Next.js 15.

```typescript {filename:instrumentation.ts}
export async function register() {
  if (process.env.NEXT_RUNTIME === "nodejs") {
    await import("./sentry.server.config");
  }

  if (process.env.NEXT_RUNTIME === "edge") {
    await import("./sentry.edge.config");
  }
}

// Capture errors from Server Components, middleware, and proxies
export const onRequestError = Sentry.captureRequestError;
```

### Capture React Render Errors

Create `app/global-error.tsx` to capture errors that occur anywhere in your App Router application.

### Server Actions

Wrap your Server Actions with `Sentry.withServerActionInstrumentation()`.

```typescript {filename:app/actions.ts}
"use server";
export async function submitForm(formData: FormData) {
  return Sentry.withServerActionInstrumentation(
    "submitForm", // Action name for Sentry
    {
      recordResponse: true, // Include response data
    },
    async () => {
      // Your server action logic
      const result = await processForm(formData);
      return { success: true, data: result };
    }
  );
}
```

### Source Maps (Optional)

Add the `authToken` option to your `next.config.ts` to enable readable stack traces. Set the `SENTRY_AUTH_TOKEN` environment variable in your CI/CD.

  Keep your auth token secret and out of version control.

```typescript {filename:next.config.ts}
export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",

  // Pass the auth token
  authToken: process.env.SENTRY_AUTH_TOKEN,

  // Upload a larger set of source maps for prettier stack traces
  widenClientFileUpload: true,
});
```

```sh {filename:.env.local}
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

### Tunneling (Optional)

Prevent ad blockers from blocking Sentry events by routing them through your Next.js server.

  This increases server load. Consider the trade-off for your application.

If you're using Next.js middleware (`middleware.ts`) that intercepts requests, exclude the tunnel route:

```typescript {filename:middleware.ts}
export const config = {
  matcher: ["/((?!monitoring|_next/static|_next/image|favicon.ico).*)"],
};
```

```typescript {filename:next.config.ts}
export default withSentryConfig(nextConfig, {
  // Use a fixed route (recommended)
  tunnelRoute: "/monitoring",
});
```

## Error Monitoring

Test your error monitoring setup by throwing an error and viewing it in Sentry.

### Throw a Test Error

Add this button to any page and click it to trigger a test error.

```jsx
<button
  type="button"
  onClick={() => {
    throw new Error("Sentry Test Error");
  }}
>
  Break the world
</button>
```

### Verify

Open [**Issues**](https://sentry.io/orgredirect/organizations/:orgslug/issues/) in Sentry to see your test error. [Learn more about capturing errors](/platforms/javascript/guides/nextjs/usage/).

## Verify Additional Features

Based on the features you selected above, verify each one is working correctly.

### Session Replay

Session Replay captures video-like reproductions of user sessions. It's configured with `replayIntegration()` in your client config.

By default, Sentry masks all text, inputs, and media. You can customize this in [Privacy Configuration](/platforms/javascript/guides/nextjs/session-replay/privacy/).

**Verify:** Trigger an error or navigate your app, then check [**Replays**](https://sentry.io/orgredirect/organizations/:orgslug/replays/) in Sentry.

```typescript {filename:instrumentation-client.ts}
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.replayIntegration({
      maskAllText: true,
      maskAllInputs: true,
      blockAllMedia: true,
    }),
  ],

  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

### Tracing

Tracing is configured with `tracesSampleRate` in your SDK init files. Next.js routes and API calls are automatically instrumented.

Add [custom spans](/platforms/javascript/guides/nextjs/tracing/instrumentation/custom-instrumentation/) to trace specific operations in your code.

**Verify:** Navigate to any page, then check [**Traces**](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/) in Sentry.

```typescript
// Wrap operations with spans
const result = await Sentry.startSpan(
  { name: "expensive-operation", op: "function" },
  async () => {
    return await fetchDataFromAPI();
  }
);
```

### Logs 

Logs are enabled with `enableLogs: true` in your SDK config. Use the Sentry logger to send structured logs from anywhere in your application.

Connect popular logging libraries via [Integrations](/platforms/javascript/guides/nextjs/logs/#integrations).

**Verify:** Add a log statement, trigger it, then check [**Logs**](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) in Sentry.

```typescript
Sentry.logger.info("User clicked checkout button");

Sentry.logger.info("Order completed", {
  orderId: "12345",
  total: 99.99,
});

Sentry.logger.warn("Warning message");
Sentry.logger.error("Error occurred");
```

### User Feedback

User Feedback adds an embeddable widget via `feedbackIntegration()` that lets users report bugs directly from your app.

**Verify:** Look for the feedback button (bottom-right corner), submit test feedback, then check [**User Feedback**](https://sentry.io/orgredirect/organizations/:orgslug/feedback/) in Sentry.

[Learn more about User Feedback](/platforms/javascript/guides/nextjs/user-feedback/)

```typescript {filename:instrumentation-client.ts}
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  integrations: [
    Sentry.feedbackIntegration({
      colorScheme: "system",
    }),
  ],
});
```

<h2 data-no-number>Hybrid Apps (App Router + Pages Router)</h2>

If your application uses both the App Router and Pages Router:

1. Follow this guide for App Router components
2. Add a `pages/_error.tsx` file for Pages Router error handling (see [Pages Router Setup](/platforms/javascript/guides/nextjs/manual-setup/pages-router/))
3. Both routers share the same Sentry configuration files

  The Sentry SDK automatically detects which router is being used and applies
  the appropriate instrumentation.

<h2 data-no-number>Next Steps</h2>

You've successfully integrated Sentry into your Next.js application! Here's what to explore next:

- [Logs Integrations](/platforms/javascript/guides/nextjs/logs/#integrations) - Connect popular logging libraries like Pino, Winston, and Bunyan
- [Distributed Tracing](/platforms/javascript/guides/nextjs/tracing/distributed-tracing/) - Trace requests across services and microservices
- [AI Agent Monitoring](/platforms/javascript/guides/nextjs/tracing/instrumentation/ai-agents-module/) - Monitor AI agents built with Vercel AI SDK, LangChain, and more
- [Connect GitHub + Seer](/organization/integrations/source-code-mgmt/github/#installing-github) - Enable AI-powered [root cause analysis](/product/ai-in-sentry/seer/) by connecting your GitHub repository
- [Configuration Options](/platforms/javascript/guides/nextjs/configuration/) - Explore extended SDK configuration options

- Try the [installation wizard](/platforms/javascript/guides/nextjs/) for automatic setup
- [Get support](https://sentry.zendesk.com/hc/en-us/)

