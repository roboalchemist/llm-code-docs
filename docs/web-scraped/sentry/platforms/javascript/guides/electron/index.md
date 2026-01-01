---
---
title: Electron
description: "Learn how to manually set up Sentry in your Electron app and capture your first errors."
---

## Step 1: Install

### Install the Sentry SDK

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash {tabTitle:npm}
npm install @sentry/electron --save
```

```bash {tabTitle:yarn}
yarn add @sentry/electron
```

```bash {tabTitle:pnpm}
pnpm add @sentry/electron
```

## Step 2: Configure

Choose the features you want to configure, and this guide will show you how:

You should initialize the SDK in both the `main` process and every `renderer` process you spawn.

### Configure the Main Process

Initialize the SDK in your Electron `main` process as early as possible:

```javascript
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  // ___PRODUCT_OPTION_START___ logs
  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
});
```

### Configure the Renderer Process

Initialize the SDK in your Electron renderer processes:

```javascript
Sentry.init({
  // Adds request headers and IP for users, for more info visit:
  // https://docs.sentry.io/platforms/javascript/guides/electron/configuration/options/#sendDefaultPii
  sendDefaultPii: true,
  integrations: [
    // ___PRODUCT_OPTION_START___ performance
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
  // ___PRODUCT_OPTION_START___ performance

  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for performance monitoring.
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
```

### Configure any Utility Processes

```javascript
Sentry.init({
  // ___PRODUCT_OPTION_START___ logs
  // Enable logs to be sent to Sentry
  enableLogs: true,
  // ___PRODUCT_OPTION_END___ logs
});
```

If your app uses a preload script and `contextIsolation: true`, Sentry can't automatically capture errors that occur in the preload context. To include those, initialize Sentry in your preload script as well:

```javascript
Sentry.init(); // don't forget to add your configuration options
```

If you change the `userData` directory used by your app, ensure this change is made before you configure the SDK as this path is used to cache scope and events between application restarts.

```javascript
app.setPath("userData", "~/.config/my-app");
Sentry.init({ dsn: "___PUBLIC_DSN___" });
```

### Using Framework-Specific SDKs

If you're using a framework in your renderers, you can combine the Electron SDK with the framework SDK:

```javascript
init(
  {
    dsn: "___PUBLIC_DSN___",
    integrations: [
      /* integrations */
    ],
    /* Other Electron and React SDK config */
  },
  reactInit
);
```

## Step 3: Add Readable Stack Traces With Source Maps (Optional)

## Step 4: Verify Your Setup

Let's test your setup and confirm that Sentry is working correctly.

### Issues

**Main process error**

Add an event listener that throws an error in your main process:

```javascript
app.on("ready", () => {
  throw new Error("Sentry test error in main process");
});
```

**Renderer process error**

Add a test button in one of your HTML pages:

```html {filename: index.html}
<button id="testError">Break the world</button>

<script src="renderer.js"></script>
```

Then, in your renderer, add the following:

```javascript
document.getElementById("testError").addEventListener("click", () => {
  throw new Error("Sentry test error in renderer process");
});
```

  Start your app and trigger two errors that Sentry will capture: one from the
  main process and one from the renderer.

### Tracing
To test tracing in your renderer, start a trace to measure the time it takes to execute your code:

```javascript
document.getElementById("testError").addEventListener("click", () => {
  Sentry.startSpan({ op: "test", name: "Renderer test span" }, () => {
    throw new Error("Sentry test error in renderer process");
  });
});
```

Start your app and trigger two errors that Sentry will capture: one from the main process and one from the renderer. It will also start a trace with the defined name.

### View Captured Data in Sentry

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

## Next Steps

At this point, you should have integrated Sentry into your Electron application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

- Continue to customize your configuration
- Learn how to manually capture errors
- Make use of Electron-specific features
- Get familiar with [Sentry's product features](/product/) like tracing, insights, and alerts

- Find various topics in Troubleshooting
- [Get support](https://sentry.zendesk.com/hc/en-us/)

