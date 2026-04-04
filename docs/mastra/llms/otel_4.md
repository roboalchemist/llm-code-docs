# Source: https://mastra.ai/reference/observability/tracing/exporters/otel

# OtelExporter

Sends Tracing data to any OpenTelemetry-compatible observability platform using standardized GenAI semantic conventions.

## Constructor

```typescript
new OtelExporter(config: OtelExporterConfig)
```

## OtelExporterConfig

```typescript
interface OtelExporterConfig {
  provider?: ProviderConfig
  timeout?: number
  batchSize?: number
  logLevel?: 'debug' | 'info' | 'warn' | 'error'
}
```

## Provider Configurations

### Dash0Config

```typescript
interface Dash0Config {
  apiKey?: string
  endpoint?: string
  dataset?: string
}
```

### SignozConfig

```typescript
interface SignozConfig {
  apiKey?: string
  region?: 'us' | 'eu' | 'in'
  endpoint?: string
}
```

### NewRelicConfig

```typescript
interface NewRelicConfig {
  apiKey?: string
  endpoint?: string
}
```

### TraceloopConfig

```typescript
interface TraceloopConfig {
  apiKey?: string
  destinationId?: string
  endpoint?: string
}
```

### LaminarConfig

```typescript
interface LaminarConfig {
  apiKey?: string
  endpoint?: string
}
```

### CustomConfig

```typescript
interface CustomConfig {
  endpoint: string
  protocol?: 'http/json' | 'http/protobuf' | 'grpc' | 'zipkin'
  headers?: Record<string, string>
}
```

## Methods

### exportTracingEvent

```typescript
async exportTracingEvent(event: TracingEvent): Promise<void>
```

Exports a tracing event to the configured OTEL backend.

### flush

```typescript
async flush(): Promise<void>
```

Force flushes any buffered spans to the OTEL backend without shutting down the exporter. Useful in serverless environments where you need to ensure spans are exported before the runtime terminates.

### shutdown

```typescript
async shutdown(): Promise<void>
```

Flushes pending traces and shuts down the exporter.

## Usage Examples

### Zero-Config (using environment variables)

```typescript
import { OtelExporter } from '@mastra/otel-exporter'

// Set SIGNOZ_API_KEY, SIGNOZ_REGION environment variables
const exporter = new OtelExporter({ provider: { signoz: {} } })

// Or for other providers:
// Set DASH0_API_KEY, DASH0_ENDPOINT for Dash0
// Set NEW_RELIC_LICENSE_KEY for New Relic
// Set TRACELOOP_API_KEY for Traceloop
// Set LMNR_PROJECT_API_KEY for Laminar
```

### Explicit Configuration

```typescript
import { OtelExporter } from '@mastra/otel-exporter'

const exporter = new OtelExporter({
  provider: {
    signoz: {
      apiKey: process.env.SIGNOZ_API_KEY,
      region: 'us',
    },
  },
})
```

### With Custom Endpoint

```typescript
const exporter = new OtelExporter({
  provider: {
    custom: {
      endpoint: 'https://my-collector.example.com/v1/traces',
      protocol: 'http/protobuf',
      headers: {
        'x-api-key': process.env.API_KEY,
      },
    },
  },
  timeout: 60000,
  logLevel: 'debug',
})
```

## Protocol Requirements

Different providers require different OTEL exporter packages:

| Protocol      | Required Package                           | Providers                  |
| ------------- | ------------------------------------------ | -------------------------- |
| gRPC          | `@opentelemetry/exporter-trace-otlp-grpc`  | Dash0                      |
| HTTP/Protobuf | `@opentelemetry/exporter-trace-otlp-proto` | SigNoz, New Relic, Laminar |
| HTTP/JSON     | `@opentelemetry/exporter-trace-otlp-http`  | Traceloop, Custom          |
| Zipkin        | `@opentelemetry/exporter-zipkin`           | Zipkin collectors          |

## Tags Support

The OtelExporter supports trace tagging for categorization and filtering. Tags are only applied to root spans and are stored as the `mastra.tags` attribute.

### Usage

```typescript
const result = await agent.generate('Hello', {
  tracingOptions: {
    tags: ['production', 'experiment-v2', 'user-request'],
  },
})
```

### How Tags Are Stored

Tags are stored as a JSON-stringified array in the `mastra.tags` span attribute for maximum backend compatibility:

```json
{
  "mastra.tags": "[\"production\",\"experiment-v2\",\"user-request\"]"
}
```

> **Note:** While the OpenTelemetry specification supports native array attributes, many backends (Jaeger, Zipkin, Tempo) have limited array support. JSON strings ensure consistent behavior across all observability platforms.

## Related

- [OtelExporter Guide](https://mastra.ai/docs/observability/tracing/exporters/otel) - Setup guide with provider configurations
- [OtelBridge](https://mastra.ai/docs/observability/tracing/bridges/otel) - For bidirectional OTEL context integration
- [Tracing Overview](https://mastra.ai/docs/observability/tracing/overview) - General tracing concepts