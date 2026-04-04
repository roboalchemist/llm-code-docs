# Source: https://docs.datadoghq.com/tracing/guide/configuring-primary-operation.md

---
title: Primary Operations in Services
description: >-
  Understand how primary operations work in services and how to configure them
  to properly organize traces and resources in APM.
breadcrumbs: Docs > APM > Tracing Guides > Primary Operations in Services
---

# Primary Operations in Services

## APM services{% #apm-services %}

APM services calculate trace metrics for errors, throughput, and latency. These are calculated based on resources that match a single span name, deemed the primary operation. These service metrics are used throughout the product, both as the default Service Page, in the Software Catalog, and the Service Map.

**Note**: Trace Metrics can be queried based on their `trace.*` [namespace](https://docs.datadoghq.com/tracing/metrics/metrics_namespace/).

## Primary operations{% #primary-operations %}

### Definition{% #definition %}

The primary operation name of a service determines how that service is represented in the UI. The Datadog backend automatically selects an operation name that is deemed the entry-point into the service based on the throughput of requests.

As an example, a `web-store` service can have multiple endpoints which are instrumented as resources. These resources then share the same primary operation because the entry-point into these resources is consistent. For example, the resources `/user/home` and `/user/new` should both have the same primary operation `web.request`. In different languages a primary operation for a service may look like:

| Service Type           | Primary Operation                                 |
| ---------------------- | ------------------------------------------------- |
| web                    | `servlet.request`, `flask.request`, `web.request` |
| db                     | `postgres.query`, `db.query`                      |
| custom-instrumentation | `trace.annotation`, `method.call`                 |

### Configuration{% #configuration %}

When there are multiple primary operations defined for a service, the highest request throughput determines the operation automatically selected to be the entry-point for the service. An admin user can set this setting manually:

1. Go to the [APM settings page](https://app.datadoghq.com/apm/settings).
1. Select the **Primary Operation Name** tab.
1. Click on the edit icon for the service that you want to manually set.
1. Click the **Set Manually** tab.
1. Select the operation that you want reflected as the entry-point to the service.
1. Click **Save**.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/primary_operation/configuring-primary-option.d713dd6d36e93cc5f68e9790046ef14a.png?auto=format"
   alt="APM save" /%}

## Viewing stats for additional span names{% #viewing-stats-for-additional-span-names %}

To ensure that all traces are being sent to Datadog correctly outside of any instrumentation, you can view your resources by additional span names that are considered a secondary operation with a dropdown menu. However, these are not used to calculate service-level statistics.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/guide/primary_operation/dropdown.mp4" /%}

## Manual instrumentation{% #manual-instrumentation %}

When writing custom spans, statically set the span name to ensure that your resources are grouped with the same primary operation (for example, `web.request`). If the span is being named dynamically, set it as the resource (for example, `/user/profile`).

See [Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/) for your programming language for detailed information.

## OpenTracing{% #opentracing %}

When using Datadog, the OpenTracing operation name is a resource and the OpenTracing "component" tag is Datadog's span name. For example, to define (in OpenTracing terms) a span that has the resource "/user/profile", and the span name "http.request":

{% tab title="Java" %}

```java
Span span = tracer.buildSpan("http.request").start();

try (Scope scope = tracer.activateSpan(span)) {
    span.setTag("service.name", "service_name");
    span.setTag("resource.name", "/user/profile");
    // code being traced
} finally {
    span.finish();
}
```

For more information, see [Setting up Java and OpenTracing](https://docs.datadoghq.com/tracing/trace_collection/opentracing/java/#opentracing).
{% /tab %}

{% tab title="Python" %}

```python
from ddtrace.opentracer.tags import Tags
import opentracing
span = opentracing.tracer.start_span('http.request')
span.set_tag(Tags.RESOURCE_NAME, '/user/profile')
span.set_tag(Tags.SPAN_TYPE, 'web')

# ...
span.finish()
```

For more information, see [Setting up Python and OpenTracing](https://docs.datadoghq.com/tracing/trace_collection/opentracing/python/#opentracing).
{% /tab %}

{% tab title="Ruby" %}

```ruby
OpenTracing.start_active_span('http.request') do |scope|
  scope.span.datadog_span.resource = '/user/profile'
  # code being traced
end
```

For more information, see [Setting up Ruby and OpenTracing](https://docs.datadoghq.com/tracing/trace_collection/opentracing/ruby/#opentracing).
{% /tab %}

{% tab title="Node.js" %}

```javascript
const span = tracer.startSpan('http.request');
span.setTag('resource.name',  '/user/profile')
span.setTag('span.type', 'web')
// code being traced
span.finish();
```

For more information, see [Setting up Node.js and OpenTracing](https://docs.datadoghq.com/tracing/trace_collection/opentracing/nodejs/#opentracing).
{% /tab %}

{% tab title=".NET" %}

```csharp
using OpenTracing;
using OpenTracing.Util;

using (var scope = GlobalTracer.Instance.BuildSpan("http.request").StartActive(finishSpanOnDispose: true))
{
    scope.Span.SetTag("resource.name", "/user/profile");
    // code being traced
}
```

For more information, see [Setting up .NET and OpenTracing](https://docs.datadoghq.com/tracing/trace_collection/opentracing/dotnet/#opentracing).
{% /tab %}

{% tab title="PHP" %}

```php
// Once, at the beginning of your index.php, right after composer's autoloader import.
// For OpenTracing <= 1.0-beta6
$otTracer = new \DDTrace\OpenTracer\Tracer(\DDTrace\GlobalTracer::get());
// For OpenTracing >= 1.0
$otTracer = new \DDTrace\OpenTracer1\Tracer(\DDTrace\GlobalTracer::get());
// Register the global tracer wrapper
 \OpenTracing\GlobalTracer::set($otTracer);

// Anywhere in your application code
$otTracer = \OpenTracing\GlobalTracer::get();
$scope = $otTracer->startActiveSpan('http.request');
$span = $scope->getSpan();
$span->setTag('service.name', 'service_name');
$span->setTag('resource.name', '/user/profile');
$span->setTag('span.type', 'web');
// ...Use OpenTracing as expected
$scope->close();
```

For more information, see [Setting up PHP and OpenTracing](https://docs.datadoghq.com/tracing/trace_collection/opentracing/php/#opentracing).
{% /tab %}

{% tab title="C++" %}

```cpp
// Create a root span for the current request.
auto root_span = tracer->StartSpan("web.request");
// Set a resource name for the root span.
root_span->SetTag(datadog::tags::resource_name, "/user/profile");
```

For more information, see [Setting up C++ and Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/cpp/#manually-instrument-a-method).
{% /tab %}

## Further Reading{% #further-reading %}

- [Learn how to set up APM tracing with your application](https://docs.datadoghq.com/tracing/trace_collection/)
- [Discover and catalog the services reporting to Datadog](https://docs.datadoghq.com/tracing/software_catalog/)
- [Learn more about services in Datadog](https://docs.datadoghq.com/tracing/services/service_page/)
- [Dive into your resource performance and traces](https://docs.datadoghq.com/tracing/services/resource_page/)
- [Understand how to read a Datadog Trace](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/)
