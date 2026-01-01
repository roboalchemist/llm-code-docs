---
---
title: SolidStart
description: Learn how to set up Sentry in your SolidStart application and capture your first errors.
---

  This SDK is currently in **beta**. Beta features are still in progress and may
  have bugs. Please reach out on
  [GitHub](https://github.com/getsentry/sentry-javascript/issues/new/choose) if
  you have any feedback or concerns.

  This SDK guide is specifically for SolidStart. For instrumenting your Solid
  app, see our [Solid SDK](/platforms/javascript/guides/solid).

## Step 1: Install

Choose the features you want to configure, and this guide will show you how:

### Install the Sentry SDK

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash {tabTitle:npm}
npm install @sentry/solidstart --save
```

```bash {tabTitle:yarn}
yarn add @sentry/solidstart
```

```bash {tabTitle:pnpm}
pnpm add @sentry/solidstart
```

## Step 2: Configure

You need to initialize and configure the Sentry SDK in two places: the client side and the server side.

  The examples in this guide will use TypeScript with a `src` folder structure.
  Make sure to adjust the file paths and extensions (`.js`, `.jsx`, `.ts`,
  `.tsx`) to match your project setup.

### Configure Client-side Sentry

Import and initialize the Sentry SDK in your `/src/entry-client.tsx` file.

  If you're using Solid Router, make sure to import and add the
  `solidRouterBrowserTracingIntegration` to enable tracing in your app:

```jsx {filename:src/entry-client.tsx}
// ___PRODUCT_OPTION_START___ performance
// import solidRouterBrowserTracingIntegration if you're using Solid Router
// ___PRODUCT_OPTION_END___ performance
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  // Adds request headers and IP for users, for more info visit:
  // https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration/options/#sendDefaultPii
  sendDefaultPii: true,
  integrations: [
    // ___PRODUCT_OPTION_START___ performance
    // add solidRouterBrowserTracingIntegration if you're using Solid Router
    solidRouterBrowserTracingIntegration(),
    // ___PRODUCT_OPTION_END___ performance
    // ___PRODUCT_OPTION_START___ session-replay
    // Replay may only be enabled for the client-side
    Sentry.replayIntegration(),
    // ___PRODUCT_OPTION_END___ session-replay
    // ___PRODUCT_OPTION_START___ user-feedback
    Sentry.feedbackIntegration({
      // Additional SDK configuration goes in here, for example:
      colorScheme: "system",
    }),
    // ___PRODUCT_OPTION_END___ user-feedback
  ],
  // ___PRODUCT_OPTION_START___ performance

  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for tracing.
  // We recommend adjusting this value in production
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/configuration/options/#traces-sample-rate
  tracesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ session-replay

  // Capture Replay for 10% of all sessions,
  // plus for 100% of sessions with an error
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/session-replay/configuration/#general-integration-configuration
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ session-replay
  // ___PRODUCT_OPTION_START___ logs

  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
});

mount(() => , document.getElementById("app"));
```

### Configure Server-side Sentry

Create a file named `instrument.server.ts` in your `src` folder. In this file, initialize and import Sentry for your server:

```javascript {filename:src/instrument.server.ts}
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  // Adds request headers and IP for users, for more info visit:
  // https://docs.sentry.io/platforms/javascript/guides/solidstart/configuration/options/#sendDefaultPii
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ performance

  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for tracing.
  // We recommend adjusting this value in production
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/configuration/options/#traces-sample-rate
  tracesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ logs

  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
});
```

### Server Instrumentation

The Sentry SDK provides [middleware lifecycle](https://docs.solidjs.com/solid-start/advanced/middleware) handlers that enhance the data collected by Sentry on the server side, enabling distributed tracing between the client and server.

Create or update your `src/middleware.ts` file and add the `sentryBeforeResponseMiddleware` handler:

```typescript {filename:src/middleware.ts} {6}
export default createMiddleware({
  onBeforeResponse: [
    sentryBeforeResponseMiddleware(),
    // Add your other middleware handlers after `sentryBeforeResponseMiddleware`
  ],
});
```

Wrap your SolidStart config in `app.config.ts` with `withSentry` so that the instrumentation file gets included in your build output.
Then, specify the middleware that you've just created:

```javascript {filename:app.config.ts} {5-15}
export default defineConfig(
  withSentry(
    {
      // other SolidStart config options...
      middleware: "./src/middleware.ts",
    },
    {
      // Your Sentry build-time config (such as source map upload options)
      // optional: if your `instrument.server.ts` file is not located inside `src`
      instrumentation: "./mypath/instrument.server.ts",
    }
  )
);
```

### Configure Solid Router
If you're using Solid Router and the Sentry `solidRouterBrowserTracingIntegration` integration, wrap your Solid Router with `withSentryRouterRouting` to enable Sentry to collect navigation spans:

```tsx {filename:app.tsx} {5,9,11}
const SentryRouter = withSentryRouterRouting(Router);

export default function App() {
  return (
    
      
    
  );
}
```

### Run Your Application

Instrumentation needs to happen as early as possible to make sure Sentry works as intended. To do this, add an `--import` flag to the `NODE_OPTIONS` environment variable when you run your application and set it to import the instrumentation file created by the build output: `.output/server/instrument.server.mjs`.

Run your build command to generate the `instrument.server.mjs` file before running your app. Depending on your build preset, the location of the file can differ. To find out where the file is located, monitor the build log output for:

`[Sentry SolidStart withSentry] Successfully created /my/project/path/.output/server/instrument.server.mjs.`

For example, update your scripts in `package.json`.

```json {filename:package.json}
{
  "scripts": {
    "start:vinxi": "NODE_OPTIONS='--import ./.output/server/instrument.server.mjs ' vinxi start",
    "start:node": "node --import ./.output/server/instrument.server.mjs .output/server/index.mjs"
  }
}
```

If you're not able to use the `--import` flag, check the alternative installation methods.

## Step 3: Capture Solid Errors

To automatically report exceptions from inside a component tree to Sentry, wrap Solid's `ErrorBoundary` with Sentry's helper function:

## Step 4: Add Readable Stack Traces With Source Maps (Optional)

To upload source maps for clear error stack traces, add your Sentry auth token, organization, and project slug in your SolidStart configuration:

```TypeScript {filename:app.config.ts}
export default defineConfig(
  withSentry(
    {
      /* Your SolidStart config */
    },
    {
      org: "___ORG_SLUG___",
      project: "___PROJECT_SLUG___",
      // store your auth token in an environment variable
      authToken: process.env.SENTRY_AUTH_TOKEN,
    }
  ),
);
```

To keep your auth token secure, always store it in an environment variable instead of directly in your files:

```bash {filename:.env}
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

Alternatively, you can create a `.env.sentry-build-plugin` file:

```bash {filename:.env.sentry-build-plugin}
SENTRY_ORG="___ORG_SLUG___"
SENTRY_PROJECT="___PROJECT_SLUG___"
SENTRY_AUTH_TOKEN="___ORG_AUTH_TOKEN___"
```

## Step 5: Avoid Ad Blockers With Tunneling (Optional)

## Step 6: Verify Your Setup

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

### Issues

To verify that Sentry captures errors and creates issues in your Sentry project, add a test button to an existing page or create a new one:

```javascript
<button
  type="button"
  onClick={() => {
    throw new Error("Sentry Test Error");
  }}
>
  Break the world
</button>
```

  Open the page in a browser and click the button to trigger a frontend error.

### Tracing

To test tracing, create a test API route like `src/routes/sentry-test.tsx`:

```javascript {filename:sentry-test.tsx}
export async function GET() {
  throw new Error("Sentry Example API Route Error");
}
```

Next, update your test button to call this route and throw an error if the response isn't `ok`:

```javascript
<button
  type="button"
  onClick={() => {
    Sentry.startSpan(
      {
        op: "test",
        name: "My First Test Transaction",
      },
      async () => {
        const res = await fetch("/sentry-test");
        if (!res.ok) {
          throw new Error("Sentry Test Error");
        }
      }
    );
  }}
>
  Break the world
</button>
```

Open the page in the browser and click the button to trigger a frontend error, an error in the API route, and a trace to measure the time it takes for the API request to complete.

### View Captured Data in Sentry

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

## Next Steps

At this point, you should have integrated Sentry into your SolidStart application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

- Learn how to manually capture errors
- Continue to customize your configuration
- Learn how to make use of SolidStart-specific features
- Get familiar with [Sentry's product features](/) like tracing, insights, and alerts

- If you encountered issues with setting up Sentry, review alternative installation methods
- Find various topics in Troubleshooting
- [Get support](https://sentry.zendesk.com/hc/en-us/)

