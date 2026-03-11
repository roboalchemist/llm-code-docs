# Source: https://uptrace.dev/raw/get/opentelemetry-swift/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-rust/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-ruby/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-python/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-php/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-js/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-java/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-go/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-erlang/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-dotnet/resources.md

# Source: https://uptrace.dev/raw/get/opentelemetry-cpp/resources.md

# Resource Attributes in OpenTelemetry C++

> Add resource attributes in C++ to describe service name, environment, and deployment metadata so Uptrace can group telemetry correctly.

![undefined](/devicon/cplusplus-original.svg)Resource attributes describe the entity producing telemetry. This information is attached to all telemetry data (traces, metrics, logs) to provide context for monitoring and debugging.

## Overview

Common resource attributes include:

- **service.name** - Logical name of the service
- **service.version** - Version of the service
- **deployment.environment** - Deployment environment (production, staging)
- **host.name** - Hostname of the machine
- **telemetry.sdk.language** - Language (cpp)

## Creating resources

```cpp
#include "opentelemetry/sdk/resource/resource.h"

namespace resource = opentelemetry::sdk::resource;

auto resource_attrs = resource::Resource::Create({
    {"service.name", "myservice"},
    {"service.version", "1.0.0"},
    {"deployment.environment", "production"},
    {"host.name", "server-01"}
});
```

## Using resources with TracerProvider

```cpp
#include <cstdlib>
#include "opentelemetry/exporters/otlp/otlp_http_exporter_factory.h"
#include "opentelemetry/sdk/trace/tracer_provider_factory.h"
#include "opentelemetry/sdk/trace/batch_span_processor_factory.h"
#include "opentelemetry/sdk/resource/resource.h"
#include "opentelemetry/trace/provider.h"

namespace otlp = opentelemetry::exporter::otlp;
namespace trace_sdk = opentelemetry::sdk::trace;
namespace resource = opentelemetry::sdk::resource;
namespace trace_api = opentelemetry::trace;

void InitTracer() {
    auto resource_attrs = resource::Resource::Create({
        {"service.name", "myservice"},
        {"service.version", "1.0.0"}
    });

    otlp::OtlpHttpExporterOptions opts;
    opts.url = "https://api.uptrace.dev/v1/traces";

    const char* dsn = std::getenv("UPTRACE_DSN");
    opts.http_headers = {{"uptrace-dsn", dsn ? dsn : ""}};

    auto exporter = otlp::OtlpHttpExporterFactory::Create(opts);

    trace_sdk::BatchSpanProcessorOptions bsp_opts{};
    auto processor = trace_sdk::BatchSpanProcessorFactory::Create(
        std::move(exporter), bsp_opts);

    std::shared_ptr<trace_api::TracerProvider> provider =
        trace_sdk::TracerProviderFactory::Create(std::move(processor), resource_attrs);
    trace_api::Provider::SetTracerProvider(provider);
}
```

## Environment variables

Set resource attributes via environment variables:

```bash
export OTEL_SERVICE_NAME="myservice"
export OTEL_RESOURCE_ATTRIBUTES="service.version=1.2.0,deployment.environment=production"
```

## Common resource attributes

### Service attributes

```cpp
auto resource_attrs = resource::Resource::Create({
    {"service.name", "myservice"},
    {"service.version", "1.0.0"},
    {"service.instance.id", "instance-001"},
    {"service.namespace", "shop"}
});
```

### Deployment attributes

```cpp
auto resource_attrs = resource::Resource::Create({
    {"deployment.environment", "production"}
});
```

### Host attributes

```cpp
#include <unistd.h>

char hostname[256];
gethostname(hostname, sizeof(hostname));

auto resource_attrs = resource::Resource::Create({
    {"host.name", hostname},
    {"host.type", "container"}
});
```

### Kubernetes attributes

```cpp
#include <cstdlib>

const char* k8s_ns = std::getenv("K8S_NAMESPACE");
const char* k8s_pod = std::getenv("K8S_POD_NAME");

auto resource_attrs = resource::Resource::Create({
    {"k8s.namespace.name", k8s_ns ? k8s_ns : ""},
    {"k8s.pod.name", k8s_pod ? k8s_pod : ""},
    {"k8s.deployment.name", "myapp"}
});
```

## Complete example

```cpp
#include "opentelemetry/sdk/resource/resource.h"
#include "opentelemetry/sdk/trace/tracer_provider_factory.h"
#include "opentelemetry/exporters/otlp/otlp_http_exporter_factory.h"
#include <unistd.h>

namespace resource = opentelemetry::sdk::resource;

resource::Resource CreateResource() {
    char hostname[256];
    gethostname(hostname, sizeof(hostname));

    return resource::Resource::Create({
        {"service.name", "myservice"},
        {"service.version", "1.0.0"},
        {"deployment.environment", "production"},
        {"host.name", hostname},
        {"process.pid", static_cast<int64_t>(getpid())}
    });
}

int main() {
    auto resource_attrs = CreateResource();
    // Use with TracerProvider, MeterProvider, LoggerProvider...
    return 0;
}
```

## What's next?

- [Get started](/get/opentelemetry-cpp)
- [OpenTelemetry C++ Tracing API](/get/opentelemetry-cpp/tracing)
- [OpenTelemetry C++ Metrics API](/get/opentelemetry-cpp/metrics)
- [OpenTelemetry Context Propagation <span>

C++

</span>

](/get/opentelemetry-cpp/propagation)
