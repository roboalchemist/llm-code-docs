# Source: https://uptrace.dev/raw/get/opentelemetry-cpp.md

# OpenTelemetry C++ SDK for Uptrace

> Step-by-step guide to install and configure OpenTelemetry C++ SDK, export telemetry to Uptrace via OTLP.

![undefined](/devicon/cplusplus-original.svg)This document explains how to configure the OpenTelemetry C++ SDK to export spans (traces), logs, and metrics to Uptrace using OTLP.

## Prerequisites

- Git
- C++ compiler supporting C++ version >= 14
- Make
- CMake version >= 3.25

## Quick Start Guide

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Install OpenTelemetry C++

```shell
git clone https://github.com/open-telemetry/opentelemetry-cpp.git
cd opentelemetry-cpp
mkdir build && cd build
cmake -DBUILD_TESTING=OFF -DWITH_OTLP_HTTP=ON ..
cmake --build .
sudo cmake --install .
```

### Step 3: Configure and Create Traces

```cpp
#include <cstdlib>
#include "opentelemetry/exporters/otlp/otlp_http_exporter_factory.h"
#include "opentelemetry/exporters/otlp/otlp_http_exporter_options.h"
#include "opentelemetry/sdk/trace/batch_span_processor_factory.h"
#include "opentelemetry/sdk/trace/tracer_provider_factory.h"
#include "opentelemetry/sdk/trace/tracer_provider.h"
#include "opentelemetry/trace/provider.h"

namespace otlp = opentelemetry::exporter::otlp;
namespace trace_sdk = opentelemetry::sdk::trace;
namespace trace_api = opentelemetry::trace;

void InitTracer() {
    otlp::OtlpHttpExporterOptions opts;
    opts.url = "https://api.uptrace.dev/v1/traces";

    const char* dsn = std::getenv("UPTRACE_DSN");
    opts.http_headers = {{"uptrace-dsn", dsn ? dsn : ""}};

    trace_sdk::BatchSpanProcessorOptions bsp_opts{};
    auto exporter = otlp::OtlpHttpExporterFactory::Create(opts);
    auto processor = trace_sdk::BatchSpanProcessorFactory::Create(
        std::move(exporter), bsp_opts);

    std::shared_ptr<trace_api::TracerProvider> provider =
        trace_sdk::TracerProviderFactory::Create(std::move(processor));
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
    InitTracer();

    auto tracer = trace_api::Provider::GetTracerProvider()
        ->GetTracer("myservice", "1.0.0");

    auto span = tracer->StartSpan("main-operation");
    span->SetAttribute("key", "value");
    span->End();

    CleanupTracer();
    return 0;
}
```

### Step 4: Build and Run

```shell
export UPTRACE_DSN="https://<secret>@api.uptrace.dev?grpc=4317"
mkdir build && cd build
cmake ..
cmake --build .
./myservice
```

### Step 5: View Your Trace

Open the Uptrace dashboard to view your traces.

## Configuration Options

<partial path="otlp-env-vars">



</partial>

## What's Next?

<table>
<thead>
  <tr>
    <th>
      I want to...
    </th>
    
    <th>
      Read this
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Configure OTLP exporter in detail
    </td>
    
    <td>
      <a href="/get/opentelemetry-cpp/otlp">
        OTLP Configuration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-cpp/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-cpp/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-cpp/logs">
        Logs integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-cpp/propagation">
        Context propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-cpp/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Add service metadata
    </td>
    
    <td>
      <a href="/get/opentelemetry-cpp/resources">
        Resource attributes
      </a>
    </td>
  </tr>
</tbody>
</table>
