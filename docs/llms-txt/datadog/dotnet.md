# Source: https://docs.datadoghq.com/profiler/profiler_troubleshooting/dotnet.md

# Source: https://docs.datadoghq.com/profiler/enabling/dotnet.md

# Source: https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/dotnet.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/enabling/dotnet.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/symdb/dotnet.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/opentracing/dotnet.md

---
title: .NET OpenTracing Instrumentation
description: OpenTracing instrumentation for .NET
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Code-Based Custom Instrumentation >
  OpenTracing Instrumentation Setup > .NET OpenTracing Instrumentation
source_url: >-
  https://docs.datadoghq.com/trace_collection/custom_instrumentation/opentracing/dotnet/index.html
---

# .NET OpenTracing Instrumentation

{% alert level="info" %}
OpenTracing support is based on a deprecated specification. If you want to instrument your code with an open spec, use OpenTelemetry instead. Try [processing data from OpenTelemetry instrumentation in Datadog Tracing Libraries](https://docs.datadoghq.com/tracing/trace_collection/otel_instrumentation/dotnet/).
{% /alert %}

For more details and information, view the [OpenTracing API](https://github.com/opentracing/opentracing-csharp).

## Setup{% #setup %}

{% alert level="danger" %}
**Note:** Starting with v3.0.0, OpenTracing support requires you also use automatic instrumentation. You should aim to keep both automatic and custom instrumentation package versions (for example: MSI and NuGet) in sync, and ensure you don't mix major versions of packages.
{% /alert %}

For OpenTracing support, add the `Datadog.Trace.OpenTracing` [NuGet package](https://www.nuget.org/packages/Datadog.Trace.OpenTracing) to your application. During application start-up, initialize the OpenTracing SDK:

```csharp
using Datadog.Trace.OpenTracing;

public void ConfigureServices(IServiceCollection services)
{
    // Create an OpenTracing ITracer with the default setting
    OpenTracing.ITracer tracer = OpenTracingTracerFactory.CreateTracer();

    // Use the tracer with ASP.NET Core dependency injection
    services.AddSingleton<ITracer>(tracer);

    // Use the tracer with OpenTracing.GlobalTracer.Instance
    GlobalTracer.Register(tracer);
}
```

## Manually instrument a method{% #manually-instrument-a-method %}

Use OpenTracing to create a span.

```csharp
using (IScope scope = GlobalTracer.Instance.BuildSpan("manual.sortorders").StartActive(finishSpanOnDispose: true))
{
    scope.Span.SetTag("resource.name", "<RESOURCE NAME>");
    SortOrders();
}
```

## Asynchronous traces{% #asynchronous-traces %}

To trace code running in an asynchronous task, create a new scope within the background task, just as you would wrap synchronous code.

```csharp
 Task.Run(
     () =>
     {
         using (IScope scope = GlobalTracer.Instance.BuildSpan("manual.sortorders").StartActive(finishSpanOnDispose: true))
         {
             scope.Span.SetTag("resource.name", "<RESOURCE NAME>");
             SortOrders();
         }
     });
```

## Further reading{% #further-reading %}

- [Propagating trace context](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/)
