# Source: https://uptrace.dev/raw/guides/opentelemetry-redis.md

# Monitor Redis with OpenTelemetry Collector

> Complete Redis OpenTelemetry monitoring setup with Collector receiver. Configure Redis Otel metrics collection and visualize performance data with Uptrace.

This guide shows you how to implement [Redis monitoring](/blog/redis-monitoring) using OpenTelemetry Collector and Uptrace.

To monitor Redis performance with OpenTelemetry, you can use OpenTelemetry Collector to collect metrics and Uptrace to visualize them.

## Prerequisites

Ensure your Redis server is running properly:

```bash
redis-cli info | grep uptime_in_seconds
```

For remote Redis instances:

```bash
redis-cli -h <host> -p <port> info | grep uptime_in_seconds
```

## What is OpenTelemetry Collector?

[OpenTelemetry Collector](/opentelemetry/collector) facilitates the collection, processing, and export of telemetry data from multiple sources. It acts as an intermediary between applications and observability backends, enabling unified data collection and export.

With OpenTelemetry Collector, you can centralize and standardize your telemetry data collection, apply data processing operations, and seamlessly export data to multiple [OpenTelemetry APMs](/opentelemetry/apm). It supports a range of processors that can manipulate data, apply sampling strategies, and perform other data transformations based on your requirements.

## OpenTelemetry Redis receiver

To start monitoring Redis with Otel Collector, you need to configure Redis [receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/redisreceiver/README.md) in `/etc/otel-contrib-collector/config.yaml` using [Uptrace DSN](/get#dsn):

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:
  redis:
    endpoint: localhost:6379
    collection_interval: 10s
    password: ${REDIS_PASSWORD}  # Optional for secured Redis

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers: { 'uptrace-dsn': '<FIXME>' }

processors:
  resourcedetection:
    detectors: [env, system]
  cumulativetodelta:
  batch:
    timeout: 10s

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
    metrics:
      receivers: [otlp, redis]
      processors: [cumulativetodelta, batch, resourcedetection]
      exporters: [otlp]
```

Don't forget to restart the service:

```shell
sudo systemctl restart otelcol-contrib
```

You can also check OpenTelemetry Collector logs for any errors:

```shell
sudo journalctl -u otelcol-contrib -f
```

## Advanced Redis receiver configuration

The OpenTelemetry Redis instrumentation supports additional configuration options:

```yaml
receivers:
  redis:
    endpoint: localhost:6379
    collection_interval: 30s
    password: ${REDIS_PASSWORD}
    username: ${REDIS_USERNAME}    # Redis 6.0+
    tls:
      insecure: false
      ca_file: /path/to/ca.pem
    initial_delay: 1s
    timeout: 10s
```

Redis receiver provides [configuration](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/redisreceiver/README.md#configuration) options to collect specific metrics, enable or disable tracing, define sampling rates for traces, and configure log collection settings.

By utilizing the OpenTelemetry Redis receiver, you can capture and collect telemetry data from Redis, enabling you to gain insights into the performance, behavior, and usage patterns of your Redis instances. This data can be invaluable for monitoring, troubleshooting, and optimizing the performance of your Redis infrastructure.

## OpenTelemetry Backend

Uptrace is a [OpenTelemetry backend](/blog/opentelemetry-backend) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues. For [APM capabilities](/opentelemetry/apm), compare with [top APM tools](/tools/top-apm-tools) for Redis monitoring.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## Available metrics

When telemetry data reaches Uptrace, it automatically generates a Redis dashboard from a pre-defined template.

The Redis Otel receiver collects key performance indicators:

- **Connection tracking** - `redis.clients.connected`, `redis.clients.blocked`
- **Memory monitoring** - `redis.memory.used`, `redis.memory.peak`, `redis.memory.fragmentation_ratio`
- **Command performance** - `redis.commands.processed`, `redis.keyspace.hits`, `redis.keyspace.misses`
- **Data persistence** - `redis.rdb.changes_since_last_save`, `redis.aof.size`

![Redis metrics](/guides/opentelemetry-redis/metrics.png)

## Redis OpenTelemetry instrumentation

For application-level Redis OpenTelemetry instrumentation, use OpenTelemetry SDKs:

Python Redis instrumentation:

```python
from opentelemetry.instrumentation.redis import RedisInstrumentor

# Automatically instrument Redis calls
RedisInstrumentor().instrument()
```

Node.js Redis instrumentation:

```javascript
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');
const { RedisInstrumentation } = require('@opentelemetry/instrumentation-redis');
const { registerInstrumentations } = require('@opentelemetry/instrumentation');

const provider = new NodeTracerProvider();
provider.register();

registerInstrumentations({
  instrumentations: [new RedisInstrumentation()]
});
```

For other languages, see [OpenTelemetry Redis instrumentation docs](https://opentelemetry.io/ecosystem/registry/?language=&component=&instrumentation=redis).

## Troubleshooting Redis monitoring

Common issues when setting up Redis OpenTelemetry monitoring:

Test Redis connectivity:

```bash
redis-cli -h localhost -p 6379 ping
```

Check OpenTelemetry Collector logs for Redis receiver errors:

```bash
sudo journalctl -u otelcol-contrib -f | grep redis
```

Verify Redis receiver configuration and ensure network connectivity between collector and Redis.

## FAQ

**Can I monitor multiple Redis instances?**<br />


Yes, configure multiple Redis receivers with different endpoints in your OpenTelemetry collector config.

**Does Redis Otel instrumentation impact performance?**<br />


Minimal impact. The collector polls Redis INFO command which is lightweight and non-blocking.

**How do I monitor Redis Cluster with OpenTelemetry?**<br />


Configure separate receivers for each cluster node or use service discovery features in advanced collector setups.

**Can I collect Redis logs with OpenTelemetry?**<br />


Yes, use filelog receiver to collect Redis log files alongside metrics for complete observability.

## Additional Resources

- [OpenTelemetry Backend Comparison](/opentelemetry/backend-comparison)
- [Uptrace Documentation](/get)
