# Source: https://uptrace.dev/raw/guides/opentelemetry-kafka.md

# Kafka Monitoring with OpenTelemetry Collector

> Monitor Apache Kafka performance using OpenTelemetry Collector kafkametrics receiver. Track broker metrics, consumer lag, and partition health with real-time observability.

Apache Kafka is a widely used distributed streaming platform known for its high throughput, fault tolerance, and scalability.

Using the OpenTelemetry Collector Kafka receiver, you can collect telemetry data from Kafka applications and send it to your observability backend for analysis and visualization.

## Why Monitor Kafka?

Monitoring Apache Kafka is critical to ensuring the health, performance, and reliability of your Kafka cluster. Kafka observability helps you:

- **Detect performance bottlenecks** - identify slow consumers and partition lag
- **Track resource utilization** - monitor CPU, disk, memory, and network usage
- **Prevent data loss** - catch replication issues before they affect availability
- **Optimize throughput** - understand message rates and broker capacity
- **Troubleshoot issues** - correlate metrics with application behavior

### Key Kafka Metrics to Monitor

**Broker Metrics:**

- Request rate and latency
- Network throughput (bytes in/out)
- Active controller count
- Under-replicated partitions

**Consumer Metrics:**

- Consumer lag (messages behind)
- Fetch rate and latency
- Commit rate
- Rebalance frequency

**Producer Metrics:**

- Produce rate and latency
- Record error rate
- Request queue size
- Batch size metrics

**Partition Metrics:**

- Partition count per broker
- Leader/follower status
- In-sync replicas (ISR)
- Log size and segment count

## What is OpenTelemetry Collector?

You can deploy [OpenTelemetry Collector](/opentelemetry/collector) as an agent that runs on individual hosts, where it periodically collects and forwards diagnostic information about the running system to various [distributed tracing tools](/tools/distributed-tracing-tools).

OpenTelemetry Collector provides powerful data processing capabilities. It can aggregate, filter, transform, and enrich telemetry data as it flows through the system.

With OpenTelemetry Collector, you can collect telemetry data from your Kafka clusters and send it to the [OpenTelemetry backend](/blog/opentelemetry-backend) of your choice. This allows you to gain insight into the behavior and performance of your Kafka messaging system, monitor message processing times, track message flows, and analyze the overall health of your Kafka-based applications.

## OpenTelemetry Kafka receiver

To start monitoring Kafka, you need to configure [Kafka receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kafkametricsreceiver) in `/etc/otel-contrib-collector/config.yaml` using [Uptrace DSN](/get#dsn):

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:
  kafkametrics:
    brokers:
      - localhost:9092
    protocol_version: 2.0.0
    scrapers:
      - brokers
      - topics
      - consumers

exporters:
  otlp/uptrace:
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
      exporters: [otlp/uptrace]
    metrics:
      receivers: [otlp, kafkametrics]
      processors: [cumulativetodelta, batch, resourcedetection]
      exporters: [otlp/uptrace]
```

### Available Scrapers

The Kafka receiver supports multiple scrapers:

- **brokers** - Collects broker-level metrics (requests, network, partitions)
- **topics** - Topic-level metrics (partition count, replication factor)
- **consumers** - Consumer group metrics (lag, offset, member count)

Configure only the scrapers you need to reduce overhead.

Don't forget to restart OpenTelemetry Collector:

```shell
sudo systemctl restart otelcol-contrib
```

You can also check OpenTelemetry Collector logs for any errors:

```shell
sudo journalctl -u otelcol-contrib -f
```

## Kafka Distributed Tracing

Beyond metrics, you can implement Kafka distributed tracing to track message flow through your event-driven architecture:

**Producer-side tracing:**

- Instrument Kafka producers to create spans when publishing messages
- Inject trace context into message headers

**Consumer-side tracing:**

- Extract trace context from message headers
- Create consumer spans linked to producer spans

This creates end-to-end visibility: see how long messages spend in Kafka topics and correlate with downstream processing.

For implementation details, see language-specific OpenTelemetry instrumentation guides.

## Troubleshooting Kafka Performance

### High Consumer Lag

**Symptom:** Messages backing up in topics, consumers can't keep up

**Diagnosis:** Check `kafka.consumer.lag` metric

**Common causes:**

- Slow consumer processing
- Insufficient consumer instances
- Network issues between consumers and brokers

**Fix:**

- Scale consumer group (add more consumers)
- Optimize consumer processing logic
- Increase consumer fetch size

### Under-Replicated Partitions

**Symptom:** `kafka.broker.under_replicated_partitions` > 0

**Meaning:** Some partition replicas are out of sync

**Causes:**

- Broker overload
- Network problems
- Disk I/O bottlenecks

**Fix:**

- Check broker resource usage (CPU, disk, network)
- Verify all brokers are healthy
- Review replication factor settings

### High Request Latency

**Symptom:** Slow produce/fetch requests

**Diagnosis:** Monitor `kafka.broker.request.latency`

**Fix:**

- Check broker CPU and disk I/O
- Optimize batch sizes
- Review compression settings
- Consider adding more brokers

## OpenTelemetry Backend

Once the metrics are collected and exported, you can visualize them using a compatible backend system. For example, you can use Uptrace to create dashboards that display metrics from the OpenTelemetry Collector.

Uptrace is a [DataDog alternative](/comparisons/datadog-alternatives) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues. For [APM capabilities](/opentelemetry/apm), compare with [top APM tools](/tools/top-apm-tools) for messaging infrastructure monitoring.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## What's next?

By monitoring Kafka metrics, you can detect problems and anomalies early and take proactive measures before they escalate. By tracking metrics such as partition lag, replication lag, and consumer lag, you can identify and address potential bottlenecks, slow consumers, or replication delays.

**Related monitoring guides:**

- [Redis monitoring](/guides/opentelemetry-redis) - Cache performance tracking
- [PostgreSQL monitoring](/guides/opentelemetry-postgresql) - Database observability
- [RabbitMQ monitoring](/guides/opentelemetry-rabbitmq) - Message queue monitoring
- [MySQL monitoring](/guides/opentelemetry-mysql) - Database metrics collection
