# Source: https://uptrace.dev/raw/opentelemetry/sampling.md

# Source: https://uptrace.dev/raw/get/opentelemetry-swift/sampling.md

# Source: https://uptrace.dev/raw/get/opentelemetry-js/sampling.md

# Source: https://uptrace.dev/raw/get/opentelemetry-go/sampling.md

# Source: https://uptrace.dev/raw/get/opentelemetry-cpp/sampling.md

# OpenTelemetry C++ Sampling

> Configure OpenTelemetry sampling in C++ with parent-based, trace ID ratio, or always-on strategies.

![undefined](/devicon/cplusplus-original.svg)## TL;DR for production

Use ParentBased sampling with TraceIdRatioBased for consistent sampling:

```cpp
#include "opentelemetry/sdk/trace/samplers/parent.h"
#include "opentelemetry/sdk/trace/samplers/trace_id_ratio_based.h"

namespace trace_sdk = opentelemetry::sdk::trace;

// 10% sampling with parent-based decisions
auto ratio_sampler = std::make_unique<trace_sdk::TraceIdRatioBasedSampler>(0.1);
auto sampler = std::make_unique<trace_sdk::ParentBasedSampler>(
    std::move(ratio_sampler));
```

## What is sampling?

[Sampling](/opentelemetry/sampling) restricts the amount of spans generated. In high-volume applications, collecting 100% of traces can be expensive. Sampling allows you to collect a representative subset while reducing costs.

## Built-in samplers

### AlwaysOnSampler

Samples every trace. Use with caution in production:

```cpp
#include "opentelemetry/sdk/trace/samplers/always_on.h"

auto sampler = std::make_unique<trace_sdk::AlwaysOnSampler>();
```

### AlwaysOffSampler

Samples no traces:

```cpp
#include "opentelemetry/sdk/trace/samplers/always_off.h"

auto sampler = std::make_unique<trace_sdk::AlwaysOffSampler>();
```

### TraceIdRatioBasedSampler

Samples a fraction of traces (0.0 to 1.0):

```cpp
#include "opentelemetry/sdk/trace/samplers/trace_id_ratio_based.h"

// Sample 10% of traces
auto sampler = std::make_unique<trace_sdk::TraceIdRatioBasedSampler>(0.1);
```

### ParentBasedSampler

Follows parent's sampling decision:

```cpp
#include "opentelemetry/sdk/trace/samplers/parent.h"
#include "opentelemetry/sdk/trace/samplers/trace_id_ratio_based.h"

auto root_sampler = std::make_unique<trace_sdk::TraceIdRatioBasedSampler>(0.1);
auto sampler = std::make_unique<trace_sdk::ParentBasedSampler>(
    std::move(root_sampler));
```

## Using samplers with TracerProvider

```cpp
#include <cstdlib>
#include "opentelemetry/exporters/otlp/otlp_http_exporter_factory.h"
#include "opentelemetry/sdk/trace/tracer_provider_factory.h"
#include "opentelemetry/sdk/trace/tracer_provider.h"
#include "opentelemetry/sdk/trace/batch_span_processor_factory.h"
#include "opentelemetry/sdk/trace/samplers/parent.h"
#include "opentelemetry/sdk/trace/samplers/trace_id_ratio_based.h"
#include "opentelemetry/trace/provider.h"

namespace otlp = opentelemetry::exporter::otlp;
namespace trace_sdk = opentelemetry::sdk::trace;
namespace trace_api = opentelemetry::trace;

void InitTracer(double sampling_ratio) {
    otlp::OtlpHttpExporterOptions opts;
    opts.url = "https://api.uptrace.dev/v1/traces";

    const char* dsn = std::getenv("UPTRACE_DSN");
    opts.http_headers = {{"uptrace-dsn", dsn ? dsn : ""}};

    auto exporter = otlp::OtlpHttpExporterFactory::Create(opts);

    trace_sdk::BatchSpanProcessorOptions bsp_opts{};
    auto processor = trace_sdk::BatchSpanProcessorFactory::Create(
        std::move(exporter), bsp_opts);

    auto root_sampler = std::make_unique<trace_sdk::TraceIdRatioBasedSampler>(
        sampling_ratio);
    auto sampler = std::make_unique<trace_sdk::ParentBasedSampler>(
        std::move(root_sampler));

    std::shared_ptr<trace_api::TracerProvider> provider =
        trace_sdk::TracerProviderFactory::Create(
            std::move(processor),
            opentelemetry::sdk::resource::Resource::Create({}),
            std::move(sampler));

    trace_api::Provider::SetTracerProvider(provider);
}

void CleanupTracer() {
    auto provider = trace_api::Provider::GetTracerProvider();
    if (provider) {
        static_cast<trace_sdk::TracerProvider*>(provider.get())->ForceFlush();
    }
    std::shared_ptr<trace_api::TracerProvider> none;
    trace_api::Provider::SetTracerProvider(none);
}

int main() {
    InitTracer(0.1);  // 10% sampling

    auto tracer = trace_api::Provider::GetTracerProvider()
        ->GetTracer("myservice", "1.0.0");

    auto span = tracer->StartSpan("sampled-operation");
    span->End();

    CleanupTracer();
    return 0;
}
```

## Environment variables

```bash
export OTEL_TRACES_SAMPLER="traceidratio"
export OTEL_TRACES_SAMPLER_ARG="0.1"

# Or with parent-based
export OTEL_TRACES_SAMPLER="parentbased_traceidratio"
export OTEL_TRACES_SAMPLER_ARG="0.1"
```

## Best practices

1. **Use parent-based sampling** for consistent distributed tracing
2. **Start with 1-10%** and adjust based on needs
3. **Different rates per environment** - higher for dev, lower for production

## Sampling decisions

<table>
<thead>
  <tr>
    <th>
      Decision
    </th>
    
    <th>
      Meaning
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        DROP
      </code>
    </td>
    
    <td>
      Span not recorded or exported
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RECORD_ONLY
      </code>
    </td>
    
    <td>
      Span recorded but not exported
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        RECORD_AND_SAMPLE
      </code>
    </td>
    
    <td>
      Span recorded and exported
    </td>
  </tr>
</tbody>
</table>

## What's next?

- [Get started with OpenTelemetry C++](/get/opentelemetry-cpp)
- [OpenTelemetry C++ Tracing API](/get/opentelemetry-cpp/tracing)
- [OpenTelemetry C++ Metrics API](/get/opentelemetry-cpp/metrics)
- [OpenTelemetry C++ Resource attributes](/get/opentelemetry-cpp/resources)
