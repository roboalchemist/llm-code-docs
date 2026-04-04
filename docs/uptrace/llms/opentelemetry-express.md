# Source: https://uptrace.dev/raw/guides/opentelemetry-express.md

# OpenTelemetry Express.js instrumentation

> Use OpenTelemetry instrumentation to monitor and optimize Express.js performance.

By combining OpenTelemetry with Express.js, you can collect and export telemetry data, including traces, metrics, and logs, to gain insight into the behavior and performance of your application.

## Quick Setup

<table>
<thead>
  <tr>
    <th>
      Step
    </th>
    
    <th>
      Action
    </th>
    
    <th>
      Code/Command
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      1. Install
    </td>
    
    <td>
      Install OpenTelemetry packages
    </td>
    
    <td>
      <code>
        npm install @opentelemetry/sdk-node @opentelemetry/auto-instrumentations-node
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      2. Configure
    </td>
    
    <td>
      Create <code>
        otel.js
      </code>
      
       with SDK configuration
    </td>
    
    <td>
      See <a href="#usage">
        Usage
      </a>
      
       section below
    </td>
  </tr>
  
  <tr>
    <td>
      3. Run
    </td>
    
    <td>
      Start your app with the <code>
        --require
      </code>
      
       flag
    </td>
    
    <td>
      <code>
        node --require ./otel.js app.js
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      4. Verify
    </td>
    
    <td>
      Check your observability backend for traces
    </td>
    
    <td>
      Traces collected automatically
    </td>
  </tr>
</tbody>
</table>

**Minimal working example:**

```js
const { NodeSDK } = require('@opentelemetry/sdk-node')
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node')

const sdk = new NodeSDK({
  serviceName: 'my-express-app',
  instrumentations: [getNodeAutoInstrumentations()],
})
sdk.start()
```

This configuration automatically instruments Express.js, HTTP requests, and common Node.js libraries without additional code changes.

## What is Express.js?

Express.js is a fast and minimalist web application framework for Node.js, a JavaScript runtime. It simplifies the development of web applications and APIs by providing a robust set of features and utilities, while maintaining a lightweight and unobtrusive approach.

Express.js is widely recognized for its simplicity, flexibility, and extensibility, making it a popular choice for building server-side applications in Node.js.

## What is OpenTelemetry?

OpenTelemetry is an open-source observability framework that aims to standardize and simplify the collection, processing, and export of telemetry data from applications and systems.

OpenTelemetry supports multiple programming languages and platforms, making it suitable for a wide range of applications and environments.

OpenTelemetry enables developers to instrument their code and collect telemetry data, which can then be exported to various [OpenTelemetry backends](/blog/opentelemetry-backend) or observability platforms for analysis and visualization. The [OpenTelemetry architecture](/opentelemetry/architecture) follows a modular design with SDKs, APIs, and exporters as its core components.

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [Node.js zero-code instrumentation guide](/get/opentelemetry-js/zero-code).

</alert>

## Express.js instrumentation

Using the OpenTelemetry Node.js library, you can easily add distributed tracing capabilities to your Express.js applications.

To instrument an Express.js app, you need to install OpenTelemetry Node.js SDK and available instrumentations:

```shell
# Using npm
npm install @opentelemetry/sdk-node @opentelemetry/api @opentelemetry/auto-instrumentations-node

# Using yarn
yarn add @opentelemetry/sdk-node @opentelemetry/api @opentelemetry/auto-instrumentations-node
```

You can let OpenTelemetry instrument your application automatically or do it explicitly by installing required instrumentations:

```shell
# Using npm
npm install @opentelemetry/instrumentation-http @opentelemetry/instrumentation-express

# Using yarn
yarn add @opentelemetry/instrumentation-http @opentelemetry/instrumentation-express
```

## Usage

After installing OpenTelemetry, you need to configure OpenTelemetry SDK to export data to an OpenTelemetry backend for storage and visualization.

```js
'use strict'

const otel = require('@opentelemetry/api')
const { BatchSpanProcessor } = require('@opentelemetry/sdk-trace-base')
const { Resource } = require('@opentelemetry/resources')
const { NodeSDK } = require('@opentelemetry/sdk-node')
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http')
const { AWSXRayIdGenerator } = require('@opentelemetry/id-generator-aws-xray')
const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http')
const {
  ExpressInstrumentation,
} = require('@opentelemetry/instrumentation-express')

const dsn = process.env.UPTRACE_DSN
console.log('using dsn:', dsn)

const exporter = new OTLPTraceExporter({
  url: 'http://localhost:14318/v1/traces',
  headers: { 'uptrace-dsn': dsn },
  compression: 'gzip',
})
const bsp = new BatchSpanProcessor(exporter, {
  maxExportBatchSize: 1000,
  maxQueueSize: 1000,
})

const sdk = new NodeSDK({
  spanProcessor: bsp,
  resource: new Resource({
    'service.name': 'myservice',
    'service.version': '1.0.0',
  }),
  idGenerator: new AWSXRayIdGenerator(),
  instrumentations: [new HttpInstrumentation(), new ExpressInstrumentation()],
})
sdk.start()
```

To avoid potential issues, it is **strongly recommended** to put the OpenTelemetry initialization code into a separate file called `otel.js` and use the `--require` flag to load the tracing code before the application code:

```shell
# JavaScript
node --require ./otel.js app.js

# TypeScript
ts-node --require ./otel.ts app.ts
```

See [OpenTelemetry Express.js example](https://github.com/uptrace/uptrace-js/tree/master/example/express) for details.

## Instrumentation Options

The Express instrumentation supports several configuration options for customizing behavior:

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
        ignoreLayers
      </code>
    </td>
    
    <td>
      Array of Express layer names to ignore (e.g., router, middleware)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ignoreLayersType
      </code>
    </td>
    
    <td>
      Array of layer types to ignore: <code>
        middleware
      </code>
      
      , <code>
        router
      </code>
      
      , <code>
        request_handler
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        requestHook
      </code>
    </td>
    
    <td>
      Hook for adding custom attributes to request spans
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        spanNameHook
      </code>
    </td>
    
    <td>
      Customize how span names are generated
    </td>
  </tr>
</tbody>
</table>

### Filtering health checks

Use the `ignoreIncomingRequestHook` option from the HTTP instrumentation to exclude certain endpoints from tracing:

```js
const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http')
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express')

const httpInstrumentation = new HttpInstrumentation({
  ignoreIncomingRequestHook: (request) => {
    // Return true to ignore this request
    const ignorePatterns = ['/health', '/ready', '/metrics', '/favicon.ico']
    return ignorePatterns.some(pattern => request.url?.includes(pattern))
  },
})

const expressInstrumentation = new ExpressInstrumentation({
  // Ignore specific middleware layers
  ignoreLayers: ['query', 'expressInit'],
  ignoreLayersType: ['middleware'],
})

const sdk = new NodeSDK({
  instrumentations: [httpInstrumentation, expressInstrumentation],
})
```

### Adding custom attributes

Use the `requestHook` option to add custom attributes to request spans:

```js
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express')

const expressInstrumentation = new ExpressInstrumentation({
  requestHook: (span, info) => {
    span.setAttribute('http.request.id', info.request.headers['x-request-id'])
    span.setAttribute('express.route.params', JSON.stringify(info.request.params))
  },
})
```

### Custom span names

Customize how span names are generated for Express routes:

```js
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express')

const expressInstrumentation = new ExpressInstrumentation({
  spanNameHook: (info, defaultName) => {
    // Use custom naming convention
    return `${info.request.method} ${info.layerPath || info.route}`
  },
})
```

## HTTP Metrics

OpenTelemetry automatically collects HTTP server metrics when you enable metrics instrumentation:

<table>
<thead>
  <tr>
    <th>
      Metric
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
        http.server.request.duration
      </code>
    </td>
    
    <td>
      Duration of HTTP server requests
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.server.request.body.size
      </code>
    </td>
    
    <td>
      Size of HTTP server request bodies
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.server.response.body.size
      </code>
    </td>
    
    <td>
      Size of HTTP server response bodies
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.server.active_requests
      </code>
    </td>
    
    <td>
      Number of concurrent active requests
    </td>
  </tr>
</tbody>
</table>

To enable metrics collection:

```js
const { NodeSDK } = require('@opentelemetry/sdk-node')
const { PeriodicExportingMetricReader } = require('@opentelemetry/sdk-metrics')
const { OTLPMetricExporter } = require('@opentelemetry/exporter-metrics-otlp-http')
const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http')
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express')

const sdk = new NodeSDK({
  serviceName: 'my-express-app',
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: 'http://localhost:4318/v1/metrics',
    }),
    exportIntervalMillis: 10000,
  }),
  instrumentations: [new HttpInstrumentation(), new ExpressInstrumentation()],
})
```

## Creating Custom Spans

In addition to automatic instrumentation, you can create custom spans to trace specific operations:

```js
const { trace, SpanStatusCode } = require('@opentelemetry/api')

const tracer = trace.getTracer('my-express-app')

app.get('/users/:id', async (req, res) => {
  // Create a custom span for database operation
  const span = tracer.startSpan('fetch-user-from-database')
  try {
    span.setAttribute('user.id', req.params.id)
    const user = await db.findUser(req.params.id)
    span.setAttribute('user.found', !!user)
    res.json(user)
  } catch (error) {
    span.recordException(error)
    span.setStatus({ code: SpanStatusCode.ERROR, message: error.message })
    res.status(500).json({ error: 'Internal server error' })
  } finally {
    span.end()
  }
})
```

## Error Handling

OpenTelemetry Express instrumentation automatically captures errors. You can also manually record exceptions:

```js
const { trace, SpanStatusCode } = require('@opentelemetry/api')

app.use((err, req, res, next) => {
  const span = trace.getActiveSpan()
  if (span) {
    span.recordException(err)
    span.setStatus({ code: SpanStatusCode.ERROR, message: err.message })
  }
  res.status(500).json({ error: 'Something went wrong' })
})
```

## What is Uptrace?

Uptrace is a [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues. For Node.js instrumentation, see the [OpenTelemetry JavaScript guide](/get/opentelemetry-js).

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## FAQ

**What is @opentelemetry/instrumentation-express?** The @opentelemetry/instrumentation-express package is the official OpenTelemetry library for automatically instrumenting Express.js applications. It creates spans for incoming HTTP requests, middleware execution, and route handlers without requiring manual instrumentation code.

**How do I filter health check endpoints from traces?** Use the `ignoreIncomingRequestHook` option from `@opentelemetry/instrumentation-http` to filter requests by URL path. Return `true` for paths like `/health` or `/ready` to exclude them from tracing.

**Does Express instrumentation work with async/await?** Yes, OpenTelemetry Express instrumentation fully supports async route handlers and middleware. Context propagation works correctly across async boundaries.

**How do I trace requests across microservices?** OpenTelemetry automatically propagates trace context through HTTP headers. When one Express service calls another, the trace context is included in the request headers, allowing you to see the full distributed trace across services.

**What's the performance impact of OpenTelemetry?** OpenTelemetry is designed for production use with minimal overhead. Using batch processors and appropriate sampling rates keeps the performance impact under 5% in most applications.

**Can I use OpenTelemetry with Express middleware like Morgan?** Yes, OpenTelemetry works alongside existing middleware. The instrumentation hooks into Express at a lower level and doesn't interfere with logging middleware like Morgan or compression middleware.

## What's next?

By integrating OpenTelemetry with Express.js, you can gain insight into your application's [distributed traces](/opentelemetry/distributed-tracing), [OpenTelemetry metrics](/opentelemetry/metrics), and [logs](/opentelemetry/logs). This helps you understand the behavior of your Express.js application across multiple services or microservices, and facilitates troubleshooting and performance optimization.

Next steps to enhance your observability:

- Add database instrumentation for [Redis](/guides/opentelemetry-redis) or [PostgreSQL](/guides/opentelemetry-postgresql)
- Learn about custom spans using the [OpenTelemetry JavaScript Tracing API](/get/opentelemetry-js/tracing)
- For full-stack React applications, see [OpenTelemetry Next.js](/guides/opentelemetry-nextjs) instrumentation
- Set up the [OpenTelemetry Collector](/opentelemetry/collector) for production deployments
