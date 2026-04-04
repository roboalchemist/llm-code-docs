# Source: https://braintrust.dev/docs/reference/integrations/otel-js/0.1.2/otel-js.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenTelemetry JS Integration

> OpenTelemetry JS Integration v0.1.2

The `@braintrust/otel` package provides OpenTelemetry integration for Braintrust tracing.

## Installation

<CodeGroup>
  ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  npm install @braintrust/otel
  ```

  ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pnpm add @braintrust/otel
  ```
</CodeGroup>

## Quick start

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { BraintrustSpanProcessor } from "@braintrust/otel";
import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";

// Add the Braintrust span processor
const provider = new NodeTracerProvider();
provider.addSpanProcessor(new BraintrustSpanProcessor());
```

## API Reference

### Functions

#### addParentToBaggage

Add braintrust.parent to OTEL baggage.

This ensures that when using propagation inject() for distributed tracing,
the braintrust.parent will be propagated via baggage to downstream services.

#### addSpanParentToBaggage

Copy braintrust.parent from span attribute to OTEL baggage.

BraintrustSpanProcessor automatically sets braintrust.parent as a span attribute
when OTEL spans are created within Braintrust contexts. This function copies that
attribute to OTEL baggage so it propagates when using inject() for distributed tracing.

#### contextFromSpanExport

Create an OTEL context from a Braintrust span export string.

Used for distributed tracing scenarios where a Braintrust span in one service
needs to be the parent of an OTEL span in another service.

#### parentFromHeaders

Extract a Braintrust-compatible parent string from W3C Trace Context headers.

This converts OTEL trace context headers (traceparent/baggage) into a format
that can be passed as the 'parent' parameter to Braintrust's traced() method.

#### resetOtelCompat

resetOtelCompat function.

#### setupOtelCompat

setupOtelCompat function.

### Classes

#### BraintrustExporter

A trace exporter that sends OpenTelemetry spans to Braintrust.

This exporter wraps the standard OTLP trace exporter and can be used with
any OpenTelemetry setup, including @vercel/otel's registerOTel function,
NodeSDK, or custom tracer providers. It can optionally filter spans to
only send AI-related telemetry.

Environment Variables:

* BRAINTRUST\_API\_KEY: Your Braintrust API key
* BRAINTRUST\_PARENT: Parent identifier (e.g., "project\_name:test")
* BRAINTRUST\_API\_URL: Base URL for Braintrust API (defaults to [https://api.braintrust.dev](https://api.braintrust.dev))

#### BraintrustSpanProcessor

A span processor that sends OpenTelemetry spans to Braintrust.

This processor uses a BatchSpanProcessor and an OTLP exporter configured
to send data to Braintrust's telemetry endpoint. Span filtering is disabled
by default but can be enabled with the filterAISpans option.

Environment Variables:

* BRAINTRUST\_API\_KEY: Your Braintrust API key
* BRAINTRUST\_PARENT: Parent identifier (e.g., "project\_name:test")
* BRAINTRUST\_API\_URL: Base URL for Braintrust API (defaults to [https://api.braintrust.dev](https://api.braintrust.dev))

## Source Code

For the complete source code and additional examples, visit the [braintrust-sdk repository](https://github.com/braintrustdata/braintrust-sdk/tree/main/integrations/otel-js).
