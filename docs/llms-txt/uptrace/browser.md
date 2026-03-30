# Source: https://uptrace.dev/raw/get/opentelemetry-js/browser.md

# OpenTelemetry Browser SDK for Uptrace

> Learn how to configure OpenTelemetry JavaScript SDK for web browsers to export spans and metrics to Uptrace using OTLP/HTTP.

![undefined](/devicon/javascript-original.svg)This guide explains how to configure the OpenTelemetry JavaScript SDK for web browsers to export spans and metrics to Uptrace using OTLP/HTTP. You'll learn how to instrument your web applications for effective client-side monitoring and observability.

If you need to monitor JavaScript web applications, using [Sentry SDK](/ingest/sentry) instead of OpenTelemetry JS might provide better results for error tracking and user experience monitoring.

To learn about the OpenTelemetry API, see [OpenTelemetry JS Tracing API](/get/opentelemetry-js/tracing) and [OpenTelemetry JS Metrics API](/get/opentelemetry-js/metrics).

## Prerequisites

Before you begin, ensure you have:

- A web application running in modern browsers (supporting ES2022)
- An Uptrace account with a valid DSN (Data Source Name)
- A build system that supports ES6 modules (Webpack, Vite, Rollup, etc.)

## Uptrace Web SDK

[uptrace-js](https://github.com/uptrace/uptrace-js) is a lightweight wrapper around [opentelemetry-js](https://github.com/open-telemetry/opentelemetry-js) that pre-configures the OpenTelemetry SDK to export data to Uptrace. It doesn't add new functionality but simplifies the setup process for your convenience.

### Installation

To install `@uptrace/web`:

```shell
# npm
npm install @uptrace/web --save-dev

# yarn
yarn add @uptrace/web --dev
```

### Configuration

Configure the Uptrace client using a [DSN](/get#dsn) (Data Source Name) from your project settings page. Replace `<FIXME>` with your actual Uptrace DSN.

<alert type="warning">

You must call `configureOpentelemetry` as early as possible and before importing other packages, because the OpenTelemetry SDK must patch libraries before you import them.

</alert>

```js
import { getWebAutoInstrumentations } from '@opentelemetry/auto-instrumentations-web'
import { configureOpentelemetry } from '@uptrace/web'

// configureOpentelemetry automatically sets up window.onerror handler.
const sdk = configureOpentelemetry({
  // Set dsn or UPTRACE_DSN env var.
  dsn: '<FIXME>',

  serviceName: 'myservice',
  serviceVersion: '1.0.0',

  instrumentations: [getWebAutoInstrumentations({})],
})
sdk.start()
```

<partial path="js-config">



</partial>

## Context Manager

`ZoneContextManager` is a context manager implementation based on the Zone.js library. It enables context propagation within the application using zones, which is particularly useful for tracking asynchronous operations in browsers.

### Installation

To install the Zone.js context manager:

```shell
npm install --save @opentelemetry/context-zone
```

### Usage

To use the Zone.js context manager:

```js
import { ZoneContextManager } from '@opentelemetry/context-zone'

configureOpentelemetry({
  contextManager: new ZoneContextManager(),
})
```

**Benefits of Zone.js context manager:**

- Automatic context propagation across async operations
- Better trace correlation for setTimeout, Promise chains, and event handlers
- Improved debugging capabilities for complex web applications

## Instrumentations

OpenTelemetry provides several instrumentations specifically designed for browser environments to automatically capture telemetry data from common web APIs and user interactions.

### Available Instrumentations

- **Fetch API**: Automatically instruments `fetch()` requests
- **XMLHttpRequest**: Instruments traditional AJAX requests
- **Document Load**: Monitors page load performance

For additional instrumentations, see the OpenTelemetry JS [web plugins](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/web) documentation.

### Basic Setup

You can use `configureOpentelemetry` to register individual instrumentations:

```js
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch'
import { XMLHttpRequestInstrumentation } from '@opentelemetry/instrumentation-xml-http-request'

const sdk = configureOpentelemetry({
  instrumentations: [
    new FetchInstrumentation(),
    new XMLHttpRequestInstrumentation(),
  ],
})
sdk.start()
```

To automatically register all available web instrumentations:

```js
import { getWebAutoInstrumentations } from '@opentelemetry/auto-instrumentations-web'

const sdk = configureOpentelemetry({
  instrumentations: [getWebAutoInstrumentations({})],
})
sdk.start()
```

### Alternative Method

You can also use `registerInstrumentations` directly:

```js
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch'
import { registerInstrumentations } from '@opentelemetry/instrumentation'

registerInstrumentations({
  instrumentations: [new FetchInstrumentation()],
})
```

See the OpenTelemetry JS [web plugins](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/web) for the full list of available instrumentations.

### Advanced Configuration

Configure instrumentations with custom options:

```js
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch'

configureOpentelemetry({
  instrumentations: [
    new FetchInstrumentation({
      // Ignore requests to specific URLs
      ignoreUrls: [/\/analytics/, /\/tracking/],
      // Add custom attributes
      requestHook: (span, request) => {
        span.setAttribute('custom.request.type', 'api')
      },
    }),
  ],
})
```

## Framework Integrations

### Instrumenting Vue.js 2.x

Integrate OpenTelemetry with Vue.js applications for comprehensive error tracking:

```js
import Vue from 'vue'
import { configureOpentelemetry } from '@uptrace/web'

const sdk = configureOpentelemetry({
  dsn: '<FIXME>',
})
sdk.start()

Vue.config.errorHandler = (err, vm, info) => {
  sdk.reportException(err, {
    vm: vm,
    info: info,
  })
}
```

### Instrumenting React

For React applications, you can set up error tracking with OpenTelemetry:

```js
import React from 'react'
import { configureOpentelemetry } from '@uptrace/web'
import { trace } from '@opentelemetry/api'

const sdk = configureOpentelemetry({
  dsn: '<FIXME>',
})
sdk.start()

const tracer = trace.getTracer('react-app', '1.0.0')

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true }
  }

  componentDidCatch(error, errorInfo) {
    const span = tracer.startSpan('react.error')
    span.recordException(error)
    span.setAttributes({
      'error.component': errorInfo.componentStack,
    })
    span.end()
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>
    }
    return this.props.children
  }
}
```

## Manual Instrumentation

Create custom spans for specific user interactions or business logic:

```js
import { trace } from '@opentelemetry/api'

const tracer = trace.getTracer('web-app', '1.0.0')

function trackUserAction(actionName) {
  const span = tracer.startSpan(`user.${actionName}`)

  span.setAttributes({
    'user.action': actionName,
    'page.url': window.location.href,
    'user.agent': navigator.userAgent,
  })

  // Your business logic here

  span.end()
}

// Usage
document.getElementById('submit-button').addEventListener('click', () => {
  trackUserAction('form_submit')
})
```

## Performance Monitoring

Monitor key performance metrics in your web application:

```js
import { trace, metrics } from '@opentelemetry/api'

const tracer = trace.getTracer('web-performance', '1.0.0')
const meter = metrics.getMeter('web-performance', '1.0.0')

// Create metrics
const pageLoadTime = meter.createHistogram('page.load_time', {
  description: 'Page load time in milliseconds',
})

// Measure page load time
window.addEventListener('load', () => {
  const loadTime =
    performance.timing.loadEventEnd - performance.timing.navigationStart
  pageLoadTime.record(loadTime, {
    'page.url': window.location.pathname,
  })
})
```

## Querying Data

Once your browser application is instrumented and sending data to Uptrace, you can analyze user behavior and performance:

### Browser-Specific Span Analysis

- **Network requests**: Monitor API calls, resource loading, and external service dependencies
- **User interactions**: Track clicks, form submissions, and navigation patterns
- **Performance bottlenecks**: Identify slow-loading resources and long-running JavaScript tasks
- **Error tracking**: Analyze client-side errors and their impact on user experience

### Client-Side Metrics

- **Page load metrics**: Monitor loading performance and user experience
- **User engagement**: Track session duration, page views, and interaction patterns
- **Resource performance**: Analyze loading times for various assets
- **Error rates**: Monitor client-side error frequency and patterns

### Cross-Platform Correlation

- **Full-stack tracing**: Correlate browser spans with backend API calls
- **User journey tracking**: Follow user interactions across multiple pages and services
- **Error propagation**: Track how client-side errors relate to server-side issues

## Verifying Your Setup

After configuration, your browser application will start sending telemetry data to Uptrace. To verify the setup:

1. **Load your application** in a browser with developer tools open
2. **Interact with your application** by clicking buttons, making requests, or navigating between pages
3. **Check the Network tab** for requests to `https://api.uptrace.dev/v1/traces`
4. **View traces in Uptrace** within 1-2 minutes of generating activity

## Troubleshooting

If OpenTelemetry is not working as expected, you can enable verbose logging to check for potential issues:

```js
import { diag, DiagConsoleLogger, DiagLogLevel } from '@opentelemetry/api'

diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.DEBUG)
```

### Browser-Specific Issues

**CORS errors:**

- Ensure your Uptrace project allows requests from your domain
- Check that the browser is not blocking requests due to CORS policy
- Verify that your DSN is correctly configured

**Bundle size concerns:**

- Use tree-shaking to include only necessary OpenTelemetry packages
- Consider lazy-loading instrumentation for non-critical paths
- Monitor the impact on your application's bundle size

**Performance impact:**

- Configure appropriate sampling rates to reduce overhead
- Use batch processors to minimize network requests
- Test performance impact in production-like environments

**Ad blockers:**

- Some ad blockers may interfere with telemetry data collection
- Consider using a custom subdomain for telemetry endpoints
- Provide fallback mechanisms for when telemetry is blocked

## What's Next?

Next, instrument more operations to get a more detailed picture. Try to prioritize network calls, disk operations, database queries, errors, and logs.

- [Learn about OpenTelemetry JavaScript Tracing API](/get/opentelemetry-js/tracing)
- [Learn about OpenTelemetry JavaScript Metrics API](/get/opentelemetry-js/metrics)
- [Learn about OpenTelemetry JavaScript Resource detectors](/get/opentelemetry-js/resources)
- [Learn about OpenTelemetry JavaScript Context Propagation](/get/opentelemetry-js/propagation)
