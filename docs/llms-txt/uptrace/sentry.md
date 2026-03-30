# Source: https://uptrace.dev/raw/ingest/sentry.md

# Sentry SDK Configuration for Uptrace

> Integrate Sentry SDKs with Uptrace by adapting DSNs, configuring browser and server clients, and mapping events to projects.

<alert type="info">

Sentry integration is a new feature that will be improved based on demand and feedback from users. If you are interested in this feature or encounter any issues, please let us know on [GitHub](https://github.com/uptrace/uptrace/).

</alert>

## Overview

Sentry is an open-source error tracking and monitoring platform that helps developers track, prioritize, and fix issues in real-time. It monitors and reports errors and exceptions in web and mobile applications, providing detailed insights into application health and performance.

The Sentry SDK has been actively developed and maintained for over 10 years and has a large, active community of users and contributors. For JavaScript web applications, using the Sentry SDK instead of [OpenTelemetry JS](/get/opentelemetry-js/browser) may provide better results, especially for error tracking and user experience monitoring.

## Understanding DSN Differences

Both Uptrace and Sentry use DSN (Data Source Name) for configuration, but they use slightly different formats:

- **Sentry DSN**: `https://public_key@sentry.example.com/project_id`
- **Uptrace DSN**: `https://public_key@api.uptrace.dev?grpc=4317`

Due to these format differences, Sentry clients will not accept Uptrace DSNs directly. You need to modify the Uptrace DSN to make it compatible with Sentry clients.

### Required DSN Modifications

To make your Uptrace DSN compatible with Sentry:

1. **Add a project ID as a path component** - You can use any numeric value (e.g., `/1`)
2. **Remove the grpc=4317 parameter** - This is optional since Sentry ignores it anyway

**Example transformation:**

- Original Uptrace DSN: `https://public_key@api.uptrace.dev?grpc=4317`
- Modified DSN for Sentry: `https://public_key@api.uptrace.dev/1`

After making these changes, Sentry clients will accept the modified DSN and send data to your Uptrace backend.

## Browser JavaScript SDK

The Sentry Browser SDK supports a wide range of web technologies and frameworks, including React, Angular, Vue.js, and vanilla JavaScript. It provides detailed error reports with stack traces, error messages, and user context, helping developers identify and fix issues quickly.

### Installation

Install the Sentry Browser SDK using your preferred package manager:

```shell
# Using npm
npm install --save @sentry/browser

# Using yarn
yarn add @sentry/browser
```

### Basic Configuration

Initialize the SDK as early as possible in your application lifecycle using your modified Uptrace DSN:

```js
import { init, captureMessage } from '@sentry/browser'

init({
  dsn: 'https://your_public_key@api.uptrace.dev/1',
  // Optional: Enable performance monitoring
  tracesSampleRate: 1.0,
  // Optional: Configure other options
  environment: 'production',
  release: 'your-app@1.0.0'
})

// Test the integration
captureMessage('Hello, world!')
```

### Framework-Specific Packages

Sentry provides specialized packages for popular JavaScript frameworks:

- **React**: [@sentry/react](https://github.com/getsentry/sentry-javascript/tree/master/packages/react)
- **Vue.js**: [@sentry/vue](https://github.com/getsentry/sentry-javascript/tree/master/packages/vue)
- **Angular**: [@sentry/angular](https://github.com/getsentry/sentry-javascript/tree/master/packages/angular)
- **Svelte**: [@sentry/svelte](https://github.com/getsentry/sentry-javascript/tree/master/packages/svelte)

For a complete list of available packages and detailed documentation, see the [sentry-javascript](https://github.com/getsentry/sentry-javascript) repository.

### Advanced Browser Configuration

For production applications, consider these additional configuration options:

```js
import * as Sentry from '@sentry/browser'

Sentry.init({
  dsn: 'https://your_public_key@api.uptrace.dev/1',
  environment: process.env.NODE_ENV,
  release: process.env.npm_package_version,

  // Performance monitoring
  tracesSampleRate: 0.1, // Capture 10% of transactions

  // Session replay (optional)
  integrations: [
    Sentry.replayIntegration({
      sessionSampleRate: 0.1,
      errorSampleRate: 1.0,
    }),
  ],

  // Filter sensitive information
  beforeSend(event) {
    // Remove sensitive data from errors
    if (event.user) {
      delete event.user.email
    }
    return event
  }
})
```

## Go SDK

Sentry provides a robust SDK for the Go programming language, enabling developers to monitor and track errors and exceptions in Go applications with minimal performance overhead.

### Installation

Install the Sentry Go SDK:

```shell
go get github.com/getsentry/sentry-go
```

### Basic Configuration

Use your modified Uptrace DSN to initialize the Sentry SDK:

```go
package main

import (
    "time"
    "github.com/getsentry/sentry-go"
)

func main() {
    err := sentry.Init(sentry.ClientOptions{
        Dsn:              "https://your_public_key@api.uptrace.dev/1",
        EnableTracing:    true,
        TracesSampleRate: 1.0,
        Environment:      "production",
        Release:          "your-app@1.0.0",
    })
    if err != nil {
        panic(err)
    }

    // Ensure all events are sent before program exits
    defer sentry.Flush(3 * time.Second)

    // Your application code here
}
```

### Error Capture Example

```go
// Capture an error with context
sentry.WithScope(func(scope *sentry.Scope) {
    scope.SetTag("component", "payment")
    scope.SetUser(sentry.User{ID: "12345"})
    scope.SetContext("payment", map[string]interface{}{
        "amount": 100.00,
        "currency": "USD",
    })
    sentry.CaptureException(err)
})
```

### Performance Monitoring

```go
// Create a transaction for performance monitoring
span := sentry.StartSpan(ctx, "payment.process")
defer span.Finish()

// Add data to the span
span.SetTag("payment.method", "credit_card")
span.SetData("amount", 100.00)
```

For comprehensive documentation and advanced usage patterns, see the [sentry-go](https://github.com/getsentry/sentry-go) documentation.

## Configuration Best Practices

1. **Initialize Early**: Always initialize Sentry as early as possible in your application lifecycle to capture all errors.
2. **Environment Configuration**: Use environment variables or configuration files to manage DSNs across different environments (development, staging, production).
3. **Sample Rates**: In production, consider using lower sample rates for performance monitoring to reduce data volume and costs.
4. **Error Filtering**: Implement `beforeSend` hooks to filter out sensitive information or noise from error reports.
5. **Release Tracking**: Always set a release version to track which version of your application generated errors.
6. **User Context**: Set user context to help with debugging and to understand which users are affected by issues.

## Troubleshooting

### Common Issues

- **No events in Uptrace**: Verify that your modified DSN is correct and that the Uptrace backend is configured to accept Sentry protocol data.
- **CORS errors**: Ensure your web application's domain is allowed to send data to your Uptrace instance.
- **Missing source maps**: For JavaScript applications, ensure source maps are properly configured for better stack traces.

### Verification

To verify that your integration is working:

1. Send a test message: `sentry.captureMessage('Test message')`
2. Trigger a test error: `throw new Error('Test error')`
3. Check your Uptrace dashboard for the events

## Related Documentation

- [Sentry vs Datadog Comparison](/comparisons/sentry-vs-datadog)
- [Uptrace Getting Started Guide](/get)
- [OpenTelemetry Integration](/ingest/opentelemetry)
