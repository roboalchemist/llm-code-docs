---
---
title: BrowserTracing
description: "Capture performance data for the Browser."
---

This integration only works inside a browser environment.

_Import name: `Sentry.browserTracingIntegration`_

With [tracing](/product/insights/overview/), Sentry tracks your software performance, measuring metrics like throughput and latency, and displaying the impact of errors across multiple systems. Sentry captures distributed traces consisting of transactions and spans, which measure individual services and individual operations within those services.

The BrowserTracing integration sets up automatic tracing for your frontend applications. It captures transactions and spans from the browser and sends them to Sentry.

Read more about [setting up BrowserTracing](./../../../tracing/).

```JavaScript
Sentry.init({
  integrations: [Sentry.browserTracingIntegration()],
});
```

See Configuration Options for a full list of available options for `browserTracingIntegration` 
