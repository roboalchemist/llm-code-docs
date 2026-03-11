# Source: https://uptrace.dev/raw/get/opentelemetry-rust.md

# OpenTelemetry Rust distro for Uptrace

> Step-by-step guide to install and configure OpenTelemetry Rust SDKs, export telemetry to Uptrace, and verify that traces, metrics, and logs arrive via OTLP.

![undefined](/devicon/rust-plain.svg)This document explains how to configure the OpenTelemetry Rust SDK to export spans (traces), logs, and metrics to Uptrace using OTLP/gRPC.

## Quick Start Guide

Follow these steps to get your first trace running in 5 minutes:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Add Dependencies

Add the required dependencies to your `Cargo.toml`:

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
tonic = { version = "0.13.1", features = ["tls-native-roots", "gzip"] }
opentelemetry = "0.30.0"
opentelemetry_sdk = { version = "0.30.0", features = ["rt-tokio"] }
opentelemetry-otlp = { version = "0.30.0", features = ["grpc-tonic", "gzip-tonic", "tls-roots", "trace"] }
opentelemetry-resource-detectors = "0.9"
```

### Step 3: Basic Configuration

Configure the OTLP exporter with your Uptrace DSN:

```rust
use std::time::Duration;
use tonic::metadata::MetadataMap;
use opentelemetry::{global, KeyValue};
use opentelemetry::trace::Tracer;
use opentelemetry_otlp::{WithExportConfig, WithTonicConfig};
use opentelemetry_sdk::{
    propagation::TraceContextPropagator,
    trace::{BatchSpanProcessor, SdkTracerProvider},
    Resource,
};

fn init_tracer(dsn: String) -> Result<SdkTracerProvider, Box<dyn std::error::Error + Send + Sync>> {
    // Configure gRPC metadata with Uptrace DSN
    let mut metadata = MetadataMap::with_capacity(1);
    metadata.insert("uptrace-dsn", dsn.parse().unwrap());

    // Create OTLP span exporter
    let exporter = opentelemetry_otlp::SpanExporter::builder()
        .with_tonic()
        .with_tls_config(tonic::transport::ClientTlsConfig::new().with_native_roots())
        .with_endpoint("https://api.uptrace.dev:4317")
        .with_metadata(metadata)
        .with_timeout(Duration::from_secs(10))
        .build()?;

    // Build the tracer provider
    let provider = SdkTracerProvider::builder()
        .with_batch_exporter(exporter)
        .with_resource(Resource::new(vec![
            KeyValue::new("service.name", "myservice"),
            KeyValue::new("service.version", "1.0.0"),
        ]))
        .build();

    Ok(provider)
}
```

### Step 4: Create Your First Trace

```rust
use opentelemetry::trace::{TraceContextExt, Tracer};
use opentelemetry::{global, KeyValue};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync + 'static>> {
    // Read Uptrace DSN from environment
    let dsn = std::env::var("UPTRACE_DSN").expect("UPTRACE_DSN not found");

    // Initialize tracer
    let provider = init_tracer(dsn)?;
    global::set_tracer_provider(provider.clone());

    let tracer = global::tracer("myservice");

    // Create a root span
    tracer.in_span("main-operation", |cx| {
        let span = cx.span();
        span.set_attribute(KeyValue::new("operation.type", "example"));

        // Create a child span
        tracer.in_span("child-operation", |cx| {
            let span = cx.span();
            span.set_attribute(KeyValue::new("http.method", "GET"));
            span.set_attribute(KeyValue::new("http.url", "http://localhost:8080/api"));
        });

        println!(
            "View trace: https://app.uptrace.dev/traces/{}",
            span.span_context().trace_id()
        );
    });

    // Flush and shutdown
    provider.force_flush()?;
    provider.shutdown()?;

    Ok(())
}
```

### Step 5: Run Your Application

Run the code, replacing `<FIXME>` with your Uptrace DSN:

```shell
$ UPTRACE_DSN="<FIXME>" cargo run
View trace: https://app.uptrace.dev/traces/<trace_id>
```

### Step 6: View Your Trace

Follow the link to view the trace:

![Basic trace](/get/basic-trace.png)

## Configuration Options

Configure OpenTelemetry using environment variables or programmatically:

<table>
<thead>
  <tr>
    <th>
      Environment Variable
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        UPTRACE_DSN
      </code>
    </td>
    
    <td>
      Uptrace DSN for authentication
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_SERVICE_NAME
      </code>
    </td>
    
    <td>
      Service name (e.g., <code>
        myservice
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_RESOURCE_ATTRIBUTES
      </code>
    </td>
    
    <td>
      Additional resource attributes
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_TRACES_SAMPLER
      </code>
    </td>
    
    <td>
      Sampling strategy (e.g., <code>
        parentbased_traceidratio
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_TRACES_SAMPLER_ARG
      </code>
    </td>
    
    <td>
      Sampling argument (e.g., <code>
        0.1
      </code>
      
       for 10%)
    </td>
  </tr>
</tbody>
</table>

<partial path="otlp-env-vars">



</partial>

## What's Next?

Instrument more operations to get a detailed picture of your application. Prioritize network calls, database queries, errors, and logs.

### By Use Case

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
      Configure OTLP exporter directly
    </td>
    
    <td>
      <a href="/get/opentelemetry-rust/otlp">
        OTLP Configuration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-rust/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-rust/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-rust/logs">
        Logs integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-rust/propagation">
        Context propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-rust/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-detect cloud environment
    </td>
    
    <td>
      <a href="/get/opentelemetry-rust/resources">
        Resource detectors
      </a>
    </td>
  </tr>
</tbody>
</table>

### Framework Guides

OpenTelemetry Rust integrates with popular frameworks through the `tracing` ecosystem:

<table>
<thead>
  <tr>
    <th>
      Framework
    </th>
    
    <th>
      Integration
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Axum
    </td>
    
    <td>
      Built-in tracing support
    </td>
  </tr>
  
  <tr>
    <td>
      Actix-web
    </td>
    
    <td>
      <code>
        tracing-actix-web
      </code>
      
       crate
    </td>
  </tr>
  
  <tr>
    <td>
      Warp
    </td>
    
    <td>
      Built-in tracing support
    </td>
  </tr>
  
  <tr>
    <td>
      Hyper
    </td>
    
    <td>
      Built-in tracing support
    </td>
  </tr>
  
  <tr>
    <td>
      Reqwest
    </td>
    
    <td>
      <code>
        tracing-opentelemetry
      </code>
      
       crate
    </td>
  </tr>
  
  <tr>
    <td>
      SQLx
    </td>
    
    <td>
      Built-in tracing support
    </td>
  </tr>
  
  <tr>
    <td>
      Tokio
    </td>
    
    <td>
      <code>
        tokio-tracing
      </code>
      
       features
    </td>
  </tr>
</tbody>
</table>

See the [OTLP Configuration](/get/opentelemetry-rust/otlp#framework-integration) page for Axum and Actix-web integration examples.
