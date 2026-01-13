# Source: https://docs.datadoghq.com/tracing/live_debugger.md

---
title: Live Debugger
description: >-
  Debug running applications in real time using non-breaking logpoints that
  collect information without stopping execution or redeploying code.
breadcrumbs: Docs > APM > Live Debugger
source_url: https://docs.datadoghq.com/live_debugger/index.html
---

# Live Debugger

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview

Live Debugger is in Limited Preview. Request access to join the waiting list.To submit questions, feedback, or requests related to Live Debugger, fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSdM9SV4fxrM_OvQ2CtI7CMl7evN0jasFb6X1QiPAbW6dPTQVQ/viewform?usp=header) with details.For time-sensitive issues, contact [Datadog support](https://www.datadoghq.com/support/).

[Request Access](https://www.datadoghq.com/product-preview/live-debugger/)
{% /callout %}

## Overview{% #overview %}

With Live Debugger, you can debug running applications in real time, without redeploying code or interrupting service. Powered by Datadog's [Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/), Live Debugger uses logpointsâauto-expiring, "non-breaking breakpoints"âto collect information from running applications without pausing execution. This makes it ideal for investigating issues in environments where traditional debugging methods aren't practical.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/live_debugger/live-debugger-demo-2025050702.mp4" /%}

## Key capabilities{% #key-capabilities %}

Live Debugger provides:

- **Real-time inspection** of variable states, method arguments, and execution paths in running code.
- **Non-invasive data collection** that captures debugging information without stopping applications or degrading performance.
- **Code instrumentation** with logpoints that can be added anywhere in your code, including third-party libraries.
- **Auto-expiring logpoints** that are automatically deactivated after a set time (default: 48 hours).
- **Conditional logging** based on user-defined criteria to capture data only when specific conditions are met.
- **Built-in [sensitive data scrubbing](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/)** to prevent exposure of personal information, passwords, and secrets.

## Getting started{% #getting-started %}

### Prerequisites{% #prerequisites %}

1. All [Dynamic Instrumentation prerequisites](https://docs.datadoghq.com/dynamic_instrumentation/#prerequisites) are met.
1. You have [created a logs index](https://docs.datadoghq.com/dynamic_instrumentation/#create-a-logs-index) to store debugging information.
1. (Recommended) You have enabled [Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/) to view and select specific code locations when adding logpoints.

### Setup Live Debugger{% #setup-live-debugger %}

Enable and disable Live Debugger on a service using one of the following methods:

#### One-click enablement (recommended){% #one-click-enablement-recommended %}

{% alert level="info" %}
Only users with the following permissions can use one-click enablement: Org Management, APM Remote Configuration Read, APM Remote Configuration Write.
{% /alert %}

1. Select the service and environment on the [Live Debugger Settings](https://app.datadoghq.com/debugging/settings) page.
1. Check that all prerequisites are met as indicated on the Settings page.
1. Click "Enable" or "Disable":
   - "Enable" to allow users to create Debug Sessions on the selected service and environment.
   - "Disable" to deactivate active Debug Sessions and prevent users from creating more.

**Note**: No service restart is required for changes to take effect. Admins and security contacts receive email notifications when services are enabled or disabled.

#### Manual enablement{% #manual-enablement %}

1. Select the service and environment on the [Live Debugger Settings](https://app.datadoghq.com/debugging/settings) page.
1. Follow the instructions to enable Live Debugger.
1. Restart the service before using Live Debugger.

## Live Debugger and Dynamic Instrumentation{% #live-debugger-and-dynamic-instrumentation %}

Due to shared underlying technology, Live Debugger and Dynamic Instrumentation are always enabled or disabled together on the same service and environment.

Like Live Debugger, Dynamic Instrumentation allows users to create logpoints (in addition to supporting other custom instrumentation like spans, span tags, and metrics). However, Live Debugger logpoints expire automatically after a set time period, while Dynamic Instrumentation logpoints remain active until manually deactivated.

When you enable or disable Live Debugger, the same action applies to Dynamic Instrumentation for that service and environment. When disabled, all data capture stops from both active Debug Session logpoints and dynamic instrumentations.

## Using Live Debugger{% #using-live-debugger %}

{% alert level="info" %}
Try using Live Debugger from your JetBrains IDE! [Click here](https://docs.datadoghq.com/developers/ide_plugins/idea/live_debugger/) to learn more.
{% /alert %}

### Creating and using a Debug Session{% #creating-and-using-a-debug-session %}

Debug Sessions let you inspect your code at runtime with auto-expiring logpoints. To create and use a Debug Session:

1. Start a Debug Session from one of the following:
   - On the [Live Debugger page](https://app.datadoghq.com/debugging/sessions), click **Create Debug Session**.
   - (Requires Code Origin feature) In the [Trace Explorer](https://app.datadoghq.com/apm/traces), click on a trace to open the side panel, find the Code Origin section, and click **Start Debug Session**.
1. Add the first logpoint to start the session.
1. Add, remove, and modify logpoints within the session.

Debug Sessions automatically expire after 48 hours. You can manually disable and re-enable both sessions and individual logpoints at any time.

### Creating logpoints{% #creating-logpoints %}

Logpoints are "non-breaking breakpoints" that specify where in the code to capture information, what data to include, and under what conditions. To add a logpoint for debugging:

1. Go to the [Live Debugger page](https://app.datadoghq.com/debugging/sessions).
1. Click **Create Debug Session**.
1. Choose your service, environment, and select where in your code to place the first logpoint.
1. Define a logpoint message template using the [Dynamic Instrumentation expression language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language/).
1. (Optional) Enable "Capture Variables" to collect all execution context (this feature is rate-limited to 1 execution per second).
1. (Optional) Define a condition for when the logs should be emitted.

**Note:** Some feature limitations may apply depending on the service's runtime language. Review the [runtime language-specific documentation](https://docs.datadoghq.com/dynamic_instrumentation/enabling) for more details.

### Protecting sensitive data{% #protecting-sensitive-data %}

Live Debugger data might contain sensitive information, especially when using the "Capture Variables" option. To protect this data:

1. Use the built-in [sensitive data scrubbing](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/) mechanisms.
1. Use [Sensitive Data Scanner](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/#redact-based-on-variable-values-with-sensitive-data-scanner) to identify and redact sensitive information based on regular expressions.

## Impact on performance and billing{% #impact-on-performance-and-billing %}

Enabling Live Debugger and Dynamic Instrumentation on a service does not trigger data capture or impact performance. Data capture only occurs when there are active Debug Sessions or dynamic instrumentations on that service.

**Performance impact**: Datadog's agent-driven instrumentation ensures minimal impact on application performance; sampling logic, rate limits, and built-in budgets prevent runaway data capture.

**Pricing impact**: Logs captured by Datadog are all billed the same way, whether they are generated from Live Debugger or logger lines in your source code. With Live Debugger, the logpoints automatically expire after the set time period, limiting unnecessary data accumulation and costs. Monitor your [Datadog Plan & Usage page](https://app.datadoghq.com/account/billing) for any unexpected increases after utilizing a new feature.

## Limitations{% #limitations %}

The following constraints apply to Live Debugger usage and configuration:

- **Language support:** Live Debugger is available for the same runtime languages as [Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/), including: Java, Python, .NET, PHP (preview), Node.js (preview), Ruby (preview).
- **Configuration scope:** Live Debugger and Dynamic Instrumentation are enabled or disabled together for the same service and environment.
- **Rate limits:**
  - Logpoints with variable capture: Limited to 1 execution per second.
  - Logpoints without variable capture: Limited to 5000 executions per second, per service instance.
- **Session duration:** Debug Sessions automatically expire after 48 hours by default.

## Further Reading{% #further-reading %}

- [Troubleshoot faster with the GitLab Source Code integration in Datadog](https://www.datadoghq.com/blog/gitlab-source-code-integration)
- [Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/)
- [Dynamic Instrumentation Expression Language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language/)
- [Live Debugger for JetBrains IDEs](https://docs.datadoghq.com/developers/ide_plugins/idea/live_debugger/)
- [Sensitive Data Scrubbing](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/)
- [Autocomplete and Search (Preview)](https://docs.datadoghq.com/dynamic_instrumentation/symdb/)
- [Exception Replay](https://docs.datadoghq.com/error_tracking/backend/exception_replay)
