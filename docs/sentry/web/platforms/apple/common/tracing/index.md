---
---
title: Set Up Tracing
description: "Learn how to enable tracing in your app and get valuable performance insights about your application."
---

With [tracing](/product/insights/overview/), Sentry tracks your software performance, measuring metrics like throughput and latency, and displaying the impact of errors across multiple systems. Sentry captures distributed traces consisting of transactions and spans, which measure individual services and individual operations within those services. Learn more about our model in [Distributed Tracing](/product/sentry-basics/tracing/distributed-tracing/).

Automatic instrumentation for monitoring the performance of your application is currently in preview. You can also use custom instrumentation to capture transactions.

## Configure

First, enable tracing and configure the sample rate for transactions. Set the sample rate for your transactions by either:

- Setting a uniform sample rate for all transactions using the  option in your SDK config to a number between `0` and `1`. (For example, to send 20% of transactions, set  to `0.2`.)
- Controlling the sample rate based on the transaction itself and the context in which it's captured, by providing a function to the  config option.

The two options are meant to be mutually exclusive. If you set both,  will take precedence.

Learn more about tracing options, how to use the tracesSampler function, or how to sample transactions.

## Verify

Verify that tracing is working correctly by using our automatic instrumentation or by starting and finishing a transaction using custom instrumentation.

Test out tracing by starting and finishing a transaction, which you _must_ do so transactions can be sent to Sentry. Learn how in our Custom Instrumentation content.

While you're testing, set  to `1.0`, as that ensures that every transaction will be sent to Sentry. Once testing is complete, you may want to set a lower  value, or switch to using  to selectively sample and filter your transactions, based on contextual data.

## Next Steps

