---
---
title: Set Up Tracing in PHP
description: "Learn how to set up and enable tracing in your PHP app and discover valuable performance insights of your application."
---

With [tracing](/product/insights/overview/), Sentry tracks your software performance, measuring metrics like throughput and latency, and displaying the impact of errors across multiple systems. Sentry captures distributed traces consisting of transactions and spans, which measure individual services and individual operations within those services. Learn more about our model in [Distributed Tracing](/product/sentry-basics/tracing/distributed-tracing/).

If you’re adopting Tracing in a high-throughput environment, we recommend testing prior to deployment to ensure that your service’s performance characteristics maintain expectations.

## Configure

First, enable tracing and configure the sample rate for transactions. Set the sample rate for your transactions by either:

- Setting a uniform sample rate for all transactions using the  option in your SDK config to a number between `0` and `1`. (For example, to send 20% of transactions, set  to `0.2`.)
- Controlling the sample rate based on the transaction itself and the context in which it's captured, by providing a function to the  config option.

The two options are meant to be mutually exclusive. If you set both,  will take precedence.

Learn more about tracing options, how to use the traces_sampler function, or how to sample transactions.

## Verify

While you're testing, set  to `1.0`, as that ensures that every transaction will be sent to Sentry. Once testing is complete, you may want to set a lower  value or switch to using  to selectively sample and filter your transactions, based on contextual data.

## Improve Response Time

Response time is somewhat impacted when you use the performance capabilities in your PHP application, (depending on the `traces_sample_rate` you've configured).

Doing this will make the PHP process send requests to your local Relay, which will then forward them to Sentry, instead of sending requests to Sentry directly.

To begin using [Relay](/product/relay/), check out our docs for [getting started](/product/relay/getting-started/).
We recommend using Relay in `managed` mode (which is the default).

Follow the instructions in the Relay docs to send a test event through Relay to Sentry.
Don't forget to update your `DSN` to point to your running Relay instance.
After you set up Relay, you should see a dramatic improvement to the impact on your server.

## Next Steps

