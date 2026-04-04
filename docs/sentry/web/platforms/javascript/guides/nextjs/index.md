---
---
title: "Next.js"
description: Learn how to set up and configure Sentry in your Next.js application using the installation wizard, capture your first errors, logs and traces and view them in Sentry.
---

## Install

Run the Sentry wizard to automatically configure Sentry in your Next.js application:

```bash
npx @sentry/wizard@latest -i nextjs
```

The wizard will prompt you to select features. Choose the ones you want to enable:

Prefer to set things up yourself? Check out the [Manual Setup](/platforms/javascript/guides/nextjs/manual-setup/) guide.

## What the Wizard Created

The wizard configured Sentry for all Next.js runtime environments and created files to test your setup.

### SDK Initialization

Next.js runs code in different environments. The wizard creates separate initialization files for each:

- **Client** (`instrumentation-client.ts`) — Runs in the browser
- **Server** (`sentry.server.config.ts`) — Runs in Node.js
- **Edge** (`sentry.edge.config.ts`) — Runs in edge runtimes

```typescript {tabTitle:Client} {filename:instrumentation-client.ts}
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ session-replay
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ session-replay
  // ___PRODUCT_OPTION_START___ logs
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
  integrations: [
    // ___PRODUCT_OPTION_START___ session-replay
    Sentry.replayIntegration(),
    // ___PRODUCT_OPTION_END___ session-replay
  ],
});
```

```typescript {tabTitle:Server} {filename:sentry.server.config.ts}
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ logs
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
  tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1,
  // ___PRODUCT_OPTION_END___ performance
});
```

The example above samples 100% of traces in development and 10% in production. Monitor your [usage stats](https://sentry.io/orgredirect/organizations/:orgslug/settings/stats/?dataCategory=spans) and adjust `tracesSampleRate` based on your traffic volume. Learn more about [sampling configuration](/platforms/javascript/guides/nextjs/configuration/sampling/).

### Server-Side Registration

The `instrumentation.ts` file registers your server and edge configurations with Next.js.

```typescript {filename:instrumentation.ts}
export async function register() {
  if (process.env.NEXT_RUNTIME === "nodejs") {
    await import("./sentry.server.config");
  }
  if (process.env.NEXT_RUNTIME === "edge") {
    await import("./sentry.edge.config");
  }
}

export const onRequestError = Sentry.captureRequestError;
```

### Next.js Configuration

Your `next.config.ts` is wrapped with `withSentryConfig` to enable source map uploads, tunneling (to avoid ad-blockers), and other build-time features.

```typescript {filename:next.config.ts}
export default withSentryConfig(nextConfig, {
  org: "___ORG_SLUG___",
  project: "___PROJECT_SLUG___",

  // Upload source maps for readable stack traces
  authToken: process.env.SENTRY_AUTH_TOKEN,

  // Route Sentry requests through your server (avoids ad-blockers)
  tunnelRoute: "/monitoring",

  silent: !process.env.CI,
});
```

### Error Handling

The wizard creates `app/global-error.tsx` to capture React rendering errors in your App Router application.

```tsx {filename:app/global-error.tsx}
"use client";

export default function GlobalError({
  error,
}: {
  error: Error & { digest?: string };
}) {
  useEffect(() => {
    Sentry.captureException(error);
  }, [error]);

  return (
    <html>
      <body>
        <h1>Something went wrong!</h1>
      </body>
    </html>
  );
}
```

### Source Maps

The wizard creates `.env.sentry-build-plugin` with your auth token for source map uploads. This file is automatically added to `.gitignore`.

For CI/CD, set the `SENTRY_AUTH_TOKEN` environment variable in your build system.

```bash {tabTitle:Local Development} {filename:.env.sentry-build-plugin}
SENTRY_AUTH_TOKEN=sntrys_eyJ...
```

```bash {tabTitle:CI/CD}
# Set as environment variable in your CI/CD system
SENTRY_AUTH_TOKEN=sntrys_eyJ...
```

### Example Page

The wizard creates `/sentry-example-page` with a button that triggers a test error. Use this to verify your setup.

```
app/
├── sentry-example-page/
│   └── page.tsx       # Test page with error button
└── api/
    └── sentry-example-api/
        └── route.ts   # Test API route
```

## Verify Your Setup

The example page tests all your enabled features with a single action:

1. Start your dev server:

```bash
npm run dev
```

2. Visit [localhost:3000/sentry-example-page](http://localhost:3000/sentry-example-page)

3. Click **"Throw Sample Error"**

### Check Your Data in Sentry

**Errors** — [Open Issues](https://sentry.io/orgredirect/organizations/:orgslug/issues/)

You should see "This is a test error" with a full stack trace pointing to your source code.

**Tracing** — [Open Traces](https://sentry.io/orgredirect/organizations/:orgslug/explore/traces/)

You should see the page load trace and the button click span. Learn more about [custom spans](/platforms/javascript/guides/nextjs/tracing/instrumentation/custom-instrumentation/).

**Session Replay** — [Open Replays](https://sentry.io/orgredirect/organizations/:orgslug/replays/)

Watch a video-like recording of your session, including the moment the error occurred. Learn more about [Session Replay configuration](/platforms/javascript/guides/nextjs/session-replay/).

**Logs** — [Open Logs](https://sentry.io/orgredirect/organizations/:orgslug/explore/logs/) 

See structured log entries from your application. You can send logs from anywhere:

```typescript
Sentry.logger.info("User action", { userId: "123" });
Sentry.logger.warn("Slow response", { duration: 5000 });
Sentry.logger.error("Operation failed", { reason: "timeout" });
```

Learn more about [Logs configuration](/platforms/javascript/guides/nextjs/logs/).

- If you encountered issues with our installation wizard, try [setting up Sentry manually](/platforms/javascript/guides/nextjs/manual-setup/)
- Check [Troubleshooting](/platforms/javascript/guides/nextjs/troubleshooting/) for common issues
- [Get support](https://sentry.io/support/)

## Next Steps

You've successfully integrated Sentry into your Next.js application! Here's what to explore next:

- [Logs Integrations](/platforms/javascript/guides/nextjs/logs/#integrations) - Connect popular logging libraries like Pino, Winston, and Bunyan
- [Distributed Tracing](/platforms/javascript/guides/nextjs/tracing/distributed-tracing/) - Trace requests across services and microservices
- [AI Agent Monitoring](/platforms/javascript/guides/nextjs/tracing/instrumentation/ai-agents-module/) - Monitor AI agents built with Vercel AI SDK, LangChain, and more
- [Connect GitHub + Seer](/organization/integrations/source-code-mgmt/github/#installing-github) - Enable AI-powered [root cause analysis](/product/ai-in-sentry/seer/) by connecting your GitHub repository
- [Configuration Options](/platforms/javascript/guides/nextjs/configuration/) - Explore extended SDK configuration options

