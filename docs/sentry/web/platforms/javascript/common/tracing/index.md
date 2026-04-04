---
---
title: Set Up Tracing
description: "Learn how to enable tracing in your app."
---

With [tracing](/product/insights/overview/), Sentry automatically tracks your software performance across your application services, measuring metrics like throughput and latency, and displaying the impact of errors across multiple systems.

  
    If you’re adopting Tracing in a high-throughput environment, we recommend testing prior to deployment to ensure that your service’s performance characteristics maintain expectations.
  

  
    
      Sentry can integrate with <strong>OpenTelemetry</strong>. You can find more
      information about it
      here.
    
  

## Enable Tracing

## Configure

  Enable tracing by configuring the sampling rate for traces. Set the sample
  rate as follows:

  Enable tracing by setting the sample rate for your traces.

- You can establish a uniform sample rate for all transactions by setting the  option in your SDK config to a number between `0` and `1`. (For example, to send 20% of transactions, set  to `0.2`.)
- For more granular control over sampling, you can set the sample rate based on the transaction itself and the context in which it's captured, by providing a function to the  config option.

The two options are mutually exclusive. If both are set,  will take precedence.

You can find more in-depth explanations and examples about sampling configuration in [Configure Sampling](./configure-sampling).

## Distributed Tracing

Sentry captures distributed traces consisting of transactions and spans, which measure individual services and individual operations within those services, respectively. Learn more about our model in [Distributed Tracing](/product/sentry-basics/tracing/distributed-tracing/).

## Verify

Verify that tracing is working correctly by using our automatic instrumentation or by starting and finishing a transaction using custom instrumentation.

While you're testing, set  to `1.0`, as that ensures that every transaction will be sent to Sentry. Once testing is complete, you may want to set a lower  value, or switch to using  to selectively sample and filter your transactions, based on contextual data.

If you leave your sample rate at `1.0`, a transaction will be sent every time a user loads a page or navigates within your app. Depending on the amount of traffic your application gets, this may mean a lot of transactions. If you have a high-load, backend application, you may want to consider setting a lower  value, or switching to using  to selectively sample and filter your transactions, based on contextual data.

  ## Automatic Instrumentation

See Automatic Instrumentation to learn about all the things that the SDK automatically instruments for you.

## Custom Instrumentation

You can also manually start spans to instrument specific parts of your code. This is useful when you want to measure the performance of a specific operation or function.

- Tracing APIs: Find
  information about APIs for custom tracing instrumentation
- Instrumentation:
  Find information about manual instrumentation with the Sentry SDK
- Sending Span Metrics:
  Learn how to capture metrics on your spans

## Disabling Tracing

If you want to disable tracing, you _should not_ set `tracesSampleRate` at
all. Setting it to `0` will not disable tracing, it will simply never send any
traces to Sentry.
Instead, neither `tracesSampleRate` nor `tracesSampler` should be defined in your SDK config to fully disable tracing.

  In addition, you can set `__SENTRY_TRACING__` to `false` to ensure the tracing code
  is removed from your production build. This will result in{" "}
  trace propagation{" "}
  being disabled as well. See{" "}
  Tree Shaking{" "}
  for more information.

## Next Steps

