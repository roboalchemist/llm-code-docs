# Source: https://uptrace.dev/raw/get/opentelemetry-swift/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-rust/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-ruby/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-python/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-php/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-js/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-java/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-go/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-erlang/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-dotnet/tracing.md

# Source: https://uptrace.dev/raw/get/opentelemetry-cpp/tracing.md

# OpenTelemetry C++ Tracing

> Instrument C++ services with the OpenTelemetry Tracing API, create spans, record errors, and send distributed traces to Uptrace.

![undefined](/devicon/cplusplus-original.svg)## Prerequisites

<partial path="otel-prereq-cpp">



</partial>

## Initialize tracing

```cpp
#include "opentelemetry/trace/provider.h"

namespace trace_api = opentelemetry::trace;

auto provider = trace_api::Provider::GetTracerProvider();
auto tracer = provider->GetTracer("foo_library", "1.0.0");
```

The `TracerProvider` is a singleton provided by the OpenTelemetry C++ SDK. The `Tracer` is used to create and start spans.

## Start a span

```cpp
auto span = tracer->StartSpan("HandleRequest");
```

This creates a span with name `"HandleRequest"` and start time set to now.

## Mark a span as active

```cpp
auto scope = tracer->WithActiveSpan(span);
```

This marks a span as active and returns a `Scope` object. The span remains active for the lifetime of the scope. New spans without an explicit parent are parented to the active span.

## Create nested spans

```cpp
auto outer_span = tracer->StartSpan("Outer operation");
auto outer_scope = tracer->WithActiveSpan(outer_span);
{
    auto inner_span = tracer->StartSpan("Inner operation");
    auto inner_scope = tracer->WithActiveSpan(inner_span);
    // ... perform inner operation
    inner_span->End();
}
// ... perform outer operation
outer_span->End();
```

## Adding span attributes

```cpp
span->SetAttribute("http.method", "GET");
span->SetAttribute("http.route", "/projects/:id");
span->SetAttribute("http.status_code", 200);
```

## Setting status code

```cpp
#include "opentelemetry/trace/span.h"

if (error) {
    span->SetStatus(trace_api::StatusCode::kError, "Error message");
}
```

## Adding span events

```cpp
span->AddEvent("log", {
    {"log.severity", "error"},
    {"log.message", "User not found"},
    {"enduser.id", "123"}
});
```

## Error monitoring

```cpp
try {
    riskyOperation();
} catch (const std::exception& e) {
    span->AddEvent("exception", {
        {"exception.type", typeid(e).name()},
        {"exception.message", e.what()}
    });
    span->SetStatus(trace_api::StatusCode::kError, e.what());
    throw;
}
```

## Complete example

```cpp
#include "opentelemetry/trace/provider.h"

namespace trace_api = opentelemetry::trace;

class Handler {
public:
    void handle() {
        auto tracer = trace_api::Provider::GetTracerProvider()
            ->GetTracer("my-app-tracer");

        auto span = tracer->StartSpan("HandleRequest");
        auto scope = tracer->WithActiveSpan(span);

        span->SetAttribute("http.method", "GET");

        try {
            processRequest();
        } catch (const std::exception& e) {
            span->SetStatus(trace_api::StatusCode::kError, e.what());
            throw;
        }

        span->End();
    }
};
```

## What's next?

- [Get started](/get/opentelemetry-cpp)
- [OpenTelemetry C++ Sampling](/get/opentelemetry-cpp/sampling)
- [OpenTelemetry C++ Metrics API](/get/opentelemetry-cpp/metrics)
- [OpenTelemetry C++ Resource attributes](/get/opentelemetry-cpp/resources)
