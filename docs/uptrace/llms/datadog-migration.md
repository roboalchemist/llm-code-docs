# Source: https://uptrace.dev/raw/get/datadog-migration.md

# Migrating from Datadog to Uptrace

> Learn how to successfully migrate your monitoring infrastructure from Datadog to Uptrace with this step-by-step guide covering infrastructure setup, application instrumentation, dashboard conversion, and validation.

This guide walks you through migrating from Datadog to Uptrace, an OpenTelemetry-native observability platform. You'll learn how to replace Datadog agents with OpenTelemetry Collector, update application instrumentation, and recreate dashboards and alerts.

## Why Migrate from Datadog to Uptrace

Organizations migrate from Datadog to Uptrace for several key reasons:

**Cost Efficiency:**

- Uptrace processes billions of spans on a single server at 10x lower cost
- No per-host pricing or unpredictable custom metrics charges
- Self-hosted option eliminates vendor data egress fees

**OpenTelemetry Native:**

- Built on open standards - no proprietary agents or lock-in
- Full compatibility with OpenTelemetry SDKs and Collector
- Export data to any backend without re-instrumenting

**Unified Observability:**

- Traces, metrics, and logs in a single platform
- Automatic correlation between telemetry signals
- Rich dashboards with PromQL-compatible query language

**Open Source Flexibility:**

- Self-host on your infrastructure or use managed cloud
- Full control over data retention and processing
- Active community and transparent development

## Inventory Existing Datadog Resources

First, create an inventory of your current Datadog implementation:

- List monitored hosts and services.
- Document custom metrics and integrations.
- Catalog dashboards, monitors, and alerts.
- Identify critical workflows and visualizations.

You can use the Datadog API to extract this information programmatically:

```bash
# Export dashboards list
curl -X GET "https://api.datadoghq.com/api/v1/dashboard" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" > dashboards_list.json

# Export monitors
curl -X GET "https://api.datadoghq.com/api/v1/monitor" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" > monitors.json
```

## Infrastructure Setup

Setting up the underlying infrastructure is the first step in your migration journey.

### Configure Uptrace Environment

Start by setting up Uptrace using either the cloud or self-hosted option:

- **Cloud-Hosted Option**: [Sign up for Uptrace Cloud](https://app.uptrace.dev/join)
- **Self-Hosted Option**: [Install Uptrace on your infrastructure](/get/hosted/install)

Once set up, obtain your project **DSN** from the project settings page. You'll need this DSN to connect your services to Uptrace.

### Deploy OpenTelemetry Collector

The OpenTelemetry Collector is the central component that will replace your Datadog agents. It collects telemetry data from various sources and forwards it to Uptrace.

**Basic OpenTelemetry Collector configuration:**

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

processors:
  batch:

exporters:
  otlp:
    endpoint: 'uptrace:4317'
    headers:
      uptrace-dsn: 'https://<secret>@api.uptrace.dev?grpc=4317'

service:
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
```

Install the [OpenTelemetry Collector](/opentelemetry/collector) on all hosts currently running the Datadog Agent to ensure comprehensive coverage.

### Configure Data Collection Strategies

Depending on your infrastructure, set up appropriate receivers in the OpenTelemetry Collector:

**Host Metrics Collection**

For system metrics, use the hostmetrics receiver:

```yaml
receivers:
  hostmetrics:
    collection_interval: 30s
    scrapers:
      cpu:
      memory:
      disk:
      filesystem:
      network:
      load:
      paging:
      process:
```

**Application Metrics Collection**

For applications already exposing Prometheus metrics:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'my-app'
          scrape_interval: 15s
          static_configs:
            - targets: ['my-app:8080']
```

**Legacy StatsD Metrics Collection**

For systems using StatsD or DogStatsD:

```yaml
receivers:
  statsd:
    endpoint: localhost:8125
    aggregation_interval: 60s
```

**Log Collection**

For collecting logs from files:

```yaml
receivers:
  filelog:
    include: [/var/log/*.log]
    start_at: end
    operators:
      - type: json_parser
```

## Application Instrumentation Changes

Updating your application code to use OpenTelemetry is a critical part of the migration process.

### Install OpenTelemetry SDKs

First, choose the appropriate SDK for your application's language:

<home-distro-list>



</home-distro-list>

### Migrating Metrics Code

Update your metric collection code to use OpenTelemetry.

**Metric Type Mapping:**

<table>
<thead>
  <tr>
    <th>
      Datadog Type
    </th>
    
    <th>
      OpenTelemetry Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Counter
    </td>
    
    <td>
      Counter
    </td>
    
    <td>
      Monotonically increasing values
    </td>
  </tr>
  
  <tr>
    <td>
      Gauge
    </td>
    
    <td>
      UpDownCounter
    </td>
    
    <td>
      Values that can increase or decrease
    </td>
  </tr>
  
  <tr>
    <td>
      Histogram
    </td>
    
    <td>
      Histogram
    </td>
    
    <td>
      Distribution of values
    </td>
  </tr>
  
  <tr>
    <td>
      Distribution
    </td>
    
    <td>
      Histogram
    </td>
    
    <td>
      Statistical distribution
    </td>
  </tr>
</tbody>
</table>

**Before (Datadog):**

<code-group>

```python [Python]
from datadog import statsd

statsd.increment('web.page_views')
statsd.gauge('web.users.online', 123)
statsd.histogram('http.request.duration', 0.25)
```

```go [Go]
import "github.com/DataDog/datadog-go/statsd"

client, _ := statsd.New("127.0.0.1:8125")
client.Incr("web.page_views", nil, 1)
client.Gauge("web.users.online", 123, nil, 1)
client.Histogram("http.request.duration", 0.25, nil, 1)
```

```javascript [Node.js]
const StatsD = require('hot-shots');
const client = new StatsD();

client.increment('web.page_views');
client.gauge('web.users.online', 123);
client.histogram('http.request.duration', 0.25);
```

</code-group>

**After (OpenTelemetry):**

<code-group>

```python [Python]
from opentelemetry import metrics

meter = metrics.get_meter("my-service")
page_views = meter.create_counter("web.page_views")
users_online = meter.create_up_down_counter("web.users.online")
request_duration = meter.create_histogram("http.request.duration")

page_views.add(1)
users_online.add(123)
request_duration.record(0.25)
```

```go [Go]
import "go.opentelemetry.io/otel/metric"

meter := otel.Meter("my-service")
pageViews, _ := meter.Int64Counter("web.page_views")
usersOnline, _ := meter.Int64UpDownCounter("web.users.online")
requestDuration, _ := meter.Float64Histogram("http.request.duration")

pageViews.Add(ctx, 1)
usersOnline.Add(ctx, 123)
requestDuration.Record(ctx, 0.25)
```

```javascript [Node.js]
const { metrics } = require('@opentelemetry/api');

const meter = metrics.getMeter('my-service');
const pageViews = meter.createCounter('web.page_views');
const usersOnline = meter.createUpDownCounter('web.users.online');
const requestDuration = meter.createHistogram('http.request.duration');

pageViews.add(1);
usersOnline.add(123);
requestDuration.record(0.25);
```

</code-group>

### Migrating Tracing Code

Replace Datadog tracing with OpenTelemetry [distributed tracing](/opentelemetry/distributed-tracing).

**Before (Datadog):**

<code-group>

```python [Python]
from ddtrace import tracer

@tracer.wrap()
def process_request(request):
    span = tracer.current_span()
    span.set_tag("request.id", request.id)
    # process request
```

```go [Go]
import "gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer"

func processRequest(request Request) {
    span, ctx := tracer.StartSpanFromContext(ctx, "process_request")
    defer span.Finish()
    span.SetTag("request.id", request.ID)
    // process request
}
```

```javascript [Node.js]
const tracer = require('dd-trace').init();

const span = tracer.startSpan('process_request');
span.setTag('request.id', request.id);
// process request
span.finish();
```

</code-group>

**After (OpenTelemetry):**

<code-group>

```python [Python]
from opentelemetry import trace

tracer = trace.get_tracer("my-service")

def process_request(request):
    with tracer.start_as_current_span("process_request") as span:
        span.set_attribute("request.id", request.id)
        # process request
```

```go [Go]
import "go.opentelemetry.io/otel"

tracer := otel.Tracer("my-service")

func processRequest(ctx context.Context, request Request) {
    ctx, span := tracer.Start(ctx, "process_request")
    defer span.End()
    span.SetAttributes(attribute.String("request.id", request.ID))
    // process request
}
```

```javascript [Node.js]
const { trace } = require('@opentelemetry/api');

const tracer = trace.getTracer('my-service');

tracer.startActiveSpan('process_request', (span) => {
    span.setAttribute('request.id', request.id);
    // process request
    span.end();
});
```

</code-group>

For language-specific tracing guides, see:

<home-distro-list page="tracing">



</home-distro-list>

### Implementing Auto-Instrumentation

For many languages, you can use auto-instrumentation to quickly add OpenTelemetry to your applications. Check our [guides](/guides) with instructions for the most popular frameworks.

### Updating Logging Code

Implement [structured logging](/glossary/structured-logging) with trace correlation. OpenTelemetry automatically injects trace context into your logs, enabling you to correlate logs with traces.

<code-group>

```python [Python]
import logging
import json
from opentelemetry import trace

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
        }

        # Add trace context
        current_span = trace.get_current_span()
        if current_span.is_recording():
            context = current_span.get_span_context()
            log_record["trace_id"] = format(context.trace_id, "032x")
            log_record["span_id"] = format(context.span_id, "016x")

        return json.dumps(log_record)

logger = logging.getLogger("app")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
```

```go [Go]
import (
    "go.opentelemetry.io/otel/trace"
    "go.uber.org/zap"
)

func logWithTrace(ctx context.Context, logger *zap.Logger, msg string) {
    span := trace.SpanFromContext(ctx)
    if span.IsRecording() {
        sc := span.SpanContext()
        logger.Info(msg,
            zap.String("trace_id", sc.TraceID().String()),
            zap.String("span_id", sc.SpanID().String()),
        )
    }
}
```

```javascript [Node.js]
const { trace } = require('@opentelemetry/api');

function logWithTrace(message, data = {}) {
    const span = trace.getActiveSpan();
    const logEntry = {
        timestamp: new Date().toISOString(),
        message,
        ...data,
    };

    if (span) {
        const context = span.spanContext();
        logEntry.trace_id = context.traceId;
        logEntry.span_id = context.spanId;
    }

    console.log(JSON.stringify(logEntry));
}
```

</code-group>

For more on logging with Uptrace, see [monitoring logs](/get/logs).

## Visualization and Alerting

Transferring your dashboards and alerts from Datadog to Uptrace ensures continuity in your monitoring capabilities.

### Converting Dashboards

When recreating dashboards in Uptrace:

1. **Start with critical dashboards** first identified in your inventory
2. **Use Uptrace's prebuilt dashboards** where applicable
3. **Convert Datadog queries** to Uptrace's PromQL-compatible syntax
4. **Validate visualizations** match your expectations

### Migrating Alerts

To transfer your alerts:

1. **Extract alert definitions** from Datadog
2. **Create equivalent alerts** in Uptrace
3. **Test alert triggering** to ensure proper functionality
4. **Update notification channels** to match your current setup

### DQL to PromQL Translation Guide

When migrating from Datadog to Uptrace, you'll need to translate Datadog Query Language (DQL) to Prometheus Query Language (PromQL). Here are common translation patterns:

**Basic Metrics Queries**

<table>
<thead>
  <tr>
    <th>
      Datadog Query (DQL)
    </th>
    
    <th>
      Uptrace Query (PromQL)
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
        avg:system.cpu.user{host:web-*}
      </code>
    </td>
    
    <td>
      <code>
        avg(system_cpu_user{host=~"web-.*"})
      </code>
    </td>
    
    <td>
      Simple average with regex matching
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        sum:http.requests{service:api}
      </code>
    </td>
    
    <td>
      <code>
        sum(http_requests_total{service="api"})
      </code>
    </td>
    
    <td>
      Summing metrics with tag matching
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        avg:system.load.1{*} by {host}
      </code>
    </td>
    
    <td>
      <code>
        avg(system_load1) by (host)
      </code>
    </td>
    
    <td>
      Grouping by a tag
    </td>
  </tr>
</tbody>
</table>

**Time Aggregation**

<table>
<thead>
  <tr>
    <th>
      Datadog Query (DQL)
    </th>
    
    <th>
      Uptrace Query (PromQL)
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
        avg:system.cpu.user{*}.rollup(avg, 60)
      </code>
    </td>
    
    <td>
      <code>
        avg_over_time(system_cpu_user[1m])
      </code>
    </td>
    
    <td>
      1-minute average
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        sum:http.requests{*}.rollup(sum, 300)
      </code>
    </td>
    
    <td>
      <code>
        sum_over_time(http_requests[5m])
      </code>
    </td>
    
    <td>
      5-minute sum
    </td>
  </tr>
</tbody>
</table>

**Rate and Change Calculations**

<table>
<thead>
  <tr>
    <th>
      Datadog Query (DQL)
    </th>
    
    <th>
      Uptrace Query (PromQL)
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
        per_second(sum:http.requests{*})
      </code>
    </td>
    
    <td>
      <code>
        rate(http_requests_total[5m])
      </code>
    </td>
    
    <td>
      Request rate (per second)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        diff(avg:system.mem.used{*})
      </code>
    </td>
    
    <td>
      <code>
        deriv(system_memory_used_bytes[5m])
      </code>
    </td>
    
    <td>
      Rate of change
    </td>
  </tr>
</tbody>
</table>

**Naming Conventions**

When migrating metrics, follow these naming conversion rules:

1. **Replace dots with underscores**:
  - Datadog: `system.cpu.user`
  - Uptrace: `system_cpu_user`
2. **Add appropriate unit suffixes**:
  - Datadog: `http.request.duration`
  - Uptrace: `http_request_duration_seconds`

## Validation and Testing

Before decommissioning Datadog, run both systems in parallel to validate data consistency.

### Data Consistency Checks

Verify that metrics in Uptrace match those in Datadog:

1. **Compare metric values** for identical time periods
2. **Check alert triggering** in both systems
3. **Ensure trace completeness** across services
4. **Validate log collection** and correlation

### Parallel Running Period

Run Datadog and Uptrace simultaneously for 1-2 weeks:

- Compare dashboards side-by-side
- Verify alerts fire correctly in both systems
- Check that all services are reporting to Uptrace
- Validate data retention and query performance

Once you confirm data parity, gradually migrate teams to Uptrace before disabling Datadog agents.

## OpenTelemetry Backend

Uptrace is an [open source APM](/get/hosted/open-source-apm) for OpenTelemetry that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## FAQ

**How long does a typical Datadog migration take?**<br />


Migration timeline depends on the complexity of your setup. Simple deployments can migrate in a few days, while complex multi-service architectures may take several weeks for full validation.

**Can I run Datadog and Uptrace simultaneously during migration?**<br />


Yes, this is the recommended approach. Run both systems in parallel to validate data parity before fully transitioning to Uptrace.

**Do I need to change my application code?**<br />


Yes, you'll need to replace Datadog SDK calls with OpenTelemetry SDKs. However, many frameworks support auto-instrumentation, reducing code changes significantly.

**What about Datadog integrations for third-party services?**<br />


Most Datadog integrations have OpenTelemetry equivalents. The [OpenTelemetry Collector](/opentelemetry/collector) provides receivers for common services like databases, message queues, and cloud providers.

**Can I keep using StatsD metrics?**<br />


Yes, OpenTelemetry Collector includes a StatsD receiver that accepts DogStatsD-formatted metrics, allowing gradual migration of custom metrics.

**How do I handle Datadog APM traces during migration?**<br />


OpenTelemetry traces are semantically similar to Datadog traces. The main changes are attribute naming conventions and SDK initialization code.

**What if I have Datadog Synthetic tests?**<br />


Uptrace focuses on application observability. For synthetic monitoring, consider tools like Checkly or Grafana Synthetic Monitoring that integrate with OpenTelemetry.

## What's Next?

Your Datadog migration journey continues with these resources:

- **Data Ingestion**: Explore all [ingestion methods](/ingest) including [OpenTelemetry SDK](/ingest/opentelemetry), [Collector](/ingest/collector), and [Prometheus](/ingest/prometheus)
- **Log Collection**: Set up log pipelines with [Vector](/ingest/logs/vector) or [FluentBit](/ingest/logs/fluentbit)
- **Kubernetes**: Deploy collectors in [Kubernetes environments](/get/kubernetes)
- **Instrumentation Guides**: Find framework-specific tutorials in our [guides section](/guides)
- **OpenTelemetry**: Learn more about [OpenTelemetry fundamentals](/opentelemetry)
