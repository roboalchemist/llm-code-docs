# Source: https://cobra.dev/docs/how-to-guides/context-and-tracing/

Title: Context & Tracing Support

URL Source: https://cobra.dev/docs/how-to-guides/context-and-tracing/

Markdown Content:
Transform your Cobra CLI applications from opaque tools into observable systems with comprehensive context propagation and distributed tracing. This guide provides practical, step-by-step instructions for implementing OpenTelemetry-based observability that makes your applications “Observable from Day One.”

Prerequisites
-------------

Before implementing observability in your Cobra CLI applications, ensure you have:

*   **Go 1.21+** - Required for OpenTelemetry SDK compatibility
*   **Basic Cobra knowledge** - Understanding of command structure and execution
*   **Observability concepts** - Familiarity with traces, spans, and context propagation
*   **Backend system** - Access to Jaeger, OTEL Collector, or cloud tracing service

Quick Start: Basic Context Usage
--------------------------------

Every Cobra command provides access to a context through `cmd.Context()`. This context carries cancellation signals, deadlines, and trace information throughout your application.

go

```
package main

import (
    "context"
    "fmt"
    "time"

    "github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
    Use: "myapp",
    RunE: func(cmd *cobra.Command, args []string) error {
        ctx := cmd.Context()
        
        // Context carries cancellation and tracing information
        return processWithContext(ctx, args)
    },
}

func processWithContext(ctx context.Context, args []string) error {
    // Check for cancellation
    select {
    case <-ctx.Done():
        return ctx.Err()
    default:
    }
    
    // Pass context to downstream operations
    return fetchDataWithTimeout(ctx, args)
}

func fetchDataWithTimeout(ctx context.Context, args []string) error {
    // Create a timeout context from the parent
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()
    
    // Simulate work that respects context cancellation
    select {
    case <-time.After(3 * time.Second):
        fmt.Println("Work completed successfully")
        return nil
    case <-ctx.Done():
        return fmt.Errorf("operation cancelled: %w", ctx.Err())
    }
}
```

OpenTelemetry Setup
-------------------

### SDK Initialization

Initialize the OpenTelemetry SDK in your main function before creating your Cobra commands:

go

```
package main

import (
    "context"
    "log"
    "os"

    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"
    "go.opentelemetry.io/otel/propagation"
    "go.opentelemetry.io/otel/sdk/resource"
    "go.opentelemetry.io/otel/sdk/trace"
    semconv "go.opentelemetry.io/otel/semconv/v1.21.0"
)

func initTracing(ctx context.Context, serviceName string) func() {
    // Create OTLP exporter
    exporter, err := otlptracehttp.New(ctx,
        otlptracehttp.WithEndpoint("http://localhost:4318"),
        otlptracehttp.WithInsecure(),
    )
    if err != nil {
        log.Printf("Failed to create exporter: %v", err)
        return func() {}
    }

    // Create resource with service information
    res, err := resource.New(ctx,
        resource.WithAttributes(
            semconv.ServiceName(serviceName),
            semconv.ServiceVersion("v1.0.0"),
            semconv.DeploymentEnvironment("development"),
        ),
    )
    if err != nil {
        log.Printf("Failed to create resource: %v", err)
        return func() {}
    }

    // Create trace provider
    tp := trace.NewTracerProvider(
        trace.WithBatcher(exporter),
        trace.WithResource(res),
        trace.WithSampler(trace.AlwaysSample()),
    )

    // Set global trace provider and propagator
    otel.SetTracerProvider(tp)
    otel.SetTextMapPropagator(propagation.TraceContext{})

    return func() {
        if err := tp.Shutdown(ctx); err != nil {
            log.Printf("Error shutting down tracer provider: %v", err)
        }
    }
}

func main() {
    ctx := context.Background()
    
    // Initialize tracing
    shutdown := initTracing(ctx, "myapp")
    defer shutdown()
    
    // Execute root command with tracing enabled
    if err := rootCmd.ExecuteContext(ctx); err != nil {
        os.Exit(1)
    }
}
```

### Environment Configuration

Make your tracing setup configurable through environment variables:

go

```
package main

import (
    "context"
    "os"
    "strconv"

    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"
    "go.opentelemetry.io/otel/sdk/trace"
)

type TracingConfig struct {
    Endpoint    string
    ServiceName string
    Environment string
    SampleRate  float64
}

func getTracingConfig() TracingConfig {
    sampleRate, _ := strconv.ParseFloat(os.Getenv("OTEL_SAMPLE_RATE"), 64)
    if sampleRate == 0 {
        sampleRate = 1.0 // Default to always sample
    }

    return TracingConfig{
        Endpoint:    getEnvDefault("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318"),
        ServiceName: getEnvDefault("OTEL_SERVICE_NAME", "cobra-app"),
        Environment: getEnvDefault("OTEL_DEPLOYMENT_ENVIRONMENT", "development"),
        SampleRate:  sampleRate,
    }
}

func getEnvDefault(key, defaultValue string) string {
    if value := os.Getenv(key); value != "" {
        return value
    }
    return defaultValue
}

func createExporter(ctx context.Context, config TracingConfig) (trace.SpanExporter, error) {
    return otlptracehttp.New(ctx,
        otlptracehttp.WithEndpoint(config.Endpoint),
        otlptracehttp.WithInsecure(),
    )
}
```

Instrumentation Patterns
------------------------

### Command-Level Tracing

Instrument individual commands to create spans for each operation:

go

```
package main

import (
    "context"
    "fmt"

    "github.com/spf13/cobra"
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/attribute"
    "go.opentelemetry.io/otel/codes"
    "go.opentelemetry.io/otel/trace"
)

var tracer = otel.Tracer("myapp")

var deployCmd = &cobra.Command{
    Use:   "deploy [environment]",
    Short: "Deploy application to specified environment",
    Args:  cobra.ExactArgs(1),
    RunE: func(cmd *cobra.Command, args []string) error {
        ctx := cmd.Context()
        environment := args[0]
        
        // Create a span for this command
        ctx, span := tracer.Start(ctx, "deploy_command",
            trace.WithAttributes(
                attribute.String("environment", environment),
                attribute.String("command", "deploy"),
            ),
        )
        defer span.End()
        
        if err := deployToEnvironment(ctx, environment); err != nil {
            span.RecordError(err)
            span.SetStatus(codes.Error, err.Error())
            return err
        }
        
        span.SetStatus(codes.Ok, "Deployment successful")
        return nil
    },
}

func deployToEnvironment(ctx context.Context, env string) error {
    // Create child span for the deployment process
    ctx, span := tracer.Start(ctx, "deployment_process",
        trace.WithAttributes(
            attribute.String("target_environment", env),
        ),
    )
    defer span.End()
    
    // Add deployment steps as events
    span.AddEvent("Starting pre-deployment checks")
    if err := runPreDeploymentChecks(ctx); err != nil {
        span.RecordError(err)
        return fmt.Errorf("pre-deployment checks failed: %w", err)
    }
    
    span.AddEvent("Deploying application")
    if err := performDeployment(ctx, env); err != nil {
        span.RecordError(err)
        return fmt.Errorf("deployment failed: %w", err)
    }
    
    span.AddEvent("Running post-deployment verification")
    return verifyDeployment(ctx, env)
}
```

### Error Handling and Span Status

Properly handle errors and set span statuses to provide meaningful observability:

go

```
package main

import (
    "context"
    "errors"
    "fmt"

    "go.opentelemetry.io/otel/attribute"
    "go.opentelemetry.io/otel/codes"
    "go.opentelemetry.io/otel/trace"
)

func processFileWithTracing(ctx context.Context, filename string) error {
    ctx, span := tracer.Start(ctx, "process_file",
        trace.WithAttributes(
            attribute.String("file.name", filename),
        ),
    )
    defer span.End()
    
    // Add file size as an attribute if available
    if size, err := getFileSize(filename); err == nil {
        span.SetAttributes(attribute.Int64("file.size", size))
    }
    
    // Process the file
    content, err := readFile(ctx, filename)
    if err != nil {
        span.RecordError(err)
        
        // Set specific error codes based on error type
        if errors.Is(err, ErrFileNotFound) {
            span.SetStatus(codes.Error, "File not found")
            span.SetAttributes(attribute.String("error.type", "file_not_found"))
        } else if errors.Is(err, ErrPermissionDenied) {
            span.SetStatus(codes.Error, "Permission denied")
            span.SetAttributes(attribute.String("error.type", "permission_denied"))
        } else {
            span.SetStatus(codes.Error, "Failed to read file")
            span.SetAttributes(attribute.String("error.type", "read_error"))
        }
        
        return fmt.Errorf("failed to process file %s: %w", filename, err)
    }
    
    // Add successful processing metrics
    span.SetAttributes(
        attribute.Int("content.lines", countLines(content)),
        attribute.Bool("processing.successful", true),
    )
    
    span.SetStatus(codes.Ok, "File processed successfully")
    return nil
}

var (
    ErrFileNotFound      = errors.New("file not found")
    ErrPermissionDenied  = errors.New("permission denied")
)
```

Backend Integration
-------------------

### Jaeger Integration

Configure your application to send traces to Jaeger:

`# Start Jaeger using Docker``docker run -d --name jaeger \``-p 16686:16686 \``-p 14250:14250 \``-p 14268:14268 \``-p 14269:14269 \``-p 4317:4317 \``-p 4318:4318 \``jaegertracing/all-in-one:latest``# Set environment variables``export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4318"``export OTEL_SERVICE_NAME="my-cobra-app"``# Run your application``./myapp deploy production`

### OTEL Collector Configuration

Use the OpenTelemetry Collector for more advanced routing and processing:

yaml

```
# otel-collector-config.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 1s
    send_batch_size: 1024
  
  attributes:
    actions:
      - key: environment
        value: production
        action: insert

exporters:
  jaeger:
    endpoint: jaeger:14250
    tls:
      insecure: true
  
  logging:
    loglevel: debug

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, attributes]
      exporters: [jaeger, logging]
```

`# Run the collector``docker run -p 4317:4317 -p 4318:4318 \``-v $(pwd)/otel-collector-config.yaml:/etc/otel-collector-config.yaml \``otel/opentelemetry-collector-contrib:latest \``--config=/etc/otel-collector-config.yaml`

### Cloud Provider Integration

#### AWS X-Ray

go

```
import (
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"
    "go.opentelemetry.io/contrib/propagators/aws/xray"
)

func initAWSTracing(ctx context.Context) func() {
    exporter, err := otlptracehttp.New(ctx,
        otlptracehttp.WithEndpoint("https://api.honeycomb.io"),
        otlptracehttp.WithHeaders(map[string]string{
            "x-honeycomb-team": os.Getenv("HONEYCOMB_API_KEY"),
        }),
    )
    if err != nil {
        log.Fatal(err)
    }

    tp := trace.NewTracerProvider(
        trace.WithBatcher(exporter),
        trace.WithResource(resource.NewWithAttributes(
            semconv.SchemaURL,
            semconv.ServiceNameKey.String("cobra-app"),
        )),
    )

    otel.SetTracerProvider(tp)
    otel.SetTextMapPropagator(xray.Propagator{})
    
    return func() { tp.Shutdown(ctx) }
}
```

#### Google Cloud Trace

go

```
import (
    texporter "github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace"
)

func initGCPTracing(ctx context.Context, projectID string) func() {
    exporter, err := texporter.New(texporter.WithProjectID(projectID))
    if err != nil {
        log.Fatal(err)
    }

    tp := trace.NewTracerProvider(
        trace.WithBatcher(exporter),
        trace.WithResource(resource.NewWithAttributes(
            semconv.SchemaURL,
            semconv.ServiceNameKey.String("cobra-app"),
            semconv.ServiceVersionKey.String("1.0.0"),
        )),
    )

    otel.SetTracerProvider(tp)
    return func() { tp.Shutdown(ctx) }
}
```

Best Practices
--------------

### Performance Considerations

**Sampling Strategy**: Don’t trace every operation in production:

go

```
import "go.opentelemetry.io/otel/sdk/trace"

// Sample 1% of traces in production
sampler := trace.TraceIDRatioBased(0.01)

// Use parent-based sampling to maintain trace consistency
sampler = trace.ParentBased(sampler)

tp := trace.NewTracerProvider(
    trace.WithSampler(sampler),
    // ... other options
)
```

**Attribute Management**: Keep span attributes relevant and bounded:

go

```
// Good: Bounded, useful attributes
span.SetAttributes(
    attribute.String("user.id", userID),
    attribute.String("operation.type", "file_upload"),
    attribute.Int("file.size_mb", sizeInMB),
)

// Avoid: Unbounded attributes that can cause cardinality issues
// span.SetAttributes(attribute.String("file.content", content)) // DON'T DO THIS
```

### Context Propagation Patterns

**Passing Context Through Command Hierarchy**:

go

```
var rootCmd = &cobra.Command{
    Use: "myapp",
    PersistentPreRunE: func(cmd *cobra.Command, args []string) error {
        ctx := cmd.Context()
        
        // Add common attributes to all child commands
        ctx, span := tracer.Start(ctx, "command_execution",
            trace.WithAttributes(
                attribute.String("command.name", cmd.Name()),
                attribute.StringSlice("command.args", args),
            ),
        )
        
        // Store span in context for cleanup in PersistentPostRun
        cmd.SetContext(context.WithValue(ctx, "rootSpan", span))
        return nil
    },
    PersistentPostRunE: func(cmd *cobra.Command, args []string) error {
        if span, ok := cmd.Context().Value("rootSpan").(trace.Span); ok {
            span.End()
        }
        return nil
    },
}
```

### Production Deployment

**Resource Configuration**:

go

```
func createProductionResource(ctx context.Context) (*resource.Resource, error) {
    return resource.New(ctx,
        resource.WithFromEnv(),      // Read OTEL_RESOURCE_ATTRIBUTES
        resource.WithProcess(),      // Add process information
        resource.WithOS(),          // Add OS information
        resource.WithContainer(),   // Add container information if running in one
        resource.WithHost(),        // Add host information
        resource.WithAttributes(
            semconv.ServiceNameKey.String(os.Getenv("SERVICE_NAME")),
            semconv.ServiceVersionKey.String(os.Getenv("SERVICE_VERSION")),
            semconv.DeploymentEnvironmentKey.String(os.Getenv("ENVIRONMENT")),
        ),
    )
}
```

**Graceful Shutdown**:

go

```
func main() {
    ctx, cancel := context.WithCancel(context.Background())
    defer cancel()

    // Setup graceful shutdown
    shutdown := make(chan os.Signal, 1)
    signal.Notify(shutdown, syscall.SIGINT, syscall.SIGTERM)

    tracingShutdown := initTracing(ctx, "myapp")
    
    go func() {
        <-shutdown
        log.Println("Shutting down gracefully...")
        cancel()
        tracingShutdown()
    }()

    if err := rootCmd.ExecuteContext(ctx); err != nil {
        log.Printf("Command execution failed: %v", err)
        os.Exit(1)
    }
}
```

Troubleshooting
---------------

### Common Issues

**Problem**: Traces not appearing in backend **Solution**: Verify exporter configuration and network connectivity:

`# Test OTLP endpoint connectivity``curl -v http://localhost:4318/v1/traces \``-H "Content-Type: application/json" \``-d '{"resourceSpans":[]}'``# Check if service is receiving traces``docker logs jaeger`

**Problem**: High memory usage from tracing **Solution**: Implement proper sampling and batch configuration:

go

```
tp := trace.NewTracerProvider(
    trace.WithSampler(trace.TraceIDRatioBased(0.1)), // Sample 10%
    trace.WithBatcher(exporter,
        trace.WithBatchTimeout(time.Second*5),
        trace.WithMaxExportBatchSize(512),
        trace.WithMaxQueueSize(2048),
    ),
)
```

**Problem**: Missing trace context between commands **Solution**: Ensure context is properly propagated:

go

```
// In parent command
subCtx := context.WithValue(cmd.Context(), "trace.parent", span.SpanContext())
cmd.SetContext(subCtx)

// In child command  
parentSpanCtx := cmd.Context().Value("trace.parent").(trace.SpanContext)
ctx, span := tracer.Start(cmd.Context(), "child_operation",
    trace.WithLinks(trace.Link{SpanContext: parentSpanCtx}),
)
```

### Debugging Techniques

**Enable Debug Logging**:

go

```
import (
    "go.opentelemetry.io/otel/exporters/stdout/stdouttrace"
)

func enableDebugTracing(ctx context.Context) trace.SpanExporter {
    return stdouttrace.New(
        stdouttrace.WithPrettyPrint(),
        stdouttrace.WithoutTimestamps(),
    )
}
```

**Validate Instrumentation**:

`# Run with trace debugging enabled``OTEL_LOG_LEVEL=debug ./myapp deploy staging``# Use otel-cli for testing``otel-cli exec --service myapp-test --name test_operation -- \``./myapp process --file example.txt`

### Performance Monitoring

Monitor the performance impact of tracing on your CLI applications:

go

```
import (
    "go.opentelemetry.io/otel/metric"
    "go.opentelemetry.io/otel/metric/global"
)

var (
    spanCounter = global.Meter("myapp").NewInt64Counter(
        "spans_created_total",
        metric.WithDescription("Total number of spans created"),
    )
    
    tracingOverhead = global.Meter("myapp").NewFloat64Histogram(
        "tracing_overhead_duration_ms",
        metric.WithDescription("Overhead introduced by tracing operations"),
    )
)

func instrumentedOperation(ctx context.Context) error {
    start := time.Now()
    defer func() {
        overhead := time.Since(start).Seconds() * 1000
        tracingOverhead.Record(ctx, overhead)
    }()
    
    ctx, span := tracer.Start(ctx, "operation")
    defer span.End()
    
    spanCounter.Add(ctx, 1)
    
    return doActualWork(ctx)
}
```

Your Cobra CLI applications are now observable from day one. This comprehensive tracing setup provides visibility into command execution, performance bottlenecks, and error patterns, transforming your CLI tools into fully observable systems that integrate seamlessly with modern observability platforms.
