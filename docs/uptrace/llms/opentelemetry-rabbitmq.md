# Source: https://uptrace.dev/raw/guides/opentelemetry-rabbitmq.md

# OpenTelemetry RabbitMQ Monitoring Guide

> Monitor your RabbitMQ cluster performance for free using Uptrace and OpenTelemetry Collector receiver. Track messages, queues, and broker health.

[Monitoring RabbitMQ performance](/blog/rabbitmq-monitoring) is essential to ensure reliable message delivery and identify potential bottlenecks in your messaging infrastructure. RabbitMQ metrics help you track queue depths, message rates, connection counts, and resource utilization.

This guide explains how to collect RabbitMQ metrics using the [OpenTelemetry Collector](/opentelemetry/collector) and visualize them in your monitoring backend.

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
      Details
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      1. Enable
    </td>
    
    <td>
      Enable RabbitMQ management plugin
    </td>
    
    <td>
      <code>
        rabbitmq-plugins enable rabbitmq_management
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      2. Configure
    </td>
    
    <td>
      Add <code>
        rabbitmq
      </code>
      
       receiver to Collector config
    </td>
    
    <td>
      Point to <code>
        http://localhost:15672
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      3. Restart
    </td>
    
    <td>
      Restart the Collector
    </td>
    
    <td>
      <code>
        sudo systemctl restart otelcol-contrib
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      4. Verify
    </td>
    
    <td>
      Check for metrics in your backend
    </td>
    
    <td>
      Look for <code>
        rabbitmq.queue.messages
      </code>
      
       metrics
    </td>
  </tr>
</tbody>
</table>

## What is RabbitMQ?

RabbitMQ is an open-source message broker that implements the Advanced Message Queuing Protocol (AMQP). It acts as an intermediary for messaging, allowing applications to communicate by sending and receiving messages through queues, exchanges, and bindings.

Key features include:

- Multiple messaging patterns: point-to-point, publish-subscribe, and request-reply
- Message durability and persistence
- Clustering, federation, and high availability
- Support for quorum queues and streams for high-throughput workloads
- Management HTTP API for monitoring and administration

## What is OpenTelemetry Collector?

[OpenTelemetry Collector](/opentelemetry/collector) is an agent that pulls telemetry data from systems you want to monitor and sends it to your observability backend using the OpenTelemetry protocol (OTLP).

You can use OpenTelemetry Collector to monitor [host metrics](/opentelemetry/collector/host-metrics), [PostgreSQL](/guides/opentelemetry-postgresql), [MySQL](/guides/opentelemetry-mysql), [Redis](/guides/opentelemetry-redis), [Kafka](/guides/opentelemetry-kafka), and more.

## Prerequisites

### Enable RabbitMQ Management Plugin

The OpenTelemetry RabbitMQ receiver requires the management plugin to be enabled, as it collects metrics through the management HTTP API:

```shell
# Enable management plugin
sudo rabbitmq-plugins enable rabbitmq_management

# Verify the plugin is enabled
sudo rabbitmq-plugins list
```

The management interface will be available at `http://localhost:15672` by default.

### Verify Management API Access

Test that the management API is accessible before configuring the Collector:

```shell
# Test API endpoint
curl -u guest:guest http://localhost:15672/api/overview

# Should return JSON with RabbitMQ overview information
```

### Create a Monitoring User

For production environments, create a dedicated monitoring user instead of using the default `guest` account:

```shell
# Create monitoring user
sudo rabbitmqctl add_user otel_monitor secure_password

# Set monitoring tag (required for management API access)
sudo rabbitmqctl set_user_tags otel_monitor monitoring

# Grant read-only permissions
sudo rabbitmqctl set_permissions -p / otel_monitor "" "" ".*"
```

## OpenTelemetry RabbitMQ Receiver

To start monitoring RabbitMQ with OpenTelemetry Collector, configure the RabbitMQ [receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/rabbitmqreceiver/README.md) in `/etc/otelcol-contrib/config.yaml` using your [Uptrace DSN](/get#dsn):

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:
  rabbitmq:
    endpoint: http://localhost:15672
    username: guest
    password: guest
    collection_interval: 10s

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
      receivers: [otlp, rabbitmq]
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

## Configuration Options

The RabbitMQ receiver provides several [configuration options](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/rabbitmqreceiver/README.md#configuration):

<table>
<thead>
  <tr>
    <th>
      Option
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
      <code>
        http://localhost:15672
      </code>
    </td>
    
    <td>
      RabbitMQ management API URL
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        username
      </code>
    </td>
    
    <td>
      (required)
    </td>
    
    <td>
      Management API username
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        password
      </code>
    </td>
    
    <td>
      (required)
    </td>
    
    <td>
      Management API password
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        collection_interval
      </code>
    </td>
    
    <td>
      <code>
        10s
      </code>
    </td>
    
    <td>
      How often to scrape metrics
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        timeout
      </code>
    </td>
    
    <td>
      <code>
        10s
      </code>
    </td>
    
    <td>
      HTTP request timeout
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        tls
      </code>
    </td>
    
    <td>
      (none)
    </td>
    
    <td>
      TLS configuration for HTTPS endpoints
    </td>
  </tr>
</tbody>
</table>

### Basic Configuration

```yaml
receivers:
  rabbitmq:
    endpoint: http://localhost:15672
    username: otel_monitor
    password: secure_password
    collection_interval: 30s
```

### Advanced Configuration with TLS

```yaml
receivers:
  rabbitmq:
    endpoint: https://rabbitmq.example.com:15671
    username: otel_monitor
    password: secure_password
    collection_interval: 10s
    tls:
      insecure: false
      ca_file: /path/to/ca.crt
      cert_file: /path/to/client.crt
      key_file: /path/to/client.key
    timeout: 60s
```

## Available Metrics

The RabbitMQ receiver collects metrics covering queues, exchanges, nodes, and connections:

### Queue Metrics

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
        rabbitmq.queue.messages
      </code>
    </td>
    
    <td>
      Total messages in queue
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.queue.messages.ready
      </code>
    </td>
    
    <td>
      Messages ready for delivery
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.queue.messages.unacknowledged
      </code>
    </td>
    
    <td>
      Messages waiting for acknowledgment
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.queue.consumers
      </code>
    </td>
    
    <td>
      Number of consumers per queue
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.queue.message.current
      </code>
    </td>
    
    <td>
      Current message count
    </td>
  </tr>
</tbody>
</table>

### Exchange Metrics

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
        rabbitmq.exchange.messages.published
      </code>
    </td>
    
    <td>
      Messages published to exchange
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.exchange.messages.confirmed
      </code>
    </td>
    
    <td>
      Confirmed published messages
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.exchange.messages.returned
      </code>
    </td>
    
    <td>
      Returned messages
    </td>
  </tr>
</tbody>
</table>

### Node Metrics

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
        rabbitmq.node.memory.used
      </code>
    </td>
    
    <td>
      Memory usage by node
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.node.disk.free
      </code>
    </td>
    
    <td>
      Available disk space
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.node.fd.used
      </code>
    </td>
    
    <td>
      File descriptors in use
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.node.sockets.used
      </code>
    </td>
    
    <td>
      Network sockets in use
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.node.process.count
      </code>
    </td>
    
    <td>
      Running Erlang processes
    </td>
  </tr>
</tbody>
</table>

### Connection Metrics

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
        rabbitmq.connection.count
      </code>
    </td>
    
    <td>
      Total active connections
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        rabbitmq.channel.count
      </code>
    </td>
    
    <td>
      Total active channels
    </td>
  </tr>
</tbody>
</table>

## Docker Compose Example

Run RabbitMQ and the OpenTelemetry Collector together for quick setup:

```yaml
services:
  rabbitmq:
    image: rabbitmq:3-management
    container_name: rabbitmq
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      RABBITMQ_DEFAULT_USER: admin
      RABBITMQ_DEFAULT_PASS: admin
    networks:
      - monitoring

  otel-collector:
    image: otel/opentelemetry-collector-contrib:0.145.0
    container_name: otel-collector
    command: ["--config=/etc/otelcol-contrib/config.yaml"]
    volumes:
      - ./config.yaml:/etc/otelcol-contrib/config.yaml
    depends_on:
      - rabbitmq
    networks:
      - monitoring

networks:
  monitoring:
    driver: bridge
```

With the corresponding `config.yaml`:

```yaml
receivers:
  rabbitmq:
    endpoint: http://rabbitmq:15672
    username: admin
    password: admin
    collection_interval: 10s

exporters:
  otlp:
    endpoint: api.uptrace.dev:4317
    headers: { 'uptrace-dsn': '<FIXME>' }

processors:
  batch:
    timeout: 10s

service:
  pipelines:
    metrics:
      receivers: [rabbitmq]
      processors: [batch]
      exporters: [otlp]
```

## Dashboard Visualization

When telemetry data reaches Uptrace, it automatically generates a RabbitMQ dashboard from a pre-defined template. You can also create custom dashboards to visualize:

- **Queue Health**: Message counts, consumer activity, and queue depths
- **Throughput Metrics**: Message publish/consume rates and acknowledgment patterns
- **Resource Utilization**: Memory usage, disk space, and connection counts
- **Node Status**: Cluster health and individual node performance
- **Exchange Activity**: Message routing and delivery statistics

For other backends, see [OpenTelemetry backend comparison](/opentelemetry/backend-comparison).

## Alerting

Set up alerts for common RabbitMQ issues:

- **Queue depth growing**: `rabbitmq.queue.messages > 10000` for 5 minutes â consumers can't keep up
- **No consumers**: `rabbitmq.queue.consumers == 0` â messages accumulating with no processing
- **Unacknowledged messages**: `rabbitmq.queue.messages.unacknowledged > 1000` â consumers may be stuck
- **Memory pressure**: `rabbitmq.node.memory.used` approaching configured limit â risk of flow control
- **Disk space low**: `rabbitmq.node.disk.free` below threshold â risk of blocking publishers

## Troubleshooting

### Common Issues

<table>
<thead>
  <tr>
    <th>
      Problem
    </th>
    
    <th>
      Likely Cause
    </th>
    
    <th>
      Solution
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Connection refused
    </td>
    
    <td>
      Management plugin not enabled
    </td>
    
    <td>
      Run <code>
        rabbitmq-plugins enable rabbitmq_management
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Authentication failed
    </td>
    
    <td>
      Wrong credentials or missing permissions
    </td>
    
    <td>
      Verify user has <code>
        monitoring
      </code>
      
       tag
    </td>
  </tr>
  
  <tr>
    <td>
      Missing metrics
    </td>
    
    <td>
      User lacks required tags
    </td>
    
    <td>
      Run <code>
        rabbitmqctl set_user_tags user monitoring
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      High CPU on Collector
    </td>
    
    <td>
      Collection interval too aggressive
    </td>
    
    <td>
      Increase <code>
        collection_interval
      </code>
      
       to 30s or 60s
    </td>
  </tr>
  
  <tr>
    <td>
      Timeout errors
    </td>
    
    <td>
      Large cluster or slow network
    </td>
    
    <td>
      Increase <code>
        timeout
      </code>
      
       value in receiver config
    </td>
  </tr>
</tbody>
</table>

### Debug Configuration

Enable debug logging to troubleshoot collection issues:

```yaml
service:
  telemetry:
    logs:
      level: debug
  pipelines:
    metrics:
      receivers: [rabbitmq]
      processors: [batch]
      exporters: [debug, otlp]  # Add debug exporter to see metrics in logs
```

### Firewall Configuration

Ensure the Collector can access RabbitMQ management port:

```shell
# Allow access to management port (15672)
sudo ufw allow 15672

# Test connectivity from Collector host
curl -u otel_monitor:password http://rabbitmq-server:15672/api/overview
```

## Security Best Practices

For production environments:

```shell
# Remove default guest user
sudo rabbitmqctl delete_user guest

# Create dedicated monitoring user with minimal permissions
sudo rabbitmqctl add_user otel_monitor $(openssl rand -base64 32)
sudo rabbitmqctl set_user_tags otel_monitor monitoring
sudo rabbitmqctl set_permissions -p / otel_monitor "" "" ".*"
```

Use TLS when the Collector and RabbitMQ are on different hosts:

```yaml
receivers:
  rabbitmq:
    endpoint: https://rabbitmq.example.com:15671
    tls:
      insecure: false
      ca_file: /etc/ssl/certs/rabbitmq-ca.crt
      cert_file: /etc/ssl/certs/client.crt
      key_file: /etc/ssl/private/client.key
```

## Performance Optimization

### Collection Interval Tuning

Adjust collection frequency based on your monitoring needs:

```yaml
receivers:
  rabbitmq:
    collection_interval: 30s  # Reduce frequency for high-traffic brokers
    timeout: 10s              # Increase timeout for slow responses
```

### Metric Filtering

Filter unnecessary metrics to reduce overhead:

```yaml
processors:
  filter/rabbitmq:
    metrics:
      exclude:
        match_type: regexp
        metric_names:
          - "rabbitmq\\.queue\\.messages\\..*"  # Exclude specific queue metrics if not needed
```

## FAQ

**What RabbitMQ versions are supported?** The receiver works with RabbitMQ 3.8+ and 4.x. It requires the management plugin which is available in all modern RabbitMQ versions.

**Does the receiver support RabbitMQ clusters?** Yes. Point the receiver at any node in the cluster and it will collect metrics for all nodes, queues, and exchanges across the cluster via the management API.

**How is this different from Prometheus scraping?** RabbitMQ also exposes a Prometheus endpoint. The OpenTelemetry receiver collects similar metrics but exports them in OTLP format, allowing you to use any [OTLP-compatible backend](/opentelemetry/backend-comparison) and correlate with traces and logs.

**Can I monitor multiple RabbitMQ clusters?** Yes. Define multiple receiver instances with different names:

```yaml
receivers:
  rabbitmq/cluster1:
    endpoint: http://rabbitmq-cluster1:15672
    username: monitor
    password: pass1
  rabbitmq/cluster2:
    endpoint: http://rabbitmq-cluster2:15672
    username: monitor
    password: pass2
```

**What's the monitoring tag vs administrator tag?** The `monitoring` tag grants read-only access to the management API, which is sufficient for metrics collection. The `administrator` tag grants full access and should not be used for monitoring.

## What's next?

RabbitMQ monitoring provides visibility into message queue performance, consumer lag, and broker health.

Next steps to enhance your infrastructure observability:

- Monitor other messaging systems with [Kafka monitoring](/guides/opentelemetry-kafka)
- Add container monitoring with [Docker](/guides/opentelemetry-docker) instrumentation
- Deploy on Kubernetes with the [OpenTelemetry Kubernetes guide](/get/kubernetes)
- Monitor your databases with [PostgreSQL](/guides/opentelemetry-postgresql) or [MySQL](/guides/opentelemetry-mysql) receivers
- Collect host-level metrics with the [host metrics receiver](/opentelemetry/collector/host-metrics)
- Explore [OpenTelemetry APM](/opentelemetry/apm) for end-to-end application monitoring
