# Source: https://uptrace.dev/raw/get/opentelemetry-swift.md

# OpenTelemetry Swift for Uptrace

> Step-by-step guide to install and configure OpenTelemetry Swift SDK, export telemetry to Uptrace, and verify that traces and metrics arrive via OTLP.

![undefined](/devicon/swift-original.svg)This document explains how to configure the OpenTelemetry Swift SDK to export spans (traces) and metrics to Uptrace using OTLP/gRPC or OTLP/HTTP.

## Overview

[OpenTelemetry Swift](https://github.com/open-telemetry/opentelemetry-swift) is the official OpenTelemetry implementation for Swift. It supports iOS, macOS, tvOS, and watchOS applications, providing:

- **Tracing** - Distributed tracing with automatic context propagation
- **Metrics** - Application metrics (counters, histograms, gauges)
- **NSURLSession instrumentation** - Automatic HTTP request tracing
- **Resource detection** - Device, OS, and application metadata

## Quick Start Guide

Follow these steps to get your first trace running:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Add Dependencies

Add OpenTelemetry Swift to your `Package.swift`:

```swift
// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "MyApp",
    platforms: [
        .macOS(.v13),
        .iOS(.v16)
    ],
    dependencies: [
        .package(url: "https://github.com/open-telemetry/opentelemetry-swift", from: "1.0.0"),
        .package(url: "https://github.com/grpc/grpc-swift.git", from: "1.0.0"),
    ],
    targets: [
        .executableTarget(
            name: "MyApp",
            dependencies: [
                .product(name: "OpenTelemetryApi", package: "opentelemetry-swift"),
                .product(name: "OpenTelemetrySdk", package: "opentelemetry-swift"),
                .product(name: "OpenTelemetryProtocolExporter", package: "opentelemetry-swift"),
                .product(name: "ResourceExtension", package: "opentelemetry-swift"),
                .product(name: "GRPC", package: "grpc-swift"),
            ]
        )
    ]
)
```

### Step 3: Configure OpenTelemetry

Create a configuration file to initialize the SDK:

```swift
import Foundation
import GRPC
import NIO
import OpenTelemetryApi
import OpenTelemetrySdk
import OpenTelemetryProtocolExporter
import ResourceExtension

func configureOpenTelemetry(dsn: String) {
    // Parse DSN to extract endpoint and token
    // DSN format: https://<token>@api.uptrace.dev?grpc=4317

    let group = MultiThreadedEventLoopGroup(numberOfThreads: 1)
    let channel = ClientConnection
        .usingPlatformAppropriateTLS(for: group)
        .connect(host: "api.uptrace.dev", port: 4317)

    // Configure OTLP trace exporter with Uptrace DSN header
    let otlpConfig = OtlpConfiguration(
        timeout: OtlpConfiguration.DefaultTimeoutInterval,
        headers: [("uptrace-dsn", dsn)]
    )

    let traceExporter = OtlpTraceExporter(
        channel: channel,
        config: otlpConfig
    )

    // Use BatchSpanProcessor for production
    let spanProcessor = BatchSpanProcessor(spanExporter: traceExporter)

    // Configure resource attributes
    let resource = DefaultResources().get().merging(other: Resource(attributes: [
        ResourceAttributes.serviceName.rawValue: AttributeValue.string("myservice"),
        ResourceAttributes.serviceVersion.rawValue: AttributeValue.string("1.0.0"),
        ResourceAttributes.deploymentEnvironment.rawValue: AttributeValue.string("production")
    ]))

    // Register the tracer provider
    OpenTelemetry.registerTracerProvider(tracerProvider:
        TracerProviderBuilder()
            .add(spanProcessor: spanProcessor)
            .with(resource: resource)
            .build()
    )
}
```

### Step 4: Create Your First Trace

```swift
import OpenTelemetryApi
import OpenTelemetrySdk

// Get the tracer
let tracer = OpenTelemetry.instance.tracerProvider.get(
    instrumentationName: "MyApp",
    instrumentationVersion: "1.0.0"
)

// Create a span
let span = tracer.spanBuilder(spanName: "my-operation")
    .setSpanKind(spanKind: .internal)
    .startSpan()

// Add attributes
span.setAttribute(key: "user.id", value: "12345")
span.setAttribute(key: "http.method", value: "GET")

// Do some work...

// End the span
span.end()
```

### Step 5: Run Your Application

Set the DSN and run your application:

```shell
UPTRACE_DSN="https://<token>@api.uptrace.dev?grpc=4317" swift run
```

### Step 6: View Your Trace

Open Uptrace and navigate to your project to see the traces:

![Basic trace](/get/basic-trace.png)

## Configuration Options

<table>
<thead>
  <tr>
    <th>
      Option
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
        OtlpConfiguration.timeout
      </code>
    </td>
    
    <td>
      Export timeout interval. Default: 10 seconds.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OtlpConfiguration.headers
      </code>
    </td>
    
    <td>
      HTTP headers for authentication. Set <code>
        uptrace-dsn
      </code>
      
       header.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        BatchSpanProcessor
      </code>
    </td>
    
    <td>
      Batches spans before export for better performance.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SimpleSpanProcessor
      </code>
    </td>
    
    <td>
      Exports spans immediately. Use for debugging only.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        Resource
      </code>
    </td>
    
    <td>
      Attributes describing the service (name, version, environment).
    </td>
  </tr>
</tbody>
</table>

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
      Configure OTLP exporter in detail
    </td>
    
    <td>
      <a href="/get/opentelemetry-swift/otlp">
        OTLP Configuration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-swift/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-swift/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Add resource attributes
    </td>
    
    <td>
      <a href="/get/opentelemetry-swift/resources">
        Resource Attributes
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-swift/propagation">
        Context Propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-swift/sampling">
        Sampling Strategies
      </a>
    </td>
  </tr>
</tbody>
</table>

### Instrumentation Libraries

OpenTelemetry Swift provides built-in instrumentation for:

- **NSURLSession** - Automatic HTTP request tracing
- **SignpostIntegration** - Integration with Apple Instruments profiler

See [Instrumentation Libraries](https://github.com/open-telemetry/opentelemetry-swift/tree/main/Sources/Instrumentation) for the full list.
