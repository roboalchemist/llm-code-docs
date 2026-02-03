# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation.md

---
title: Dynamic Instrumentation
description: >-
  Add instrumentation to your running production systems without restarts to
  collect logs, metrics, spans, and tags from any location in your code.
breadcrumbs: Docs > APM > Application Instrumentation > Dynamic Instrumentation
---

# Dynamic Instrumentation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Dynamic Instrumentation allows you to add instrumentation into your running production systems without any restarts and at any location in your application's code, including third-party libraries. You can add or modify telemetry for logs, metrics, spans, and corresponding tagging, from the Datadog UI. Dynamic Instrumentation has low overhead and has no side effects on your system.

If you are interested in trying out the latest user experience improvements for Dynamic Instrumentation, consider opting into the [autocomplete and search Preview](https://docs.datadoghq.com/dynamic_instrumentation/symdb/).

## Getting started{% #getting-started %}

### Prerequisites{% #prerequisites %}

Dynamic Instrumentation requires the following:

- [Datadog Agent](https://docs.datadoghq.com/agent/) 7.49.0 or higher (7.73.0+ for Go) is installed alongside your service.
- [Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config) is enabled in that Agent.
- For Java applications, tracing library [`dd-trace-java`](https://github.com/DataDog/dd-trace-java) 1.34.0 or higher.
- For Python applications, tracing library [`dd-trace-py`](https://github.com/DataDog/dd-trace-py) 2.2.0 or higher.
- For .NET applications, tracing library [`dd-trace-dotnet`](https://github.com/DataDog/dd-trace-dotnet) 2.54.0 or higher.
- For Node.js applications, tracing library [`dd-trace-js`](https://github.com/DataDog/dd-trace-js) 5.39.0 or higher.
- (Limited Preview) For Ruby applications, tracing library [`dd-trace-rb`](https://github.com/DataDog/dd-trace-rb) 2.9.0 or higher.
- (Limited Preview) For PHP applications, tracing library [`dd-trace-php`](https://github.com/DataDog/dd-trace-php) 1.5.0 or higher.
- (Limited Preview) For Go applications, tracing library [`dd-trace-go`](https://github.com/DataDog/dd-trace-go) >=1.74.6 (major version 1), or >=2.2.3 (major version 2).
- (Limited Preview) For Go applications, the Agent and your application must run on the same host, with Linux kernel >=5.17.
- [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) tags `service`, `env`, and `version` are applied to your deployment.
- Recommended, [autocomplete and search (in Preview)](https://docs.datadoghq.com/dynamic_instrumentation/symdb/) is enabled.
- Recommended, [Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/) is set up for your service.

### Permissions{% #permissions %}

The following permissions are required to use Dynamic Instrumentation:

- **Dynamic Instrumentation Read Configuration** (`debugger_read`) - Required to access the Dynamic Instrumentation page.
- One of the following write permissions:
  - **Dynamic Instrumentation Write Configuration** (`debugger_write`) - Required to create or modify instrumentations in any environment.
  - **Dynamic Instrumentation Write Pre-Prod** (`debugger_write_preprod`) - Required to create or modify instrumentations in known pre-production environments only (such as staging or QA).
- **Dynamic Instrumentation Capture Variables** (`debugger_capture_variables`) - Required to use the **Capture method parameters and local variables** option.

For more information about roles and how to assign roles to users, see [Role Based Access Control](https://docs.datadoghq.com/account_management/rbac/permissions#apm).

### Create a logs index{% #create-a-logs-index %}

Dynamic Instrumentation creates "dynamic logs" that are sent to Datadog and appear alongside your regular application logs.

If you use [Exclusion filters](https://docs.datadoghq.com/logs/log_configuration/indexes/#exclusion-filters), ensure Dynamic Instrumentation logs are not filtered:

1. Create a logs index and [configure it](https://docs.datadoghq.com/logs/log_configuration/indexes/#add-indexes) to the desired retention with **no sampling**.
1. Set the filter to match on the `source:dd_debugger` tag. All Dynamic Instrumentation logs have this source.
1. Ensure that the new index takes precedence over any other with filters that match that tag, because the first match wins.

### Enable Dynamic Instrumentation{% #enable-dynamic-instrumentation %}

To enable Dynamic Instrumentation on a service, go to the [in-app setup page](https://app.datadoghq.com/dynamic-instrumentation/setup).

For more detailed instructions, select your runtime below:

- [Java](https://docs.datadoghq.com/dynamic_instrumentation/enabling/java)
- [Python](https://docs.datadoghq.com/dynamic_instrumentation/enabling/python)
- [Dotnet](https://docs.datadoghq.com/dynamic_instrumentation/enabling/dotnet)
- [Dotnet](https://docs.datadoghq.com/dynamic_instrumentation/enabling/dotnet)
- [Node.js](https://docs.datadoghq.com/dynamic_instrumentation/enabling/nodejs)
- [Ruby](https://docs.datadoghq.com/dynamic_instrumentation/enabling/ruby)
- [PHP](https://docs.datadoghq.com/dynamic_instrumentation/enabling/php)
- [Go](https://docs.datadoghq.com/dynamic_instrumentation/enabling/go)

### Limitations{% #limitations %}

- Dynamic Instrumentation is not yet compatible with Azure App Services or serverless environments.
- Full support is available for applications built with Python, Java, .NET, and Node.js.
- Limited previews are ongoing for applications built with Ruby and PHP.
- The Java tracer library does not support Kotlin coroutines.

## Explore Dynamic Instrumentation{% #explore-dynamic-instrumentation %}

Dynamic Instrumentation can help you understand what your application is doing at runtime. By adding a Dynamic Instrumentation probe you are exporting additional data from your application, without the need to change code or redeploy it.

### Using probes{% #using-probes %}

A probe allows you to collect data from specific points in your code without halting the execution of the program.

Think of using probes as enhancing your observability by adding dynamic logs, metrics, and spans to a running application without needing to change code, deploy it, or restart a service. You can gather data immediately without disturbing the user experience or requiring lengthy deployments.

As a developer, you can also think of a probe as a "non-breaking breakpoint". In traditional debugging, a breakpoint is a point in the program where the execution stops, allowing the developer to inspect the state of the program at that point. However, in real-world production environments, it's not practical or even possible to stop the execution of the program. Probes fill in this gap by allowing you to inspect variable state in production environments in a non-intrusive way.

### Creating a probe{% #creating-a-probe %}

All probe types require the same initial setup:

1. Go to the [Dynamic Instrumentation page](https://app.datadoghq.com/dynamic-instrumentation).
1. Click **Create Probe** in the top right, or click the three-dot menu on a service and select **Add a probe for this service**.
1. If they are not prefilled, choose service, runtime, environment, and version.
1. In the source code, specify where to set the probe by selecting either a class and method or a source file and line. If you opted into the [autocomplete and search Preview](https://docs.datadoghq.com/dynamic_instrumentation/symdb/), autocomplete shows suggestions for selecting a class or method.

See the individual probe types below for specific creation steps for each probe type.

Alternatively, you can create a probe from these other contexts:

{% dl %}

{% dt %}
Profiling
{% /dt %}

{% dd %}
On a profiler flame graph, you can create a probe for a method by selecting **Instrument this frame with a probe** from the frame's context menu.
{% /dd %}

{% dt %}
Error Tracking
{% /dt %}

{% dd %}
On a stack trace, mouse over a stack frame and click **Instrument**. This prefills the probe creation form with the Issue context.
{% /dd %}

{% /dl %}

### Creating log probes{% #creating-log-probes %}

A *log probe* emits a log when it executes.

To create a log probe:

1. Select **Log** as the probe type.
1. Complete the generic probe setup (choose service, environment, version, and probe location).
1. Define a log message template. You can use the Dynamic Instrumentation expression language to reference values from the execution context.
1. (In Preview) Optionally enable extra data capturing from the probe.
1. Optionally define a condition using the Dynamic Instrumentation expression language. The log is emitted when the expression evaluates to true.

Log probes are enabled by default on all service instances that match the specified environment and version. They are rate-limited to execute at most 5000 times per second, on each instance of your service.

You must set a log message template on every log probe. The template supports embedding [expressions](https://docs.datadoghq.com/dynamic_instrumentation/expression-language) inside curly brackets. For example: `User {user.id} purchased {count(products)} products`.

You can also set a condition on a log probe using the [expression language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language). The expression must evaluate to a Boolean. The probe executes if the expression is true, and does not capture or emit any data if the expression is false.

{% image
   source="https://datadog-docs.imgix.net/images/dynamic_instrumentation/log_probe.c3d31d71c4fa78762921a9fbdba464a1.png?auto=format"
   alt="Creating a Dynamic Instrumentation log probe" /%}

(In Preview) If you enable **Capture method parameters and local variables** on the log probe, all execution context is added the log event:

- **Method arguments**, **local variables**, and **fields**, with the following default limits:
  - Follow references three levels deep (configurable in the UI).
  - The first 100 items inside collections.
  - The first 255 characters for string values.
  - 20 fields inside objects. Static fields are not collected.
- Call **stack trace**.
- Caught and uncaught **exceptions**.

Probes with this setting enabled are rate-limited to one hit per second.

{% alert level="info" %}
**Warning: The captured data may contain sensitive information, including personal data, passwords, and secrets such as AWS keys.**

To ensure this information is properly redacted:

- Datadog Dynamic Instrumentation employs several techniques to redact sensitive information. To learn more about the default mechanisms or how to extend the it to meet your needs, read [Sensitive Data Scrubbing](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/).
- Turn off the **Capture method parameters and local variables** option and explicitly select the variables you want to include in the log message template. Doing so ensures that log probes contain only data related to the variables that you specifically identify, thus reducing the risk of unintentional sensitive data leaks.
- If you are the Administrator of your Datadog account and would like to prevent other users from being able to use the **Capture method parameters and local variables** option, you can revoke their Dynamic Instrumentation Capture Variables (`debugger_capture_variables`) permission.



Alternatively, if you need to log this data but want to mitigate the risk associated with it being accessible in the Datadog product, you can limit which users in your organization can view the captured data by setting up a [Restriction query](https://docs.datadoghq.com/logs/guide/logs-rbac/?tab=ui#restrict-access-to-logs) on `source:dd_debugger`.
{% /alert %}

### Creating metric probes{% #creating-metric-probes %}

A *metric probe* emits a metric when it executes.

To create a metric probe:

1. Select **Metric** as the probe type.
1. Complete the generic probe setup (choose service, environment, version, and probe location).
1. Specify a name for the metric, which will be prefixed with `dynamic.instrumentation.metric.probe.`.
1. Select a metric type (count, gauge, or histogram).
1. Choose the value of the metric using the [Dynamic Instrumentation expression language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language). You can use any numeric value you'd like from the execution context, such as a method parameter, local variable, a class field, or an expression that yields a numeric value. For count metrics this is optional, and if you omit it, every invocation increments the count by one.

{% image
   source="https://datadog-docs.imgix.net/images/dynamic_instrumentation/metric_probe.64b08a90d0b7226219cee8078c7364ab.png?auto=format"
   alt="Creating a Dynamic Instrumentation metric probe" /%}

Metric probes are automatically enabled on all service instances that match the configured environment and version. Metric probes are not rate limited and execute every time the method or line is invoked.

Dynamic Instrumentation metric probes support the following metric types:

- **Count**: Counts how many times a given method or line is executed. Can be combined with [metric expressions](https://docs.datadoghq.com/dynamic_instrumentation/expression-language) to use the value of a variable to increment the count.
- **Gauge**: Generates a gauge based on the last value of a variable. This metric requires a [metric expression](https://docs.datadoghq.com/dynamic_instrumentation/expression-language).
- **Histogram**: Generates a statistical distribution of a variable. This metric requires a [metric expression](https://docs.datadoghq.com/dynamic_instrumentation/expression-language).

### Creating span probes{% #creating-span-probes %}

A *span probe* emits a span when a method is executed.

To create a span probe:

1. Select **Span** as the probe type.
1. Complete the generic probe setup (choose service, environment, version, and probe location).

{% image
   source="https://datadog-docs.imgix.net/images/dynamic_instrumentation/span_probe.86fbd11e97100473a0e70cf3aa4af07d.png?auto=format"
   alt="Creating a Dynamic Instrumentation span probe" /%}

You can use a *span probe* as an alternative to [creating new spans with Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/#adding-spans). If the method throws an exception, the details of the exception are associated with the newly created span's `error` tag.

### Creating span tag probes{% #creating-span-tag-probes %}

A *span tag* probe adds a tag value to an existing span. You can add a tag either to the *active* span or to the *service entry* span. Keep in mind that internal spans are not indexed by default and so might not be searchable in APM.

To create a span tag probe:

1. Select **Span Tag** as the probe type.
1. Complete the generic probe setup (choose service, environment, version, and probe location).
1. Specify a name for the tag.
1. Specify the value of the tag using the [Dynamic Instrumentation expression language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language).
1. Optionally define a condition using the Dynamic Instrumentation expression language. The tag will only be added when the expression evaluates to true.
1. Optionally add additional tags, each with their own name, expression, and optional condition.

{% image
   source="https://datadog-docs.imgix.net/images/dynamic_instrumentation/span_tag_probe.18ebd7014186b909d658d23c25f9c0cc.png?auto=format"
   alt="Creating a Dynamic Instrumentation span tag probe" /%}

You can use a *span tag probe* as an alternative to [using Custom Instrumentation to add tags in code](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/#adding-tags).

## Further Reading{% #further-reading %}

- [Learn more about the Dynamic Instrumentation Expression Language](https://docs.datadoghq.com/dynamic_instrumentation/expression-language/)
- [Removing sensitive information from your Dynamic Instrumentation data](https://docs.datadoghq.com/dynamic_instrumentation/sensitive-data-scrubbing/)
- [Learn more about how to instrument your application](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries)
- [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/)
- [Discover and catalog the services reporting to Datadog](https://docs.datadoghq.com/tracing/software_catalog/)
- [Learn more about Metrics](https://docs.datadoghq.com/metrics)
- [Use Datadog Dynamic Instrumentation to add application logs without redeploying](https://www.datadoghq.com/blog/dynamic-instrumentation-application-logging/)
