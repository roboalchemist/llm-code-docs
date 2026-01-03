---
---
title: React Router Framework
description: Learn how to set up and configure Sentry in your React Router v7 application using the installation wizard, capture your first errors, and view them in Sentry.
---

  This SDK is currently in **beta**. Beta features are still in progress and may
  have bugs. Please reach out on
  [GitHub](https://github.com/getsentry/sentry-javascript/issues/new/choose) if
  you have any feedback or concerns.

If you're using React Router in data or declarative mode, follow the instructions in our [React guide](/platforms/javascript/guides/react/features/react-router/v7).

## Install

To install Sentry using the installation wizard, run the command on the right within your project directory.

The wizard guides you through the setup process, asking you to enable additional (optional) Sentry features for your application beyond error monitoring.

This guide assumes that you enable all features and allow the wizard to create an example page and route. You can add or remove features at any time, but setting them up now will save you the effort of configuring them manually later.

- Installs the `@sentry/react-router` package (and optionally `@sentry/profiling-node`)
- Reveals React Router entry point files (`entry.client.tsx` and `entry.server.tsx`) if not already visible
- Initializes Sentry in your client and server entry files with default configuration
- Creates `instrument.server.mjs` for server-side instrumentation
- Updates your `app/root.tsx` to capture errors in the error boundary
- Configures source map upload in `vite.config.ts` and `react-router.config.ts`
- Creates `.env.sentry-build-plugin` with an auth token to upload source maps (this file is automatically added to `.gitignore`)
- Creates example page and API route to help verify your Sentry setup

```bash
npx @sentry/wizard@latest -i reactRouter
```

## Configure

If you prefer to configure Sentry manually, here are the configuration files the wizard would create:

In addition to capturing errors, you can monitor interactions between multiple services or applications by [enabling tracing](/concepts/key-terms/tracing/). You can also get to the root of an error or performance issue faster, by watching a video-like reproduction of a user session with [session replay](/product/explore/session-replay/web/getting-started/).

Select which Sentry features you'd like to install in addition to Error Monitoring to get the corresponding installation and configuration instructions below.

### Client-Side Configuration

The wizard creates a client configuration file that initializes the Sentry SDK in your browser.

The configuration includes your DSN (Data Source Name), which connects your app to your Sentry project, and enables the features you selected during installation.

```tsx {tabTitle:Client} {filename:entry.client.tsx}
Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users, for more info visit:
  // https://docs.sentry.io/platforms/javascript/guides/react-router/configuration/options/#sendDefaultPii
  sendDefaultPii: true,

  integrations: [
    // ___PRODUCT_OPTION_START___ performance
    // Registers and configures the Tracing integration,
    // which automatically instruments your application to monitor its
    // performance, including custom Angular routing instrumentation
    Sentry.reactRouterTracingIntegration(),
    // ___PRODUCT_OPTION_END___ performance
    // ___PRODUCT_OPTION_START___ session-replay
    // Registers the Replay integration,
    // which automatically captures Session Replays
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
  // We recommend adjusting this value in production
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/guides/react-router/configuration/options/#traces-sample-rate
  tracesSampleRate: 1.0,

  // Set `tracePropagationTargets` to declare which URL(s) should have trace propagation enabled
  tracePropagationTargets: [/^\//, /^https:\/\/yourserver\.io\/api/],
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ session-replay

  // Capture Replay for 10% of all sessions,
  // plus 100% of sessions with an error
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/guides/react-router/session-replay/configuration/#general-integration-configuration
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ session-replay
});

startTransition(() => {
  hydrateRoot(
    document,
    
      
    
  );
});
```

### Server-Side Configuration

The wizard also creates a server configuration file for Node.js runtime.

For more advanced configuration options or to set up Sentry manually, check out our [manual setup guide](/platforms/javascript/guides/react-router/manual-setup/).

```js {tabTitle:Server} {filename:instrument.server.mjs}
// ___PRODUCT_OPTION_START___ profiling
// ___PRODUCT_OPTION_END___ profiling

Sentry.init({
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users, for more info visit:
  // https://docs.sentry.io/platforms/javascript/guides/react-router/configuration/options/#sendDefaultPii
  sendDefaultPii: true,
  // ___PRODUCT_OPTION_START___ logs

  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
  // ___PRODUCT_OPTION_START___ profiling

  // Add our Profiling integration
  integrations: [nodeProfilingIntegration()],
  // ___PRODUCT_OPTION_END___ profiling
  // ___PRODUCT_OPTION_START___ performance
  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for tracing.
  // We recommend adjusting this value in production
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/guides/react-router/configuration/options/#tracesSampleRate
  tracesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ performance
  // ___PRODUCT_OPTION_START___ profiling
  // Set profilesSampleRate to 1.0 to profile 100%
  // of sampled transactions.
  // This is relative to tracesSampleRate
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/guides/react-router/configuration/options/#profilesSampleRate
  profilesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ profiling
});
```

## Verify Your Setup

If you haven't tested your Sentry configuration yet, let's do it now. You can confirm that Sentry is working properly and sending data to your Sentry project by using the example page created by the installation wizard:

1. Open the example page `/sentry-example-page` in your browser. For most React Router applications, this will be at localhost.
2. Observe the example page with a button that triggers test errors.

Clicking the button triggers an error that Sentry captures for you. The example also demonstrates how to test performance tracing.

Don't forget to explore the example files' code in your project to understand what's happening after your button click.

### View Captured Data in Sentry

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

## Next Steps

At this point, you should have integrated Sentry into your React Router Framework application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics.
Our next recommended steps for you are:

- Learn how to manually capture errors
- Continue to customize your configuration
- Get familiar with [Sentry's product features](/product/) like tracing, insights, and alerts

- If you encountered issues with our installation wizard, try [setting up Sentry manually](/platforms/javascript/guides/react-router/manual-setup/)
- Find various topics in Troubleshooting
- [Get support](https://sentry.zendesk.com/hc/en-us/)

