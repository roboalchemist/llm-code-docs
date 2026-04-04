# Source: https://docs.datadoghq.com/error_tracking/backend/exception_replay.md

# Source: https://docs.datadoghq.com/tracing/error_tracking/exception_replay.md

---
title: Exception Replay in Error Tracking
description: Learn about Exception Replay in APM Error Tracking.
breadcrumbs: >-
  Docs > APM > Error Tracking for Backend Services > Exception Replay in Error
  Tracking
---

# Exception Replay in Error Tracking

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="info" %}
Exception Replay is generally available for Python, Java, .NET, PHP, and is enabled by default when supported.
{% /alert %}

## Overview{% #overview %}

Exception Replay captures execution context and local variable values when an exception occurs, helping you diagnose, reproduce, and resolve issues faster. It records the surrounding state, including the stack trace and variable snapshots, then surfaces this data directly in Error Tracking alongside the rest of the issue details.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/error_tracking/error_tracking_executional_context-3.d6c8b6d269fe29196ad7854101a73e67.png?auto=format"
   alt="Error Tracking Explorer Exception Replay" /%}

Exception Replay is designed for production use. Snapshots are rate-limited, and sensitive data is automatically redacted. When enabled, it waits for exceptions in an application and captures snapshots of the stack trace and local variables before forwarding them to Datadog.

{% alert level="info" %}
What products are supported? Exception Replay is available only for APM-based exceptions and does not support errors from Logs or RUM.
{% /alert %}

## Requirements & Setup{% #requirements--setup %}

Exception Replay supports Python, Java, .NET, and PHP, and captures only APM-based exceptions. It requires the [Datadog Agent](https://docs.datadoghq.com/agent/) and an [APM-instrumented application](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/). You can enable it for an entire environment, an individual service in-app, or a specific service using environment variables.

The enablement method depends on your tracer version and whether [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config) is available. See the table below for details.

| By Environment(Bulk)               | By Service(In-App)                                                                                                                                                                                                                                                                                                                                            | By Service(Env Var)                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **How to Enable**                  | Enabled by default                                                                                                                                                                                                                                                                                                                                            | Settings page                                                                                                                                                                                                                                                                                                                                                 | Environment variables                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Agent Version**                  | v7.49.0+                                                                                                                                                                                                                                                                                                                                                      | v7.49.0+                                                                                                                                                                                                                                                                                                                                                      | v7.49.0+                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Minimum Tracer Versions**        | [Python](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/python/) â¥ 3.15.0[Java](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/java/) â¥ 1.54.0[.NET](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/dotnet-core) â¥ 3.29.0 | [Python](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/python/) â¥ 3.10.0[Java](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/java/) â¥ 1.48.0[.NET](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/dotnet-core) â¥ 3.29.0 | [Python](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/python/) â¥ 1.16.0[Java](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/java/) â¥ 1.47.0[.NET](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/dotnet-core) â¥ 2.53.0[PHP](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/php) â¥ 1.12.1 |
| **Remote Configuration Required?** | Yes                                                                                                                                                                                                                                                                                                                                                           | Yes                                                                                                                                                                                                                                                                                                                                                           | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

To enable Exception Replay in-app, navigate to the Exception Replay **Settings** page in Error Tracking, select the desired environment or service, and toggle it to **Enabled**.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/error_tracking/error_tracking_exception_replay_enablement.mp4" /%}

If in-app enablement isn't available, set the environment variable:

```bash
DD_EXCEPTION_REPLAY_ENABLED=true
```

This can also be used to override in-app configuration and takes precedence when both are set.

### Create a logs index for Exception Replay snapshots{% #create-a-logs-index-for-exception-replay-snapshots %}

Create a logs index dedicated to Exception Replay snapshots and configure it with the desired retention and no sampling.

- Set the filter to match `source:dd_debugger`.
- Ensure the index takes precedence over other indexes matching this tag (the first match wins).

{% alert level="info" %}
Why create a logs index? Exception Replay snapshots are emitted as logs enriched with links back to the originating APM spans.
{% /alert %}

### Link your source code{% #link-your-source-code %}

If you enable the Datadog Source Code Integration, you can see code previews directly inside your Error Tracking stack traces. When Exception Replay snapshots are captured, you can hover over variable names in the code preview to view their captured values.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/error_tracking/error_tracking_exception_replay_sci.mp4" /%}

## Sensitive data redaction{% #sensitive-data-redaction %}

Exception Replay applies automatic mode- and identifier-based redaction to ensure sensitive data is protected before snapshots becomes available.

### Mode-based redaction{% #mode-based-redaction %}

Exception Replay has two redaction modes:

- **Strict Mode:** Redacts all values except numbers and Booleans.
- **Targeted Mode:** Redacts known sensitive patterns such as credit card numbers, API keys, IPs, and other PII.

These redaction modes cannot be disabled, only switched, and Targeted Mode is applied automatically in common pre-production environments like `staging` or `preprod`.

### Identifier-based redaction{% #identifier-based-redaction %}

Variable values associated with [common sensitive identifiers](https://github.com/DataDog/dd-trace-py/blob/main/ddtrace/debugging/_redaction.py) (for example, `password`, `accessToken`, and similar terms) are scrubbed before snapshots leave the host. Additional language-specific redaction rules are built into each tracer (for example, the Python tracer maintains a list of default sensitive identifiers).

You can extend redaction behavior through:

- Custom identifier-based redaction
- Class/type-based redaction rules
- Sensitive Data Scanner rules

See the [Dynamic Instrumentation Sensitive Data Scrubbing instructions](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/) and [Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner/) documentation for configuration details.

{% alert level="info" %}
Why DI instructions? Exception Replay is built on [Dynamic Instrumentation (DI)](https://docs.datadoghq.com/tracing/dynamic_instrumentation/), so its sensitive data scrubbing configuration options also apply here.
{% /alert %}

## Troubleshooting{% #troubleshooting %}

### Missing variable values{% #missing-variable-values %}

Exception Replay snapshots are rate-limited to **one snapshot per exception type per instance per hour**. In some runtimes, a snapshot is only captured after the **second occurrence** for a given exception.

### Additional reasons a snapshot may not appear{% #additional-reasons-a-snapshot-may-not-appear %}

- Exception Replay not enabled
- Snapshot occurred outside selected time window
- Third-party package exclusions (use `DD_THIRD_PARTY_DETECTION_EXCLUDES` to include these)
- Logs with `source:dd_debugger` missing due to [Log Index](https://app.datadoghq.com/logs/pipelines/indexes) retention settings or [Exclusion Filters](https://docs.datadoghq.com/logs/log_configuration/indexes/#exclusion-filters) in preceding indexes
- Exception Replay is not available in the FedRAMP region

Use the query `@error.debug_info_captured:true` in Error Tracking Explorer to find errors with Exception Replay snapshots.

## Further Reading{% #further-reading %}

- [Simplify production debugging with Datadog Exception Replay](https://www.datadoghq.com/blog/exception-replay-datadog/)
- [Learn about Datadog Live Debugger](https://docs.datadoghq.com/tracing/live_debugger)
- [Learn about Error Tracking Monitors](https://docs.datadoghq.com/error_tracking/monitors)
- [Learn about Error Tracking for APM Backend Services](https://docs.datadoghq.com/tracing/error_tracking)
