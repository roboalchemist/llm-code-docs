# Source: https://uptrace.dev/raw/opentelemetry/env-vars.md

# Guide to OpenTelemetry Environment Variables

> Master OpenTelemetry environment variables for production deployments. Complete guide covering OTEL_EXPORTER_OTLP_ENDPOINT, sampling, batching, SSL/TLS, and signal-specific configuration with practical examples.

OpenTelemetry environment variables let you configure observability settings without modifying your application code. This guide covers all critical environment variables, advanced configuration techniques, and performance optimization strategies for production environments.

## What Are OpenTelemetry Environment Variables?

OpenTelemetry environment variables provide a flexible configuration mechanism for the OpenTelemetry SDK and [Collector](/opentelemetry/collector). These variables control telemetry data collection, processing, and export behavior across different environments without requiring application code modifications.

Key advantages:

- **Zero-code configuration** changes between environments
- **Runtime flexibility** for tuning performance and resource usage
- **Standardized configuration** across different programming languages
- **Production-ready** settings management

## Main OpenTelemetry Environment Variables

### 1. OTEL_EXPORTER_OTLP_ENDPOINT

The most critical variable for configuring where your telemetry data is sent via the OpenTelemetry Protocol (OTLP).

```bash
# HTTP endpoint (default port 4318)
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318

# gRPC endpoint (default port 4317)
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# Production endpoint with TLS
export OTEL_EXPORTER_OTLP_ENDPOINT=https://otel-collector.company.com:4317
```

### 2. OTEL_RESOURCE_ATTRIBUTES

Define resource attributes that provide context for all telemetry data from your service.

```bash
export OTEL_RESOURCE_ATTRIBUTES="service.name=user-service,service.version=1.2.0,deployment.environment=production,service.namespace=auth"
```

**Essential attributes to include:**

- `service.name` - Service identifier
- `service.version` - Application version
- `deployment.environment` - Environment (dev/staging/prod)
- `service.instance.id` - Unique instance identifier

### 3. OTEL_SERVICE_NAME

Quick way to set the service name (takes precedence over service.name in OTEL_RESOURCE_ATTRIBUTES).

```bash
export OTEL_SERVICE_NAME=payment-processor
```

### 4. OTEL_TRACES_SAMPLER

Control trace sampling to manage data volume and costs.

```bash
# Sample 10% of traces
export OTEL_TRACES_SAMPLER=traceidratio
export OTEL_TRACES_SAMPLER_ARG=0.1

# Always sample (development only)
export OTEL_TRACES_SAMPLER=always_on

# Never sample
export OTEL_TRACES_SAMPLER=always_off

# Parent-based sampling (production recommended)
export OTEL_TRACES_SAMPLER=parentbased_traceidratio
export OTEL_TRACES_SAMPLER_ARG=0.05
```

### 5. OTEL_PROPAGATORS

Configure [context propagation](/opentelemetry/context-propagation) formats for distributed tracing.

```bash
export OTEL_PROPAGATORS=tracecontext,baggage
export OTEL_PROPAGATORS=tracecontext,baggage,b3
export OTEL_PROPAGATORS=tracecontext,baggage,jaeger,xray
```

See the [Context Propagation](/opentelemetry/context-propagation) guide for details on W3C TraceContext, B3, and other propagation formats.

## Signal-Specific Configuration

OpenTelemetry handles three types of telemetry signals: [traces](/opentelemetry/distributed-tracing), [metrics](/opentelemetry/metrics), and [logs](/opentelemetry/logs). Each signal type can be configured independently with its own exporter, endpoint, and processing settings. This granular control allows you to optimize each signal type based on your specific observability requirements and route different data types to specialized backends for optimal performance and cost management.

### Traces Configuration

Distributed tracing tracks requests as they flow through your system, providing visibility into service dependencies and performance bottlenecks. Trace configuration controls how trace data is collected, processed, and exported to your observability backend.

```bash
# Trace exporter
export OTEL_TRACES_EXPORTER=otlp

# Trace-specific endpoint
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4317/v1/traces

# Trace headers
export OTEL_EXPORTER_OTLP_TRACES_HEADERS="api-key=your-key,custom-header=value"

# Trace timeout
export OTEL_EXPORTER_OTLP_TRACES_TIMEOUT=10000
```

### Metrics Configuration

Metrics provide quantitative measurements of your system's performance and health over time. Unlike traces that capture individual request flows, metrics aggregate data points to reveal trends, patterns, and statistical insights about system behavior and resource utilization.

```bash
# Metrics exporter
export OTEL_METRICS_EXPORTER=otlp

# Metrics-specific endpoint
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://localhost:4317/v1/metrics

# Metrics export interval (milliseconds)
export OTEL_METRIC_EXPORT_INTERVAL=60000

# Metrics timeout
export OTEL_EXPORTER_OTLP_METRICS_TIMEOUT=10000
```

### Logs Configuration

[Structured logging](/glossary/structured-logging) integration allows correlation between logs and traces, providing complete context for troubleshooting and debugging. Log configuration manages how application logs are collected and exported alongside telemetry data for comprehensive observability.

```bash
# Logs exporter
export OTEL_LOGS_EXPORTER=otlp

# Logs-specific endpoint
export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://localhost:4317/v1/logs

# Logs timeout
export OTEL_EXPORTER_OTLP_LOGS_TIMEOUT=10000
```

## Batch Processing in OpenTelemetry

Batch processing controls how spans and log records are aggregated and sent to exporters. Properly configuring batch processing allows you to balance the efficiency of data transmission with resource usage, especially in high-throughput environments. OpenTelemetry offers several configuration options to manage how data is batched before being exported.

### Span Batch Processor (BSP) Configuration

The Span Batch Processor collects spans and exports them in batches to improve performance and reduce network overhead. Understanding these settings helps optimize both throughput and resource consumption for trace data processing.

```bash
# Maximum batch size for spans
export OTEL_BSP_MAX_EXPORT_BATCH_SIZE=512

# Export timeout in milliseconds
export OTEL_BSP_EXPORT_TIMEOUT=30000

# Schedule delay between batches
export OTEL_BSP_SCHEDULE_DELAY=5000

# Maximum queue size
export OTEL_BSP_MAX_QUEUE_SIZE=2048
```

### Batch Log Record Processor (BLRP) Configuration

Similar to span processing, log record batching optimizes the export of structured logs and ensures efficient correlation with trace data. Log records often contain more detailed contextual information than spans, making proper batching configuration crucial for maintaining performance.

```bash
# Maximum batch size for logs
export OTEL_BLRP_MAX_EXPORT_BATCH_SIZE=512

# Export timeout
export OTEL_BLRP_EXPORT_TIMEOUT=30000

# Schedule delay
export OTEL_BLRP_SCHEDULE_DELAY=1000

# Maximum queue size
export OTEL_BLRP_MAX_QUEUE_SIZE=2048
```

## Managing Resource and Attribute Limits

OpenTelemetry provides configuration options to limit both the number of attributes and spans processed, helping prevent excessive memory usage and ensuring efficient resource utilization in production environments. These limits act as safeguards against runaway telemetry generation that could impact application performance.

### Span Limits Configuration

Spans carry attributes, events, and links that provide context about operations. However, unlimited data can lead to memory exhaustion and performance degradation, especially in high-cardinality scenarios.

**OTEL_SPAN_ATTRIBUTE_COUNT_LIMIT**<br />


Sets the maximum number of attributes allowed per span. This prevents spans from growing too large while ensuring essential context is preserved. When the limit is reached, additional attributes are dropped.

```bash
export OTEL_SPAN_ATTRIBUTE_COUNT_LIMIT=128
```

**OTEL_SPAN_ATTRIBUTE_VALUE_LENGTH_LIMIT**<br />


Controls the maximum length of attribute values in characters. Long attribute values, such as SQL queries or request payloads, can significantly impact memory usage and export performance.

```bash
export OTEL_SPAN_ATTRIBUTE_VALUE_LENGTH_LIMIT=4096
```

**OTEL_SPAN_EVENT_COUNT_LIMIT**<br />


Defines the maximum number of events that can be added to a single span. Events represent discrete occurrences during span execution, such as exceptions or custom markers.

```bash
export OTEL_SPAN_EVENT_COUNT_LIMIT=128
```

**OTEL_SPAN_LINK_COUNT_LIMIT**<br />


Specifies the maximum number of links allowed per span. Links connect spans to other spans, typically used for correlation across different traces or asynchronous operations.

```bash
export OTEL_SPAN_LINK_COUNT_LIMIT=128
```

### Global Attribute Limits

These settings apply across all telemetry signals and provide system-wide protection against excessive attribute usage.

**OTEL_ATTRIBUTE_COUNT_LIMIT**<br />


Sets a global limit on the number of attributes for any telemetry record. This acts as a fallback when signal-specific limits are not configured.

```bash
export OTEL_ATTRIBUTE_COUNT_LIMIT=128
```

**OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT**<br />


Establishes a global maximum length for attribute values across all signals. This helps maintain consistent memory usage patterns throughout your telemetry pipeline.

```bash
export OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT=4096
```

### Impact of Limit Configuration

- **Memory Protection**: Properly configured limits prevent individual spans or records from consuming excessive memory
- **Performance Optimization**: Smaller, bounded telemetry records improve processing speed and reduce network overhead
- **Data Quality**: Limits encourage developers to include only essential context, improving signal-to-noise ratio
- **Backend Compatibility**: Many observability backends have their own limits; SDK limits should align with backend capabilities

## Advanced OpenTelemetry Configuration

OpenTelemetry provides advanced configuration options for fine-tuning security, performance, and integration with existing infrastructure. These settings help optimize your observability setup for production environments and complex deployment scenarios.

### SSL/TLS Configuration

OpenTelemetry supports various authentication and encryption mechanisms to protect your observability data in transit and ensure secure communication with backend systems.

```bash
# Disable TLS (development only)
export OTEL_EXPORTER_OTLP_INSECURE=true

# Custom certificate path
export OTEL_EXPORTER_OTLP_CERTIFICATE=/path/to/cert.pem

# Client certificate authentication
export OTEL_EXPORTER_OTLP_CLIENT_KEY=/path/to/client.key
export OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE=/path/to/client.crt
```

### Multiple Exporters Configuration

OpenTelemetry supports sending telemetry data to multiple destinations simultaneously. This capability is valuable for gradual migrations, backup systems, or sending different signals to specialized backends optimized for specific data types.

```bash
# Multiple trace exporters
export OTEL_TRACES_EXPORTER=otlp,jaeger,zipkin

# Multiple metrics exporters
export OTEL_METRICS_EXPORTER=otlp,prometheus
```

### Legacy Exporter Configuration

While OTLP is the recommended protocol for new deployments, many organizations still use legacy exporters during migration phases or for integration with existing [monitoring infrastructure](/glossary/what-is-infrastructure-monitoring). Understanding these configurations helps maintain compatibility during transitions.

#### Uptrace Integration

Uptrace is an OpenTelemetry-native observability platform that provides comprehensive monitoring capabilities. These variables configure direct export to Uptrace for organizations adopting modern observability practices.

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317
export OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=https://token@api.uptrace.dev/project"
```

#### Jaeger Integration

Jaeger remains a popular distributed tracing backend, especially in organizations that adopted distributed tracing early. These variables configure direct export to Jaeger without requiring an OpenTelemetry Collector intermediary.

```bash
export OTEL_EXPORTER_JAEGER_ENDPOINT=http://localhost:14268/api/traces
export OTEL_EXPORTER_JAEGER_USER=username
export OTEL_EXPORTER_JAEGER_PASSWORD=password
```

#### Zipkin Integration

Zipkin provides a lightweight tracing solution with a simple HTTP API. This configuration enables direct trace export to Zipkin servers for organizations using Zipkin as their primary tracing backend.

```bash
export OTEL_EXPORTER_ZIPKIN_ENDPOINT=http://localhost:9411/api/v2/spans
```

#### Prometheus Configuration

For environments using Prometheus for metrics collection, configure the built-in HTTP server that exposes metrics in Prometheus format for scraping. This allows integration with existing Prometheus-based monitoring infrastructure.

```bash
export OTEL_EXPORTER_PROMETHEUS_HOST=0.0.0.0
export OTEL_EXPORTER_PROMETHEUS_PORT=9464
```

## Environment-Specific Configuration Best Practices

Different deployment environments require distinct observability configurations to balance development productivity, staging accuracy, and production efficiency. Proper environment-specific setup ensures optimal performance and cost management across your entire deployment pipeline.

### Development Environment Configuration

Development environments prioritize debugging capabilities and fast feedback loops over efficiency. Configuration should maximize visibility while maintaining developer productivity and enabling comprehensive testing of observability features.

```bash
export OTEL_SERVICE_NAME=my-service-dev
export OTEL_TRACES_SAMPLER=always_on
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
export OTEL_EXPORTER_OTLP_INSECURE=true
export OTEL_LOG_LEVEL=debug
```

### Staging Environment Configuration

Staging environments should closely mirror production settings while allowing for comprehensive testing and validation of observability configuration before production deployment. This environment serves as the final validation step for configuration changes.

```bash
export OTEL_SERVICE_NAME=my-service-staging
export OTEL_TRACES_SAMPLER=parentbased_traceidratio
export OTEL_TRACES_SAMPLER_ARG=0.1
export OTEL_EXPORTER_OTLP_ENDPOINT=https://staging-otel.company.com:4317
export OTEL_LOG_LEVEL=info
```

### Production Environment Configuration

Production environments require carefully tuned settings that balance observability needs with performance impact and cost considerations. Every setting should be optimized for efficiency and reliability while maintaining adequate visibility for operations and incident response.

```bash
export OTEL_SERVICE_NAME=my-service
export OTEL_RESOURCE_ATTRIBUTES="service.name=my-service,service.version=1.0.0,deployment.environment=production"
export OTEL_TRACES_SAMPLER=parentbased_traceidratio
export OTEL_TRACES_SAMPLER_ARG=0.01
export OTEL_EXPORTER_OTLP_ENDPOINT=https://otel-collector.company.com:4317
export OTEL_BSP_MAX_EXPORT_BATCH_SIZE=512
export OTEL_BSP_EXPORT_TIMEOUT=30000
export OTEL_LOG_LEVEL=warn
```

## Best Practices for OpenTelemetry Environment Variables

Successful OpenTelemetry deployments require thoughtful configuration management, security considerations, and operational practices. Following established best practices ensures reliable, secure, and maintainable observability infrastructure.

### Environment-Specific Variable Management

Configure environment variables specifically for each deployment environment to prevent misconfigurations and ensure optimal performance. Development environments should use comprehensive sampling and debug logging, staging should mirror production with higher sampling rates for testing, and production requires optimized settings for performance and cost control.

### Configuration Management Tools

Use configuration management tools like Ansible, Terraform, or Kubernetes ConfigMaps to maintain consistency across environments. These tools provide centralized management, version control tracking, and automated deployment while reducing manual errors and configuration drift.

### Security Considerations

Protect sensitive information in environment variables through dedicated secret management systems like HashiCorp Vault or AWS Secrets Manager. Never log environment variable values, implement proper access controls, and regularly rotate credentials according to security policies.

### Monitoring and Logging Infrastructure

Monitor the health of your observability infrastructure itself. Configure appropriate logging levels for each environment, track export success rates and processing latency, and set up alerts for infrastructure failures to maintain confidence in monitoring capabilities.

### Documentation and Knowledge Management

Maintain comprehensive documentation of all environment variables, including their purpose, recommended values, and dependencies. Keep configuration change logs and create troubleshooting guides to help team members resolve issues quickly and understand configuration decisions.

## Conclusion

OpenTelemetry environment variables provide powerful configuration capabilities for production observability without requiring code changes. This comprehensive approach to configuration management enables teams to optimize their observability setup for different environments, performance requirements, and operational constraints.

Key takeaways for effective OpenTelemetry configuration:

**Start with essential variables** like `OTEL_SERVICE_NAME`, `OTEL_EXPORTER_OTLP_ENDPOINT`, and `OTEL_TRACES_SAMPLER` to establish basic telemetry flow, then gradually optimize based on your specific requirements and constraints.

**Implement environment-specific configuration** that balances development productivity, staging accuracy, and production efficiency. Each environment serves different purposes and requires tailored observability settings.

**Optimize sampling and batching** to control costs and resource usage while maintaining adequate observability coverage. The right configuration prevents both data overload and visibility gaps.

**Prioritize security and monitoring** of your observability infrastructure itself. Proper secret management, TLS configuration, and infrastructure monitoring ensure reliable telemetry collection.

Mastering these environment variables enables you to build robust, scalable observability solutions that adapt to your operational needs and provide actionable insights for maintaining healthy, performant applications in production environments.
