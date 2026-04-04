---
---
title: Legacy OpenTelemetry Integration Support
description: "Using OpenTelemetry with Sentry Performance."
---

We now have a dedicated  OTLPIntegration that can directly ingest OpenTelemetry Traces into Sentry. We recommend moving over to the new setup since it is much simpler.

You can configure your [OpenTelemetry SDK](https://opentelemetry.io/) to send traces and spans to Sentry.

## Install

## Usage

## OpenTelemetry and Sentry

With Sentry’s OpenTelemetry SDK, an OpenTelemetry `Span` becomes a Sentry `Transaction` or `Span`. The first `Span` sent through the Sentry `SpanProcessor` is a `Transaction`, and any child `Span` gets attached to the first `Transaction` upon checking the parent `Span` context. This is true for the OpenTelemetry root `Span` and any top level `Span` in the system. For example, a request sent from frontend to backend will create an OpenTelemetry root `Span` with a corresponding Sentry `Transaction`. The backend request will create a new Sentry `Transaction` for the OpenTelemetry `Span`. The Sentry `Transaction` and `Span` are linked as a trace for navigation and error tracking purposes.

## Additional Configuration

If you need more fine-grained control over Sentry, take a look at the Configuration page. In case you'd like to apply client-side sampling or filter out transactions before sending them to Sentry (to get rid of health checks, for example), you may find the Filtering page helpful.
