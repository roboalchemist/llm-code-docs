---
---
title: Solid Router
description: "Learn about Sentry's Solid Router integration."
---

  The routing instrumentation supports [Solid Router](https://docs.solidjs.com/solid-router) 0.13.4 and up.

The Sentry SDK provides a routing instrumentation for Solid Router to create navigation spans to ensure
you collect meaningful performance data about the health of your page loads and associated requests.

To get started, import `solidRouterBrowserTracingIntegration` from `@sentry/solid/solidrouter` and add it to `Sentry.init`
instead of the regular `Sentry.browserTracingIntegration` to enable performance tracing.

Import `withSentryRouterRouting` from `@sentry/solid/solidrouter` and use it to wrap `Router`, `MemoryRouter` or `HashRouter` from `@solidjs/router`.
This creates a higher order component, which will enable Sentry to reach your router context.

```jsx
Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [solidRouterBrowserTracingIntegration()],
  tracesSampleRate: 1.0, //  Capture 100% of the transactions
});

// Wrap Solid Router to collect meaningful performance data on route changes
const SentryRouter = withSentryRouterRouting(Router);

render(
  () => (
    
      
      ...
    
  ),
  document.getElementById("root"),
);
```
