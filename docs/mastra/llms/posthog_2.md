# Source: https://mastra.ai/reference/observability/tracing/exporters/posthog

# PosthogExporter

Sends Tracing data to PostHog for AI observability and analytics.

## Constructor

```typescript
new PosthogExporter(config: PosthogExporterConfig)
```

## PosthogExporterConfig

```typescript
interface PosthogExporterConfig extends BaseExporterConfig {
  apiKey?: string
  host?: string
  flushAt?: number
  flushInterval?: number
  serverless?: boolean
  defaultDistinctId?: string
  enablePrivacyMode?: boolean
}
```

Extends `BaseExporterConfig`, which includes:

- `logger?: IMastraLogger` - Logger instance
- `logLevel?: LogLevel | 'debug' | 'info' | 'warn' | 'error'` - Log level (default: INFO)

## Methods

### exportTracingEvent

```typescript
async exportTracingEvent(event: TracingEvent): Promise<void>
```

Exports a tracing event to PostHog.

### flush

```typescript
async flush(): Promise<void>
```

Force flushes any buffered events to PostHog without shutting down the exporter. Useful in serverless environments where you need to ensure spans are exported before the runtime terminates.

### shutdown

```typescript
async shutdown(): Promise<void>
```

Flushes pending batched events and shuts down the PostHog client.

## Usage

### Zero-Config (using environment variables)

```typescript
import { PosthogExporter } from '@mastra/posthog'

// Reads from POSTHOG_API_KEY, POSTHOG_HOST
const exporter = new PosthogExporter()
```

### Explicit Configuration

```typescript
import { PosthogExporter } from '@mastra/posthog'

const exporter = new PosthogExporter({
  apiKey: process.env.POSTHOG_API_KEY!,
  host: 'https://us.i.posthog.com',
  serverless: true,
})
```

## Span Type Mapping

| Mastra Span Type    | PostHog Event Type |
| ------------------- | ------------------ |
| `MODEL_GENERATION`  | `$ai_generation`   |
| `MODEL_STEP`        | `$ai_generation`   |
| `MODEL_CHUNK`       | `$ai_span`         |
| `TOOL_CALL`         | `$ai_span`         |
| `MCP_TOOL_CALL`     | `$ai_span`         |
| `PROCESSOR_RUN`     | `$ai_span`         |
| `AGENT_RUN`         | `$ai_span`         |
| `WORKFLOW_RUN`      | `$ai_span`         |
| All other workflows | `$ai_span`         |
| `GENERIC`           | `$ai_span`         |