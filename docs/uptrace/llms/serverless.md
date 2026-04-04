# Source: https://uptrace.dev/raw/get/opentelemetry-go/serverless.md

# OpenTelemetry Go for Serverless

> Configure OpenTelemetry Go for serverless environments like AWS Lambda and Vercel, with proper initialization and flushing patterns.

![undefined](/devicon/go-original.svg)This document covers how to configure OpenTelemetry Go for serverless environments. Serverless functions have unique requirements: short-lived execution, cold starts, and no persistent connections.

## Key Considerations

Serverless environments require special handling:

1. **Initialize once**: Configure OpenTelemetry in `init()` to avoid cold start overhead
2. **Flush on every request**: Call `ForceFlush()` before the function exits to ensure spans are sent
3. **Use environment variables**: Configure DSN via `UPTRACE_DSN` for easier deployment

## AWS Lambda

For comprehensive AWS Lambda instrumentation including automatic span creation and context propagation, see the dedicated guide:

â [OpenTelemetry Go Lambda](/guides/opentelemetry-go-lambda)

### Quick Setup

```go
package main

import (
    "context"

    "github.com/aws/aws-lambda-go/lambda"
    "github.com/uptrace/uptrace-go/uptrace"
    "go.opentelemetry.io/otel"
)

var tracer = otel.Tracer("app_or_package_name")

func init() {
    uptrace.ConfigureOpentelemetry(
        // Use UPTRACE_DSN environment variable
        uptrace.WithServiceName("my-lambda-function"),
        uptrace.WithServiceVersion("1.0.0"),
    )
}

func handler(ctx context.Context, event any) error {
    // Flush spans before Lambda freezes the execution environment
    defer uptrace.ForceFlush(ctx)

    ctx, span := tracer.Start(ctx, "handle-event")
    defer span.End()

    // Your handler logic here
    return nil
}

func main() {
    lambda.Start(handler)
}
```

## Vercel

On [Vercel](https://vercel.com/docs/runtimes#official-runtimes/go), configure OpenTelemetry in the `init` function and force flush spans when the handler exits.

```go
package handler

import (
    "fmt"
    "net/http"

    "go.opentelemetry.io/otel"
    "github.com/uptrace/uptrace-go/uptrace"
)

var tracer = otel.Tracer("app_or_package_name")

func init() {
    uptrace.ConfigureOpentelemetry(
        // Use UPTRACE_DSN environment variable
        uptrace.WithServiceName("my-vercel-function"),
        uptrace.WithServiceVersion("1.0.0"),
    )
}

func Handler(w http.ResponseWriter, req *http.Request) {
    ctx := req.Context()

    // Flush buffered spans before the function exits
    defer uptrace.ForceFlush(ctx)

    ctx, span := tracer.Start(ctx, "handler-name")
    defer span.End()

    fmt.Fprintf(w, "<h1>Hello from Go!</h1>")
}
```

## Google Cloud Functions

Google Cloud Functions follow the same pattern as Vercel:

```go
package function

import (
    "net/http"

    "go.opentelemetry.io/otel"
    "github.com/uptrace/uptrace-go/uptrace"
)

var tracer = otel.Tracer("app_or_package_name")

func init() {
    uptrace.ConfigureOpentelemetry(
        uptrace.WithServiceName("my-cloud-function"),
    )
}

func MyFunction(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    defer uptrace.ForceFlush(ctx)

    ctx, span := tracer.Start(ctx, "my-function")
    defer span.End()

    // Your function logic here
}
```

## Best Practices

### Use Environment Variables

Configure your DSN via environment variables rather than hardcoding:

```go
// The SDK automatically reads UPTRACE_DSN
uptrace.ConfigureOpentelemetry(
    uptrace.WithServiceName("my-function"),
)
```

### Minimize Cold Start Impact

Keep `init()` lightweight. The OpenTelemetry SDK initialization is fast, but avoid loading large resources during init.

### Handle Timeouts Gracefully

If your function times out, spans may not be flushed. Consider setting a shorter internal timeout to allow time for flushing:

```go
func handler(ctx context.Context, event any) error {
    // Create a context with slightly shorter timeout
    ctx, cancel := context.WithTimeout(ctx, 25*time.Second) // Lambda timeout is 30s
    defer cancel()

    defer uptrace.ForceFlush(ctx)

    // Your logic here
    return nil
}
```

## What's Next?

- [OpenTelemetry Go Tracing](/get/opentelemetry-go/tracing) - Create spans and instrument your code
- [OpenTelemetry Go Sampling](/get/opentelemetry-go/sampling) - Reduce costs in high-volume functions
- [OpenTelemetry Go Lambda Guide](/guides/opentelemetry-go-lambda) - Detailed AWS Lambda setup
