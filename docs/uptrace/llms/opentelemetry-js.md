# Source: https://uptrace.dev/raw/get/opentelemetry-js.md

# OpenTelemetry JavaScript distro for Uptrace

> Step-by-step guide to install and configure OpenTelemetry JavaScript SDKs, export telemetry to Uptrace, and verify that traces, metrics, and logs arrive via OTLP.

![undefined](/devicon/nodejs-original.svg)This document explains how to configure the OpenTelemetry JavaScript SDK to export spans (traces), logs, and metrics to Uptrace using OTLP/HTTP.

## Choose Your Setup Path

### Option A: Node.js Applications

Best for: Server-side JavaScript, backend services, APIs

[uptrace-js](https://github.com/uptrace/uptrace-js) is a thin wrapper over [opentelemetry-js](https://github.com/open-telemetry/opentelemetry-js) that configures the OpenTelemetry SDK to export data to Uptrace. It does not add any new functionality and is provided only for your convenience.

> [Quick Start below](#quick-start) | [Detailed Node.js Guide](/get/opentelemetry-js/node)

### Option B: Browser Applications

Best for: Client-side web apps, SPAs, frontend monitoring

> [Browser SDK Setup](/get/opentelemetry-js/browser)

## Quick Start Guide

Follow these steps to get your first trace running in 5 minutes:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Install @uptrace/node

<code-group>

```shell [npm]
npm install @uptrace/node --save
```

```shell [yarn]
yarn add @uptrace/node --save
```

</code-group>

### Step 3: Basic Configuration

Configure the Uptrace client using a [DSN](/get#dsn) (Data Source Name) from the project settings page. Replace `<FIXME>` with your actual Uptrace DSN, and `myservice` with a name that identifies your application.

<alert type="warning">

You must call `configureOpentelemetry` as early as possible and before importing other packages, because the OpenTelemetry SDK must patch libraries before you import them.

</alert>

```js
// The very first import must be Uptrace and/or OpenTelemetry.
const uptrace = require('@uptrace/node')
const otel = require('@opentelemetry/api')

// Start OpenTelemetry SDK and invoke instrumentations to patch the code.
const sdk = uptrace.configureOpentelemetry({
  // Copy your project DSN here or use UPTRACE_DSN env var
  //dsn: '<FIXME>',
  serviceName: 'myservice',
  serviceVersion: '1.0.0',
  deploymentEnvironment: 'production',
})
sdk.start()
```

### Step 4: Create Your First Trace

Copy the [code](https://github.com/uptrace/uptrace-js/tree/master/example/basic-node) to `main.js`:

```js
'use strict'

// The very first import must be Uptrace/OpenTelemetry.
const otel = require('@opentelemetry/api')
const uptrace = require('@uptrace/node')

// Start OpenTelemetry SDK and invoke instrumentations to patch the code.
const sdk = uptrace.configureOpentelemetry({
  // Set dsn or UPTRACE_DSN env var.
  //dsn: '<FIXME>',
  serviceName: 'myservice',
  serviceVersion: '1.0.0',
})
sdk.start()

// Create a tracer. Usually, tracer is a global variable.
const tracer = otel.trace.getTracer('app_or_package_name', '1.0.0')

// Create a root span (a trace) to measure some operation.
tracer.startActiveSpan('main-operation', (main) => {
  tracer.startActiveSpan('GET /posts/:id', (child1) => {
    child1.setAttribute('http.method', 'GET')
    child1.setAttribute('http.route', '/posts/:id')
    child1.setAttribute('http.url', 'http://localhost:8080/posts/123')
    child1.setAttribute('http.status_code', 200)
    child1.recordException(new Error('error1'))
    child1.end()
  })

  tracer.startActiveSpan('SELECT', (child2) => {
    child2.setAttribute('db.system', 'mysql')
    child2.setAttribute('db.statement', 'SELECT * FROM posts LIMIT 100')
    child2.end()
  })

  // End the span when the operation we are measuring is done.
  main.end()

  console.log(sdk.traceUrl(main))
})

setTimeout(async () => {
  // Send buffered spans and free resources.
  await sdk.shutdown()
})
```

### Step 5: Run Your Application

Execute the example, replacing `<FIXME>` with your Uptrace DSN:

```shell
$ UPTRACE_DSN="<FIXME>" node main.js
https://app.uptrace.dev/traces/<trace_id>
```

### Step 6: View Your Trace

Click the generated link to view your trace in the Uptrace dashboard:

![Basic trace](/get/basic-trace.png)

## Configuration Options

You can find the full list of available options at the [@uptrace/node](https://github.com/uptrace/uptrace-js) repository.

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
        dsn
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
        serviceName
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
        serviceVersion
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
        deploymentEnvironment
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
        resourceAttributes
      </code>
    </td>
    
    <td>
      Any other resource attributes.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        resource
      </code>
    </td>
    
    <td>
      Resource attributes representing an entity that produces telemetry.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        instrumentations
      </code>
    </td>
    
    <td>
      Custom <a href="#instrumentations">
        instrumentations
      </a>
      
       to register.
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
      <a href="/get/opentelemetry-js/zero-code">
        Zero-code instrumentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Learn more about Node.js setup
    </td>
    
    <td>
      <a href="/get/opentelemetry-js/node">
        Node.js SDK
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument browser applications
    </td>
    
    <td>
      <a href="/get/opentelemetry-js/browser">
        Browser SDK
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Use OTLP exporter directly
    </td>
    
    <td>
      <a href="/get/opentelemetry-js/otlp">
        Direct OTLP Configuration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-js/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-js/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-js/logs">
        Logs integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-js/propagation">
        Context propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-js/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-detect cloud environment
    </td>
    
    <td>
      <a href="/get/opentelemetry-js/resources">
        Resource detectors
      </a>
    </td>
  </tr>
</tbody>
</table>

### Framework Guides

- [OpenTelemetry Express.js](/guides/opentelemetry-express)
- [OpenTelemetry Next.js](/guides/opentelemetry-nextjs)
