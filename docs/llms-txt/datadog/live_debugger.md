# Source: https://docs.datadoghq.com/tracing/live_debugger.md

---
title: Live Debugger
description: >-
  Debug running applications in real time using non-breaking logpoints that
  collect information without stopping execution or redeploying code.
breadcrumbs: Docs > APM > Live Debugger
---

# Live Debugger

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Live Debugger lets you inspect application behavior in real time, directly in running services, without redeploying code or interrupting execution.

Instead of adding temporary debug logs or reproducing issues locally, you can dynamically capture application state at specific points in the code. This includes variable values, method parameters, and execution context. Live Debugger is well suited for diagnosing issues in production or other long-running environments.

Live Debugger uses logpoints: auto-expiring, non-breaking breakpoints that collect diagnostic data without pausing the application. Since execution continues normally, Live Debugger can be used safely on production systems to investigate problems as they happen.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/live_debugger/live-debugger-demo-2025050702.mp4" /%}

## Key capabilities{% #key-capabilities %}

Live Debugger provides:

- **Real-time inspection** of variable values, method arguments, and execution context in running code.
- **Safe, non-invasive data capture** that collects debugging information without pausing applications or requiring redeploys.
- **Dynamic logpoint placement** anywhere in your codebase, including in third-party libraries.
- **Auto-expiring logpoints** that deactivate automatically after a configurable duration.
- **Conditional data capture** based on user-defined expressions, so information is collected only when specific conditions are met.
- **Built-in [sensitive data scrubbing](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/)** to help prevent exposure of personal data, secrets, and credentials.

## Requirements and setup{% #requirements-and-setup %}

Live Debugger supports Python, Java, .NET, Ruby, Node.js, PHP, and Go. It requires the [Datadog Agent](https://docs.datadoghq.com/agent/), an [APM-instrumented application](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/), and [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config). You can enable it for an individual service either in-app, or by setting an environment variable.

The enablement method depends on your tracer version, see the table below for details.

| By Service(In-App)          | By Service(Env Var)                                                                                                                                                                                                                                                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **How to Enable**           | Settings page                                                                                                                                                                                                                                                                                                                                                 | Environment variables                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Agent Version**           | v7.49.0+                                                                                                                                                                                                                                                                                                                                                      | v7.49.0+                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Minimum Tracer Versions** | [Python](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/python/) â¥ 3.10.0[Java](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/java/) â¥ 1.48.0[.NET](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/dotnet-core) â¥ 3.29.0 | [Python](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/python/) â¥ 2.2.0[Java](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/java/) â¥ 1.34.0[.NET](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/dotnet-core) â¥ 2.54.0[Node.js](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/nodejs/) â¥ 5.39.0[Ruby](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/ruby/) â¥ 2.24.0[PHP](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/php) â¥ 1.5.0[Go](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/go) â¥ 2.2.3 (or 1.74.6) |

To enable Live Debugger in-app, navigate to the Live Debugger **Settings** page, select the desired service, and toggle it to **Enabled**.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/live_debugger/live_debugger_enablement.mp4" /%}

If in-app enablement isn't available, follow the instructions below for your target language:

- [Java](https://docs.datadoghq.com/dynamic_instrumentation/enabling/java)
- [Python](https://docs.datadoghq.com/dynamic_instrumentation/enabling/python)
- [Dotnet](https://docs.datadoghq.com/dynamic_instrumentation/enabling/dotnet)
- [Dotnet](https://docs.datadoghq.com/dynamic_instrumentation/enabling/dotnet)
- [Node.js](https://docs.datadoghq.com/dynamic_instrumentation/enabling/nodejs)
- [Ruby](https://docs.datadoghq.com/dynamic_instrumentation/enabling/ruby)
- [PHP](https://docs.datadoghq.com/dynamic_instrumentation/enabling/php)
- [Go](https://docs.datadoghq.com/dynamic_instrumentation/enabling/go)

{% alert level="info" %}
Why DI instructions? Live Debugger is built on [Dynamic Instrumentation (DI)](https://docs.datadoghq.com/tracing/dynamic_instrumentation/), so its setup instructions and limitations also apply here.
{% /alert %}

### Permissions{% #permissions %}

The following permissions are required to use Live Debugger:

- **Dynamic Instrumentation Read Configuration** (`debugger_read`) - Required to access the Live Debugger page.
- One of the following write permissions:
  - **Dynamic Instrumentation Write Configuration** (`debugger_write`) - Required to create or modify debug logs in any environment.
  - **Dynamic Instrumentation Write Pre-Prod** (`debugger_write_preprod`) - Required to create or modify debug logs in known pre-production environments only (such as staging or QA).
- **Dynamic Instrumentation Capture Variables** (`debugger_capture_variables`) - Required to use the **Capture method parameters and local variables** option.

For more information about roles and how to assign roles to users, see [Role Based Access Control](https://docs.datadoghq.com/account_management/rbac/permissions#apm).

### Create a logs index{% #create-a-logs-index %}

Live Debugger generates logs that are sent to Datadog and appear alongside your application logs.

If you use [Exclusion filters](https://docs.datadoghq.com/logs/log_configuration/indexes/#exclusion-filters), make sure Live Debugger logs are not filtered:

1. Create a logs index and [configure it](https://docs.datadoghq.com/logs/log_configuration/indexes/#add-indexes) to the desired retention with **no sampling**.
1. Set the filter to match on the `source:dd_debugger` tag. All Dynamic Instrumentation logs have this source.
1. Make sure the new index takes precedence over any other with filters that match that tag, because the first match wins.

### Link your source code{% #link-your-source-code %}

If you enable the Datadog Source Code Integration, you can debug code directly through Live Debugger.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/live_debugger/live_debugger_code_viewer.126301475f481ff16a82d78f6320ad1a.png?auto=format"
   alt="Live Debugger with Source Code Integration enabled showing code viewer" /%}

## Using Live Debugger{% #using-live-debugger %}

{% alert level="info" %}
Rather debug in your IDE? Try using Live Debugger directly from JetBrains! [Click here](https://docs.datadoghq.com/developers/ide_plugins/idea/live_debugger/) to learn more.
{% /alert %}

### Creating and using a Debug Session{% #creating-and-using-a-debug-session %}

A Debug Session lets you inspect running code using auto-expiring logpoints. To create and use a Debug Session:

1. Start a Debug Session from one of the following locations:
   - On the [Live Debugger page](https://app.datadoghq.com/debugging/sessions), click **Create Debug Session**.
   - (Requires the [Code Origin](https://docs.datadoghq.com/tracing/code_origin) feature) In the [Trace Explorer](https://app.datadoghq.com/apm/traces), open a trace, locate the Code Origin section in the side panel, and click **Start Debug Session**.
1. Add a logpoint to begin collecting diagnostic data.
1. Add, remove, or modify logpoints as needed during the session.

Debug Sessions expire automatically. You can also manually disable or re-enable a session, as well as individual logpoints, at any time.

### Creating logpoints{% #creating-logpoints %}

Logpoints are "non-breaking breakpoints" that specify where in the code to capture information, what data to include, and under what conditions. To add a logpoint for debugging:

1. Go to the [Live Debugger page](https://app.datadoghq.com/debugging/sessions).
1. Click **Create Debug Session**.
1. Choose your service, environment, and select where in your code to place the first logpoint.
1. Define a logpoint message template using the [expression language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language/).
1. (Optional) Enable "Capture Variables" to collect all execution context (this feature is rate-limited to 1 execution per second).
1. (Optional) Define a condition for when the logs should be emitted.

**Note:** Some feature limitations may apply depending on the service's runtime language. Review the [runtime language-specific documentation](https://docs.datadoghq.com/dynamic_instrumentation/enabling) for more details.

### Protecting sensitive data{% #protecting-sensitive-data %}

Live Debugger data might contain sensitive information, especially when using the "Capture Variables" option. To protect this data:

1. Use the built-in [sensitive data scrubbing](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/) mechanisms.
1. Use [Sensitive Data Scanner](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/#redact-based-on-variable-values-with-sensitive-data-scanner) to identify and redact sensitive information based on regular expressions.

## Impact on performance and billing{% #impact-on-performance-and-billing %}

Enabling Live Debugger on a service does not trigger data capture or impact performance. Data capture only occurs when there are active Debug Sessions on that service.

**Performance impact**: Datadog's agent-driven instrumentation ensures minimal impact on application performance; sampling logic, rate limits, and built-in budgets prevent runaway data capture.

**Pricing impact**: Logs captured by Datadog are all billed the same way. This applies whether they are generated from Live Debugger or logger lines in your source code. With Live Debugger, the logpoints automatically expire after the set time period, limiting unnecessary data accumulation and costs. Monitor your [Datadog Plan & Usage page](https://app.datadoghq.com/account/billing) for any unexpected increases after utilizing a new feature.

## Limitations{% #limitations %}

The following constraints apply to Live Debugger usage and configuration:

- **Configuration scope:** Live Debugger and Dynamic Instrumentation are enabled or disabled together for the same service and environment.
- **Rate limits:**
  - Logpoints with variable capture: Limited to 1 execution per second.
  - Logpoints without variable capture: Limited to 5000 executions per second, per service instance.

## Further Reading{% #further-reading %}

- [Troubleshoot faster with the GitLab Source Code integration in Datadog](https://www.datadoghq.com/blog/gitlab-source-code-integration)
- [Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/)
- [Dynamic Instrumentation Expression Language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language/)
- [Live Debugger for JetBrains IDEs](https://docs.datadoghq.com/developers/ide_plugins/idea/live_debugger/)
- [Sensitive Data Scrubbing](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/)
- [Autocomplete and Search](https://docs.datadoghq.com/dynamic_instrumentation/symdb/)
- [Exception Replay](https://docs.datadoghq.com/error_tracking/backend/exception_replay)
