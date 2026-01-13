# Source: https://docs.datadoghq.com/tracing/trace_collection/library_config/rust.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/compatibility/rust.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/rust.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/rust.md

---
title: Tracing Rust Applications
description: Set up the Datadog Rust SDK to send traces to Datadog.
breadcrumbs: Docs > APM > Application Instrumentation > Tracing Rust Applications
source_url: >-
  https://docs.datadoghq.com/trace_collection/automatic_instrumentation/dd_libraries/rust/index.html
---

# Tracing Rust Applications

{% callout %}
The Datadog Rust SDK is in Preview.
{% /callout %}

{% alert level="info" %}
The Rust SDK does not provide automatic instrumentation. Tracing is achieved by manually instrumenting your application using the OpenTelemetry API.
{% /alert %}

## Overview{% #overview %}

Datadog provides tracing support for Rust applications through the [`datadog-opentelemetry` crate](https://crates.io/crates/datadog-opentelemetry), which is built on the OpenTelemetry (OTel) API and SDK.

To get started, make sure you have [installed and configured the Datadog Agent](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/?tab=datadoglibraries#install-and-configure-the-agent).

## Instrumentation{% #instrumentation %}

The Datadog Rust SDK does not provide automatic instrumentation.

You must manually instrument your application using the OpenTelemetry API. This includes:

- Creating spans for functions or operations.
- Adding attributes (tags) and events to spans.
- Manually propagating trace context for distributed traces.

For examples, see the [Rust Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/rust) documentation.

## Configuration{% #configuration %}

The Rust SDK can be configured using environment variables. For a full list of options, see the [Library Configuration](https://docs.datadoghq.com/tracing/trace_collection/library_config/rust) documentation.

## Compatibility{% #compatibility %}

The Rust SDK requires a Minimum Supported Rust Version (MSRV) and specific OpenTelemetry library versions. For a full list of compatibility requirements, see the [Compatibility Requirements](https://docs.datadoghq.com/tracing/trace_collection/compatibility/rust) page.

## Further reading{% #further-reading %}

- [Source code](https://github.com/DataDog/dd-trace-rs)
- [Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/rust)
