# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/server-side.md

---
title: Server-Side Custom Instrumentation
description: >-
  Add custom spans, tags, and instrumentation to capture application-specific
  observability data using Datadog APIs and OpenTelemetry.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Code-Based Custom Instrumentation >
  Server-Side Custom Instrumentation
---

{% section displayed-if="Language is C++" %}
This section only applies to users who meet the following criteria: Language is C++

{% section displayed-if="API is OpenTelemetry" %}
This section only applies to users who meet the following criteria: API is OpenTelemetry

{% alert level="danger" %}
C++ does not support the OpenTelemetry API. Select **Datadog** from the API dropdown to see C++ custom instrumentation documentation.
{% /alert %}
{% /section %}
{% /section %}

{% section displayed-if="Language is Rust" %}
This section only applies to users who meet the following criteria: Language is Rust

{% section displayed-if="API is Datadog" %}
This section only applies to users who meet the following criteria: API is Datadog

{% alert level="danger" %}
Rust does not support the Datadog API. Select **OpenTelemetry** from the API dropdown to see Rust custom instrumentation documentation.
{% /alert %}
{% /section %}
{% /section %}

{% section displayed-if="Language is Elixir" %}
This section only applies to users who meet the following criteria: Language is Elixir

{% section displayed-if="API is Datadog" %}
This section only applies to users who meet the following criteria: API is Datadog

{% alert level="danger" %}
Elixir does not support the Datadog API. Select **OpenTelemetry** from the API dropdown to see Elixir custom instrumentation documentation.
{% /alert %}
{% /section %}
{% /section %}

{% section displayed-if="API is OpenTelemetry" %}
This section only applies to users who meet the following criteria: API is OpenTelemetry

{% section displayed-if="Language is Elixir" %}
This section only applies to users who meet the following criteria: Language is Elixir

Datadog does not provide an Elixir tracing library. To send traces to Datadog, use the [OpenTelemetry SDK for Elixir](https://opentelemetry.io/docs/languages/beam/).
{% /section %}

{% section displayed-if="not (Language is C++) or (Language is Elixir)" %}
This section only applies to users who meet the following criteria: not (Language is C++) or (Language is Elixir)

## Overview{% #overview %}

There are a few reasons to manually instrument your applications with the OpenTelemetry API:

- You are not using Datadog supported library instrumentation.
- You want to extend the Datadog SDK's functionality.
- You need finer control over instrumenting your applications.

The Datadog SDK provides several techniques to help you achieve these goals. The following sections demonstrate how to use the OpenTelemetry API for custom instrumentation to use with Datadog.

{% section displayed-if="Language is Java" %}
This section only applies to users who meet the following criteria: Language is Java

## Setup{% #setup-otel-java %}

{% alert level="info" %}
OpenTelemetry is supported in Java after version 1.24.0.
{% /alert %}

To configure OpenTelemetry to use the Datadog trace provider:

1. If you have not yet read the instructions for auto-instrumentation and setup, start with the [Java Setup Instructions](https://docs.datadoghq.com/tracing/setup/java/).

1. Make sure you only depend on the OpenTelemetry API (and not the OpenTelemetry SDK).

1. Set the `dd.trace.otel.enabled` system property or the `DD_TRACE_OTEL_ENABLED` environment variable to `true`.

## Adding span tags{% #adding-span-tags-otel-java %}

### Add custom span tags{% #add-custom-span-tags-otel-java %}

Add custom tags to your spans corresponding to any dynamic value within your application code such as `customer.id`.

```
import io.opentelemetry.api.trace.Span;

public void doSomething() {
  Span span = Span.current();
  span.setAttribute("user-name", "Some User");
}
```

### Adding tags globally to all spans{% #adding-tags-globally-otel-java %}

The `dd.tags` property allows you to set tags across all generated spans for an application. This is useful for grouping stats for your applications, data centers, or any other tags you would like to see in Datadog.

```
java -javaagent:<DD-JAVA-AGENT-PATH>.jar \
    -Ddd.tags=datacenter:njc,<TAG_KEY>:<TAG_VALUE> \
    -jar <YOUR_APPLICATION_PATH>.jar
```

### Setting errors on span{% #setting-errors-on-span-otel-java %}

To set an error on a span, use the `setStatus` method:

```
import static io.opentelemetry.api.trace.StatusCode.ERROR;
import io.opentelemetry.api.trace.Span;

public void doSomething() {
  Span span = Span.current();
  span.setStatus(ERROR, "Some error details...");
}
```

### Setting tags and errors on a root span from a child span{% #setting-tags-errors-root-span-otel-java %}

When you want to set tags or errors on the root span from within a child span, you can use the OpenTelemetry Context API:

```
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.context.Context;
import io.opentelemetry.context.ContextKey;
import io.opentelemetry.context.Scope;

public class Example {

  private final static ContextKey<Span> CONTEXT_KEY =
    ContextKey.named("opentelemetry-traces-local-root-span");

  public void begin() {
    Tracer tracer = GlobalOpenTelemetry.getTracer("my-scope", "0.1.0");
    Span parentSpan = tracer.spanBuilder("begin").startSpan();
    try (Scope scope = parentSpan.makeCurrent()) {
      createChildSpan();
    } finally {
      parentSpan.end();
    }
  }

  private void createChildSpan() {
    Tracer tracer = GlobalOpenTelemetry.getTracer("my-scope", "0.1.0");
    Span childSpan = tracer.spanBuilder("child-span").startSpan();
    try {
      Span rootSpan = Context.current().get(CONTEXT_KEY);
        if (null != rootSpan) {
          rootSpan.setAttribute("my-attribute", "my-attribute-value");
          rootSpan.setStatus(StatusCode.ERROR, "Some error details...");
        }
    } finally {
      childSpan.end();
    }
  }

}
```

## Adding spans{% #adding-spans-otel-java %}

If you aren't using a [supported framework instrumentation](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/java/?tab=wget#compatibility), or you would like additional depth in your application's [traces](https://docs.datadoghq.com/tracing/glossary/#trace), you may want to add custom instrumentation to your code for complete flame graphs or to measure execution times for pieces of code.

If modifying application code is not possible, use the environment variable `dd.trace.methods` to detail these methods.

If you have existing `@Trace` or similar annotations, or prefer to use annotations to complete any incomplete traces within Datadog, use Trace Annotations.

### Trace annotations{% #trace-annotations-otel-java %}

Add `@WithSpan` to methods to have them be traced when running OpenTelemetry and the `dd-java-agent.jar`. If the Agent is not attached, this annotation has no effect on your application.

OpenTelemetry's `@WithSpan` annotation is provided by the `opentelemetry-instrumentation-annotations` dependency.

```
import io.opentelemetry.instrumentation.annotations.WithSpan;

public class SessionManager {

  @WithSpan
  public static void saveSession() {
    // your method implementation here
  }
}
```

### Manually creating a new span{% #manually-creating-a-new-span-otel-java %}

To manually create new spans within the current trace context:

```
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.context.Scope;

public class Example {

  public void doSomething() {
    Tracer tracer = GlobalOpenTelemetry.getTracer("my-scope", "0.1.0");
    Span span = tracer.spanBuilder("my-resource").startSpan();
    try (Scope scope = span.makeCurrent()) {
      // do some work
    } catch (Throwable t) {
      span.recordException(t);
      throw t;
    } finally {
      span.end();
    }
  }
}
```

## Adding span events{% #adding-span-events-otel-java %}

{% alert level="info" %}
Adding span events requires SDK version 1.40.0 or higher.
{% /alert %}

You can add span events using the `addEvent` API. This method requires a `name` parameter and optionally accepts `attributes` and `timestamp` parameters. The method creates a new span event with the specified properties and associates it with the corresponding span.

- **Name** [*required*]: A string representing the event's name.
- **Attributes** [*optional*]: Key-value pairs where the key is a non-empty string and the value is a primitive type or a homogeneous array of primitive values.
- **Timestamp** [*optional*]: A UNIX timestamp representing the event's occurrence time. Expects an `Instant` object.

```
Attributes eventAttributes = Attributes.builder()
    .put(AttributeKey.longKey("int_val"), 1L)
    .put(AttributeKey.stringKey("string_val"), "two")
    .put(AttributeKey.longArrayKey("int_array"), Arrays.asList(3L, 4L))
    .put(AttributeKey.stringArrayKey("string_array"), Arrays.asList("5", "6"))
    .put(AttributeKey.booleanArrayKey("bool_array"), Arrays.asList(true, false))
    .build();

span.addEvent("Event With No Attributes");
span.addEvent("Event With Some Attributes", eventAttributes);
```

Read the [OpenTelemetry specification for adding events](https://opentelemetry.io/docs/specs/otel/trace/api/#add-events) for more information.

### Recording exceptions{% #recording-exceptions-otel-java %}

To record exceptions, use the `recordException` API:

```
span.recordException(new Exception("Error Message"));
span.recordException(new Exception("Error Message"),
    Attributes.builder().put(AttributeKey.stringKey("status"), "failed").build());
```

Read the [OpenTelemetry specification for recording exceptions](https://opentelemetry.io/docs/specs/otel/trace/api/#record-exception) for more information.

## Trace client and Agent configuration{% #trace-client-agent-config-otel-java %}

Both the tracing client and Datadog Agent offer additional configuration options for context propagation. You can also exclude specific resources from sending traces to Datadog if you don't want those traces to be included in calculated metrics, such as traces related to health checks.

### Propagating context with headers extraction and injection{% #propagating-context-otel-java %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.

### Resource filtering{% #resource-filtering-otel-java %}

Traces can be excluded based on their resource name, to remove synthetic traffic such as health checks from reporting traces to Datadog. This and other security and fine-tuning configurations can be found on the [Security](https://docs.datadoghq.com/tracing/security) page or in [Ignoring Unwanted Resources](https://docs.datadoghq.com/tracing/guide/ignoring_apm_resources/).
{% /section %}

{% section displayed-if="Language is Python" %}
This section only applies to users who meet the following criteria: Language is Python

## Setup{% #setup-otel-python %}

To configure OpenTelemetry to use the Datadog trace provider:

1. If you have not yet read the instructions for auto-instrumentation and setup, start with the [Python Setup Instructions](https://docs.datadoghq.com/tracing/setup/python/).

1. Set `DD_TRACE_OTEL_ENABLED` environment variable to `true`.

### Creating custom spans{% #creating-custom-spans-otel-python %}

To create custom spans within an existing trace context:

```
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def do_work():
    with tracer.start_as_current_span("operation_name") as span:
        # Perform the work that you want to track with the span
        print("Doing work...")
        # When the 'with' block ends, the span is automatically closed
```

## Accessing active spans{% #accessing-active-spans-otel-python %}

To access the currently active span, use the `get_current_span()` function:

```
from opentelemetry import trace

current_span = trace.get_current_span()
# enrich 'current_span' with information
```

## Adding span tags{% #adding-span-tags-otel-python %}

Add attributes to a span to provide additional context or metadata:

```
from opentelemetry import trace

current_span = trace.get_current_span()

current_span.set_attribute("attribute_key1", 1)
```

## Adding span events{% #adding-span-events-otel-python %}

{% alert level="info" %}
Adding span events requires SDK version 2.9.0 or higher.
{% /alert %}

You can add span events using the `add_event` API. This method requires a `name` parameter and optionally accepts `attributes` and `timestamp` parameters.

```
span.add_event("Event With No Attributes")
span.add_event("Event With Some Attributes", {"int_val": 1, "string_val": "two", "int_array": [3, 4], "string_array": ["5", "6"], "bool_array": [True, False]})
```

Read the [OpenTelemetry specification for adding events](https://opentelemetry.io/docs/specs/otel/trace/api/#add-events) for more information.

### Recording exceptions{% #recording-exceptions-otel-python %}

To record exceptions, use the `record_exception` API:

```
span.record_exception(Exception("Error Message"))
span.record_exception(Exception("Error Message"), {"status": "failed"})
```

Read the [OpenTelemetry specification for recording exceptions](https://opentelemetry.io/docs/specs/otel/trace/api/#record-exception) for more information.
{% /section %}

{% section displayed-if="Language is Node.js" %}
This section only applies to users who meet the following criteria: Language is Node.js

## Setup{% #setup-otel-nodejs %}

To instrument your application, initialize the Datadog tracer (`dd-trace`) and explicitly register its `TracerProvider` with the OpenTelemetry API. This ensures all OpenTelemetry calls are routed through Datadog.

1. **Add the dependencies**:

   ```
   npm install dd-trace @opentelemetry/api
   ```

1. **Initialize and register the tracer** in your application's entry file (for example, `index.js`), before any other imports:

### Complete example{% #complete-example-otel-nodejs %}

```
// 1. Import the dd-trace library (do not initialize it yet)
const ddtrace = require('dd-trace');

// 2. Initialize the Datadog tracer. This must be the first operation.
const tracer = ddtrace.init({
  // service: 'my-nodejs-app'
  // ... other Datadog configurations
});

// 3. Create and register Datadog's TracerProvider.
const provider = new tracer.TracerProvider();
provider.register(); // This wires the @opentelemetry/api to Datadog

// 4. Import and use the OpenTelemetry API
const otel = require('@opentelemetry/api');
const otelTracer = otel.trace.getTracer(
  'my-custom-instrumentation' // A name for your specific instrumentation
);

// You can now use 'otelTracer' to create spans throughout your application.
```

Datadog combines these OpenTelemetry spans with other Datadog APM spans into a single trace of your application. It also supports [integration instrumentation](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/nodejs#integration-instrumentation) and [OpenTelemetry automatic instrumentation](https://opentelemetry.io/docs/instrumentation/js/automatic/).

## Adding span tags{% #adding-span-tags-otel-nodejs %}

Add custom attributes to your spans to provide additional context:

```
function processData(i, param1, param2) {
  return otelTracer.startActiveSpan(`processData:${i}`, (span) => {
    const result = someOperation(param1, param2);

    // Add an attribute to the span
    span.setAttribute('app.processedData', result.toString());
    span.end();
    return result;
    });
}
```

## Creating spans{% #creating-spans-otel-nodejs %}

To create a new span and properly close it, use the `startActiveSpan` method:

```
function performTask(iterations, param1, param2) {
  // Create a span. A span must be closed.
  return otelTracer.startActiveSpan('performTask', (span) => {
    const results = [];
    for (let i = 0; i < iterations; i++) {
      results.push(processData(i, param1, param2));
    }
    // Be sure to end the span!
    span.end();
    return results;
  });
}
```

## Adding span events{% #adding-span-events-otel-nodejs %}

{% alert level="info" %}
Adding span events requires SDK version 5.17.0/4.41.0 or higher.
{% /alert %}

You can add span events using the `addEvent` API:

```
span.addEvent('Event With No Attributes')
span.addEvent('Event With Some Attributes', {"int_val": 1, "string_val": "two", "int_array": [3, 4], "string_array": ["5", "6"], "bool_array": [true, false]})
```

Read the [OpenTelemetry specification for adding events](https://opentelemetry.io/docs/specs/otel/trace/api/#add-events) for more information.

### Recording exceptions{% #recording-exceptions-otel-nodejs %}

To record exceptions, use the `recordException` API:

```
span.recordException(new TestError())
```

Read the [OpenTelemetry specification for recording exceptions](https://opentelemetry.io/docs/specs/otel/trace/api/#record-exception) for more information.

## Filtering requests{% #filtering-requests-otel-nodejs %}

In some cases, you may want to exclude certain requests from being instrumented, such as health checks or synthetic traffic. You can use the `blocklist` or `allowlist` option on the `http` plugin to ignore these requests.

```
// at the top of the entry point right after tracer.init()
tracer.use('http', {
  blocklist: ['/health', '/ping']
})
```

You can also split the configuration between client and server if needed:

```
tracer.use('http', {
  server: {
    blocklist: ['/ping']
  }
})
```

Additionally, you can exclude traces based on their resource name to prevent the Agent from sending them to Datadog. For more information on security and fine-tuning Agent configurations, read the [Security](https://docs.datadoghq.com/tracing/security) or [Ignoring Unwanted Resources](https://docs.datadoghq.com/tracing/guide/ignoring_apm_resources/) documentation.
{% /section %}

{% section displayed-if="Language is Go" %}
This section only applies to users who meet the following criteria: Language is Go

## Imports{% #imports-otel-go %}

Import the following packages to setup the Datadog trace provider:

```
import (
    "context"
    "log"
    "os"

   "github.com/DataDog/dd-trace-go/v2/ddtrace/ext"
   "github.com/DataDog/dd-trace-go/v2/ddtrace/opentelemetry"
   "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"

    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/attribute"
)
```

## Setup{% #setup-otel-go %}

To configure OpenTelemetry to use the Datadog trace provider:

1. Add your desired manual OpenTelemetry instrumentation to your Go code following the [OpenTelemetry Go Manual Instrumentation documentation](https://opentelemetry.io/docs/instrumentation/go/manual/). **Important!** Where those instructions indicate that your code should call the OpenTelemetry SDK, call the Datadog tracing library instead.

1. Install the OpenTelemetry package:

   ```
   go get go.opentelemetry.io/otel
   ```

1. Install the Datadog OpenTelemetry wrapper package:

   ```
   go get github.com/DataDog/dd-trace-go/v2/ddtrace/opentelemetry
   ```

1. Import packages:

   ```
   import (
      "go.opentelemetry.io/otel"
      ddotel "github.com/DataDog/dd-trace-go/v2/ddtrace/opentelemetry"
   )
   ```

1. Create a TracerProvider and defer the Shutdown method:

   ```
   provider := ddotel.NewTracerProvider()
   defer provider.Shutdown()
   ```

1. Set the global TracerProvider:

   ```
   otel.SetTracerProvider(provider)
   ```

1. Run your application.

## Adding span tags{% #adding-span-tags-otel-go %}

Add custom tags to your spans to attach additional metadata and context:

```
// Start a span.
ctx, span := t.Start(ctx, "read.file")
// Set an attribute, or a tag in Datadog terminology, on a span.
span.SetAttributes(attribute.String(ext.ResourceName, "test.json"))
```

### Adding tags globally to all spans{% #adding-tags-globally-otel-go %}

Add tags to all spans by configuring the tracer with the `WithGlobalTag` option:

```
provider := ddotel.NewTracerProvider(
    ddtracer.WithGlobalTag("datacenter", "us-1"),
    ddtracer.WithGlobalTag("env", "dev"),
)
defer provider.Shutdown()

otel.SetTracerProvider(provider)
t := otel.Tracer("")
```

### Setting errors on a span{% #setting-errors-on-a-span-otel-go %}

To set an error on a span:

```
// Start a span.
ctx, span := t.Start(context.Background(), "spanName")

// Set an error on a span with 'span.SetAttributes'.
span.SetAttributes(attribute.String(ext.ErrorMsg, "errorMsg"))

// Alternatively, set an error via end span options.
EndOptions(span, tracer.WithError(errors.New("myErr")))
span.End()
```

## Adding spans{% #adding-spans-otel-go %}

Unlike other Datadog tracing libraries, when tracing Go applications, Datadog recommends that you explicitly manage and pass the Go context of your spans.

```
ctx, span := t.Start(
    ddotel.ContextWithStartOptions(context.Background(), ddtracer.Measured()), "span_name")

span.End()
```

## Adding span events{% #adding-span-events-otel-go %}

{% alert level="info" %}
Adding span events requires SDK version 1.67.0 or higher.
{% /alert %}

You can add span events using the `AddEvent` API:

```
ctx, span := tracer.StartSpan(context.Background(), "span_name")
span.AddEvent("Event With No Attributes")
span.AddEvent("Event With Some Attributes", oteltrace.WithAttributes(attribute.Int("int_val", 1), attribute.String("string_val", "two")))
span.Finish()
```

Read the [OpenTelemetry specification for adding events](https://opentelemetry.io/docs/specs/otel/trace/api/#add-events) for more information.

## Trace client and Agent configuration{% #trace-client-agent-config-otel-go %}

### Propagating context with headers extraction and injection{% #propagating-context-otel-go %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.

### Resource filtering{% #resource-filtering-otel-go %}

Traces can be excluded based on their resource name, to remove synthetic traffic such as health checks from reporting traces to Datadog. This and other security and fine-tuning configurations can be found on the [Security](https://docs.datadoghq.com/tracing/security) page.
{% /section %}

{% section displayed-if="Language is Ruby" %}
This section only applies to users who meet the following criteria: Language is Ruby

## Requirements and limitations{% #requirements-and-limitations-otel-ruby %}

- Datadog Ruby tracing library `dd-trace-rb` version 1.9.0 or greater.
- Gem version support 1.1.0 or greater.

The following OpenTelemetry features implemented in the Datadog library as noted:

| Feature                           | Support notes                                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- |
| OpenTelemetry Context propagation | Datadog and W3C Trace Context header formats are enabled by default.                                    |
| Span processors                   | Unsupported                                                                                             |
| Span Exporters                    | Unsupported                                                                                             |
| `OpenTelemetry.logger`            | `OpenTelemetry.logger` is set to the same object as `Datadog.logger`. Configure through custom logging. |
| Trace/span ID generators          | ID generation is performed by the tracing library, with support for 128-bit trace IDs.                  |

## Configuring OpenTelemetry to use the Datadog tracing library{% #configuring-otel-ruby %}

1. Add your desired manual OpenTelemetry instrumentation to your Ruby code following the [OpenTelemetry Ruby Manual Instrumentation documentation](https://opentelemetry.io/docs/instrumentation/ruby/manual/). **Important!** Where those instructions indicate that your code should call the OpenTelemetry SDK, call the Datadog tracing library instead.

1. Add the `datadog` gem to your Gemfile:

   ```
   source 'https://rubygems.org'
   gem 'datadog' # For dd-trace-rb v1.x, use the `ddtrace` gem.
   ```

1. Install the gem by running `bundle install`.

1. Add the following lines to your OpenTelemetry configuration file:

   ```
   require 'opentelemetry/sdk'
   require 'datadog/opentelemetry'
   ```

1. Add a configuration block to your application:

   ```
   Datadog.configure do |c|
     ...
   end
   ```

Datadog combines these OpenTelemetry spans with other Datadog APM spans into a single trace of your application. It supports [integration instrumentation](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ruby#integration-instrumentation) and [OpenTelemetry Automatic instrumentation](https://opentelemetry.io/docs/languages/ruby/libraries/) also.

## Adding span events{% #adding-span-events-otel-ruby %}

{% alert level="info" %}
Adding span events requires SDK version 2.3.0 or higher.
{% /alert %}

You can add span events using the `add_event` API:

```
span.add_event('Event With No Attributes')
span.add_event(
  'Event With All Attributes',
  attributes: { 'int_val' => 1, 'string_val' => 'two', 'int_array' => [3, 4], 'string_array' => ['5', '6'], 'bool_array' => [false, true]}
)
```

Read the [OpenTelemetry specification for adding events](https://opentelemetry.io/docs/specs/otel/trace/api/#add-events) for more information.

### Recording exceptions{% #recording-exceptions-otel-ruby %}

To record exceptions, use the `record_exception` API:

```
span.record_exception(
  StandardError.new('Error Message')
)
span.record_exception(
  StandardError.new('Error Message'),
  attributes: { 'status' => 'failed' }
)
```

Read the [OpenTelemetry specification for recording exceptions](https://opentelemetry.io/docs/specs/otel/trace/api/#record-exception) for more information.
{% /section %}

{% section displayed-if="Language is .NET" %}
This section only applies to users who meet the following criteria: Language is .NET

## Setup{% #setup-otel-dotnet %}

To configure OpenTelemetry to use the Datadog trace provider:

1. Add your desired manual OpenTelemetry instrumentation to your .NET code following the [OpenTelemetry .NET Manual Instrumentation documentation](https://opentelemetry.io/docs/instrumentation/net/manual/). **Note**: Where those instructions indicate that your code should call the OpenTelemetry SDK, call the Datadog tracing library instead.

1. Install the Datadog .NET tracing library and enable the tracer for your [.NET Framework service](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-framework/#installation-and-getting-started) or your [.NET Core (and .NET 5+) service](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-core/#installation-and-getting-started). You can optionally do this with [Single Step APM Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/single-step-apm/).

1. Set `DD_TRACE_OTEL_ENABLED` environment variable to `true`.

1. Run your application.

Datadog combines these OpenTelemetry spans with other Datadog APM spans into a single trace of your application. It also supports [OpenTelemetry instrumentation libraries](https://opentelemetry.io/docs/instrumentation/net/libraries/).

## Creating custom spans{% #creating-custom-spans-otel-dotnet %}

To manually create spans that start a new, independent trace:

```
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

// Start a new span
using (Activity? activity = Telemetry.ActivitySource.StartActivity("<RESOURCE NAME>"))
{
  activity?.SetTag("operation.name", "custom-operation");
  // Do something
}
```

## Creating spans{% #creating-spans-otel-dotnet %}

To create custom spans within an existing trace context:

```
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

using (Activity? parentScope = Telemetry.ActivitySource.StartActivity("<RESOURCE NAME>"))
{
   parentScope?.SetTag("operation.name", "manual.sortorders");
   using (Activity? childScope = Telemetry.ActivitySource.StartActivity("<RESOURCE NAME>"))
   {
       childScope?.SetTag("operation.name", "manual.sortorders.child");
       SortOrders();
   }
}
```

## Adding span tags{% #adding-span-tags-otel-dotnet %}

Add custom tags to your spans to provide additional context:

```
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

public class ShoppingCartController : Controller
{
    [HttpGet]
    public IActionResult Index(int customerId)
    {
      Activity? activity = Telemetry.ActivitySource.StartActivity("<RESOURCE NAME>")

      // Add a tag to the span for use in the Datadog web UI
      activity?.SetTag("customer.id", customerId.ToString());

      var cart = _shoppingCartRepository.Get(customerId);
      return View(cart);
    }
}
```

## Setting errors on spans{% #setting-errors-on-spans-otel-dotnet %}

Set error information on a span when an error occurs during its execution:

```
try
{
    // do work that can throw an exception
}
catch(Exception e)
{
    activity?.SetTag("error", 1);
    activity?.SetTag("error.message", exception.Message);
    activity?.SetTag("error.stack", exception.ToString());
    activity?.SetTag("error.type", exception.GetType().ToString());
}
```

## Adding span events{% #adding-span-events-otel-dotnet %}

{% alert level="info" %}
Adding span events requires SDK version 2.53.0 or higher.
{% /alert %}

You can add span events using the `AddEvent` API:

```
var eventTags = new ActivityTagsCollection
{
    { "int_val", 1 },
    { "string_val", "two" },
    { "int_array", new int[] { 3, 4 } },
    { "string_array", new string[] { "5", "6" } },
    { "bool_array", new bool[] { true, false } }
};

activity.AddEvent(new ActivityEvent("Event With No Attributes"));
activity.AddEvent(new ActivityEvent("Event With Some Attributes", DateTimeOffset.Now, eventTags));
```

Read the [OpenTelemetry specification for adding events](https://opentelemetry.io/docs/specs/otel/trace/api/#add-events) for more information.

## Propagating context with headers extraction and injection{% #propagating-context-otel-dotnet %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.
{% /section %}

{% section displayed-if="Language is PHP" %}
This section only applies to users who meet the following criteria: Language is PHP

## Setup{% #setup-otel-php %}

To configure OpenTelemetry to use the Datadog trace provider:

1. Install [OpenTelemetry API packages](https://opentelemetry.io/docs/languages/php/instrumentation/#instrumentation-setup):

   ```
   composer require open-telemetry/sdk
   ```

1. Add your desired manual OpenTelemetry instrumentation to your PHP code following the [OpenTelemetry PHP Manual Instrumentation documentation](https://opentelemetry.io/docs/instrumentation/php/manual/).

1. Install the [Datadog PHP tracing library](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/php#getting-started).

1. Set `DD_TRACE_OTEL_ENABLED` to `true`.

Datadog combines these OpenTelemetry spans with other Datadog APM spans into a single trace of your application.

## Adding span tags{% #adding-span-tags-otel-php %}

You can add attributes at the exact moment as you are starting the span:

```
$span = $tracer->spanBuilder('mySpan')
    ->setAttribute('key', 'value')
    ->startSpan();
```

Or while the span is active:

```
$activeSpan = OpenTelemetry\API\Trace\Span::getCurrent();
$activeSpan->setAttribute('key', 'value');
```

## Setting errors on a span{% #setting-errors-on-a-span-otel-php %}

Exception information is captured and attached to a span if one is active when the exception is raised:

```
// Create a span
$span = $tracer->spanBuilder('mySpan')->startSpan();

throw new \Exception('Oops!');

// 'mySpan' will be flagged as erroneous and have
// the stack trace and exception message attached as tags
```

Flagging a trace as erroneous can also be done manually:

```
use OpenTelemetry\API\Trace\Span;
use OpenTelemetry\Context\Context;

try {
    throw new \Exception('Oops!');
} catch (\Exception $e) {
    $rootSpan = Span::fromContext(Context::getRoot());
    $rootSpan->recordException($e);
}
```

## Adding spans{% #adding-spans-otel-php %}

To add a span:

```
// Get a tracer or use an existing one
$tracerProvider = \OpenTelemetry\API\Globals::tracerProvider();
$tracer = $tracerProvider->getTracer('datadog')

// Create a span
$span = $tracer->spanBuilder('mySpan')->startSpan();

// ... do stuff

// Close the span
$span->end();
```

## Adding span events{% #adding-span-events-otel-php %}

{% alert level="info" %}
Adding span events requires SDK version 1.3.0 or higher.
{% /alert %}

You can add span events using the `addEvent` API:

```
$span->addEvent("Event With No Attributes");
$span->addEvent(
    "Event With Some Attributes",
    [
        'int_val' => 1,
        'string_val' => "two",
        'int_array' => [3, 4],
        'string_array' => ["5", "6"],
        'bool_array' => [true, false]
    ]
);
```

Read the [OpenTelemetry specification for adding events](https://opentelemetry.io/docs/specs/otel/trace/api/#add-events) for more information.

### Recording exceptions{% #recording-exceptions-otel-php %}

To record exceptions, use the `recordException` API:

```
$span->recordException(new \Exception("Error Message"));
$span->recordException(new \Exception("Error Message"), [ "status" => "failed" ]);
```

Read the [OpenTelemetry specification for recording exceptions](https://opentelemetry.io/docs/specs/otel/trace/api/#record-exception) for more information.

## Accessing active spans{% #accessing-active-spans-otel-php %}

To access the currently active span:

```
$span = OpenTelemetry\API\Trace\Span::getCurrent();
```
{% /section %}

{% section displayed-if="Language is Rust" %}
This section only applies to users who meet the following criteria: Language is Rust

{% alert level="info" %}
The Datadog Rust SDK is in Preview.
{% /alert %}

Datadog provides support for custom instrumentation in Rust applications through the [`datadog-opentelemetry` crate](https://crates.io/crates/datadog-opentelemetry). This library is built on the OpenTelemetry (OTel) API and SDK, providing a tracer that includes Datadog-specific features and an exporter.

Because this library is built on OpenTelemetry, you use the standard OpenTelemetry API to create traces and spans.

## Setup{% #setup-otel-rust %}

To configure your Rust application to send OpenTelemetry traces to Datadog:

### 1. Add dependencies{% #add-dependencies-otel-rust %}

Add `datadog-opentelemetry` and the core `opentelemetry` crate to your `Cargo.toml`:

```
cargo add datadog-opentelemetry opentelemetry
```

### 2. Initialize the Tracer{% #initialize-tracer-otel-rust %}

In your application's main function, initialize the Datadog tracer provider:

{% alert level="info" %}
You must shut down the provider before your application exits to ensure all pending traces are flushed.
{% /alert %}

```
use datadog_opentelemetry;
use opentelemetry::{global, trace::Tracer};
use std::time::Duration;

fn main() {
    // This picks up env var configuration (like DD_SERVICE)
    // and initializes the global tracer provider
    let tracer_provider = datadog_opentelemetry::tracing()
        .init();

    // --- Your application code starts here ---
    let tracer = global::tracer("my-component");

    tracer.in_span("my-operation", |_cx| {
        // ... do work ...
    });

    println!("Doing work...");

    // --- Your application code ends here ---

    // Shut down the tracer provider to flush remaining spans
    tracer_provider.shutdown_with_timeout(Duration::from_secs(5)).expect("tracer shutdown error");
}
```

### 3. Ensure Agent is running{% #ensure-agent-running-otel-rust %}

The Datadog exporter sends traces to the Datadog Agent, which must be running and accessible.

## Configuration{% #configuration-otel-rust %}

The Datadog Rust SDK is configured using environment variables. For a complete list of options, see the [Configuration documentation](https://docs.datadoghq.com/tracing/trace_collection/library_config/rust).

## Examples{% #examples-otel-rust %}

### Get a Tracer{% #get-a-tracer-otel-rust %}

Get an instance of a `Tracer` from the global provider:

```
use opentelemetry::global;

let tracer = global::tracer("my-component");
```

### Create a span{% #create-a-span-otel-rust %}

Use `tracer.in_span` to create a new span. The span is automatically ended when the closure finishes:

```
use opentelemetry::{global, trace::Tracer};

fn do_work() {
    let tracer = global::tracer("my-component");

    tracer.in_span("operation_name", |_cx| {
        // The span is active within this closure
        println!("Doing work...");
    });
}
```

### Create a child span{% #create-a-child-span-otel-rust %}

To create a child span, nest `in_span` calls:

```
use opentelemetry::{global, trace::Tracer};

fn parent_operation() {
    let tracer = global::tracer("my-component");

    tracer.in_span("parent_operation", |_cx| {
        tracer.in_span("child_operation", |_cx| {
            // This span is automatically parented to "parent_operation"
            println!("Doing child work...");
        });
        println!("Doing parent work...");
    });
}
```

### Add span tags{% #add-span-tags-otel-rust %}

Add attributes to a span using the `set_attribute` method:

```
use opentelemetry::trace::{Tracer, TraceContextExt};
use opentelemetry::KeyValue;

fn add_tags_to_span() {
    let tracer = opentelemetry::global::tracer("my-component");

    tracer.in_span("operation.with.tags", |cx| {
        let span = cx.span();

        span.set_attribute(KeyValue::new("customer.id", "12345"));
        span.set_attribute(KeyValue::new("http.method", "GET"));
    });
}
```

### Add span events{% #add-span-events-otel-rust %}

Add time-stamped log messages to a span using the `add_event` method:

```
use opentelemetry::trace::{Tracer, TraceContextExt};
use opentelemetry::KeyValue;

fn add_events_to_span() {
    let tracer = opentelemetry::global::tracer("my-component");

    tracer.in_span("operation.with.events", |cx| {
        let span = cx.span();

        span.add_event("Data received", vec![]);
        span.add_event(
            "Processing data",
            vec![
                KeyValue::new("data.size_bytes", 1024),
                KeyValue::new("data.format", "json"),
            ],
        );
    });
}
```

## Context propagation{% #context-propagation-otel-rust %}

Because Rust does not have automatic instrumentation, you must manually propagate the trace context when making or receiving remote calls to connect traces across services.

For more information, see [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/?tab=rust).
{% /section %}
{% /section %}
{% /section %}

{% section displayed-if="API is Datadog" %}
This section only applies to users who meet the following criteria: API is Datadog

{% section displayed-if="not (Language is Rust) or (Language is Elixir)" %}
This section only applies to users who meet the following criteria: not (Language is Rust) or (Language is Elixir)

## Overview{% #overview-2 %}

Use the Datadog API to programmatically create, modify, or delete traces to send to Datadog. This is useful for tracing in-house code not captured by automatic instrumentation, removing unwanted spans from traces, and providing deeper visibility and context into spans, including adding span tags.

{% section displayed-if="Language is Java" %}
This section only applies to users who meet the following criteria: Language is Java

{% alert level="info" %}
The Datadog Java tracer interoperates with the `opentracing-api` library for custom instrumentation. If you would prefer to use the OpenTelemetry API for your custom instrumentation, see [Java Custom Instrumentation using OpenTelemetry](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/server-side/?api_type=otel_api&prog_lang=java) instead.
{% /alert %}

## Prerequisites{% #prerequisites-java %}

- If you have not read the setup instructions for automatic instrumentation, start with the [Java Setup Instructions](https://docs.datadoghq.com/tracing/setup/java/).
- To compile the examples on this page, add the [opentracing-api](https://mvnrepository.com/artifact/io.opentracing/opentracing-api) dependency to your project.

## Adding tags{% #adding-tags-java %}

Add custom [span tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) to your [spans](https://docs.datadoghq.com/tracing/glossary/#spans) to customize your observability within Datadog. The span tags are applied to your incoming traces, allowing you to correlate observed behavior with code-level information such as merchant tier, checkout amount, or user ID.

### Add custom span tags{% #add-custom-span-tags-java %}

Add custom tags to your spans corresponding to any dynamic value within your application code such as `customer.id`.

```
import org.apache.cxf.transport.servlet.AbstractHTTPServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import io.opentracing.Tracer;
import io.opentracing.util.GlobalTracer;

@WebServlet
class ShoppingCartServlet extends AbstractHttpServlet {
    @Override
    void doGet(HttpServletRequest req, HttpServletResponse resp) {
        // Get the active span
        final Span span = GlobalTracer.get().activeSpan();
        if (span != null) {
          // customer_id -> 254889
          // customer_tier -> platinum
          // cart_value -> 867
          span.setTag("customer.id", customer_id);
          span.setTag("customer.tier", customer_tier);
          span.setTag("cart.value", cart_value);
        }
        // [...]
    }
}
```

### Adding tags globally to all spans{% #adding-tags-globally-java %}

The `dd.tags` property allows setting tags across all generated spans for an application. This can be useful for grouping stats for your applications, datacenters, or any other tags you would like to see within the Datadog UI.

```
java -javaagent:<DD-JAVA-AGENT-PATH>.jar \
     -Ddd.tags=datacenter:njc,<TAG_KEY>:<TAG_VALUE> \
     -jar <YOUR_APPLICATION_PATH>.jar
```

### Set errors on a span{% #set-errors-on-a-span-java %}

To customize an error associated with one of your spans, set the error tag on the span and use `Span.log()` to set an "error event". The error event is a `Map<String,Object>` containing a `Fields.ERROR_OBJECT->Throwable` entry, a `Fields.MESSAGE->String`, or both.

```
import io.opentracing.Span;
import io.opentracing.tag.Tags;
import io.opentracing.util.GlobalTracer;
import io.opentracing.log.Fields;
...
    // Get active span if not available in current method
    final Span span = GlobalTracer.get().activeSpan();
    if (span != null) {
      span.setTag(Tags.ERROR, true);
      span.log(Collections.singletonMap(Fields.ERROR_OBJECT, ex));
    }
```

**Note**: `Span.log()` is a generic OpenTracing mechanism for associating events to the current timestamp. The Java Tracer only supports logging error events. Alternatively, you can set error tags directly on the span without `log()`:

```
import io.opentracing.Span;
import io.opentracing.tag.Tags;
import io.opentracing.util.GlobalTracer;
import datadog.trace.api.DDTags;
import java.io.PrintWriter;
import java.io.StringWriter;

...
    final Span span = GlobalTracer.get().activeSpan();
    if (span != null) {
      span.setTag(Tags.ERROR, true);
      span.setTag(DDTags.ERROR_MSG, ex.getMessage());
      span.setTag(DDTags.ERROR_TYPE, ex.getClass().getName());

      final StringWriter errorString = new StringWriter();
      ex.printStackTrace(new PrintWriter(errorString));
      span.setTag(DDTags.ERROR_STACK, errorString.toString());
    }
```

**Note**: You can add any relevant error metadata listed in the [trace view docs](https://docs.datadoghq.com/tracing/glossary/#trace). If the current span isn't the root span, mark it as an error by using the `dd-trace-api` library to grab the root span with `MutableSpan`, then use `setError(true)`. See the [setting tags & errors on a root span](https://docs.datadoghq.com/tracing/custom_instrumentation/java/#set-tags-errors-on-a-root-span-from-a-child-span) section for more details.

### Set tags and errors on a root span from a child span{% #set-tags-errors-root-span-java %}

When an event or condition happens downstream, you may want that behavior or value reflected as a tag on the top level or root span. This can be useful to count an error or for measuring performance, or setting a dynamic tag for observability.

```
import java.util.Collections;
import io.opentracing.Span;
import io.opentracing.Scope;
import datadog.trace.api.interceptor.MutableSpan;
import io.opentracing.log.Fields;
import io.opentracing.util.GlobalTracer;
import io.opentracing.util.Tracer;

Tracer tracer = GlobalTracer.get();
final Span span = tracer.buildSpan("<OPERATION_NAME>").start();
// Note: The scope in the try with resource block below
// will be automatically closed at the end of the code block.
// If you do not use a try with resource statement, you need
// to call scope.close().
try (final Scope scope = tracer.activateSpan(span)) {
    // exception thrown here
} catch (final Exception e) {
    // Set error tag on span as normal
    span.log(Collections.singletonMap(Fields.ERROR_OBJECT, e));

    // Set error on root span
    if (span instanceof MutableSpan) {
        MutableSpan localRootSpan = ((MutableSpan) span).getLocalRootSpan();
        localRootSpan.setError(true);
        localRootSpan.setTag("some.other.tag", "value");
    }
} finally {
    // Close span in a finally block
    span.finish();
}
```

If you are not manually creating a span, you can still access the root span through the `GlobalTracer`:

```
import io.opentracing.Span;
import io.opentracing.util.GlobalTracer;
import datadog.trace.api.interceptor.MutableSpan;

...

final Span span = GlobalTracer.get().activeSpan();
if (span != null && (span instanceof MutableSpan)) {
    MutableSpan localRootSpan = ((MutableSpan) span).getLocalRootSpan();
    // do stuff with root span
}
```

**Note**: Although `MutableSpan` and `Span` share many similar methods, they are distinct types. `MutableSpan` is Datadog specific and not part of the OpenTracing API.

## Adding spans{% #adding-spans-java %}

If you aren't using a [supported framework instrumentation](https://docs.datadoghq.com/tracing/setup/java/#compatibility), or you would like additional depth in your application's [traces](https://docs.datadoghq.com/tracing/glossary/#trace), you may want to add custom instrumentation to your code for complete flame graphs or to measure execution times for pieces of code.

If modifying application code is not possible, use the environment variable `dd.trace.methods` to detail these methods.

If you have existing `@Trace` or similar annotations, or prefer to use annotations to complete any incomplete traces within Datadog, use Trace Annotations.

### Datadog trace methods{% #datadog-trace-methods-java %}

Using the `dd.trace.methods` system property, you can get visibility into unsupported frameworks without changing application code.

```
java -javaagent:/path/to/dd-java-agent.jar -Ddd.env=prod -Ddd.service.name=db-app -Ddd.trace.methods=store.db.SessionManager[saveSession] -jar path/to/application.jar
```

To trace several functions within the same class, use the following syntax:

```
java -javaagent:/path/to/dd-java-agent.jar -Ddd.env=prod -Ddd.service.name=db-app -Ddd.trace.methods=store.db.SessionManager[saveSession,loadSession] -jar path/to/application.jar
```

The only difference between this approach and using `@Trace` annotations is the customization options for the operation and resource names. With DD Trace Methods, `operationName` is `trace.annotation` and `resourceName` is `SessionManager.saveSession`.

### Trace annotations{% #trace-annotations-java %}

Add `@Trace` to methods to have them be traced when running with `dd-java-agent.jar`. If the Agent is not attached, this annotation has no effect on your application.

Datadog's Trace annotation is provided by the [dd-trace-api dependency](https://mvnrepository.com/artifact/com.datadoghq/dd-trace-api).

The available arguments for the `@Trace` annotation are:

- `operationName`: Set the operation name for the trace (default: The method's name).
- `resourceName`: Set the resource name for the trace (default: The same value as `operationName`).
- `noParent`: Set to `true` to always start a new trace at that method. Supported from v1.22.0+ of `dd-trace-java` (default: `false`).

```
import datadog.trace.api.Trace;

public class SessionManager {

    @Trace(operationName = "database.persist", resourceName = "SessionManager.saveSession")
    public static void saveSession() {
        // your method implementation here
    }
}
```

**Note**: Through the `dd.trace.annotations` system property, other tracing method annotations can be recognized by Datadog as `@Trace`. You can find a list in [TraceAnnotationsInstrumentation.java](https://github.com/DataDog/dd-trace-java/blob/master/dd-java-agent/instrumentation/trace-annotation/src/main/java/datadog/trace/instrumentation/trace_annotation/TraceAnnotationsInstrumentation.java#L37) if you have previously decorated your code.

### Manually creating a new span{% #manually-creating-a-new-span-java %}

In addition to automatic instrumentation, the `@Trace` annotation, and `dd.trace.methods` configurations , you can customize your observability by programmatically creating spans around any block of code. Spans created in this manner integrate with other tracing mechanisms automatically. In other words, if a trace has already started, the manual span will have its caller as its parent span. Similarly, any traced methods called from the wrapped block of code will have the manual span as its parent.

```
import datadog.trace.api.DDTags;
import io.opentracing.Scope;
import io.opentracing.Span;
import io.opentracing.Tracer;
import io.opentracing.util.GlobalTracer;

class SomeClass {
    void someMethod() {
        Tracer tracer = GlobalTracer.get();

        // Service and resource name tags are required.
        // You can set them when creating the span:
        Span span = tracer.buildSpan("<OPERATION_NAME>")
            .withTag(DDTags.SERVICE_NAME, "<SERVICE_NAME>")
            .withTag(DDTags.RESOURCE_NAME, "<RESOURCE_NAME>")
            .start();
        // Note: The scope in the try with resource block below
        // will be automatically closed at the end of the code block.
        // If you do not use a try with resource statement, you need
        // to call scope.close().
        try (Scope scope = tracer.activateSpan(span)) {
            // Alternatively, set tags after creation
            span.setTag("my.tag", "value");

            // The code you're tracing

        } catch (Exception e) {
            // Set error on span
        } finally {
            // Close span in a finally block
            span.finish();
        }
    }
}
```

### Extending tracers{% #extending-tracers-java %}

The tracing libraries are designed to be extensible. Customers may consider writing a custom post-processor called a `TraceInterceptor` to intercept Spans then adjust or discard them accordingly (for example, based on regular expressions). The following example implements two interceptors to achieve complex post-processing logic.

```
import java.util.List;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Map;
import datadog.trace.api.interceptor.TraceInterceptor;
import datadog.trace.api.interceptor.MutableSpan;

class FilteringInterceptor implements TraceInterceptor {
    @Override
    public Collection<? extends MutableSpan> onTraceComplete(
            Collection<? extends MutableSpan> trace) {

        List<MutableSpan> filteredTrace = new ArrayList<>();
        for (final MutableSpan span : trace) {
          String orderId = (String) span.getTags().get("order.id");

          // Drop spans when the order id starts with "TEST-"
          if (orderId == null || !orderId.startsWith("TEST-")) {
            filteredTrace.add(span);
          }
        }

        return filteredTrace;
    }

    @Override
    public int priority() {
        // some high unique number so this interceptor is last
        return 100;
    }
}

class PricingInterceptor implements TraceInterceptor {
    @Override
    public Collection<? extends MutableSpan> onTraceComplete(
            Collection<? extends MutableSpan> trace) {

        for (final MutableSpan span : trace) {
          Map<String, Object> tags = span.getTags();
          Double originalPrice = (Double) tags.get("order.price");
          Double discount = (Double) tags.get("order.discount");

          // Set a tag from a calculation from other tags
          if (originalPrice != null && discount != null) {
            span.setTag("order.value", originalPrice - discount);
          }
        }

        return trace;
    }

    @Override
    public int priority() {
        return 20; // some unique number
    }
}
```

Near the start of your application, register the interceptors with the following:

```
datadog.trace.api.GlobalTracer.get().addTraceInterceptor(new FilteringInterceptor());
datadog.trace.api.GlobalTracer.get().addTraceInterceptor(new PricingInterceptor());
```

## Trace client and Agent configuration{% #trace-client-agent-config-java %}

There are additional configurations possible for both the tracing client and Datadog Agent for context propagation, as well as to exclude specific Resources from sending traces to Datadog in the event these traces are not wanted to count in metrics calculated, such as Health Checks.

### Propagating context with headers extraction and injection{% #propagating-context-java %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.

### Resource filtering{% #resource-filtering-java %}

Traces can be excluded based on their resource name, to remove synthetic traffic such as health checks from reporting traces to Datadog. This and other security and fine-tuning configurations can be found on the [Security](https://docs.datadoghq.com/tracing/security) page or in [Ignoring Unwanted Resources](https://docs.datadoghq.com/tracing/guide/ignoring_apm_resources/).
{% /section %}

{% section displayed-if="Language is Python" %}
This section only applies to users who meet the following criteria: Language is Python

If you have not read the setup instructions for automatic instrumentation, start with the [Python Setup Instructions](https://docs.datadoghq.com/tracing/setup/python/).

If you aren't using supported library instrumentation (see [library compatibility](https://docs.datadoghq.com/tracing/compatibility_requirements/python)), you may want to manually instrument your code.

You may also want to extend the functionality of the `ddtrace` library or gain finer control over instrumenting your application. Several techniques are provided by the library to accomplish this.

## Creating spans{% #creating-spans-python %}

The `ddtrace` library creates spans automatically with `ddtrace-run` for [many libraries and frameworks](https://docs.datadoghq.com/tracing/compatibility_requirements/python). However, you may want to gain visibility into your own code and this is achieved by using spans.

Within your web request (for example, `make_sandwich_request`), you may perform several operations, like `get_ingredients()` and `assemble_sandwich()`, which are useful to measure.

```
def make_sandwich_request(request):
    ingredients = get_ingredients()
    sandwich = assemble_sandwich(ingredients)
```

### Using decorators{% #using-decorators-python %}

`ddtrace` provides a decorator `tracer.wrap()` that can be used to decorate the functions of interest. This is useful if you would like to trace the function regardless of where it is being called from.

```
from ddtrace import tracer

@tracer.wrap(service="my-sandwich-making-svc", resource="resource_name")
def get_ingredients():
    # go to the pantry
    # go to the fridge
    # maybe go to the store
    return

# You can provide more information to customize the span
@tracer.wrap("assemble_sandwich", service="my-sandwich-making-svc", resource="resource_name")
def assemble_sandwich(ingredients):
    return
```

To learn more, read [API details for the decorator for `ddtrace.Tracer.wrap()`](https://ddtrace.readthedocs.io/en/stable/api.html#ddtrace.Tracer.wrap).

### Using context managers{% #using-context-managers-python %}

To trace an arbitrary block of code, use the `ddtrace.Span` context manager as below, or view the [advanced usage documentation](https://ddtrace.readthedocs.io/en/stable/advanced_usage.html#ddtrace.Span).

```
from ddtrace import tracer

def make_sandwich_request(request):
    # Capture both operations in a span
    with tracer.trace("sandwich.make"):
        ingredients = get_ingredients()
        sandwich = assemble_sandwich(ingredients)

def make_sandwich_request(request):
    # Capture both operations in a span
    with tracer.trace("sandwich.create", resource="resource_name") as outer_span:

        with tracer.trace("get_ingredients", resource="resource_name") as span:
            ingredients = get_ingredients()

        with tracer.trace("assemble_sandwich", resource="resource_name") as span:
            sandwich = assemble_sandwich(ingredients)
```

To learn more, read the full [API details for `ddtrace.Tracer()`](https://ddtrace.readthedocs.io/en/stable/advanced_usage.html#tracer).

### Manual span creation{% #manual-span-creation-python %}

If the decorator and context manager methods are still not enough to satisfy your tracing needs, a manual API is provided which allows you to start and finish [spans](https://docs.datadoghq.com/tracing/glossary/#spans) however you may require:

```
def make_sandwich_request(request):
    span = tracer.trace("sandwich.create", resource="resource_name")
    ingredients = get_ingredients()
    sandwich = assemble_sandwich(ingredients)
    span.finish()  # remember to finish the span
```

For more API details of the decorator, read the [`ddtrace.Tracer.trace` documentation](https://ddtrace.readthedocs.io/en/stable/advanced_usage.html#ddtrace.Tracer.trace) or the [`ddtrace.Span.finish` documentation](https://ddtrace.readthedocs.io/en/stable/advanced_usage.html#ddtrace.Span.finish).

## Accessing active spans{% #accessing-active-spans-python %}

The built-in instrumentation and your own custom instrumentation create spans around meaningful operations. You can access the active span in order to include meaningful data.

```
from ddtrace import tracer

def make_sandwich_request(request):
    # Capture both operations in a span
    with tracer.trace("sandwich.make") as my_span:
        ingredients = get_ingredients()
        sandwich = assemble_sandwich(ingredients)
```

### Current span{% #current-span-python %}

```
def get_ingredients():
    # Get the active span
    span = tracer.current_span()
    # this span is my_span from make_sandwich_request above
```

### Root span{% #root-span-python %}

```
def assemble_sandwich(ingredients):
    with tracer.trace("another.operation") as another_span:
        # Get the active root span
        span = tracer.current_root_span()
        # this span is my_span from make_sandwich_request above
```

## Adding tags{% #adding-tags-python %}

### Adding tags locally{% #adding-tags-locally-python %}

Tags can be added to a span using the `set_tag` method on a span:

```
from ddtrace import tracer

def make_sandwich_request(request):
    with tracer.trace("sandwich.make") as span:
        ingredients = get_ingredients()
        span.set_tag("num_ingredients", len(ingredients))
```

### Adding tags globally{% #adding-tags-globally-python %}

Tags can be globally set on the tracer. These tags are be applied to every span that is created.

```
from ddtrace import tracer
from myapp import __version__

# This will be applied to every span
tracer.set_tags({"version": __version__, "<TAG_KEY_2>": "<TAG_VALUE_2>"})
```

### Setting errors on a span{% #setting-errors-on-a-span-python %}

Exception information is captured and attached to a span if there is one active when the exception is raised.

```
from ddtrace import tracer

with tracer.trace("throws.an.error") as span:
    raise Exception("Oops!")

# `span` will be flagged as erroneous and have
# the stack trace and exception message attached as tags
```

Flagging a span as erroneous can also be done manually:

```
from ddtrace import tracer

span = tracer.trace("operation")
span.error = 1
span.finish()
```

In the event you want to flag the local root span with the error raised:

```
import os
from ddtrace import tracer

try:
    raise TypeError
except TypeError as e:
    root_span = tracer.current_root_span()
    (exc_type, exc_val, exc_tb) = sys.exc_info()
    # this sets the error type, marks the span as an error, and adds the traceback
    root_span.set_exc_info(exc_type, exc_val, exc_tb)
```

## Propagating context with headers extraction and injection{% #propagating-context-python %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.

### Baggage{% #baggage-python %}

Manipulating [Baggage](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/#baggage) on a span:

```
from ddtrace import tracer

# Start a new span and set baggage
with tracer.trace("example") as span:
    # set_baggage_item
    span.context.set_baggage_item("key1", "value1")
    span.context.set_baggage_item("key2", "value2")

    # get_all_baggage_items
    all_baggage = span.context.get_all_baggage_items()
    print(all_baggage) # {'key1': 'value1', 'key2': 'value2'}

    # remove_baggage_item
    span.context.remove_baggage_item("key1")
    print(span.context.get_all_baggage_items()) # {'key2': 'value2'}

    # get_baggage_item
    print(span.context.get_baggage_item("key1")) # None
    print(span.context.get_baggage_item("key2")) # value2

    # remove_all_baggage_items
    span.context.remove_all_baggage_items()
    print(span.context.get_all_baggage_items()) # {}
```

To see an example in action, see [flask-baggage on trace-examples](https://github.com/DataDog/trace-examples/tree/master/python/flask-baggage).

## ddtrace-api{% #ddtrace-api-python %}

{% alert level="info" %}
The `ddtrace-api` Python package is in Preview and may not include all the API calls you need. If you need more complete functionality, use the API as described in the previous sections.
{% /alert %}

The [ddtrace-api package](https://pypi.org/project/ddtrace-api/) provides a stable public API for Datadog APM's custom Python instrumentation. This package implements only the API interface, not the underlying functionality that creates and sends spans to Datadog.

This separation between interface (`ddtrace-api`) and implementation (`ddtrace`) offers several benefits:

- You can rely on an API that changes less frequently and more predictably for your custom instrumentation
- If you only use automatic instrumentation, you can ignore API changes entirely
- If you implement both single-step and custom instrumentation, you avoid depending on multiple copies of the `ddtrace` package

To use `ddtrace-api`:

1. Install both the `ddtrace` and `ddtrace-api` libraries:

   ```
   pip install 'ddtrace>=3.1' ddtrace-api
   ```

1. Instrument your Python application using `ddtrace-run` by prefixing your Python entry-point command:

   ```
   ddtrace-run python app.py
   ```

1. After this is set up, you can write custom instrumentation exactly like the examples in the previous sections, but you import from `ddtrace_api` instead of `ddtrace`.

For example:

   ```
   from ddtrace_api import tracer

   @tracer.wrap(service="my-sandwich-making-svc", resource="resource_name")
   def get_ingredients():
       # go to the pantry
       # go to the fridge
       # maybe go to the store
       return
   ```

See that package's [API definition](https://datadoghq.dev/dd-trace-api-py/pdocs/ddtrace_api.html) for the full list of supported API calls.
{% /section %}

{% section displayed-if="Language is Node.js" %}
This section only applies to users who meet the following criteria: Language is Node.js

{% alert level="info" %}
If you have not yet read the setup instructions for automatic instrumentation and setup, start with the [Node.js Setup Instructions](https://docs.datadoghq.com/tracing/setup/nodejs/).
{% /alert %}

If you aren't using supported library instrumentation (see [library compatibility](https://docs.datadoghq.com/tracing/compatibility_requirements/nodejs/)), you may want to manually instrument your code.

You may also want to extend the functionality of the `dd-trace` library or gain finer control over instrumenting your application. Several techniques are provided by the library to accomplish this.

## Adding tags{% #adding-tags-nodejs %}

The built-in instrumentation and your own custom instrumentation create spans around meaningful operations.

### Adding tags locally{% #adding-tags-locally-nodejs %}

You can access the active span in order to include meaningful data by adding tags.

```
const span = tracer.scope().active()
```

To learn more, read [API details for `Scope`](https://datadoghq.dev/dd-trace-js/interfaces/Scope.html).

You can add tags to a span using the `setTag` or `addTags` method on a span. Supported value types are string, number, and object.

```
// add a foo:bar tag
span.setTag('foo', 'bar')

// add a user_id:5 tag
span.setTag('user_id', 5)

// add a obj.first:foo and obj.second:bar tags
span.setTag('obj', { first: 'foo', second: 'bar' })

// add a foo:bar and baz:qux tags
span.addTags({
  foo: 'bar',
  baz: 'qux'
})
```

### Adding tags globally{% #adding-tags-globally-nodejs %}

You can add tags to every span by configuring them directly on the tracer, either with the comma-separated `DD_TAGS` environment variable or with the `tags` option on the tracer initialization:

```
// equivalent to DD_TAGS=foo:bar,baz:qux
tracer.init({
  tags: {
    foo: 'bar',
    baz: 'qux'
  }
})

// All spans will now have these tags
```

### Adding tags through component hooks{% #adding-tags-through-component-hooks-nodejs %}

Some Datadog integrations support span hooks that can be used to update the span right before it's finished. This is useful to modify or add tags to a span that is otherwise inaccessible from your code.

```
// at the top of the entry point right after tracer.init()
tracer.use('express', {
  // hook will be executed right before the request span is finished
  hooks: {
    request: (span, req, res) => {
      span.setTag('customer.id', req.query.customer_id)
    }
  }
})
```

To learn more, read [API details for individual plugins](https://datadoghq.dev/dd-trace-js/modules/plugins.html).

### Setting errors on a span{% #setting-errors-on-a-span-nodejs %}

Errors can be added to a span with the special `error` tag that supports error objects. This splits the error into three tags: `error.type`, `error.message`, and `error.stack`.

```
try {
  getIngredients()
} catch (e) {
  span.setTag('error', e)
}

```

When using `tracer.trace()` or `tracer.wrap()` this is done automatically when an error is thrown.

## Creating spans{% #creating-spans-nodejs %}

The `dd-trace` library creates [spans](https://docs.datadoghq.com/tracing/glossary/#spans) automatically with `tracer.init()` for [many libraries and frameworks](https://docs.datadoghq.com/tracing/compatibility_requirements/nodejs/). However, you may want to gain visibility into your own code and this is achieved using spans.

Within your web request (for example, `/make-sandwich`), you may perform several operations, like `getIngredients()` and `assembleSandwich()`, which are useful to measure.

### Synchronous code{% #synchronous-code-nodejs %}

Synchronous code can be traced with `tracer.trace()` which automatically finishes the span when its callback returns and captures any thrown error automatically.

```
app.get('/make-sandwich', (req, res) => {
  const sandwich = tracer.trace('sandwich.make', { resource: 'resource_name' }, () => {
    const ingredients = tracer.trace('get_ingredients', { resource: 'resource_name' }, () => {
      return getIngredients()
    })

    return tracer.trace('assemble_sandwich', { resource: 'resource_name' }, () => {
      assembleSandwich(ingredients)
    })
  })

  res.end(sandwich)
})
```

To learn more, read [API details for `tracer.trace()`](https://datadoghq.dev/dd-trace-js/interfaces/Tracer.html#trace).

### Promises{% #promises-nodejs %}

Promises can be traced with `tracer.trace()` which automatically finishes the span when the returned promise resolves, and captures any rejection error automatically.

```
const getIngredients = () => {
    return new Promise((resolve, reject) => {
        resolve('Salami');
    });
};

app.get('/make-sandwich', (req, res) => {
  return tracer.trace('sandwich.make', { resource: 'resource_name' }, () => {
    return tracer.trace('get_ingredients', { resource: 'resource_name' }, () => getIngredients())
      .then((ingredients) => {
        return tracer.trace('assemble_sandwich', { resource: 'resource_name' }, () => {
          return assembleSandwich(ingredients)
        })
      })
  }).then(sandwich => res.end(sandwich))
})
```

### Async/await{% #async-await-nodejs %}

Async/await can be traced with `tracer.trace()` which automatically finishes the span when the returned promise resolves, and captures any rejection error automatically.

```
app.get('/make-sandwich', async (req, res) => {
  const sandwich = await tracer.trace('sandwich.make', { resource: 'resource_name' }, async () => {
    const ingredients = await tracer.trace('get_ingredients', { resource: 'resource_name' }, () => {
      return getIngredients()
    })

    return tracer.trace('assemble_sandwich', { resource: 'resource_name' }, () => {
      return assembleSandwich(ingredients)
    })
  })

  res.end(sandwich)
})
```

### Wrapper{% #wrapper-nodejs %}

You can wrap an existing function without changing its code. This is useful to trace functions for which you don't control the code. This can be done with `tracer.wrap()` which takes the same arguments as `tracer.trace()` except its last argument which is the function to wrap instead of a callback.

```

// After the functions are defined
getIngredients = tracer.wrap('get_ingredients', { resource: 'resource_name' }, getIngredients)
assembleSandwich = tracer.wrap('assemble_sandwich', { resource: 'resource_name' }, assembleSandwich)

// Where routes are defined
app.get('/make-sandwich', (req, res) => {

  const sandwich = tracer.trace('sandwich.make', { resource: 'resource_name' }, () => {
    const ingredients = getIngredients()

    return assembleSandwich(ingredients)
  })

  res.end(sandwich)
})
```

To learn more, read [API details for `tracer.wrap()`](https://datadoghq.dev/dd-trace-js/interfaces/Tracer.html#wrap).

## Request filtering{% #request-filtering-nodejs %}

You may not want some requests of an application to be instrumented. A common case would be health checks or other synthetic traffic. These can be ignored by using the `blocklist` or `allowlist` option on the `http` plugin.

```
// at the top of the entry point right after tracer.init()
tracer.use('http', {
  blocklist: ['/health', '/ping']
})
```

This configuration can be split between client and server if needed. For example,

```
tracer.use('http', {
  server: {
    blocklist: ['/ping']
  }
})
```

Additionally, traces can be excluded based on their resource name, so that the Agent doesn't send them to Datadog. This and other security and fine-tuning Agent configurations can be found on the [Security](https://docs.datadoghq.com/tracing/security) page or in [Ignoring Unwanted Resources](https://docs.datadoghq.com/tracing/guide/ignoring_apm_resources/).

## dd-trace-api{% #dd-trace-api-nodejs %}

{% alert level="info" %}
The `dd-trace-api` packages is in Preview and may not include all the API calls you need. If you need more complete functionality, use the API as described in the previous sections.
{% /alert %}

The [dd-trace-api package](https://npm.im/dd-trace-api) provides a stable public API for Datadog APM's custom Node.js instrumentation. This package implements only the API interface, not the underlying functionality that creates and sends spans to Datadog.

This separation between interface (`dd-trace-api`) and implementation (`dd-trace`) offers several benefits:

- You can rely on an API that changes less frequently and more predictably for your custom instrumentation
- If you only use automatic instrumentation, you can ignore API changes entirely
- If you implement both single-step and custom instrumentation, you avoid depending on multiple copies of the `dd-trace` package

To use `dd-trace-api`:

1. Install the `dd-trace` and `dd-trace-api` libraries in your app. **Note**: `dd-trace` is installed for you with single-step instrumentation, but you need to install `dd-trace-api` manually in your app.

   ```
   npm install dd-trace dd-trace-api
   ```

1. Instrument your Node.js application using `dd-trace`. If you're using single-step instrumentation, you can skip this step.

   ```
    node --require dd-trace/init app.js
   ```

1. After this is set up, you can write custom instrumentation exactly like the examples in the previous sections, but you require `dd-trace-api` instead of `dd-trace`.

For example:

```
const tracer = require('dd-trace-api')
const express = require('express')
const app = express()

app.get('/make-sandwich', (req, res) => {
  const sandwich = tracer.trace('sandwich.make', { resource: 'resource_name' }, () => {
    const ingredients = tracer.trace('get_ingredients', { resource: 'resource_name' }, () => {
      return getIngredients()
    })

    return tracer.trace('assemble_sandwich', { resource: 'resource_name' }, () => {
      assembleSandwich(ingredients)
    })
  })

  res.end(sandwich)
})
```

See that package's [API definition](https://github.com/DataDog/dd-trace-api-js/blob/master/index.d.ts) for the full list of supported API calls.
{% /section %}

{% section displayed-if="Language is Go" %}
This section only applies to users who meet the following criteria: Language is Go

{% alert level="info" %}
If you have not yet read the instructions for auto-instrumentation and setup, start with the [Go Setup Instructions](https://docs.datadoghq.com/tracing/setup/go/).
{% /alert %}

{% alert level="info" %}
This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.
{% /alert %}

This page details common use cases for adding and customizing observability with Datadog APM.

## Adding tags{% #adding-tags-go %}

Add custom [span tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) to your [spans](https://docs.datadoghq.com/tracing/glossary/#spans) to customize your observability within Datadog. The span tags are applied to your incoming traces, allowing you to correlate observed behavior with code-level information such as merchant tier, checkout amount, or user ID.

### Add custom span tags{% #add-custom-span-tags-go %}

Add [tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) directly to a `Span` interface by calling `SetTag`:

```
package main

import (
    "log"
    "net/http"

    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
)

func handler(w http.ResponseWriter, r *http.Request) {
    // Create a span for a web request at the /posts URL.
    span := tracer.StartSpan("web.request", tracer.ResourceName("/posts"))
    defer span.Finish()

    // Set tag
    span.SetTag("http.url", r.URL.Path)
    span.SetTag("<TAG_KEY>", "<TAG_VALUE>")
}

func main() {
    tracer.Start(tracer.WithService("<SERVICE_NAME>"))
    defer tracer.Stop()
    http.HandleFunc("/posts", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

Datadog's integrations make use of the `Context` type to propagate the current active [span](https://docs.datadoghq.com/tracing/glossary/#spans). If you want to add span tags attached to a `Context`, call the `SpanFromContext` function:

```
package main

import (
    "net/http"

    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
)

func handler(w http.ResponseWriter, r *http.Request) {
    // Retrieve a span for a web request attached to a Go Context.
    if span, ok := tracer.SpanFromContext(r.Context()); ok {
        // Set tag
        span.SetTag("http.url", r.URL.Path)
    }
}
```

### Adding tags globally to all spans{% #adding-tags-globally-go %}

Add [tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) to all [spans](https://docs.datadoghq.com/tracing/glossary/#spans) by configuring the tracer with the `WithGlobalTag` option:

```
package main

import (
    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
)

func main() {
    tracer.Start(
        tracer.WithGlobalTag("datacenter", "us-1"),
        tracer.WithGlobalTag("env", "dev"),
    )
    defer tracer.Stop()
}
```

### Set errors on a span{% #set-errors-on-a-span-go %}

To set an error on one of your spans, use `tracer.WithError` as below:

```
err := someOperation()
span.Finish(tracer.WithError(err))
```

## Adding spans{% #adding-spans-go %}

If you aren't using supported library instrumentation (see [Library compatibility](https://docs.datadoghq.com/tracing/setup/go/#compatibility)), you may want to manually instrument your code.

{% alert level="info" %}
Unlike other Datadog tracing libraries, when tracing Go applications, it's recommended that you explicitly manage and pass the Go context of your spans. This approach helps ensure accurate span relationships and meaningful tracing. For more information, see the [Go context library documentation](https://pkg.go.dev/context) or documentation for any third-party libraries integrated with your application.
{% /alert %}

### Manually creating a span{% #manually-creating-a-span-go %}

To manually create spans, use the `tracer` package (see the [v2 API on Datadog's godoc](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace/tracer); for v1, see the [v1 godoc](https://pkg.go.dev/gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer)).

You can create spans in two ways:

- Start a child from an existing span with [`StartChild` for v2](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace/tracer#StartSpan) or [`StartSpan` for v1](https://pkg.go.dev/gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer#StartSpan).
- Start a span from a context with `StartSpanFromContext` (see API details for [v2](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace/tracer#StartSpanFromContext) or [v1](https://pkg.go.dev/gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer#StartSpanFromContext)).

```
//v2: Create a span with a resource name, which is the child of parentSpan.
span := parentSpan.StartChild("mainOp", tracer.ResourceName("/user"))

//v1: Create a span with a resource name, which is the child of parentSpan.
span := tracer.StartSpan("mainOp", tracer.ResourceName("/user"), tracer.ChildOf(parentSpan))

// v1 and v2: Create a span which will be the child of the span in the Context ctx, if there is a span in the context.
// Returns the new span, and a new context containing the new span.
span, ctx := tracer.StartSpanFromContext(ctx, "mainOp", tracer.ResourceName("/user"))
```

### Asynchronous traces{% #asynchronous-traces-go %}

```
func main() {
    span, ctx := tracer.StartSpanFromContext(context.Background(), "mainOp")
    defer span.Finish()

    go func() {
        asyncSpan := tracer.StartSpanFromContext(ctx, "asyncOp")
        defer asyncSpan.Finish()
        performOp()
    }()
}
```

### Distributed tracing{% #distributed-tracing-go %}

Create a distributed [trace](https://docs.datadoghq.com/tracing/glossary/#trace) by manually propagating the tracing context:

```
package main

import (
    "net/http"

    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
)

func handler(w http.ResponseWriter, r *http.Request) {
    span, ctx := tracer.StartSpanFromContext(r.Context(), "post.process")
    defer span.Finish()

    req, err := http.NewRequest("GET", "http://example.com", nil)
    req = req.WithContext(ctx)
    // Inject the span Context in the Request headers
    err = tracer.Inject(span.Context(), tracer.HTTPHeadersCarrier(req.Header))
    if err != nil {
        // Handle or log injection error
    }
    http.DefaultClient.Do(req)
}
```

Then, on the server side, to continue the trace, start a new [Span](https://docs.datadoghq.com/tracing/glossary/#spans) from the extracted `Context`:

```
package main

import (
    "net/http"

    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
)

func handler(w http.ResponseWriter, r *http.Request) {
    // Extract the span Context and continue the trace in this service
    sctx, err := tracer.Extract(tracer.HTTPHeadersCarrier(r.Header))
    if err != nil {
        // Handle or log extraction error
    }

    span := tracer.StartSpan("post.filter", tracer.ChildOf(sctx))
    defer span.Finish()
}
```

## Trace client and Agent configuration{% #trace-client-agent-config-go %}

There are additional configurations possible for both the tracing client and Datadog Agent for context propagation with B3 Headers, as well as excluding specific resources from sending traces to Datadog in the event these traces are not wanted in metrics calculated, such as Health Checks.

### Propagating context with headers extraction and injection{% #propagating-context-go %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.

### Resource filtering{% #resource-filtering-go %}

Traces can be excluded based on their resource name, to remove synthetic traffic such as health checks from reporting traces to Datadog. This and other security and fine-tuning configurations can be found on the [Security](https://docs.datadoghq.com/tracing/security) page.
{% /section %}

{% section displayed-if="Language is Ruby" %}
This section only applies to users who meet the following criteria: Language is Ruby

{% alert level="info" %}
If you have not yet read the instructions for auto-instrumentation and setup, read the [Ruby Setup Instructions](https://docs.datadoghq.com/tracing/setup/ruby/).
{% /alert %}

This page details describes use cases for adding and customizing observability with Datadog APM.

## Requirements{% #requirements-ruby %}

Make sure you require the appropriate gem for your [Ruby tracer version](https://github.com/DataDog/dd-trace-rb/releases):

- For v2.x, require the `datadog` gem:

  ```
  require 'datadog'
  ```

- For v1.x, require the `ddtrace` gem:

  ```
  require 'ddtrace'
  ```

## Adding tags{% #adding-tags-ruby %}

Add custom [span tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) to your [spans](https://docs.datadoghq.com/tracing/glossary/#spans) to customize your observability within Datadog. The span tags are applied to your incoming traces, allowing you to correlate observed behavior with code-level information such as merchant tier, checkout amount, or user ID.

### Add custom span tags{% #add-custom-span-tags-ruby %}

Add custom tags to your spans corresponding to any dynamic value within your application code such as `customer.id`.

#### Active spans{% #active-spans-ruby %}

Access the current active [span](https://docs.datadoghq.com/tracing/glossary/#span-tags) from any method within your code.

**Note**: If the method is called and there is no active span, `active_span` is `nil`.

```
# get '/shopping_cart/:customer_id', to: 'shopping_cart#index'
class ShoppingCartController < ApplicationController
  # GET /shopping_cart
  def index
    # Get the active span and set customer_id -> 254889
    Datadog::Tracing.active_span&.set_tag('customer.id', params.permit([:customer_id]))

    # [...]
  end

  # POST /shopping_cart
  def create
    # [...]
  end
end
```

#### Manually instrumented spans{% #manually-instrumented-spans-ruby %}

Add [tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) directly to `Datadog::Span` objects by calling `#set_tag`:

```
# An example of a Sinatra endpoint,
# with Datadog tracing around the request.
get '/posts' do
  Datadog::Tracing.trace('web.request') do |span|
    span.set_tag('http.url', request.path)
    span.set_tag('<TAG_KEY>', '<TAG_VALUE>')
  end
end
```

### Adding tags globally to all spans{% #adding-tags-globally-ruby %}

Add [tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) to all [spans](https://docs.datadoghq.com/tracing/glossary/#spans) by configuring the tracer with the `tags` option:

```
Datadog.configure do |c|
  c.tags = { 'team' => 'qa' }
end
```

You can also use the `DD_TAGS` environment variable to set tags on all spans for an application. For more information on Ruby environment variables, read the [setup documentation](https://docs.datadoghq.com/tracing/setup/ruby/#environment-and-tags).

### Setting errors on a span{% #setting-errors-on-a-span-ruby %}

There are two ways to set an error on a span:

- Call `span.set_error` and pass in the Exception Object. This automatically extracts the error type, message, and backtrace.

```
require 'timeout'

def example_method
  span = Datadog::Tracing.trace('example.trace')
  puts 'some work'
  sleep(1)
  raise StandardError, "This is an exception"
rescue StandardError => error
  Datadog::Tracing.active_span&.set_error(error)
  raise
ensure
  span.finish
end

example_method()
```

- Or, use `tracer.trace` which by default sets the error type, message, and backtrace. To configure this behavior you can use the `on_error` option, which is the Handler invoked when a block is provided to `trace`, and the block raises an error. The Proc is provided `span` and `error` as arguments. By default, `on_error` sets error on the span.

Default behavior for `on_error`:

```
require 'timeout'

def example_method
  puts 'some work'
  sleep(1)
  raise StandardError, "This is an exception"
end

Datadog::Tracing.trace('example.trace') do |span|
  example_method()
end
```

Custom behavior for `on_error`:

```
require 'timeout'

def example_method
  puts 'some work'
  sleep(1)
  raise StandardError.new "This is a special exception"
end

custom_error_handler = proc do |span, error|
  span.set_tag('custom_tag', 'custom_value')
  span.set_error(error) unless error.message.include?("a special exception")
end

Datadog::Tracing.trace('example.trace', on_error: custom_error_handler) do |span|
  example_method()
end
```

## Adding spans{% #adding-spans-ruby %}

If you aren't using supported library instrumentation (see [library compatibility](https://docs.datadoghq.com/tracing/compatibility_requirements/ruby/)), you can manually instrument your code. Add tracing to your code by using the `Datadog::Tracing.trace` method, which you can wrap around any Ruby code.

To trace any Ruby code, you can use the `Datadog::Tracing.trace` method:

```
Datadog::Tracing.trace(name, resource: resource, **options) do |span|
  # Wrap this block around the code you want to instrument
  # Additionally, you can modify the span here.
  # for example, change the resource name, or set tags
end
```

Where `name` is a `String` that describes the generic kind of operation being done (for example `'web.request'`, or `'request.parse'`).

`resource` is a `String` with the name of the action being operated on. Traces with the same resource value will be grouped together for the purpose of metrics. Resources are usually domain specific, such as a URL, query, request, etc. (e.g. 'Article#submit', http://example.com/articles/list.)

For all the available `**options`, see the [reference guide](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ruby/#manual-instrumentation).

### Manually creating a new span{% #manually-creating-a-new-span-ruby %}

Programmatically create spans around any block of code. Spans created in this manner integrate with other tracing mechanisms automatically. In other words, if a trace has already started, the manual span will have its caller as its parent span. Similarly, any traced methods called from the wrapped block of code will have the manual span as its parent.

```
# An example of a Sinatra endpoint,
# with Datadog tracing around the request,
# database query, and rendering steps.
get '/posts' do
  Datadog::Tracing.trace('web.request', service: '<SERVICE_NAME>', resource: 'GET /posts') do |span|
    # Trace the activerecord call
    Datadog::Tracing.trace('posts.fetch') do
      @posts = Posts.order(created_at: :desc).limit(10)
    end

    # Add some APM tags
    span.set_tag('http.method', request.request_method)
    span.set_tag('posts.count', @posts.length)

    # Trace the template rendering
    Datadog::Tracing.trace('template.render') do
      erb :index
    end
  end
end
```

### Post-processing traces{% #post-processing-traces-ruby %}

Some applications might require that traces be altered or filtered out before they are sent to Datadog. The processing pipeline allows you to create *processors* to define such behavior.

#### Filtering{% #filtering-ruby %}

You can use the `Datadog::Tracing::Pipeline::SpanFilter` processor to remove spans, when the block evaluates as truthy:

```
Datadog::Tracing.before_flush(
  # Remove spans that match a particular resource
  Datadog::Tracing::Pipeline::SpanFilter.new { |span| span.resource =~ /PingController/ },
  # Remove spans that are trafficked to localhost
  Datadog::Tracing::Pipeline::SpanFilter.new { |span| span.get_tag('host') == 'localhost' }
)
```

#### Processing{% #processing-ruby %}

You can use the `Datadog::Tracing::Pipeline::SpanProcessor` processor to modify spans:

```
Datadog::Tracing.before_flush(
  # Strip matching text from the resource field
  Datadog::Tracing::Pipeline::SpanProcessor.new { |span| span.resource.gsub!(/password=.*/, '') }
)
```

#### Custom processor{% #custom-processor-ruby %}

Processors can be any object that responds to `#call` accepting `trace` as an argument (which is an `Array` of `Datadog::Span`.)

For example, using the short-hand block syntax:

```
Datadog::Tracing.before_flush do |trace|
   # Processing logic...
   trace
end
```

The following example implements a processor to achieve complex post-processing logic:

```
Datadog::Tracing.before_flush do |trace|
  trace.spans.each do |span|
    originalPrice = span.get_tag('order.price'))
    discount = span.get_tag('order.discount'))

    # Set a tag from a calculation from other tags
    if (originalPrice != nil && discount != nil)
      span.set_tag('order.value', originalPrice - discount)
    end
  end
  trace
end
```

For a custom processor class:

```
class MyCustomProcessor
  def call(trace)
    # Processing logic...
    trace
  end
end

Datadog::Tracing.before_flush(MyCustomProcessor.new)
```

In both cases, the processor method *must* return the `trace` object; this return value will be passed to the next processor in the pipeline.

## Trace client and Agent configuration{% #trace-client-agent-config-ruby %}

There are additional configurations possible for both the tracing client and Datadog Agent for context propagation with B3 Headers, as well as to exclude specific Resources from sending traces to Datadog in the event these traces are not wanted to count in metrics calculated, such as Health Checks.

### Propagating context with headers extraction and injection{% #propagating-context-ruby %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.

#### Baggage{% #baggage-ruby %}

Baggage is a hash that can be accessed through the API and is propagated by default. See the following example to manipulate [Baggage](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/#baggage):

```
# set_baggage_item
Datadog::Tracing.baggage['key1'] = 'value1'
Datadog::Tracing.baggage['key2'] = 'value2'

# get_all_baggage_items
all_baggage = Datadog::Tracing.baggage
puts(all_baggage) # {"key1"=>"value1", "key2"=>"value2"}

# remove_baggage_item
Datadog::Tracing.baggage.delete('key1')
puts(Datadog::Tracing.baggage) # {"key2"=>"value2"}

# get_baggage_item
puts(Datadog::Tracing.baggage['key1']) # nil
puts(Datadog::Tracing.baggage['key2']) # "value2"

# remove_all_baggage_items
Datadog::Tracing.baggage.clear
puts(Datadog::Tracing.baggage) # {}
```

### Resource filtering{% #resource-filtering-ruby %}

Traces can be excluded based on their resource name, to remove synthetic traffic such as health checks from reporting traces to Datadog. This and other security and fine-tuning configurations can be found on the [Security](https://docs.datadoghq.com/tracing/security) page.
{% /section %}

{% section displayed-if="Language is .NET" %}
This section only applies to users who meet the following criteria: Language is .NET

{% alert level="info" %}
If you have not yet read the instructions for automatic instrumentation and setup, start with the [.NET/.NET Core](https://docs.datadoghq.com/tracing/setup/dotnet-core/) or [.NET Framework](https://docs.datadoghq.com/tracing/setup/dotnet-framework/) Setup Instructions.
{% /alert %}

This page details common use cases for adding and customizing observability with Datadog APM. For a list of supported runtimes, see the [.NET Framework Compatibility Requirements](https://docs.datadoghq.com/tracing/trace_collection/compatibility/dotnet-framework) or the [.NET Core Compatibility Requirements](https://docs.datadoghq.com/tracing/trace_collection/compatibility/dotnet-core).

There are several ways to get more than the [default automatic instrumentation](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-core):

- Through configuration, which does not allow you to add specific tags.
- Using attributes, which allows you to customize operation and resource names.
- Using custom code, which gives you the most control on the spans.

You can combine these solutions with each other to achieve the instrumentation detail you want. However, automatic instrumentation must be setup first.

## Instrument methods through configuration{% #instrument-methods-through-configuration-dotnet %}

Using the `DD_TRACE_METHODS` environment variable, you can get visibility into unsupported frameworks without changing application code. For full details on the input format for `DD_TRACE_METHODS`, see the [.NET Framework configuration instructions](https://docs.datadoghq.com/tracing/trace_collection/library_config/dotnet-framework/#automatic-instrumentation-optional-configuration) or the [.NET Core configuration instructions](https://docs.datadoghq.com/tracing/trace_collection/library_config/dotnet-core/#automatic-instrumentation-optional-configuration). For example, to instrument a method called `SaveSession` defined on the `Store.Managers.SessionManager` type, set:

```
DD_TRACE_METHODS=Store.Managers.SessionManager[SaveSession]
```

The resulting span has an `operationName` attribute with the value `trace.annotation` and a `resourceName` attribute with the value `SaveSession`.

If you want to customize the span's attributes and you have the ability to modify the source code, you can instrument methods through attributes instead.

## Instrument methods through attributes{% #instrument-methods-through-attributes-dotnet %}

Add `[Trace]` to methods for Datadog to trace them when running with automatic instrumentation. If automatic instrumentation is not enabled, this attribute has no effect on your application.

`[Trace]` attributes have the default operation name `trace.annotation` and resource name of the traced method. You can set **operation name** and **resource name** as named arguments of the `[Trace]` attribute to better reflect what is being instrumented. Operation name and resource name are the only possible arguments that can be set for the `[Trace]` attribute. For example:

```
using Datadog.Trace.Annotations;

namespace Store.Managers
{
    public class SessionManager
    {
        [Trace(OperationName = "database.persist", ResourceName = "SessionManager.SaveSession")]
        public static void SaveSession()
        {
            // your method implementation here
        }
    }
}
```

## Custom instrumentation with code{% #custom-instrumentation-with-code-dotnet %}

{% alert level="info" %}
This feature requires adding the [`Datadog.Trace` NuGet package](https://www.nuget.org/packages/Datadog.Trace) to your application. It provides an API to directly access the Tracer and the active span.
{% /alert %}

{% alert level="danger" %}
Starting with v3.0.0, custom instrumentation requires you also use automatic instrumentation. You should aim to keep both automatic and custom instrumentation package versions (for example: MSI and NuGet) in sync, and ensure you don't mix major versions of packages.
{% /alert %}

### Configuring Datadog in code{% #configuring-datadog-in-code-dotnet %}

There are multiple ways to configure your application: using environment variables, a `web.config` file, or a `datadog.json` file, [as described in our documentation](https://docs.datadoghq.com/tracing/trace_collection/library_config/dotnet-core/). The `Datadog.Trace` NuGet package also allows you to configure settings in code.

To override configuration settings, create an instance of `TracerSettings`, and pass it to the static `Tracer.Configure()` method:

```
using Datadog.Trace;

// Create a settings object using the existing
// environment variables and config sources
var settings = TracerSettings.FromDefaultSources();

// Override a value
settings.GlobalTags.Add("SomeKey", "SomeValue");

// Replace the tracer configuration
Tracer.Configure(settings);
```

Calling `Tracer.Configure()` replaces the settings for all subsequent traces, both for custom instrumentation and for automatic instrumentation.

{% alert level="danger" %}
Replacing the configuration should be done **once, as early as possible** in your application.
{% /alert %}

### Create custom traces/spans{% #create-custom-traces-spans-dotnet %}

In addition to automatic instrumentation, the `[Trace]` attribute, and `DD_TRACE_METHODS` configurations, you can customize your observability by programmatically creating spans around any block of code.

To create and activate a custom span, use `Tracer.Instance.StartActive()`. If a trace is already active (when created by automatic instrumentation, for example), the span is part of the current trace. If there is no current trace, a new one is started.

{% alert level="danger" %}
Ensure you dispose of the scope returned from `StartActive`. Disposing the scope closes the span, and ensures the trace is flushed to Datadog once all its spans are closed.
{% /alert %}

```
using Datadog.Trace;

// Start a new span
using (var scope = Tracer.Instance.StartActive("custom-operation"))
{
    // Do something
}
```

Add custom [span tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) to your [spans](https://docs.datadoghq.com/tracing/glossary/#spans) to customize your observability within Datadog. The span tags are applied to your incoming traces, allowing you to correlate observed behavior with code-level information such as merchant tier, checkout amount, or user ID.

### Manually creating a new span{% #manually-creating-a-new-span-dotnet %}

Manually created spans automatically integrate with spans from other tracing mechanisms. In other words, if a trace has already started, the manual span has its caller as its parent span. Similarly, any traced methods called from the wrapped block of code have the manual span as its parent.

```
using (var parentScope =
       Tracer.Instance.StartActive("manual.sortorders"))
{
    parentScope.Span.ResourceName = "<RESOURCE NAME>";
    using (var childScope =
           Tracer.Instance.StartActive("manual.sortorders.child"))
    {
        // Nest using statements around the code to trace
        childScope.Span.ResourceName = "<RESOURCE NAME>";
        SortOrders();
    }
}
```

### Add custom span tags{% #add-custom-span-tags-dotnet %}

Add custom tags to your spans corresponding to any dynamic value within your application code such as `customer.id`.

```
using Datadog.Trace;

public class ShoppingCartController : Controller
{
    private IShoppingCartRepository _shoppingCartRepository;

    [HttpGet]
    public IActionResult Index(int customerId)
    {
        // Access the active scope through the global tracer
        // Note: This can return null if there is no active span
        var scope = Tracer.Instance.ActiveScope;

        if (scope != null)
        {
            // Add a tag to the span for use in the Datadog web UI
            scope.Span.SetTag("customer.id", customerId.ToString());
        }

        var cart = _shoppingCartRepository.Get(customerId);

        return View(cart);
    }
}
```

### Usage with ASP.NET `IHttpModule`{% #usage-with-aspnet-ihttpmodule-dotnet %}

To access the current request span from a custom ASP.NET `IHttpModule`, it is best to read `Tracer.Instance.ActiveScope` in the `PreRequestHandlerExecute` event (or `AcquireRequestState` if you require session state).

While Datadog creates the request span at the start of the ASP.NET pipeline, the execution order of `IHttpModules` is not guaranteed. If your module runs before Datadog's, `ActiveScope` may be `null` during early events like `BeginRequest`. The `PreRequestHandlerExecute` event occurs late enough in the lifecycle to help ensure the Datadog module has run and the span is available.

`ActiveScope` can still be `null` for other reasons (for example, if instrumentation is disabled), so you should always check for `null`.

```
using System;
using System.Web;
using Datadog.Trace;

public class MyCustomModule : IHttpModule
{
    public void Init(HttpApplication context)
    {
        // Prefer reading ActiveScope late in the pipeline
        context.PreRequestHandlerExecute += OnPreRequestHandlerExecute;

        // If you need session state, you can also hook AcquireRequestState:
        // context.AcquireRequestState += OnPreRequestHandlerExecute;
    }

    private void OnPreRequestHandlerExecute(object sender, EventArgs e)
    {
        // Earlier events (e.g., BeginRequest) may run before the Datadog module,
        // so ActiveScope can be null there. Here it should be available.
        var scope = Tracer.Instance.ActiveScope;
        if (scope == null)
        {
            return; // there is no active scope, for example, if instrumentation is disabled
        }

        // Example: add a custom tag
        scope.Span.SetTag("my.custom.tag", "some_value");
    }

    public void Dispose()
    {
    }
}
```

### Set errors on a span{% #set-errors-on-a-span-dotnet %}

To mark errors that occur in your code, use the `Span.SetException(Exception)` method. The method marks the span as an error and adds [related span metadata](https://docs.datadoghq.com/tracing/glossary/#span-tags) to provide insight into the exception.

```
try
{
    // do work that can throw an exception
}
catch(Exception e)
{
    span.SetException(e);
}
```

This sets the following tags on the span:

- `"error.message":exception.Message`
- `"error.stack":exception.ToString()`
- `"error.type":exception.GetType().ToString()`

## Propagating context with headers extraction and injection{% #propagating-context-dotnet %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.

## Adding tags globally to all spans{% #adding-tags-globally-dotnet %}

Use the `DD_TAGS` environment variable to set tags across all generated spans for an application. This can be useful for grouping stats for your applications, data centers, or regions within the Datadog UI. For example:

```
DD_TAGS=datacenter:njc,key2:value2
```

## Resource filtering{% #resource-filtering-dotnet %}

You can exclude traces based on the resource name to remove Synthetics traffic such as health checks. For more information about security and additional configurations, see [Configure the Datadog Agent or Tracer for Data Security](https://docs.datadoghq.com/tracing/security).
{% /section %}

{% section displayed-if="Language is PHP" %}
This section only applies to users who meet the following criteria: Language is PHP

{% alert level="info" %}
If you have not yet read the instructions for auto-instrumentation and setup, start with the [PHP Setup Instructions](https://docs.datadoghq.com/tracing/setup/php/). Even if Datadog does not officially support your web framework, you may not need to perform any manual instrumentation. See [automatic instrumentation](https://docs.datadoghq.com/tracing/setup/php/#automatic-instrumentation) for more details.
{% /alert %}

## Annotations{% #annotations-php %}

If you are using PHP 8, as of v0.84 of the tracer, you can add attributes to your code to instrument it. It is a lighter alternative to custom instrumentation written in code. For example, add the `#[DDTrace\Trace]` attribute to methods for Datadog to trace them.

```
<?php
class Server {
    #[\DDTrace\Trace(name: "spanName", resource: "resourceName", type: "Custom", service: "myService", tags: ["aTag" => "aValue"])]
    static function process($arg) {}

    #[\DDTrace\Trace]
    function get() {
      Foo::simple(1);
    }
}
```

You can provide the following arguments:

- `$name`: The operation name to be assigned to the span. Defaults to the function name.
- `$resource`: The resource to be assigned to the span.
- `$type`: The type to be assigned to the span.
- `$service`: The service to be assigned to the span. Defaults to default or inherited service name.
- `$tags`: The tags to be assigned to the span.
- `$recurse`: Whether recursive calls shall be traced.
- `$run_if_limited`: Whether the function shall be traced in limited mode. (For example, when span limit exceeded)

{% alert level="danger" %}
If a namespace is present, you **must** use the fully qualified name of the attribute `#[\DDTrace\Trace]`. Alternatively, you can import the namespace with `use DDTrace\Trace;` and use `#[Trace]`.
{% /alert %}

## Writing custom instrumentation{% #writing-custom-instrumentation-php %}

{% alert level="info" %}
To write custom instrumentation, you do not need any additional composer package.
{% /alert %}

{% alert level="info" %}
The Datadog APM PHP Api is fully documented [in stubs](https://github.com/DataDog/dd-trace-php/blob/master/ext/ddtrace.stub.php). This allows you to have automated documentation in PHPStorm.
{% /alert %}

### A sample application to be instrumented{% #sample-application-php %}

Assume the following directory structure:

```
.
|-- composer.json
|-- docker-compose.yml
|-- index.php
`-- src
    |-- Exceptions
    |   `-- NotFound.php
    |-- Services
    |   `-- SampleRegistry.php
    `-- utils
        `-- functions.php
```

Within this, two files contain the functions and methods that are interesting to instrument. The most relevant files are `src/utils/functions.php`:

```
namespace App;

function some_utility_function($someArg)
{
    return 'result';
}
```

And `src/Services/SampleRegistry.php`:

```
namespace App\Services;

use App\Exceptions\NotFound;
use Exception;

class SampleRegistry
{
    public function put($key, $value)
    {
        \App\some_utility_function('some argument');
        // Return the id of the item inserted
        return 456;
    }

    public function faultyMethod()
    {
        throw new Exception('Generated at runtime');
    }

    public function get($key)
    {
        // The service uses an exception to report a key not found.
        throw new NotFound('The key was not found');
    }

    public function compact()
    {
        // This function executes some operations on the registry and
        // returns nothing. In the middle of the function, we have an
        // interesting value that is not returned but can be related
        // to the slowness of the function

        $numberOfItemsProcessed = 123;

        // ...
    }
}
```

### Steps to instrument the sample application{% #steps-to-instrument-php %}

To avoid mixing application or service business logic with instrumentation code, write the required code in a separate file:

1. Create a file `datadog/instrumentation.php` and add it to the composer autoloader:

   ```
   {
       ...
       "autoload": {
           ...
           "files": [
               ...
               "datadog/instrumentation.php"
           ]
       },
       ...
   }
   ```

1. Dump the autoloader by running `composer dump`.
Important alert (level: info):
The file that contains the custom instrumentation code and the actual classes that are instrumented are not required to be in the same codebase and package. By separating them, you can publish an open source composer package containing only your instrumentation code, which others might find useful.

1. In the `datadog/instrumentation.php` file, check if the extension is loaded:

   ```
   if (!extension_loaded('ddtrace')) {
       return;
   }
   ```

1. Instrument a function. For `\App\some_utility_function`, if you are not interested in any specific aspect of the function other than the execution time:

   ```
   \DDTrace\trace_function('App\some_utility_function', function (\DDTrace\SpanData $span, $args, $ret, $exception) {});
   ```

1. For the `SampleRegistry::put` method, add tags with the returned item identifier and the key. Because `put` is a method, use `\DDTrace\trace_method` instead of `\DDTrace\trace_function`:

   ```
   \DDTrace\trace_method(
       'App\Services\SampleRegistry',
       'put',
       function (\DDTrace\SpanData $span, $args, $ret, $exception) {
           $span->meta['app.cache.key'] = $args[0]; // The first argument is the 'key'
           $span->meta['app.cache.item_id'] = $ret; // The returned value
       }
   );
   ```

1. For `SampleRegistry::faultyMethod`, which generates an exception, there is nothing extra to do. If the method is instrumented, the default exception reporting mechanism attaches the exception message and stack trace.

1. For `SampleRegistry::get`, which uses a `NotFound` exception as part of business logic, you can prevent marking the span as an error by unsetting the exception:

   ```
   \DDTrace\trace_method(
       'App\Services\SampleRegistry',
       'get',
       function (\DDTrace\SpanData $span, $args, $ret, $exception) {
           if ($exception instanceof \App\Exceptions\NotFound) {
               unset($span->exception);
               $span->resource = 'cache.get.not_found';
           }
       }
   );
   ```

1. For `SampleRegistry::compact`, to add a tag with a value that is neither an argument nor the return value, you can access the active span directly from within the method:

   ```
   public function compact()
   {
       $numberOfItemsProcessed = 123;

       // Add instrumenting code within your business logic.
       if (\function_exists('\DDTrace\active_span') && $span = \DDTrace\active_span()) {
           $span->meta['registry.compact.items_processed'] = $numberOfItemsProcessed;
       }

       // ...
   }
   ```

## Details about `trace_function` and `trace_method`{% #details-trace-function-method-php %}

The `DDTrace\trace_function` and `DDTrace\trace_method` functions instrument (trace) specific function and method calls. These functions automatically handle the following tasks:

- Open a [span](https://docs.datadoghq.com/tracing/glossary/#spans) before the code executes.
- Set any errors from the instrumented call on the span.
- Close the span when the instrumented call is done.

Additional [tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) are set on the span from the closure (called a tracing closure).

For example, the following snippet traces the `CustomDriver::doWork` method and adds custom tags:

```
<?php
\DDTrace\trace_method(
    'CustomDriver',
    'doWork',
    function (\DDTrace\SpanData $span, array $args, $retval, $exception) {
        // This closure runs after the instrumented call
        $span->name = 'CustomDriver.doWork';
        $span->resource = 'CustomDriver.doWork';
        $span->service = 'php';

        // If an exception was thrown from the instrumented call, return value is null
        $span->meta['doWork.size'] = $exception ? 0 : count($retval),
        // Access object members via $this
        $span->meta['doWork.thing'] = $this->workToDo;
    }
);
?>
```

## Accessing active spans{% #accessing-active-spans-php %}

The built-in instrumentation and your own custom instrumentation creates spans around meaningful operations. You can access the active span in order to include meaningful data.

### Current span{% #current-span-php %}

The following method returns a `DDTrace\SpanData` object. When tracing is disabled, `null` is returned.

```
<?php
$span = \DDTrace\active_span();
if ($span) {
    $span->meta['customer.id'] = get_customer_id();
}
?>
```

### Root span{% #root-span-php %}

The following method returns a `DDTrace\SpanData` object. When tracing is disabled, `null` is returned. This is useful in contexts where the metadata to be added to the root span does not exist in early script execution.

```
<?php
$span = \DDTrace\root_span();
if ($span) {
    $span->meta['customer.id'] = get_customer_id();
}
?>
```

## Adding tags{% #adding-tags-php %}

{% alert level="danger" %}
When you set tags, to avoid overwriting existing tags automatically added by the Datadog core instrumentation, **do write `$span->meta['mytag'] = 'value'`**. Do not write `$span->meta = ['mytag' => 'value']`.
{% /alert %}

### Adding tags locally{% #adding-tags-locally-php %}

Add tags to a span by using the `DDTrace\SpanData::$meta` array.

```
<?php

\DDTrace\trace_function(
    'myRandFunc',
    function(\DDTrace\SpanData $span, array $args, $retval) {
        // ...
        $span->meta['rand.range'] = $args[0] . ' - ' . $args[1];
        $span->meta['rand.value'] = $retval;
    }
);
```

### Adding tags globally{% #adding-tags-globally-php %}

Set the `DD_TAGS` environment variable (version 0.47.0+) to automatically apply tags to every span that is created.

```
DD_TAGS=key1:value1,<TAG_KEY>:<TAG_VALUE>
```

### Setting errors on a span{% #setting-errors-on-a-span-php %}

Thrown exceptions are automatically attached to the active span, unless the exception is thrown at a deeper level in the call stack and it is caught before it reaches any function that is traced.

```
<?php

function doRiskyThing() {
    throw new Exception('Oops!');
}

\DDTrace\trace_function(
    'doRiskyThing',
    function() {
        // Span will be flagged as erroneous and have
        // the stack trace and exception message attached as tags
    }
);
```

Set the `error.message` tag to manually flag a span as erroneous.

```
<?php

function doRiskyThing() {
    return SOME_ERROR_CODE;
}

\DDTrace\trace_function(
    'doRiskyThing',
    function(\DDTrace\SpanData $span, $args, $retval) {
        if ($retval === SOME_ERROR_CODE) {
            $span->meta['error.message'] = 'Foo error';
            // Optional:
            $span->meta['error.type'] = 'CustomError';
            $span->meta['error.stack'] = (new \Exception)->getTraceAsString();
        }
    }
);
```

## Adding span links{% #adding-span-links-php %}

Span links associate one or more spans together that don't have a typical parent-child relationship. They may associate spans within the same trace or spans across different traces.

To add a span link from an existing span:

```
$spanA = \DDTrace\start_trace_span();
$spanA->name = 'spanA';
\DDTrace\close_span();

$spanB = \DDTrace\start_trace_span();
$spanB->name = 'spanB';
// Link spanB to spanA
$spanB->links[] = $spanA->getLink();
\DDTrace\close_span();
```

## Context propagation for distributed traces{% #context-propagation-php %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.

## Resource filtering{% #resource-filtering-php %}

Traces can be excluded based on their resource name, to remove synthetic traffic such as health checks from reporting traces to Datadog. This and other security and fine-tuning configurations can be found on the [Security](https://docs.datadoghq.com/tracing/security) page.

## API reference{% #api-reference-php %}

{% alert level="info" %}
The Datadog APM PHP Api is fully documented [in stubs](https://github.com/DataDog/dd-trace-php/blob/master/ext/ddtrace.stub.php). This allows you to have automated documentation in PHPStorm.
{% /alert %}

### Parameters of the tracing closure{% #parameters-tracing-closure-php %}

The tracing closure provided to `DDTrace\trace_method()` and `DDTrace\trace_function()` has four parameters:

```
function(
    DDTrace\SpanData $span,
    array $args,
    mixed $retval,
    Exception|null $exception
);
```

1. **$span**: An instance of `DDTrace\SpanData` to write to the span properties
1. **$args**: An `array` of arguments from the instrumented call
1. **$retval**: The return value of the instrumented call
1. **$exception**: An instance of the exception that was thrown in the instrumented call or `null` if no exception was thrown

## Advanced configurations{% #advanced-configurations-php %}

### Tracing internal functions and methods{% #tracing-internal-functions-php %}

As of version 0.76.0, all internal functions can unconditionally be traced.

On older versions, tracing internal functions and methods requires setting the `DD_TRACE_TRACED_INTERNAL_FUNCTIONS` environment variable, which takes a CSV of functions or methods that is to be instrumented. For example, `DD_TRACE_TRACED_INTERNAL_FUNCTIONS=array_sum,mt_rand,DateTime::add`. Once a function or method has been added to the list, it can be instrumented using `DDTrace\trace_function()` and `DDTrace\trace_method()` respectively. The `DD_TRACE_TRACED_INTERNAL_FUNCTIONS` environment variable is obsolete as of version 0.76.0.

### Running the tracing closure before the instrumented call{% #tracing-closure-before-php %}

By default, tracing closures are treated as `posthook` closures meaning they are executed *after* the instrumented call. Some cases require running the tracing closure *before* the instrumented call. In that case, tracing closures are marked as `prehook` using an associative configuration array.

```
\DDTrace\trace_function('foo', [
    'prehook' => function (\DDTrace\SpanData $span, array $args) {
        // This tracing closure will run before the instrumented call
    }
]);
```

### Debugging sandboxed errors{% #debugging-sandboxed-errors-php %}

Tracing closures are "sandboxed" in that exceptions thrown and errors raised inside of them do no impact the instrumented call.

```
<?php

function my_func() {
  echo 'Hello!' . PHP_EOL;
}

\DDTrace\trace_function(
  'my_func',
  function() {
    throw new \Exception('Oops!');
  }
);

my_func();
echo 'Done.' . PHP_EOL;

/*
Hello!
Done.
*/
```

To debug, set the environment variable `DD_TRACE_DEBUG=1` to expose any exceptions or errors that may have occurred in a tracing closure.

```
/*
Hello!
Exception thrown in tracing closure for my_func: Oops!
Done.
*/
```

### Zend framework 1 manual instrumentation{% #zend-framework-1-php %}

Zend framework 1 is automatically instrumented by default, so you are not required to modify your ZF1 project. However, if automatic instrumentation is disabled, enable the tracer manually.

First, [download the latest source code from the releases page](https://github.com/DataDog/dd-trace-php/releases/latest). Extract the zip file and copy the `src/DDTrace` folder to your application's `/library` folder. Then add the following to your `application/configs/application.ini` file:

```
autoloaderNamespaces[] = "DDTrace_"
pluginPaths.DDTrace = APPLICATION_PATH "/../library/DDTrace/Integrations/ZendFramework/V1"
resources.ddtrace = true
```

### PHP code optimization{% #php-code-optimization-php %}

Prior to PHP 7, some frameworks provided ways to compile PHP classes (for example, through the Laravel's `php artisan optimize` command).

While this [has been deprecated](https://laravel-news.com/laravel-5-6-removes-artisan-optimize) if you are using PHP 7.x, you still may use this caching mechanism in your app prior to version 7.x. In this case, Datadog suggests you use the [OpenTracing](https://docs.datadoghq.com/tracing/trace_collection/opentracing/php#opentracing) API instead of adding `datadog/dd-trace` to your Composer file.
{% /section %}

{% section displayed-if="Language is C++" %}
This section only applies to users who meet the following criteria: Language is C++

{% alert level="info" %}
If you have not yet read the setup instructions, start with the [C++ Setup Instructions](https://docs.datadoghq.com/tracing/setup/cpp/).
{% /alert %}

## Creating spans{% #creating-spans-cpp %}

To manually instrument a method:

```
{
  // Create a root span for the current request.
  auto root_span = tracer.create_span();
  root_span.set_name("get_ingredients");
  // Set a resource name for the root span.
  root_span.set_resource_name("bologna_sandwich");
  // Create a child span with the root span as its parent.
  auto child_span = root_span.create_child();
  child_span.set_name("cache_lookup");
  // Set a resource name for the child span.
  child_span.set_resource_name("ingredients.bologna_sandwich");
  // Spans can be finished at an explicit time ...
  child_span.set_end_time(std::chrono::steady_clock::now());
} // ... or implicitly when the destructor is invoked.
  // For example, root_span finishes here.
```

## Adding tags{% #adding-tags-cpp %}

Add custom [span tags](https://docs.datadoghq.com/tracing/glossary/#span-tags) to your [spans](https://docs.datadoghq.com/tracing/glossary/#spans) to customize your observability within Datadog. Span tags are applied to your incoming traces, allowing you to correlate observed behavior with code-level information such as merchant tier, checkout amount, or user ID.

Note that some Datadog tags are necessary for [unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging).

### Adding tags locally{% #adding-tags-locally-cpp %}

Add tags directly to a span object by calling `Span::set_tag`. For example:

```
// Add tags directly to a span by calling `Span::set_tag`
auto span = tracer.create_span();
span.set_tag("key must be string", "value must also be a string");

// Or, add tags by setting a `SpanConfig`
datadog::tracing::SpanConfig opts;
opts.tags.emplace("team", "apm-proxy");
auto span2 = tracer.create_span(opts);
```

### Adding tags globally{% #adding-tags-globally-cpp %}

#### Environment variable{% #environment-variable-cpp %}

To set tags across all your spans, set the `DD_TAGS` environment variable as a list of `key:value` pairs separated by commas.

```
export DD_TAGS=team:apm-proxy,key:value
```

#### In code{% #in-code-cpp %}

```
datadog::tracing::TracerConfig tracer_config;
tracer_config.tags = {
  {"team", "apm-proxy"},
  {"apply", "on all spans"}
};

const auto validated_config = datadog::tracing::finalize_config(tracer_config);
auto tracer = datadog::tracing::Tracer(*validated_config);

// All new spans will have contains tags defined in `tracer_config.tags`
auto span = tracer.create_span();
```

### Set errors on a span{% #set-errors-on-a-span-cpp %}

To associate a span with an error, set one or more error-related tags on the span. For example:

```
span.set_error(true);
```

Add more specific information about the error by setting any combination of `error.message`, `error.stack`, or `error.type` by using respectively `Span::set_error_message`, `Span::set_error_stack` and `Span::set_error_type`. See [Error Tracking](https://docs.datadoghq.com/tracing/error_tracking/) for more information about error tags.

An example of adding a combination of error tags:

```
// Associate this span with the "bad file descriptor" error from the standard
// library.
span.set_error_message("error");
span.set_error_stack("[EBADF] invalid file");
span.set_error_type("errno");
```

{% alert level="info" %}
Using any of the `Span::set_error_*` result in an underlying call to `Span::set_error(true)`.
{% /alert %}

To unset an error on a span, set `Span::set_error` to `false`, which removes any combination of `Span::set_error_stack`, `Span::set_error_type` or `Span::set_error_message`.

```
// Clear any error information associated with this span.
span.set_error(false);
```

## Propagating context with headers extraction and injection{% #propagating-context-cpp %}

You can configure the propagation of context for distributed traces by injecting and extracting headers. Read [Trace Context Propagation](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/) for information.

## Resource filtering{% #resource-filtering-cpp %}

Traces can be excluded based on their resource name, to remove synthetic traffic such as health checks from sending traces and influencing trace metrics. Find information about this and other security and fine-tuning configuration on the [Security](https://docs.datadoghq.com/tracing/security) page.
{% /section %}
{% /section %}
{% /section %}

## Further reading{% #further-reading %}

- [Instrument a custom method to get deep visibility into your business logic](https://docs.datadoghq.com/tracing/guide/instrument_custom_method)
- [Connect your Logs and Traces together](https://docs.datadoghq.com/tracing/connect_logs_and_traces)
- [Explore your services, resources, and traces](https://docs.datadoghq.com/tracing/visualization/)
- [Learn More about Datadog and the OpenTelemetry initiative](https://www.datadoghq.com/blog/opentelemetry-instrumentation/)
