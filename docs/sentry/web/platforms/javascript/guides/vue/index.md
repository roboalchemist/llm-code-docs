---
---
title: Vue
description: "Learn how to manually set up Sentry in your Vue app and capture your first errors."
---

## Step 1: Install

### Install the Sentry SDK

Run the command for your preferred package manager to add the Sentry SDK to your application:

```bash {tabTitle:npm}
npm install @sentry/vue --save
```

```bash {tabTitle:yarn}
yarn add @sentry/vue
```

```bash {tabTitle:pnpm}
pnpm add @sentry/vue
```

## Step 2: Configure

Choose the features you want to configure, and this guide will show you how:

To initialize Sentry in your Vue application, add the following code snippet to your `main.js`:

```javascript {tabTitle:Vue 3} {filename:main.js} {3, 12-41}
const app = createApp({
  // ...
});
const router = createRouter({
  // ...
});

Sentry.init({
  app,
  dsn: "___PUBLIC_DSN___",

  // Adds request headers and IP for users, for more info visit:
  // https://docs.sentry.io/platforms/javascript/guides/vue/configuration/options/#sendDefaultPii
  sendDefaultPii: true,

  integrations: [
    // ___PRODUCT_OPTION_START___ performance
    Sentry.browserTracingIntegration({ router }),
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
  // We recommend adjusting this value in production
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/configuration/options/#traces-sample-rate
  tracesSampleRate: 1.0,

  // Set `tracePropagationTargets` to control for which URLs trace propagation should be enabled
  tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],
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

app.use(router);
app.mount("#app");
```

```javascript {tabTitle:Vue 2} {filename:main.js} {3, 11-35}
Vue.use(Router);

const router = new Router({
  // ...
});

Sentry.init({
  Vue,
  dsn: "___PUBLIC_DSN___",
  integrations: [
    // ___PRODUCT_OPTION_START___ performance
    Sentry.browserTracingIntegration({ router }),
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
  // We recommend adjusting this value in production
  // Learn more at
  // https://docs.sentry.io/platforms/javascript/configuration/options/#traces-sample-rate
  tracesSampleRate: 1.0,

  // Set `tracePropagationTargets` to control for which URLs trace propagation should be enabled
  tracePropagationTargets: ["localhost", /^https:\/\/yourserver\.io\/api/],
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

// ...

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
```

If you're creating more than one Vue 3 app within your application, check out how to initialize the SDK for [multiple apps](./features/multiple-apps).

### Configuration for Late-Defined Vue Apps

If your Vue application is not defined from the start, you can add error monitoring for Vue-specific errors later on.
To manually add the integration for late-defined Vue applications, update your `main.js` file:

```javascript {filename:main.js}
Sentry.init({
  dsn: "...",
  // Filter out default `Vue` integration
  integrations: (integrations) =>
    integrations.filter((integration) => integration.name !== "Vue"),
});

// Sometimes later
const app = createApp({
  template: "<div>hello</div>",
});

Sentry.addIntegration(Sentry.vueIntegration({ app }));
```

### Configuration for Pinia

To capture Pinia state data, use `Sentry.createSentryPiniaPlugin()` and add it to your Pinia store instance:

```javascript
const pinia = createPinia();

pinia.use(createSentryPiniaPlugin());
```

Learn more about the [Pinia Plugin](./features/pinia) and its options.

## Step 3: Add Readable Stack Traces With Source Maps (Optional)

## Step 4: Avoid Ad Blockers With Tunneling (Optional)

## Step 5: Verify Your Setup

Let's test your setup and confirm that Sentry is working correctly and sending data to your Sentry project.

### Issues

To verify that Sentry is capturing errors and creating issues in your Sentry project, add the following test button to one of your pages, which will trigger an error that Sentry will capture when you click it:

```javascript {filename:App.vue}
// ...
<button @click="throwError">Throw error</button>
// ...

export default {
  // ...
  methods: {
    throwError() {
      throw new Error('Sentry Error');
    }
  }
};
```

  Open the page in a browser and click the button to trigger a frontend error.

### Tracing

To test your tracing configuration, update the previous code snippet to start a performance trace to measure the time it takes for your code to execute:

```javascript {filename:App.vue}
// ...
<button @click="throwError">Throw error</button>
// ...

export default {
  // ...
  methods: {
    throwError() {
      Sentry.startSpan({ op: "test", name: "Example Frontend Span" }, async () => {
        // Simulate an asynchronous operation
        await new Promise(resolve => setTimeout(resolve, 99));

        throw new Error("Sentry Error");
      });
    }
  }
};

```

Open the page in a browser and click the button to trigger a frontend error and performance trace.

### View Captured Data in Sentry

Now, head over to your project on [Sentry.io](https://sentry.io/) to view the collected data (it takes a couple of moments for the data to appear).

## Next Steps

At this point, you should have integrated Sentry into your Vue application and should already be sending data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

- Extend Sentry to your backend using one of our [SDKs](/)
- Continue to customize your configuration
- Make use of Vue-specific features
- Learn how to manually capture errors

- Find various topics in Troubleshooting
- [Get support](https://sentry.zendesk.com/hc/en-us/)

