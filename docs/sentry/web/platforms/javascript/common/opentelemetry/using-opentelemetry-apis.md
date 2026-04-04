---
---
title: Using OpenTelemetry APIs
description: "Learn how to use OpenTelemetry APIs with Sentry."
---

Sentry supports OpenTelemetry APIs out of the box. Any spans started using OpenTelemetry APIs will be automatically captured by Sentry, while any spans started using the Sentry SDK will be automatically propagated to OpenTelemetry.

## Adding Additional OpenTelemetry Instrumentation

While the Sentry SDK includes some OpenTelemetry instrumentation out of the box, you may want to add additional instrumentation to your application. This can be done by registering the instrumentation through OpenTelemetry like the example below:

```javascript {tabTitle: ESM} {12-13}
import {
  GenericPoolInstrumentation,
} from "@opentelemetry/instrumentation-generic-pool";

Sentry.init({
  dsn: "___DSN___",

  // The SentrySampler will use this to determine which traces to sample
  tracesSampleRate: 1.0,

  // Add additional OpenTelemetry instrumentation:
  openTelemetryInstrumentations: [new GenericPoolInstrumentation()],
});
```
```javascript {tabTitle: CJS} {12-13}
const Sentry = require("@sentry/node");
const {
  GenericPoolInstrumentation,
} = require("@opentelemetry/instrumentation-generic-pool");

Sentry.init({
  dsn: "___DSN___",

  // The SentrySampler will use this to determine which traces to sample
  tracesSampleRate: 1.0,

  // Add additional OpenTelemetry instrumentation:
  openTelemetryInstrumentations: [new GenericPoolInstrumentation()],
});
```

  It is possible to add instrumentations via `registerInstrumentations()` from
  `@opentelemetry/instrumentation`. However, with ESM (`import`/`export` syntax)
  you need to be careful to do so before importing any modules that should be
  instrumented.

As a rule of thumb, `registerInstrumentations()` should be called right after, and in the same context as registering ESM Loaders.

## Using an OpenTelemetry Tracer

We recommend using `Sentry.startSpan()` and related APIs to create spans, but you can also create spans using native OpenTelemetry APIs.

You can access the tracer Sentry uses via `client.tracer` and then create spans with OpenTelemetry APIs, as shown below:

```javascript {tabTitle: ESM}
const tracer = Sentry.getClient()?.tracer;
// Now you can use native APIs on the tracer:
tracer.startActiveSpan("span name", () => {
  // measure something
});
```
```javascript {tabTitle: CJS}
const Sentry = require("@sentry/node");

const tracer = Sentry.getClient()?.tracer;
// Now you can use native APIs on the tracer:
tracer.startActiveSpan("span name", () => {
  // measure something
});
```

You can also use any other tracer. All OpenTelemetry spans will be picked up by Sentry automatically.

## Modifying the default OpenTelemetry TracerProvider

You can access the tracer provider set up by Sentry when using Sentry's default OpenTelemetry instrumentation.

```javascript {tabTitle: ESM}
const provider = Sentry.getClient()?.traceProvider;
```
```javascript {tabTitle: CJS}
const Sentry = require("@sentry/node");

const provider = Sentry.getClient()?.traceProvider;
```

## Adding Additional Span Processors

You can add additional span processors to the tracer provider set up by Sentry when using Sentry's default OpenTelemetry instrumentation.

```javascript {tabTitle: ESM}
Sentry.init({
  dsn: "___DSN___",

  // The SentrySampler will use this to determine which traces to sample
  tracesSampleRate: 1.0,

  // Add additional OpenTelemetry SpanProcessors:
  openTelemetrySpanProcessors: [new MySpanProcessor()],
});
```
```javascript {tabTitle: CJS}
const Sentry = require("@sentry/node");

Sentry.init({
  dsn: "___DSN___",

  // The SentrySampler will use this to determine which traces to sample
  tracesSampleRate: 1.0,

  // Add additional OpenTelemetry SpanProcessors:
  openTelemetrySpanProcessors: [new MySpanProcessor()],
});
```
