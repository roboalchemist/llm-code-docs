# Source: https://uptrace.dev/raw/get/opentelemetry-go.md

# OpenTelemetry Go distro for Uptrace

> Step-by-step guide to install and configure OpenTelemetry Go SDKs, export telemetry to Uptrace, and verify that traces, metrics, and logs arrive via OTLP.

![undefined](/devicon/go-original.svg)This document explains how to configure the OpenTelemetry Go SDK to export spans (traces), logs, and metrics to Uptrace using OTLP/gRPC.

## Choose Your Setup Path

### Option A: Quick Start with uptrace-go

Best for: Getting started quickly, automatic configuration

[uptrace-go](https://github.com/uptrace/uptrace-go) is a thin wrapper over [opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go) that configures the OpenTelemetry SDK to export data to Uptrace. It does not add any new functionality and is provided only for your convenience.

â [Continue below](#quick-start)

### Option B: Direct OTLP Configuration

Best for: Existing OpenTelemetry users, custom exporters, fine-grained control

â [Direct OTLP Setup](/get/opentelemetry-go/otlp)

## Quick Start Guide

Follow these steps to get your first trace running in 5 minutes:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Install uptrace-go

```shell
go get github.com/uptrace/uptrace-go
```

### Step 3: Basic Configuration

You can configure the Uptrace client using a [DSN](/get#dsn) (Data Source Name) from the project settings page. Replace `<FIXME>` with your actual Uptrace DSN, and `myservice` with a name that identifies your application.

```go
import "github.com/uptrace/uptrace-go/uptrace"

uptrace.ConfigureOpentelemetry(
    // copy your project DSN here or use UPTRACE_DSN env var
    //uptrace.WithDSN("<FIXME>"),

    uptrace.WithServiceName("myservice"),
    uptrace.WithServiceVersion("v1.0.0"),
    uptrace.WithDeploymentEnvironment("production"),
)
```

### Step 4: Create Your First Trace

Copy the [code](https://github.com/uptrace/uptrace-go/tree/master/example/basic) to `main.go`:

```go
package main

import (
    "context"
    "errors"
    "fmt"

    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/attribute"
    "go.opentelemetry.io/otel/codes"
    "go.opentelemetry.io/otel/trace"

    "github.com/uptrace/uptrace-go/uptrace"
)

func main() {
    ctx := context.Background()

    // Configure OpenTelemetry with sensible defaults.
    uptrace.ConfigureOpentelemetry(
        // copy your project DSN here or use UPTRACE_DSN env var
        // uptrace.WithDSN("<FIXME>"),

        uptrace.WithServiceName("myservice"),
        uptrace.WithServiceVersion("1.0.0"),
    )
    // Send buffered spans and free resources.
    defer uptrace.Shutdown(ctx)

    // Create a tracer. Usually, tracer is a global variable.
    tracer := otel.Tracer("app_or_package_name")

    // Create a root span (a trace) to measure some operation.
    ctx, main := tracer.Start(ctx, "main-operation")
    // End the span when the operation we are measuring is done.
    defer main.End()

    // The passed ctx carries the parent span (main).
    // That is how OpenTelemetry manages span relations.
    _, child1 := tracer.Start(ctx, "GET /posts/:id")
    child1.SetAttributes(
        attribute.String("http.method", "GET"),
        attribute.String("http.route", "/posts/:id"),
        attribute.String("http.url", "http://localhost:8080/posts/123"),
        attribute.Int("http.status_code", 200),
    )
    if err := errors.New("dummy error"); err != nil {
        child1.RecordError(err, trace.WithStackTrace(true))
        child1.SetStatus(codes.Error, err.Error())
    }
    child1.End()

    _, child2 := tracer.Start(ctx, "SELECT")
    child2.SetAttributes(
        attribute.String("db.system", "mysql"),
        attribute.String("db.statement", "SELECT * FROM posts LIMIT 100"),
    )
    child2.End()

    fmt.Printf("trace: %s\n", uptrace.TraceURL(main))
}
```

### Step 5: Run Your Application

Run the code, replacing `<FIXME>` with your Uptrace DSN:

```shell
$ UPTRACE_DSN="<FIXME>" go run main.go
trace: https://app.uptrace.dev/traces/<trace_id>
```

### Step 6: View Your Trace

Follow the link to view the trace:

![Basic trace](/get/basic-trace.png)

## Configuration Options

You can find the full list of available options at [pkg.go.dev](https://pkg.go.dev/github.com/uptrace/uptrace-go/uptrace#Option).

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
        WithDSN
      </code>
    </td>
    
    <td>
      A data source that specifies Uptrace project credentials. For example, <code>
        https://<secret>@api.uptrace.dev?grpc=4317
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WithServiceName
      </code>
    </td>
    
    <td>
      <code>
        service.name
      </code>
      
       resource attribute. For example, <code>
        myservice
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WithServiceVersion
      </code>
    </td>
    
    <td>
      <code>
        service.version
      </code>
      
       resource attribute. For example, <code>
        1.0.0
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WithDeploymentEnvironment
      </code>
    </td>
    
    <td>
      <code>
        deployment.environment
      </code>
      
       resource attribute. For example, <code>
        production
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WithResourceAttributes
      </code>
    </td>
    
    <td>
      Any other resource attributes.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WithResourceDetectors
      </code>
    </td>
    
    <td>
      Configures <a href="/get/opentelemetry-go/resources">
        resource detectors
      </a>
      
       for cloud environments (AWS, GCP).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WithResource
      </code>
    </td>
    
    <td>
      Resource attributes representing an entity that produces telemetry.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        WithTraceSampler
      </code>
    </td>
    
    <td>
      Configures <a href="/get/opentelemetry-go/sampling">
        sampling
      </a>
      
       to reduce costs in high-volume applications.
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
      Instrument without code changes
    </td>
    
    <td>
      <a href="/get/opentelemetry-go/zero-code">
        Zero-code instrumentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-go/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-go/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-go/logs">
        Logs integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Deploy to AWS Lambda or Vercel
    </td>
    
    <td>
      <a href="/get/opentelemetry-go/serverless">
        Serverless
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-go/propagation">
        Context propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-go/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-detect cloud environment
    </td>
    
    <td>
      <a href="/get/opentelemetry-go/resources">
        Resource detectors
      </a>
    </td>
  </tr>
</tbody>
</table>

### Framework Guides

- [OpenTelemetry net/http](/guides/opentelemetry-net-http)
- [OpenTelemetry Go gRPC](/guides/opentelemetry-go-grpc)
- [OpenTelemetry database/sql](/guides/opentelemetry-database-sql)
- [OpenTelemetry Gin](/guides/opentelemetry-gin)
- [OpenTelemetry GORM](/guides/opentelemetry-gorm)

### Logging Libraries

- [OpenTelemetry slog](/guides/opentelemetry-slog)
- [OpenTelemetry Zap](/guides/opentelemetry-zap)
- [OpenTelemetry Logrus](/guides/opentelemetry-logrus)
