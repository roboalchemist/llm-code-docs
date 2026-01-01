---
---
title: Using Your Existing OpenTelemetry Setup
description: "Learn how to use your existing custom OpenTelemetry setup with Sentry."
---

Use this guide when you already have a completely custom OpenTelemetry setup or when you intend to add a custom OpenTelemetry setup next to the Sentry SDK.

Setting `skipOpenTelemetrySetup: true` disables the Sentry SDK's automatic OpenTelemetry configuration, **requiring** you to perform the setup manually. For example, to ensure errors are correctly associated with their scope, you must add the `SentryContextManager` to your OpenTelemetry setup. You can find details on the required manual setup further down on this page.

If you are looking to simply add individual OpenTelemetry instrumentation to your Sentry setup, you should read Adding Additional OpenTelemetry Instrumentation instead.

## Using Sentry for Error Monitoring Only

If you have a custom OpenTelemetry setup and only want to use Sentry for error monitoring, you can skip adding the `SentrySpanProcessor`. You'll still need to add the `SentryContextManager`, `SentryPropagator`, and `SentrySampler` to your setup even if you don't want to send any tracing data to Sentry. Read on to learn why this is needed.

In order for the Sentry SDK to work as expected, and for it to be in sync with OpenTelemetry, we need a few components to be in place.

**Components needed for Sentry to work correctly:**

- **SentryContextManager**: Ensures that the OpenTelemetry context is in sync with Sentry, for example to correctly isolate data between simultaneous requests.
- **SentrySampler**: Ensures that the Sentry `tracesSampleRate` is respected. Even if you don't use Sentry for tracing, you'll still need this in order for trace propagation to work as expected. Read [Using a Custom Sampler](./#using-a-custom-sampler) if you want to use a custom sampler.
- **SentryPropagator**: Ensures that trace propagation works correctly.
- [Required Instrumentation](./#required-instrumentation): Ensures that trace propagation works correctly.

**Additional components needed to also use Sentry for tracing:**

- **SentrySpanProcessor**: Ensures that spans are correctly sent to Sentry.

  Trace propagation is needed for Sentry to automatically connect services
  together. (For example, if you want to connect the frontend and backend, or
  different backend services.) This makes it possible to see related errors
  across services.{" "}
  
    Learn more about Trace Propagation.
  

The following code snippet shows how to set up Sentry for error monitoring only:

## Required Instrumentation

By default, Sentry will register OpenTelemetry instrumentation to automatically capture spans for traces spanning incoming and outgoing HTTP requests, DB queries, and more.

If tracing is not enabled (no `tracesSampleRate` is defined in the SDK configuration), only a minimal amount of OpenTelemetry instrumentation will be registered. This includes the following:

{/* prettier-ignore-start */}

- A Sentry-specific HTTP instrumentation that handles request isolation and trace propagation. This can work in parallel with [@opentelemetry/instrumentation-http](https://www.npmjs.com/package/@opentelemetry/instrumentation-http), if you register it.
- nativeNodeFetchIntegration registers [opentelemetry-instrumentation-fetch-node](https://www.npmjs.com/package/opentelemetry-instrumentation-fetch-node) which is needed for trace propagation.

{/* prettier-ignore-end */}

  
    If tracing is not enabled, performance instrumentations will not be
    registered but they will still be included in the bundle. If you want to
    reduce the bundle size or used dependencies, you can also{" "}
    
      Set up Sentry without Performance Integrations
    
  

These are needed to make sure that trace propagation works correctly.

If you want to add your own http/node-fetch instrumentation, you have to follow the following steps:

### Custom HTTP Instrumentation

_Available since SDK version 8.35.0_

You can add your own `@opentelemetry/instrumentation-http` instance in your OpenTelemetry setup. However, in this case, you need to disable span creation in Sentry's `httpIntegration`:

  ```javascript
  const sentryClient = Sentry.init({
  dsn: "___DSN___",
  skipOpenTelemetrySetup: true,
  integrations: [Sentry.httpIntegration({ spans: false })],
});
  ```

```javascript
  const sentryClient = Sentry.init({
  dsn: "___DSN___",
  skipOpenTelemetrySetup: true,
  integrations: (integrations) =>
  // Also filter out the BunServer integration to avoid emitting duplicated spans from Sentry AND your custom OTel instrumentation
  integrations.filter((i) => i.name !== "BunServer")
});
```

It's important that `httpIntegration` is still registered this way to ensure that the Sentry SDK can correctly isolate requests, for example when capturing errors.

### Custom Node Fetch Instrumentation

If tracing is disabled, the Node Fetch instrumentation will not emit any spans. In this scenario, it will only inject sentry-specific trace propagation headers. You are free to add your own Node Fetch instrumentation on top of this which may emit spans as you like.

## Using a Custom Sampler

While you can use your own sampler, we recommend that you use the `SentrySampler`. This will ensure that the correct subset of traces will be sent to Sentry, based on your `tracesSampleRate`. It will also ensure that all other Sentry features like trace propagation work as expected. If you do need to use your own sampler, make sure to wrap your `SamplingResult` with our `wrapSamplingDecision` method like in the example below:

It is recommended registering your own ESM loader hooks when you have a complete custom OpenTelemetry setup, first and foremost because it makes the most sense architecturally.
You likely went through the effort to set up OpenTelemetry by itself and now you want to add Sentry to your application without messing with your OpenTelemetry setup.

Additionally, there are a few pitfalls that can very simply be avoided by registering your own hooks:

- Registering loader hooks multiple times might result in duplicated spans being created. [More details.](https://github.com/getsentry/sentry-javascript/issues/14065#issuecomment-2435546961)
- OpenTelemetry instrumentation in ESM is very sensitive as to _when_ it is added relative to _when_ the loader hooks are registered.
  The control over this should stay with the owner of the OpenTelemetry setup and not the Sentry SDK.

  
    
      Learn more about ESM installation methods.
    
  

