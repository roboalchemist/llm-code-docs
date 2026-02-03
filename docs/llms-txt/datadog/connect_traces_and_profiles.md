# Source: https://docs.datadoghq.com/profiler/connect_traces_and_profiles.md

---
title: Investigate Slow Traces or Endpoints
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Continuous Profiler > Investigate Slow Traces or Endpoints
---

# Investigate Slow Traces or Endpoints

If your application is showing performance problems in production, integrating distributed tracing with code stack trace benchmarks from profiling is a powerful way to identify the performance bottlenecks. Application processes that have both APM distributed tracing and continuous profiler enabled are automatically linked.

You can move directly from span information to profiling data on the **Profiles** tab, and find specific lines of code related to performance issues. Similarly, you can also debug slow and resource consuming endpoints directly in the Profiling UI.

## Identify code performance issues in slow traces{% #identify-code-performance-issues-in-slow-traces %}

### Prerequisites{% #prerequisites %}

{% tab title="Java" %}
The Trace to Profiling integration is enabled by default when you [turn on profiling for your Java service](https://docs.datadoghq.com/profiler/enabling/java) on Linux and macOS. The feature is not available on Windows.

For manually instrumented code, continuous profiler requires scope activation of spans:

```java
final Span span = tracer.buildSpan("ServicehandlerSpan").start();
try (final Scope scope = tracer.activateSpan(span)) { // mandatory for Datadog continuous profiler to link with span
    // worker thread impl
  } finally {
    // Step 3: Finish Span when work is complete
    span.finish();
  }
```

{% alert level="danger" %}
It's highly recommended to [use the Datadog profiler](https://docs.datadoghq.com/profiler/enabling/java/?tab=datadog#requirements) instead of Java Flight Recorder (JFR).
{% /alert %}

{% /tab %}

{% tab title="Python" %}
The Trace to Profiling integration is enabled when you:

- Upgrade `dd-trace-py` to version 2.12.0+, 2.11.4+, or 2.10.7+.
- Set environment variable `DD_PROFILING_TIMELINE_ENABLED` to `true`

{% /tab %}

{% tab title="Ruby" %}
The Trace to Profiling integration is enabled by default when you [turn on profiling for your Ruby service](https://docs.datadoghq.com/profiler/enabling/ruby) and update `dd-trace-rb` to 1.22.0+.
{% /tab %}

{% tab title="Node.js" %}
The Trace to Profiling integration is enabled by default when you [turn on profiling for your Node.js service](https://docs.datadoghq.com/profiler/enabling/nodejs) on Linux and macOS. The feature is not available on Windows.

Requires `dd-trace-js` 5.11.0+, 4.35.0+, and 3.56.0+.
{% /tab %}

{% tab title="Go" %}
The Trace to Profiling integration is enabled when you [turn on profiling for your Go service](https://docs.datadoghq.com/profiler/enabling/go) and set the environment variables below:

```go
os.Setenv("DD_PROFILING_EXECUTION_TRACE_ENABLED", "true")
os.Setenv("DD_PROFILING_EXECUTION_TRACE_PERIOD", "15m")
```

Setting these variables will record up to 1 minute (or 5 MiB) of execution tracing data [every 15 minutes](https://github.com/DataDog/dd-trace-go/issues/2099).

You can find this data:

- In the [Profile List](https://docs.datadoghq.com/profiler/profile_visualizations/#single-profile) by adding `go_execution_traced:yes` to your search query. Click on a profile to view the [Profile Timeline](https://docs.datadoghq.com/profiler/profile_visualizations/#timeline-view). To go even deeper, download the profile and use `go tool trace` or [gotraceui](https://github.com/dominikh/gotraceui) to view the contained `go.trace` files.
- In the [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/) by adding `@go_execution_traced:yes` (note the `@`) to your search query. Click on a span and then select the **Profiles** tab to view the Span Timeline.

While recording execution traces, your application may observe an increase in CPU usage similar to a garbage collection. Although this should not have a significant impact for most applications, Go 1.21 includes [patches](https://blog.felixge.de/waiting-for-go1-21-execution-tracing-with-less-than-one-percent-overhead/) to eliminate this overhead.

This capability requires `dd-trace-go` version 1.37.0+ (1.52.0+ for timeline view) and works best with Go version 1.18 or later (1.21 or later for timeline view).
{% /tab %}

{% tab title=".NET" %}
The Trace to Profiling integration is enabled by default when you [turn on profiling for your .NET service](https://docs.datadoghq.com/profiler/enabling/dotnet).

This capability requires `dd-trace-dotnet` version 2.30.0+.
{% /tab %}

{% tab title="PHP" %}
The Trace to Profiling integration is enabled when you [turn on profiling for your PHP service](https://docs.datadoghq.com/profiler/enabling/php) and meet the following criteria:

- You are on `dd-trace-php` version 0.98+
- You set the environment variable `DD_PROFILING_TIMELINE_ENABLED=1` or INI setting `datadog.profiling.timeline_enabled=1`

{% /tab %}

### Span execution timeline view{% #span-execution-timeline-view %}

{% image
   source="https://datadog-docs.imgix.net/images/profiler/profiling_automated_analysis_individual.6955582dfafc55661f841bca40df8602.png?auto=format"
   alt="Profiles tab has a timeline view that breaks down threads and execution over time" /%}

The timeline view surfaces time-based patterns and work distribution over the period of the span. It provides a visual breakdown of how threads contributed to the request over time.

With the span timeline view, you can:

- Isolate time-consuming methods
- Sort out complex interactions between threads
- Surface runtime activity that impacted the request
- Leverage [Automated Analysis](https://docs.datadoghq.com/profiler/automated_analysis/) to highlight performance issues directly in the view, such as oversized thread pools or GC contention

Depending on the runtime and language, the lanes vary:

{% tab title="Java" %}
Each lane represents a **thread**. Threads from a common pool are grouped together. You can expand the pool to view details for each thread.

Lanes on top are runtime activities that may add extra latency. They can be unrelated to the request itself.

For additional information about debugging slow p95 requests or timeouts using the timeline, see the blog post [Understanding Request Latency with Profiling](https://www.datadoghq.com/blog/request-latency-profiling/).
{% /tab %}

{% tab title="Python" %}
See prerequisites to learn how to enable this feature for Python.

Each lane represents a **thread**. Threads from a common pool are grouped together. You can expand the pool to view details for each thread.
{% /tab %}

{% tab title="Go" %}
Each lane represents a **goroutine**. This includes the goroutine that started the selected span, as well as any goroutines it created and their descendants. Goroutines created by the same `go` statement are grouped together. You can expand the group to view details for each goroutine.

Lanes on top are runtime activities that may add extra latency. They can be unrelated to the request itself.

For additional information about debugging slow p95 requests or timeouts using the timeline, see the blog post [Debug Go Request Latency with Datadog's Profiling Timeline](https://blog.felixge.de/debug-go-request-latency-with-datadogs-profiling-timeline/).
{% /tab %}

{% tab title="Ruby" %}
See prerequisites to learn how to enable this feature for Ruby.

Each lane represents a **thread**. Threads from a common pool are grouped together. You can expand the pool to view details for each thread.
{% /tab %}

{% tab title=".NET" %}
Each lane represents a **thread**. Threads with the same name are grouped together. You can expand a group to view details for each thread. Note that threads that are explicitly created by code are grouped under *Managed Threads*.

Lanes on top are runtime activities that may add extra latency. They can be unrelated to the request itself.
{% /tab %}

{% tab title="Node.js" %}
See prerequisites to learn how to enable this feature for Node.js.

There is one lane for the JavaScript **thread**.

Lanes on the top are garbage collector **runtime activities** that may add extra latency to your request.
{% /tab %}

{% tab title="PHP" %}
See prerequisites to learn how to enable this feature for PHP.

There is one lane for each PHP **thread** (in PHP NTS, this is only one lane). Fibers that run in this **thread** are represented in the same lane.

Lanes on the top are runtime activities that may add extra latency to your request, due to file compilation and garbage collection.
{% /tab %}

### Viewing a profile from a trace{% #viewing-a-profile-from-a-trace %}

{% image
   source="https://datadog-docs.imgix.net/images/profiler/view_profile_from_trace-2.64b0a27ebda19f748a8189b6421c8342.png?auto=format"
   alt="Opening a view of the profile in a flame graph" /%}

From the timeline, click **Open in Profiling** to see the same data on a new page. From there, you can change the visualization to a flame graph. Click the **Focus On** selector to define the scope of the data:

- **Span & Children** scopes the profiling data to the selected span and all descendant spans in the same service.
- **Span only** scopes the profiling data to the previously selected span.
- **Span time period** scopes the profiling data to all threads during the time period the span was active.
- **Full profile** scopes the data to 60 seconds of the whole service process that executed the previously selected span.

## Break down code performance by API endpoints{% #break-down-code-performance-by-api-endpoints %}

### Prerequisites{% #prerequisites-1 %}

{% tab title="Java" %}
Endpoint profiling is enabled by default when you [turn on profiling for your Java service](https://docs.datadoghq.com/profiler/enabling/java).

Requires [using the Datadog profiler](https://docs.datadoghq.com/profiler/enabling/java/?tab=datadog#requirements). JFR is not supported.
{% /tab %}

{% tab title="Python" %}
Endpoint profiling is enabled by default when you [turn on profiling for your Python service](https://docs.datadoghq.com/profiler/enabling/python).

Requires `dd-trace-py` version 0.54.0+.
{% /tab %}

{% tab title="Go" %}
Endpoint profiling is enabled by default when you [turn on profiling for your Go service](https://docs.datadoghq.com/profiler/enabling/go).

Requires `dd-trace-go` version 1.37.0+ and works best with Go version 1.18 or newer.
{% /tab %}

{% tab title="Ruby" %}
Endpoint profiling is enabled by default when you [turn on profiling for your Ruby service](https://docs.datadoghq.com/profiler/enabling/ruby).
{% /tab %}

{% tab title="Node.js" %}
Endpoint profiling is enabled by default when you [turn on profiling for your Node.js service](https://docs.datadoghq.com/profiler/enabling/nodejs) on Linux and macOS. The feature is not available on Windows.

Requires `dd-trace-js` version 5.0.0+, 4.24.0+ or 3.45.0+.
{% /tab %}

{% tab title=".NET" %}
Endpoint profiling is enabled by default when you [turn on profiling for your .NET service](https://docs.datadoghq.com/profiler/enabling/dotnet).

Requires `dd-trace-dotnet` version 2.15.0+.
{% /tab %}

{% tab title="PHP" %}
Endpoint profiling is enabled by default when you [turn on profiling for your PHP service](https://docs.datadoghq.com/profiler/enabling/php).

Requires `dd-trace-php` version 0.79.0+.
{% /tab %}

### Endpoint profiling{% #endpoint-profiling %}

Endpoint profiling allows you to scope your flame graphs by any endpoint of your web service to find endpoints that are slow, latency-heavy, and causing poor end-user experience. These endpoints can be tricky to debug and understand why they are slow. The slowness could be caused by an unintended large amount of resource consumption such as the endpoint consuming lots of CPU cycles.

With endpoint profiling you can:

- Identify the bottleneck methods that are slowing down your endpoint's overall response time.
- Isolate the top endpoints responsible for the consumption of valuable resources such as CPU, memory, or exceptions. This is particularly helpful when you are generally trying to optimize your service for performance gains.
- Understand if third-party code or runtime libraries are the reason for your endpoints being slow or resource-consumption heavy.

{% image
   source="https://datadog-docs.imgix.net/images/profiler/endpoint_agg.fe615c5594a27f1bcac90f13a144d038.png?auto=format"
   alt="Troubleshooting a slow endpoint by using endpoint aggregation" /%}

### Surface code that impacted your production latency{% #surface-code-that-impacted-your-production-latency %}

In the APM Service page, use the information in the **Profiling** tab to correlate a latency or throughput change to a code performance change.

In this example, you can see how latency is linked to a lock contention increase on `/GET train` that is caused by the following line of code:

```java
Thread.sleep(DELAY_BY.minus(elapsed).toMillis());
```

{% video
   url="https://datadog-docs.imgix.net/images/profiler/apm_service_page_pivot_to_contention_comparison.mp4" /%}

### Track endpoints that consume the most resources{% #track-endpoints-that-consume-the-most-resources %}

It is valuable to track top endpoints that are consuming valuable resources such as CPU and wall time. The list can help you identify if your endpoints have regressed or if you have newly introduced endpoints that are consuming drastically more resources, slowing down your overall service.

The following image shows that `GET /store_history` is periodically impacting this service by consuming 20% of its CPU and 50% of its allocated memory:

{% image
   source="https://datadog-docs.imgix.net/images/profiler/apm_endpoint_metric.9fdcd1102a1e1a0b898589a1f890e200.png?auto=format"
   alt="Graphing top endpoints in terms of resource consumption" /%}

### Track average resource consumption per request{% #track-average-resource-consumption-per-request %}

Select `Per endpoint call` to see behavior changes even as traffic shifts over time. This is useful for progressive rollout sanity checks or analyzing daily traffic patterns.

The following example shows that CPU per request increased for `/GET train`:

{% video
   url="https://datadog-docs.imgix.net/images/profiler/endpoint_per_request2.mp4" /%}

## Further reading{% #further-reading %}

- [APM Distributed Tracing](https://docs.datadoghq.com/tracing)
- [Enable Continuous Profiler for Your Application](https://docs.datadoghq.com/profiler/enabling)
- [Getting Started with Profiler](https://docs.datadoghq.com/getting_started/profiler)
