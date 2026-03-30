# Source: https://uptrace.dev/raw/guides/opentelemetry-httpcheck.md

# OpenTelemetry HTTPcheck Receiver

> Learn how to monitor HTTP endpoints with the OpenTelemetry Collector HTTPcheck receiver for uptime checks, response validation, and TLS certificate monitoring.

Learn how to use the OpenTelemetry Collector HTTPcheck receiver to perform synthetic checks against HTTP endpoints, monitor uptime, validate responses, and track TLS certificate expiration.

## What is OpenTelemetry Collector?

[OpenTelemetry Collector](/opentelemetry/collector) is an agent that pulls telemetry data from systems you want to monitor and exports the collected data to an [OpenTelemetry backend](/blog/opentelemetry-backend).

The Collector provides powerful data processing capabilities, allowing you to perform aggregation, filtering, sampling, and enrichment of telemetry data before sending it to backend systems.

## What is the HTTPcheck receiver?

The HTTPcheck [receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/httpcheckreceiver) is a component of the OpenTelemetry Collector that performs synthetic checks against HTTP endpoints. It makes periodic requests to specified URLs and records metrics about availability, response time, and response content.

Use cases include:

- **Uptime monitoring** - Check if services are reachable and responding
- **Response validation** - Verify response content matches expectations
- **TLS certificate monitoring** - Track certificate expiration dates
- **Performance tracking** - Measure DNS, connection, and response times

## Basic configuration

Here's a minimal configuration to monitor an HTTP endpoint:

```yaml
receivers:
  httpcheck:
    targets:
      - endpoint: 'https://api.uptrace.dev/health/status'
        method: GET
    collection_interval: 60s

processors:
  batch:

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers: { 'uptrace-dsn': '<FIXME>' }

service:
  pipelines:
    metrics:
      receivers: [httpcheck]
      processors: [batch]
      exporters: [otlp]
```

## Monitoring multiple endpoints

Check several endpoints with different methods and configurations:

```yaml
receivers:
  httpcheck:
    targets:
      - endpoint: 'https://api.example.com/health'
        method: GET
      - endpoint: 'https://api.example.com/v2/status'
        method: GET
      - endpoint: 'https://staging.example.com/health'
        method: GET
    collection_interval: 30s
```

## Target configuration options

Each target supports the following options:

<table>
<thead>
  <tr>
    <th>
      Option
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Default
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
        endpoint
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      required
    </td>
    
    <td>
      The URL to check
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        method
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      <code>
        GET
      </code>
    </td>
    
    <td>
      HTTP method to use
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        headers
      </code>
    </td>
    
    <td>
      map
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Additional HTTP headers
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        body
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Request body content
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        auto_content_type
      </code>
    </td>
    
    <td>
      bool
    </td>
    
    <td>
      false
    </td>
    
    <td>
      Auto-set Content-Type based on body
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        timeout
      </code>
    </td>
    
    <td>
      duration
    </td>
    
    <td>
      <code>
        10s
      </code>
    </td>
    
    <td>
      Request timeout
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        tls
      </code>
    </td>
    
    <td>
      object
    </td>
    
    <td>
      -
    </td>
    
    <td>
      TLS configuration
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        auth
      </code>
    </td>
    
    <td>
      object
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Authentication configuration
    </td>
  </tr>
</tbody>
</table>

## Response validation

Validate response content using rules:

```yaml
receivers:
  httpcheck:
    targets:
      - endpoint: 'https://api.example.com/health'
        method: GET
        validations:
          - contains: '"status":"healthy"'
          - not_contains: '"error"'
          - min_size: 10
          - max_size: 10000
```

### Validation types

<table>
<thead>
  <tr>
    <th>
      Type
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
        contains
      </code>
    </td>
    
    <td>
      Response body must contain this string
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        not_contains
      </code>
    </td>
    
    <td>
      Response body must not contain this string
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        json_path
      </code>
    </td>
    
    <td>
      JSON path expression to extract a value
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        equals
      </code>
    </td>
    
    <td>
      Value must match exactly (used with json_path)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        min_size
      </code>
    </td>
    
    <td>
      Minimum response body size in bytes
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        max_size
      </code>
    </td>
    
    <td>
      Maximum response body size in bytes
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        regex
      </code>
    </td>
    
    <td>
      Regular expression pattern to match
    </td>
  </tr>
</tbody>
</table>

### JSON path validation

Validate specific JSON fields in the response:

```yaml
receivers:
  httpcheck:
    targets:
      - endpoint: 'https://api.example.com/health'
        method: GET
        validations:
          - json_path: 'status'
            equals: 'ok'
          - json_path: 'version'
            regex: '^\d+\.\d+\.\d+$'
```

## Authentication

### Basic auth

```yaml
receivers:
  httpcheck:
    targets:
      - endpoint: 'https://api.example.com/internal/health'
        method: GET
        auth:
          authenticator: basicauth

extensions:
  basicauth:
    client_auth:
      username: monitoring
      password: ${env:MONITOR_PASSWORD}
```

### Bearer token

```yaml
receivers:
  httpcheck:
    targets:
      - endpoint: 'https://api.example.com/health'
        method: GET
        headers:
          Authorization: 'Bearer ${env:API_TOKEN}'
```

## TLS configuration

Monitor HTTPS endpoints with custom TLS settings:

```yaml
receivers:
  httpcheck:
    targets:
      - endpoint: 'https://internal.example.com/health'
        method: GET
        tls:
          insecure_skip_verify: false
          ca_file: /etc/ssl/certs/ca.pem
          cert_file: /etc/ssl/certs/client.pem
          key_file: /etc/ssl/certs/client-key.pem
    collection_interval: 60s
```

## Health Check Extension

You can use the HTTPcheck receiver with the Collector's own Health Check Extension to monitor the Collector itself:

```yaml
extensions:
  health_check:
    endpoint: 0.0.0.0:13133

receivers:
  httpcheck:
    targets:
      - endpoint: 'http://localhost:13133/health/status'
        method: GET
    collection_interval: 15s
```

## Metrics reference

### Default metrics (enabled)

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Unit
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
        httpcheck.duration
      </code>
    </td>
    
    <td>
      Gauge
    </td>
    
    <td>
      ms
    </td>
    
    <td>
      Total duration of the HTTP check
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.status
      </code>
    </td>
    
    <td>
      Sum
    </td>
    
    <td>
      1
    </td>
    
    <td>
      1 if status code matches expected class, 0 otherwise
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.error
      </code>
    </td>
    
    <td>
      Sum
    </td>
    
    <td>
      count
    </td>
    
    <td>
      Count of errors during HTTP checks
    </td>
  </tr>
</tbody>
</table>

### Optional metrics (disabled by default)

Enable these in your metrics builder config for detailed timing breakdowns:

<table>
<thead>
  <tr>
    <th>
      Metric
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Unit
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
        httpcheck.dns.lookup.duration
      </code>
    </td>
    
    <td>
      Gauge
    </td>
    
    <td>
      ms
    </td>
    
    <td>
      DNS resolution time
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.client.connection.duration
      </code>
    </td>
    
    <td>
      Gauge
    </td>
    
    <td>
      ms
    </td>
    
    <td>
      TCP connection establishment time
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.tls.handshake.duration
      </code>
    </td>
    
    <td>
      Gauge
    </td>
    
    <td>
      ms
    </td>
    
    <td>
      TLS handshake time
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.client.request.duration
      </code>
    </td>
    
    <td>
      Gauge
    </td>
    
    <td>
      ms
    </td>
    
    <td>
      HTTP request transmission time
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.response.duration
      </code>
    </td>
    
    <td>
      Gauge
    </td>
    
    <td>
      ms
    </td>
    
    <td>
      HTTP response receipt time
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.response.size
      </code>
    </td>
    
    <td>
      Gauge
    </td>
    
    <td>
      bytes
    </td>
    
    <td>
      Response body size
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.tls.cert_remaining
      </code>
    </td>
    
    <td>
      Gauge
    </td>
    
    <td>
      s
    </td>
    
    <td>
      Time until TLS certificate expiry
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.validation.passed
      </code>
    </td>
    
    <td>
      Sum
    </td>
    
    <td>
      count
    </td>
    
    <td>
      Count of successful response validations
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpcheck.validation.failed
      </code>
    </td>
    
    <td>
      Sum
    </td>
    
    <td>
      count
    </td>
    
    <td>
      Count of failed response validations
    </td>
  </tr>
</tbody>
</table>

### Metric attributes

<table>
<thead>
  <tr>
    <th>
      Attribute
    </th>
    
    <th>
      Metrics
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
        http.url
      </code>
    </td>
    
    <td>
      All metrics
    </td>
    
    <td>
      The checked URL
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.method
      </code>
    </td>
    
    <td>
      <code>
        httpcheck.status
      </code>
    </td>
    
    <td>
      HTTP method used
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.status_code
      </code>
    </td>
    
    <td>
      <code>
        httpcheck.status
      </code>
    </td>
    
    <td>
      Response status code
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.status_class
      </code>
    </td>
    
    <td>
      <code>
        httpcheck.status
      </code>
    </td>
    
    <td>
      Status class (1xx, 2xx, 3xx, 4xx, 5xx)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        error.message
      </code>
    </td>
    
    <td>
      <code>
        httpcheck.error
      </code>
    </td>
    
    <td>
      Error description
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.tls.issuer
      </code>
    </td>
    
    <td>
      <code>
        httpcheck.tls.cert_remaining
      </code>
    </td>
    
    <td>
      Certificate issuer
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.tls.cn
      </code>
    </td>
    
    <td>
      <code>
        httpcheck.tls.cert_remaining
      </code>
    </td>
    
    <td>
      Certificate common name
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        http.tls.san
      </code>
    </td>
    
    <td>
      <code>
        httpcheck.tls.cert_remaining
      </code>
    </td>
    
    <td>
      Subject alternative names
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        validation.type
      </code>
    </td>
    
    <td>
      <code>
        httpcheck.validation.*
      </code>
    </td>
    
    <td>
      Type of validation (contains, regex, etc.)
    </td>
  </tr>
</tbody>
</table>

## Enabling optional metrics

To enable optional metrics, add a `metrics` section to your receiver config:

```yaml
receivers:
  httpcheck:
    targets:
      - endpoint: 'https://api.example.com/health'
        method: GET
    collection_interval: 60s
    metrics:
      httpcheck.dns.lookup.duration:
        enabled: true
      httpcheck.tls.handshake.duration:
        enabled: true
      httpcheck.tls.cert_remaining:
        enabled: true
      httpcheck.response.size:
        enabled: true
      httpcheck.validation.passed:
        enabled: true
      httpcheck.validation.failed:
        enabled: true
```

## Complete example

A production-ready configuration monitoring multiple services with validation and TLS monitoring:

```yaml
receivers:
  httpcheck:
    targets:
      - endpoint: 'https://api.example.com/health'
        method: GET
        validations:
          - contains: '"status":"ok"'
      - endpoint: 'https://web.example.com'
        method: GET
        validations:
          - min_size: 1000
          - contains: '</html>'
      - endpoint: 'https://internal.example.com/api/v1/status'
        method: POST
        headers:
          Content-Type: application/json
        body: '{"check": "full"}'
        validations:
          - json_path: 'healthy'
            equals: 'true'
    collection_interval: 60s
    metrics:
      httpcheck.tls.cert_remaining:
        enabled: true
      httpcheck.dns.lookup.duration:
        enabled: true

processors:
  batch:

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers: { 'uptrace-dsn': '<FIXME>' }

service:
  pipelines:
    metrics:
      receivers: [httpcheck]
      processors: [batch]
      exporters: [otlp]
```

## OpenTelemetry Backend

Once the metrics are collected and exported, you can visualize them using a compatible backend system. For example, you can use Uptrace to create dashboards that display metrics from the OpenTelemetry Collector.

Uptrace is an [open source APM](/get/hosted/open-source-apm) for OpenTelemetry that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules, notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## FAQ

**What is the HTTPcheck receiver?** The HTTPcheck receiver is an OpenTelemetry Collector component that performs synthetic HTTP checks against endpoints. It records metrics about availability, response time, status codes, and can validate response content.

**How often should I check endpoints?** For production health checks, 30-60 seconds is typical. For critical services, you might use 15 seconds. Avoid very short intervals as they can generate unnecessary load on your services.

**Can I validate JSON responses?** Yes, use the `json_path` validation type with `equals` to check specific fields. For example, `json_path: 'status'` with `equals: 'ok'` validates that the JSON response has `{"status": "ok"}`.

**How do I monitor TLS certificate expiration?** Enable the `httpcheck.tls.cert_remaining` metric. It reports the time remaining in seconds until certificate expiry. Negative values indicate an expired certificate. Set up alerts when the value drops below 30 days (2592000 seconds).

**What happens when a check fails?** Failed checks increment the `httpcheck.error` metric with an `error.message` attribute describing the failure. The `httpcheck.status` metric will report 0 for the expected status class.

**Can I use POST requests with a body?** Yes, specify `method: POST` and provide a `body` string. Use `auto_content_type: true` to automatically detect the content type, or set it manually via `headers`.

## What's next?

HTTP endpoint monitoring is now active, providing uptime checks and response time metrics for your services. Combine with [Kubernetes monitoring](/get/kubernetes) for cluster health checks, or add [Docker instrumentation](/guides/opentelemetry-docker) for containerized service monitoring. Set up the [OpenTelemetry Collector](/opentelemetry/collector) for additional receivers and processing pipelines.
