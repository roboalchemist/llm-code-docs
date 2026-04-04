---
---
title: OpenTelemetry Protocol (OTLP)
description: "Learn how to send OpenTelemetry trace data directly to Sentry from OpenTelemetry SDKs."
---

Sentry can ingest [OpenTelemetry](https://opentelemetry.io) traces and logs directly via the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otel/protocol/). Sentry does not support ingesting OTLP metrics.

## OpenTelemetry Traces

If you have an existing OpenTelemetry trace instrumentation, you can configure your OpenTelemetry exporter to send traces to Sentry directly. Sentry's OTLP ingestion traces endpoint is currently in development, and has a few known limitations:

- Span events are not supported. All span events are dropped during ingestion.
- Span links are partially supported. We ingest and display span links, but they cannot be searched, filtered, or aggregated. Links are shown in the [Trace View](/concepts/key-terms/tracing/trace-view/).
- Array attributes are partially supported. We ingest and display array attributes, but they cannot be searched, filtered, or aggregated. Array attributes are shown in the [Trace View](/concepts/key-terms/tracing/trace-view/).

You can find the values of Sentry's OTLP traces endpoint and public key in your Sentry project settings.

1. Go to the [Settings > Projects](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/) page in Sentry.
2. Select a project from the list.
3. Go to the "Client Keys (DSN)" sub-page for this project under the "SDK Setup" heading.

The easiest way to configure an OpenTelemetry exporter is with environment variables. You'll need to configure the trace endpoint URL, as well as the authentication headers. Set these variables on the server where your application is running.

```bash {filename: .env}
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="___OTLP_TRACES_URL___"
export OTEL_EXPORTER_OTLP_TRACES_HEADERS="x-sentry-auth=sentry sentry_key=___PUBLIC_KEY___"
```

If you prefer to explicitly configure an OpenTelemetry SDK or OTEL collector instance, see the following:

### Using the OTEL Collector

You can configure your OTEL collector instance to send traces to Sentry directly. This requires you to add an `otlphttp` exporter to your collector instance. Sentry's OTLP endpoints are project-specific, so you might also need to add a [routing connector](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/connector/routingconnector) to route traces to the correct project.

```yaml {filename: otel-collector.yaml}
exporters:
  otlphttp:
    traces_endpoint: ___OTLP_TRACES_URL___
    headers:
      x-sentry-auth: "sentry sentry_key=___PUBLIC_KEY___"
    compression: gzip
    encoding: proto
    timeout: 30s
```

### Using an OpenTelemetry SDK

You can configure the OpenTelemetry Exporter directly in your application code. Here is an example with the OpenTelemetry Node SDK:

```typescript {filename: app.ts}
const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({
    url: "___OTLP_TRACES_URL___",
    headers: {
      "x-sentry-auth": "sentry sentry_key=___PUBLIC_KEY___",
    },
  }),
});

sdk.start();
```

## OpenTelemetry Logs

If you have an existing OpenTelemetry log instrumentation, you can configure your OpenTelemetry exporter to send logs to Sentry directly. Sentry's OTLP ingestion logs endpoint has the following known limitations:

- Array attributes are partially supported. We ingest and display array attributes, but they cannot be searched, filtered, or aggregated.

You can find the values of Sentry's OTLP logs endpoint and public key in your Sentry project settings.

1. Go to the [Settings > Projects](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/) page in Sentry.
2. Select a project from the list.
3. Go to the "Client Keys (DSN)" sub-page for this project under the "SDK Setup" heading.

The easiest way to configure an OpenTelemetry exporter is with environment variables. You'll need to configure the logs endpoint URL, as well as the authentication headers. Set these variables on the server where your application is running.

```bash {filename: .env}
export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT="___OTLP_LOGS_URL___"
export OTEL_EXPORTER_OTLP_LOGS_HEADERS="x-sentry-auth=sentry sentry_key=___PUBLIC_KEY___"
```

If you prefer to explicitly configure an OpenTelemetry SDK or OTEL collector instance, see the following:

### Using the OTEL Collector

You can configure your OTEL collector instance to send logs to Sentry directly. This requires you to add an `otlphttp` exporter to your collector instance. Sentry's OTLP endpoints are project-specific, so you might also need to add a [routing connector](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/connector/routingconnector) to route logs to the correct project.

```yaml {filename: otel-collector.yaml}
exporters:
  otlphttp:
    logs_endpoint: ___OTLP_LOGS_URL___
    headers:
      x-sentry-auth: "sentry sentry_key=___PUBLIC_KEY___"
    compression: gzip
    encoding: proto
    timeout: 30s
```

### Using an OpenTelemetry SDK

Alternatively, you can configure the OpenTelemetry Exporter directly in your application code. Here is an example with the OpenTelemetry Node SDK:

```typescript {filename: app.ts}
import {
  LoggerProvider,
  BatchLogRecordProcessor,
} from "@opentelemetry/sdk-logs";
const logExporter = new OTLPLogExporter({
  url: "___OTLP_LOGS_URL___",
  headers: {
    "x-sentry-auth": "sentry sentry_key=___PUBLIC_KEY___",
  },
});
const loggerProvider = new LoggerProvider({
  processors: [new BatchLogRecordProcessor(logExporter)],
});

const logger = loggerProvider.getLogger("default", "1.0.0");
```

## Distributed Tracing between Sentry Instrumentation and OpenTelemetry Instrumentation

If you have a frontend or services instrumented with the Sentry SDK, and you are also instrumenting with OpenTelemetry, you can use the `propagateTraceparent` exposed in the Sentry SDK to propagate the W3C Trace Context `traceparent` header to the OpenTelemetry instrumentation. This will allow you to continue traces from Sentry instrumented services.

The following SDKs support the `propagateTraceparent` option:

### JavaScript

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

### Mobile

- 
- 
- 
- 

## Dedicated Integrations

The following SDKs have dedicated integrations that make OTLP setup easy:

- 

## OpenTelemetry Collector Guides

View the [OpenTelemetry Collector Guides](/product/drains/integration/opentelemetry-collector/#open-telemetry-collector-guides) to learn how to leverage the OpenTelemetry Collector to send traces and logs to Sentry from different sources like Kafka or Nginx.
