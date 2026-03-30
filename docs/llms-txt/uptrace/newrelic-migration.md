# Source: https://uptrace.dev/raw/get/newrelic-migration.md

# Migrating from New Relic to Uptrace

> Learn how to successfully migrate your monitoring infrastructure from New Relic to Uptrace with this step-by-step guide covering infrastructure setup, application instrumentation, dashboard conversion, and validation.

This guide walks you through migrating from New Relic to Uptrace, an OpenTelemetry-native observability platform. You'll learn how to replace New Relic agents with OpenTelemetry SDKs, configure the OpenTelemetry Collector, and recreate dashboards and alerts.

## Why Migrate from New Relic to Uptrace

Organizations migrate from New Relic to Uptrace for several key reasons:

**Cost Efficiency:**

- Uptrace processes billions of spans on a single server at 10x lower cost
- No per-host pricing or unpredictable usage-based charges
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

## Inventory Existing New Relic Resources

First, create an inventory of your current New Relic implementation:

- **APM Services**: List all applications monitored by New Relic APM
- **Custom Instrumentation**: Identify any manually added instrumentation
- **Infrastructure Monitoring**: Document hosts, containers, and cloud integrations
- **Logs & Metrics**: Catalog important logs, custom metrics, and alerting rules
- **Dashboards & NRQL Queries**: Note any NRQL-based queries you need to migrate
- **Alerts & Notifications**: Document alert conditions and notification channels

You can use the New Relic API to extract this information programmatically:

```bash
# Export all dashboards
curl -X GET 'https://api.newrelic.com/v2/dashboards.json' \
  -H "Api-Key:${NEWRELIC_API_KEY}" > dashboards.json

# Export alert policies
curl -X GET 'https://api.newrelic.com/v2/alerts_policies.json' \
  -H "Api-Key:${NEWRELIC_API_KEY}" > alert_policies.json

# List APM applications
curl -X GET 'https://api.newrelic.com/v2/applications.json' \
  -H "Api-Key:${NEWRELIC_API_KEY}" > applications.json
```

## Infrastructure Setup

Setting up the underlying infrastructure is the first step in your migration journey.

### Configure Uptrace Environment

Start by setting up Uptrace using either the cloud or self-hosted option:

- **Cloud-Hosted Option**: [Sign up for Uptrace Cloud](https://app.uptrace.dev/join)
- **Self-Hosted Option**: [Install Uptrace on your infrastructure](/get/hosted/install)

Once set up, obtain your project **DSN** from the project settings page. You'll need this DSN to connect your services to Uptrace.

### Deploy OpenTelemetry Collector

The OpenTelemetry Collector is the central component that will replace your New Relic agents. It collects telemetry data from various sources and forwards it to Uptrace.

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
    endpoint: 'https://api.uptrace.dev:4317'
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

Install the [OpenTelemetry Collector](/opentelemetry/collector) on all hosts currently running the New Relic agent to ensure comprehensive coverage.

### Configure Data Collection Strategies

Depending on your infrastructure, set up appropriate receivers in the OpenTelemetry Collector:

**Host Metrics Collection**

For system metrics previously collected by New Relic Infrastructure:

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

For applications exposing Prometheus metrics:

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

### Migrating Tracing Code

Replace New Relic tracing with OpenTelemetry [distributed tracing](/opentelemetry/distributed-tracing).

**Before (New Relic):**

<code-group>

```python [Python]
import newrelic.agent

@newrelic.agent.background_task()
def process_request(request):
    newrelic.agent.add_custom_attribute('request.id', request.id)
    # process request
```

```go [Go]
import "github.com/newrelic/go-agent/v3/newrelic"

func processRequest(txn *newrelic.Transaction, request Request) {
    defer txn.StartSegment("process_request").End()
    txn.AddAttribute("request.id", request.ID)
    // process request
}
```

```javascript [Node.js]
const newrelic = require('newrelic');

newrelic.startBackgroundTransaction('process_request', function () {
  const transaction = newrelic.getTransaction();
  newrelic.addCustomAttribute('request.id', request.id);
  // process request
  transaction.end();
});
```

```java [Java]
import com.newrelic.api.agent.NewRelic;
import com.newrelic.api.agent.Trace;

public class RequestProcessor {
    @Trace
    public void processRequest(Request request) {
        NewRelic.addCustomParameter("request.id", request.getId());
        // process request
    }
}
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

```java [Java]
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.api.trace.Span;

public class RequestProcessor {
    private final Tracer tracer = openTelemetry.getTracer("my-service");

    public void processRequest(Request request) {
        Span span = tracer.spanBuilder("process_request").startSpan();
        try (Scope scope = span.makeCurrent()) {
            span.setAttribute("request.id", request.getId());
            // process request
        } finally {
            span.end();
        }
    }
}
```

</code-group>

For language-specific tracing guides, see:

<home-distro-list page="tracing">



</home-distro-list>

### Migrating Metrics Code

Update your metric collection code to use OpenTelemetry.

**Metric Type Mapping:**

<table>
<thead>
  <tr>
    <th>
      New Relic Type
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
      recordMetric (count)
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
      recordMetric (gauge)
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
      recordResponseTime
    </td>
    
    <td>
      Histogram
    </td>
    
    <td>
      Distribution of values
    </td>
  </tr>
</tbody>
</table>

**Before (New Relic):**

<code-group>

```python [Python]
import newrelic.agent

newrelic.agent.record_custom_metric('Custom/PageViews', 1)
newrelic.agent.record_custom_metric('Custom/ActiveUsers', 123)
```

```go [Go]
import "github.com/newrelic/go-agent/v3/newrelic"

app.RecordCustomMetric("Custom/PageViews", 1)
app.RecordCustomMetric("Custom/ActiveUsers", 123)
```

```javascript [Node.js]
const newrelic = require('newrelic');

newrelic.recordMetric('Custom/PageViews', 1);
newrelic.recordMetric('Custom/ActiveUsers', 123);
```

</code-group>

**After (OpenTelemetry):**

<code-group>

```python [Python]
from opentelemetry import metrics

meter = metrics.get_meter("my-service")
page_views = meter.create_counter("web.page_views")
users_online = meter.create_up_down_counter("web.users.online")

page_views.add(1)
users_online.add(123)
```

```go [Go]
import "go.opentelemetry.io/otel/metric"

meter := otel.Meter("my-service")
pageViews, _ := meter.Int64Counter("web.page_views")
usersOnline, _ := meter.Int64UpDownCounter("web.users.online")

pageViews.Add(ctx, 1)
usersOnline.Add(ctx, 123)
```

```javascript [Node.js]
const { metrics } = require('@opentelemetry/api');

const meter = metrics.getMeter('my-service');
const pageViews = meter.createCounter('web.page_views');
const usersOnline = meter.createUpDownCounter('web.users.online');

pageViews.add(1);
usersOnline.add(123);
```

</code-group>

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

Transferring your dashboards and alerts from New Relic to Uptrace ensures continuity in your monitoring capabilities.

### Converting Dashboards

When recreating dashboards in Uptrace:

1. **Start with critical dashboards** first identified in your inventory
2. **Use Uptrace's prebuilt dashboards** where applicable
3. **Convert NRQL queries** to Uptrace's PromQL-compatible syntax
4. **Validate visualizations** match your expectations

### Migrating Alerts

To transfer your alerts:

1. **Extract alert definitions** from New Relic
2. **Create equivalent alerts** in Uptrace
3. **Test alert triggering** to ensure proper functionality
4. **Update notification channels** to match your current setup

### NRQL to PromQL Translation Guide

When migrating from New Relic to Uptrace, you'll need to translate New Relic Query Language (NRQL) to Prometheus Query Language (PromQL). Here are common translation patterns:

**Basic Metrics Queries**

<table>
<thead>
  <tr>
    <th>
      NRQL
    </th>
    
    <th>
      PromQL
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
        SELECT average(duration) FROM Transaction
      </code>
    </td>
    
    <td>
      <code>
        avg(http_request_duration_seconds)
      </code>
    </td>
    
    <td>
      Simple average
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SELECT average(duration) FROM Transaction WHERE appName = 'my-app'
      </code>
    </td>
    
    <td>
      <code>
        avg(http_request_duration_seconds{app="my-app"})
      </code>
    </td>
    
    <td>
      Average with filter
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SELECT sum(count) FROM Transaction FACET host
      </code>
    </td>
    
    <td>
      <code>
        sum(http_requests_total) by (host)
      </code>
    </td>
    
    <td>
      Grouping by attribute
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SELECT count(*) FROM Transaction WHERE httpResponseCode >= 500
      </code>
    </td>
    
    <td>
      <code>
        count(http_requests_total{status_code=~"5.."})
      </code>
    </td>
    
    <td>
      Counting with regex
    </td>
  </tr>
</tbody>
</table>

**Time Aggregation**

<table>
<thead>
  <tr>
    <th>
      NRQL
    </th>
    
    <th>
      PromQL
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
        SELECT average(cpuPercent) FROM SystemSample TIMESERIES 1 minute
      </code>
    </td>
    
    <td>
      <code>
        avg_over_time(system_cpu_percent[1m])
      </code>
    </td>
    
    <td>
      1-minute average
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SELECT sum(count) FROM Transaction TIMESERIES 5 minutes
      </code>
    </td>
    
    <td>
      <code>
        sum_over_time(http_requests_total[5m])
      </code>
    </td>
    
    <td>
      5-minute sum
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SELECT max(duration) FROM Transaction SINCE 1 hour ago
      </code>
    </td>
    
    <td>
      <code>
        max_over_time(http_request_duration_seconds[1h])
      </code>
    </td>
    
    <td>
      Maximum over 1 hour
    </td>
  </tr>
</tbody>
</table>

**Rate and Throughput Calculations**

<table>
<thead>
  <tr>
    <th>
      NRQL
    </th>
    
    <th>
      PromQL
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
        SELECT rate(count(*), 1 second) FROM Transaction
      </code>
    </td>
    
    <td>
      <code>
        rate(http_requests_total[5m])
      </code>
    </td>
    
    <td>
      Request rate per second
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SELECT derivative(count, 1 minute) FROM Metric
      </code>
    </td>
    
    <td>
      <code>
        deriv(metric_name[5m])
      </code>
    </td>
    
    <td>
      Rate of change
    </td>
  </tr>
</tbody>
</table>

**Percentile Queries**

<table>
<thead>
  <tr>
    <th>
      NRQL
    </th>
    
    <th>
      PromQL
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
        SELECT percentile(duration, 95) FROM Transaction
      </code>
    </td>
    
    <td>
      <code>
        histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
      </code>
    </td>
    
    <td>
      95th percentile
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SELECT percentile(duration, 50, 90, 99) FROM Transaction
      </code>
    </td>
    
    <td>
      Use multiple <code>
        histogram_quantile()
      </code>
      
       calls
    </td>
    
    <td>
      Multiple percentiles
    </td>
  </tr>
</tbody>
</table>

**Naming Conventions**

When migrating metrics, follow these naming conversion rules:

1. **Replace dots with underscores**:
  - New Relic: `Custom/PageViews`
  - OpenTelemetry: `custom_page_views`
2. **Add appropriate unit suffixes**:
  - New Relic: `duration` (milliseconds implied)
  - OpenTelemetry: `http_request_duration_seconds`
3. **Use standard metric names** where possible following [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/)

## Validation and Testing

Before decommissioning New Relic, run both systems in parallel to validate data consistency.

### Data Consistency Checks

Verify that metrics in Uptrace match those in New Relic:

1. **Compare metric values** for identical time periods
2. **Check alert triggering** in both systems
3. **Ensure trace completeness** across services
4. **Validate log collection** and correlation

### Parallel Running Period

Run New Relic and Uptrace simultaneously for 1-2 weeks:

- Compare dashboards side-by-side
- Verify alerts fire correctly in both systems
- Check that all services are reporting to Uptrace
- Validate data retention and query performance

Once you confirm data parity, gradually migrate teams to Uptrace before disabling New Relic agents.

## Decommission New Relic

Once you confirm everything is running smoothly in Uptrace:

1. **Remove New Relic agents** from your applications
2. **Uninstall New Relic Infrastructure** agents from hosts
3. **Disable log forwarding** to New Relic
4. **Archive your New Relic configuration** for reference
5. **Cancel your New Relic subscription**

## OpenTelemetry Backend

Uptrace is an [open source APM](/get/hosted/open-source-apm) for OpenTelemetry that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## FAQ

**How long does a typical New Relic migration take?**<br />


Migration timeline depends on the complexity of your setup. Simple deployments can migrate in a few days, while complex multi-service architectures may take several weeks for full validation.

**Can I run New Relic and Uptrace simultaneously during migration?**<br />


Yes, this is the recommended approach. Run both systems in parallel to validate data parity before fully transitioning to Uptrace.

**Do I need to change my application code?**<br />


Yes, you'll need to replace New Relic SDK calls with OpenTelemetry SDKs. However, many frameworks support auto-instrumentation, reducing code changes significantly.

**What about New Relic integrations for cloud services?**<br />


Most New Relic integrations have OpenTelemetry equivalents. The [OpenTelemetry Collector](/opentelemetry/collector) provides receivers for common services like databases, message queues, and cloud providers.

**How do I handle New Relic APM traces during migration?**<br />


OpenTelemetry traces are semantically similar to New Relic traces. The main changes are attribute naming conventions and SDK initialization code.

**What if I have New Relic Synthetic tests?**<br />


Uptrace focuses on application observability. For synthetic monitoring, consider tools like Checkly or Grafana Synthetic Monitoring that integrate with OpenTelemetry.

**Can I migrate New Relic Browser monitoring?**<br />


Yes, you can use OpenTelemetry JavaScript SDK for browser instrumentation. It provides similar real user monitoring (RUM) capabilities.

## What's Next?

Your New Relic migration journey continues with these resources:

- **Data Ingestion**: Explore all [ingestion methods](/ingest) including [OpenTelemetry SDK](/ingest/opentelemetry), [Collector](/ingest/collector), and [Prometheus](/ingest/prometheus)
- **Log Collection**: Set up log pipelines with [Vector](/ingest/logs/vector) or [FluentBit](/ingest/logs/fluentbit)
- **Kubernetes**: Deploy collectors in [Kubernetes environments](/get/kubernetes)
- **Instrumentation Guides**: Find framework-specific tutorials in our [guides section](/guides)
- **OpenTelemetry**: Learn more about [OpenTelemetry fundamentals](/opentelemetry)
