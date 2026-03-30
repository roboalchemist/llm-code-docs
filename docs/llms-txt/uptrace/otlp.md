# Source: https://uptrace.dev/raw/get/opentelemetry-swift/otlp.md

# Source: https://uptrace.dev/raw/get/opentelemetry-rust/otlp.md

# Source: https://uptrace.dev/raw/get/opentelemetry-ruby/otlp.md

# Source: https://uptrace.dev/raw/get/opentelemetry-python/otlp.md

# Source: https://uptrace.dev/raw/get/opentelemetry-php/otlp.md

# Source: https://uptrace.dev/raw/get/opentelemetry-js/otlp.md

# Source: https://uptrace.dev/raw/get/opentelemetry-go/otlp.md

# Source: https://uptrace.dev/raw/get/opentelemetry-erlang/otlp.md

# Source: https://uptrace.dev/raw/get/opentelemetry-dotnet/otlp.md

# Source: https://uptrace.dev/raw/get/opentelemetry-cpp/otlp.md

# OTLP Configuration for OpenTelemetry C++

> Configure OpenTelemetry C++ to export traces, metrics, and logs to Uptrace using the OTLP exporter.

![undefined](/devicon/cplusplus-original.svg)This document shows how to export telemetry to Uptrace using the OTLP exporter. For a quick introduction, see [Getting started with OpenTelemetry C++](/get/opentelemetry-cpp).

<partial path="otlp-env-vars">



</partial>

## Build requirements

Enable OTLP exporters when building OpenTelemetry C++ from source:

```shell
cmake -DBUILD_TESTING=OFF \
      -DWITH_OTLP_HTTP=ON \
      -DWITH_OTLP_GRPC=ON \
      ..
```

## Exporting Traces

### OTLP/HTTP

```cpp
#include <chrono>
#include <cstdlib>
#include "opentelemetry/exporters/otlp/otlp_http_exporter_factory.h"
#include "opentelemetry/exporters/otlp/otlp_http_exporter_options.h"
#include "opentelemetry/sdk/trace/batch_span_processor_factory.h"
#include "opentelemetry/sdk/trace/tracer_provider_factory.h"
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
```

### OTLP/gRPC

```cpp
#include <cstdlib>
#include "opentelemetry/exporters/otlp/otlp_grpc_exporter_factory.h"
#include "opentelemetry/exporters/otlp/otlp_grpc_exporter_options.h"
#include "opentelemetry/sdk/trace/batch_span_processor_factory.h"
#include "opentelemetry/sdk/trace/tracer_provider_factory.h"
#include "opentelemetry/trace/provider.h"

namespace otlp = opentelemetry::exporter::otlp;
namespace trace_sdk = opentelemetry::sdk::trace;
namespace trace_api = opentelemetry::trace;

void InitTracer() {
    otlp::OtlpGrpcExporterOptions opts;
    opts.endpoint = "api.uptrace.dev:4317";

    const char* dsn = std::getenv("UPTRACE_DSN");
    opts.metadata = {{"uptrace-dsn", dsn ? dsn : ""}};
    opts.use_ssl_credentials = true;

    trace_sdk::BatchSpanProcessorOptions bsp_opts{};
    auto exporter = otlp::OtlpGrpcExporterFactory::Create(opts);
    auto processor = trace_sdk::BatchSpanProcessorFactory::Create(
        std::move(exporter), bsp_opts);

    std::shared_ptr<trace_api::TracerProvider> provider =
        trace_sdk::TracerProviderFactory::Create(std::move(processor));
    trace_api::Provider::SetTracerProvider(provider);
}
```

## Exporting Metrics

```cpp
#include <cstdlib>
#include "opentelemetry/exporters/otlp/otlp_http_metric_exporter_factory.h"
#include "opentelemetry/exporters/otlp/otlp_http_metric_exporter_options.h"
#include "opentelemetry/sdk/metrics/meter_provider_factory.h"
#include "opentelemetry/sdk/metrics/meter_context_factory.h"
#include "opentelemetry/sdk/metrics/export/periodic_exporting_metric_reader_factory.h"
#include "opentelemetry/metrics/provider.h"

namespace otlp = opentelemetry::exporter::otlp;
namespace metrics_sdk = opentelemetry::sdk::metrics;
namespace metrics_api = opentelemetry::metrics;

void InitMetrics() {
    otlp::OtlpHttpMetricExporterOptions opts;
    opts.url = "https://api.uptrace.dev/v1/metrics";

    const char* dsn = std::getenv("UPTRACE_DSN");
    opts.http_headers = {{"uptrace-dsn", dsn ? dsn : ""}};

    auto exporter = otlp::OtlpHttpMetricExporterFactory::Create(opts);

    metrics_sdk::PeriodicExportingMetricReaderOptions reader_opts;
    reader_opts.export_interval_millis = std::chrono::milliseconds(15000);
    reader_opts.export_timeout_millis = std::chrono::milliseconds(10000);

    auto reader = metrics_sdk::PeriodicExportingMetricReaderFactory::Create(
        std::move(exporter), reader_opts);

    auto context = metrics_sdk::MeterContextFactory::Create();
    context->AddMetricReader(std::move(reader));

    auto u_provider = metrics_sdk::MeterProviderFactory::Create(std::move(context));
    std::shared_ptr<metrics_api::MeterProvider> provider(std::move(u_provider));
    metrics_api::Provider::SetMeterProvider(provider);
}
```

## Exporting Logs

```cpp
#include <cstdlib>
#include "opentelemetry/exporters/otlp/otlp_http_log_record_exporter_factory.h"
#include "opentelemetry/exporters/otlp/otlp_http_log_record_exporter_options.h"
#include "opentelemetry/sdk/logs/logger_provider_factory.h"
#include "opentelemetry/sdk/logs/simple_log_record_processor_factory.h"
#include "opentelemetry/logs/provider.h"

namespace otlp = opentelemetry::exporter::otlp;
namespace logs_sdk = opentelemetry::sdk::logs;
namespace logs_api = opentelemetry::logs;

void InitLogger() {
    otlp::OtlpHttpLogRecordExporterOptions opts;
    opts.url = "https://api.uptrace.dev/v1/logs";

    const char* dsn = std::getenv("UPTRACE_DSN");
    opts.http_headers = {{"uptrace-dsn", dsn ? dsn : ""}};

    auto exporter = otlp::OtlpHttpLogRecordExporterFactory::Create(opts);
    auto processor = logs_sdk::SimpleLogRecordProcessorFactory::Create(
        std::move(exporter));

    std::shared_ptr<logs_api::LoggerProvider> provider =
        logs_sdk::LoggerProviderFactory::Create(std::move(processor));
    logs_api::Provider::SetLoggerProvider(provider);
}
```

## Complete Example

```cpp
#include "opentelemetry/trace/provider.h"
#include "opentelemetry/metrics/provider.h"
#include "opentelemetry/logs/provider.h"
#include "opentelemetry/sdk/trace/tracer_provider.h"
#include "opentelemetry/sdk/metrics/meter_provider.h"
#include "opentelemetry/sdk/logs/logger_provider.h"

namespace trace_api = opentelemetry::trace;
namespace metrics_api = opentelemetry::metrics;
namespace logs_api = opentelemetry::logs;

void Cleanup() {
    // Flush and shutdown TracerProvider
    auto trace_provider = trace_api::Provider::GetTracerProvider();
    if (trace_provider) {
        static_cast<opentelemetry::sdk::trace::TracerProvider*>(
            trace_provider.get())->ForceFlush();
    }

    // Flush and shutdown MeterProvider
    auto meter_provider = metrics_api::Provider::GetMeterProvider();
    if (meter_provider) {
        static_cast<opentelemetry::sdk::metrics::MeterProvider*>(
            meter_provider.get())->ForceFlush();
    }

    // Flush and shutdown LoggerProvider
    auto logger_provider = logs_api::Provider::GetLoggerProvider();
    if (logger_provider) {
        static_cast<opentelemetry::sdk::logs::LoggerProvider*>(
            logger_provider.get())->ForceFlush();
    }
}

int main() {
    InitTracer();
    InitMetrics();
    InitLogger();

    auto tracer = trace_api::Provider::GetTracerProvider()
        ->GetTracer("myservice", "1.0.0");

    auto span = tracer->StartSpan("main-operation");
    span->SetAttribute("key", "value");
    span->End();

    Cleanup();
    return 0;
}
```

## What's next?

- [Get started with OpenTelemetry C++](/get/opentelemetry-cpp)
- [OpenTelemetry C++ Tracing API](/get/opentelemetry-cpp/tracing)
- [OpenTelemetry C++ Metrics API](/get/opentelemetry-cpp/metrics)
- [OpenTelemetry C++ Resource attributes](/get/opentelemetry-cpp/resources)
