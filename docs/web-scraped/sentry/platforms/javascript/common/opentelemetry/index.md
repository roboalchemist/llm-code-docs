---
---
title: OpenTelemetry Support
description: "Learn how to use OpenTelemetry with Sentry."
---

The Sentry SDK uses [OpenTelemetry](https://opentelemetry.io/) under the hood. This means that any OpenTelemetry instrumentation that emits spans will automatically be picked up by Sentry without any further configuration.

To start capturing traces and spans, set up Tracing and Performance Monitoring with your Sentry SDK. If you don't use tracing, Sentry still connects to OpenTelemetry under the hood to ensure that context isolation and trace propagation works correctly.

By default, Sentry will automatically set up OpenTelemetry for you, but you can also use your own OpenTelemetry setup. Read the guides below to learn how to use a custom OpenTelemetry setup or how to get the most out of the Sentry and OpenTelemetry integration.

