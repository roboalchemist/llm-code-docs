# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation.md

---
title: Code-Based Custom Instrumentation
description: >-
  Add custom spans, tags, and instrumentation to capture application-specific
  observability data using Datadog APIs and OpenTelemetry.
breadcrumbs: Docs > APM > Application Instrumentation > Code-Based Custom Instrumentation
---

# Code-Based Custom Instrumentation

## Overview{% #overview %}

Code-based custom instrumentation allows for precise monitoring of specific components in your application. It allows you to capture observability data from in-house code or complex functions that aren't captured by automatic instrumentation. Automatic instrumentation includes [Single Step Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/single-step-apm) or using [Datadog tracing libraries](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/).

Code-based custom instrumentation involves embedding tracing code directly into your application code. This allows for the programmatic creation, modification, or deletion of traces to send to Datadog.

{% alert level="info" %}
To add custom instrumentation at specific application code locations from the Datadog UI, without code changes, see [Dynamic Instrumentation](https://docs.datadoghq.com/tracing/dynamic_instrumentation/).
{% /alert %}

## Getting started{% #getting-started %}

Before you begin, make sure you've already [installed and configured the Agent](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/?tab=datadoglibraries#install-and-configure-the-agent).

Follow the relevant documentation for your custom instrumentation approach to learn more:

{% tab title="OpenTelemetry API (Recommended)" %}
Datadog tracing libraries provide an implementation of the OpenTelemetry API for instrumenting your code. This means you can maintain vendor-neutral instrumentation of all your services, while still taking advantage of Datadog's native implementation, features, and products. You can configure it to generate Datadog-style spans and traces to be processed by the Datadog tracing library for your language, and send those to Datadog.

- [Java](otel_instrumentation/java)
- [Python](otel_instrumentation/python)
- [Ruby](otel_instrumentation/ruby)
- [go](otel_instrumentation/go)
- [Node.js](otel_instrumentation/nodejs)
- [PHP](otel_instrumentation/php)
- [.Net](otel_instrumentation/dotnet)
- [iOS](otel_instrumentation/ios)
- [Android](android/otel)
- [Rust](rust/)

{% /tab %}

{% tab title="Datadog API" %}
Use the Datadog API to add custom instrumentation that allows you to programmatically create, modify, or delete traces to send to Datadog. This is useful for tracing in-house code not captured by automatic instrumentation, removing unwanted spans from traces, and for providing deeper visibility and context into spans, including adding span tags.

- [Java](dd_libraries/java)
- [Python](dd_libraries/python)
- [Ruby](dd_libraries/ruby)
- [go](dd_libraries/go)
- [Node.js](dd_libraries/nodejs)
- [PHP](dd_libraries/php)
- [C++](dd_libraries/cpp)
- [.Net](dd_libraries/dotnet)
- [Android](android/otel)

{% /tab %}

{% tab title="OpenTracing (Legacy)" %}
If [OpenTelemetry](https://docs.datadoghq.com/tracing/trace_collection/otel_instrumentation/) or [`ddtrace`](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/) custom instrumentation doesn't work for you, each of the supported languages also has support for sending [OpenTracing](https://opentracing.io/docs/) data to Datadog. OpenTracing is archived and the project is unsupported.

- [Java](opentracing/java)
- [Python](opentracing/python)
- [Node.js](opentracing/nodejs)
- [Ruby](opentracing/ruby)
- [.Net](opentracing/dotnet)
- [PHP](opentracing/php)
- [Android](opentracing/android)

{% /tab %}

## Further reading{% #further-reading %}

- [Instrument a custom method to get deep visibility into your business logic](https://docs.datadoghq.com/tracing/guide/instrument_custom_method)
- [Connect your Logs and Traces together](https://docs.datadoghq.com/tracing/connect_logs_and_traces)
- [Explore your services, resources, and traces](https://docs.datadoghq.com/tracing/visualization/)
- [Learn More about Datadog and the OpenTelemetry initiative](https://www.datadoghq.com/blog/opentelemetry-instrumentation/)
