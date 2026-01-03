---
---
title: React
description: "Learn how to manually set up Sentry in your React app and capture your first errors."
---

## Install

### Install the Sentry SDK

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash {tabTitle:npm}
npm install @sentry/react --save
```

```bash {tabTitle:yarn}
yarn add @sentry/react
```

```bash {tabTitle:pnpm}
pnpm add @sentry/react
```

## Configure

Choose the features you want to configure, and this guide will show you how:

### Initialize the Sentry SDK

To import and initialize Sentry, create a file in your project's root directory, for example, `instrument.js`, and add the following code:

```javascript {filename:instrument.js}
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users, for more info visit:
  // https://docs.sentry.io/platforms/javascript/guides/react/configuration/options/#sendDefaultPii
  sendDefaultPii: true,

  integrations: [
    // ___PRODUCT_OPTION_START___ performance
    // If you're using react router, use the integration for your react router version instead.
    // Learn more at
    // https://docs.sentry.io/platforms/javascript/guides/react/configuration/integrations/react-router/
    Sentry.browserTracingIntegration(),
    // ___PRODUCT_OPTION_END___ performance
    // ___PRODUCT_OPTION_START___ session-replay
    Sentry.replayIntegration(),
    // ___PRODUCT_OPTION_END___ session-replay
    // ___PRODUCT_OPTION_START___ user-feedback
    Sentry.feedbackIntegration({
      // Additional SDK configuration goes in here, for example:
      colorScheme: "system",
    }),
    // ___PRODUCT_OPTION_END___ user-feedback
  ],
  // ___PRODUCT_OPTION_START___ logs

  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
  // ___PRODUCT_OPTION_START___ performance

  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for tracing.
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/configuration/options/#traces-sample-rate
  tracesSampleRate: 1.0,

  // Set `tracePropagationTargets` to control for which URLs trace propagation should be enabled
  tracePropagationTargets: [/^\//, /^https:\/\/yourserver\.io\/api/],
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ session-replay

  // Capture Replay for 10% of all sessions,
  // plus for 100% of sessions with an error
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/session-replay/configuration/#general-integration-configuration
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ session-replay
});
```

### Apply Instrumentation to Your App

Initialize Sentry as early as possible in your application. We recommend putting the import of your initialization code as the first import in your app's entry point:

```javascript
// Sentry initialization should be imported first!
import "./instrument";
const container = document.getElementById(“app”);
const root = createRoot(container);
root.render();
```

## Capture React Errors

To make sure Sentry captures all your app's errors, configure error handling based on your React version.

### Configure Error Hooks (React 19+)

The `createRoot` and `hydrateRoot` methods provide error hooks to capture errors automatically. These hooks apply to all React components mounted to the root container.
Integrate Sentry with these hooks and customize error handling:

```javascript
const container = document.getElementById(“app”);
const root = createRoot(container, {
  // Callback called when an error is thrown and not caught by an ErrorBoundary.
  onUncaughtError: Sentry.reactErrorHandler((error, errorInfo) => {
    console.warn('Uncaught error', error, errorInfo.componentStack);
  }),
  // Callback called when React catches an error in an ErrorBoundary.
  onCaughtError: Sentry.reactErrorHandler(),
  // Callback called when React automatically recovers from errors.
  onRecoverableError: Sentry.reactErrorHandler(),
});
root.render();
```

### Add Error Boundary Components (React \<19)

Use the [`ErrorBoundary`](features/error-boundary/) component to automatically send errors from specific component trees to Sentry and provide a fallback UI:

```javascript
An error has occurred</p>}>
  
</Sentry.ErrorBoundary>;
```

  To capture errors manually with your own error boundary, use the
  `captureReactException` function as described
  [here](features/error-boundary/#manually-capturing-errors).

## Set Up React Router
If you're using `react-router` in your application, you need to set up the Sentry integration for your specific React Router version to trace `navigation` events.\
Select your React Router version to start instrumenting your routing:

- [React Router v7 (non-framework)](features/react-router/v7)
- [React Router v6](features/react-router/v6)
- [Older React Router versions](features/react-router)
- [TanStack Router](features/tanstack-router)

## Capture Redux State Data (Optional)

To capture Redux state data, use `Sentry.createReduxEnhancer` when initializing your Redux store.

## Add Readable Stack Traces With Source Maps (Optional)

## Avoid Ad Blockers With Tunneling (Optional)

## Verify Your Setup

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

### Issues

To verify that Sentry captures errors and creates issues in your Sentry project, add the following test button to one of your pages, which will trigger an error that Sentry will capture when you click it:

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

  Open the page in a browser (for most React applications, this will be at
  localhost) and click the button to trigger a frontend error.

### Tracing

To test your tracing configuration, update the previous code snippet to start a performance trace to measure the time it takes for the execution of your code:

```javascript
<button
  type="button"
  onClick={() => {
    Sentry.startSpan({ op: "test", name: "Example Frontend Span" }, () => {
      setTimeout(() => {
        throw new Error("Sentry Test Error");
      }, 99);
    });
  }}
>
  Break the world
</button>
```

Open the page in a browser (for most React applications, this will be at localhost) and click the button to trigger a frontend error and performance trace.

### View Captured Data in Sentry

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

## Next Steps

At this point, you should have integrated Sentry into your React application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

- Extend Sentry to your backend using one of our [SDKs](/)
- Continue to customize your configuration
- Make use of React-specific features
- Learn how to manually capture errors
- Avoid ad-blockers with tunneling

- [Get support](https://sentry.zendesk.com/hc/en-us/)

