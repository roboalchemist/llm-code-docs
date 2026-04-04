# Source: https://uptrace.dev/raw/guides/opentelemetry-php-fpm.md

# PHP-FPM Monitoring with OpenTelemetry Collector

> Monitor PHP-FPM performance using OpenTelemetry Collector and php-fpm_exporter. Track metrics, analyze performance, and set up alerting for your PHP applications.

To monitor PHP FPM performance, you can use OpenTelemetry Collector to collect metrics and Uptrace to visualize them.

It works like this:

- PHP-FPM exporter provides a Prometheus endpoint with metrics.
- OpenTelemetry Collector scrapes the PHP-FPM Prometheus endpoint and exports data to Uptrace.
- Uptrace stores and visualizes the metrics it receives from OpenTelemetry Collector.

## Why Monitor PHP-FPM?

PHP-FPM (FastCGI Process Manager) handles PHP requests for your web applications. Monitoring PHP-FPM helps you identify performance bottlenecks, prevent resource exhaustion, and optimize your configuration.

### Key PHP-FPM Metrics

Monitor these metrics to ensure optimal PHP-FPM performance:

- **Active processes** - concurrent PHP requests being processed
- **Idle processes** - available workers ready to handle requests
- **Max children reached** - indicates worker pool exhaustion
- **Listen queue** - pending requests waiting for workers
- **Slow requests** - requests exceeding configured threshold
- **Memory usage** - memory consumption per process

## PHP-FPM exporter

[PHP-FPM Exporter](https://github.com/hipages/php-fpm_exporter) is a Prometheus exporter that allows you to scrape PHP-FPM metrics using Prometheus or OpenTelemetry Collector.

PHP-FPM Exporter collects metrics such as request counts, response times, memory usage, and various other performance-related data from PHP-FPM. These metrics can then be visualized, monitored, and used for alerting in Uptrace.

To retrieve information from PHP-FPM running on `127.0.0.1:9000` with status endpoint being `/status`:

```shell
php-fpm_exporter get --phpfpm.scrape-uri tcp://127.0.0.1:9000/status
```

See [php-fpm_exporter](https://github.com/hipages/php-fpm_exporter) documentation for more details.

## What is OpenTelemetry Collector?

You can deploy [OpenTelemetry Collector](/opentelemetry/collector) as an agent that runs on individual hosts, where it periodically collects and forwards diagnostic information about the running system to various [distributed tracing tools](/tools/distributed-tracing-tools).

OpenTelemetry Collector provides powerful data processing capabilities. It can aggregate, filter, transform, and enrich telemetry data as it flows through the system.

## Scraping PHP FPM metrics

To start monitoring PHP-FPM with OpenTelemetry, you need to configure OpenTelemetry Collector to scrape the PHP-FPM exporter endpoint.

Here is the OpenTelemetry Collector config from [php-fpm](https://github.com/uptrace/uptrace-php/tree/master/example/php-fpm) Docker example:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:
  prometheus/phpfpm:
    config:
      scrape_configs:
        - job_name: php-fpm
          static_configs:
            - targets: [php-fpm-exporter:9253]

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
      receivers: [otlp, prometheus/phpfpm]
      processors: [cumulativetodelta, batch, resourcedetection]
      exporters: [otlp/uptrace]
  telemetry:
    logs:
      level: 'debug'
```

### Available Metrics

php-fpm_exporter exposes these key metrics:

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
        phpfpm_up
      </code>
    </td>
    
    <td>
      PHP-FPM pool status (1=up, 0=down)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        phpfpm_active_processes
      </code>
    </td>
    
    <td>
      Currently processing requests
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        phpfpm_idle_processes
      </code>
    </td>
    
    <td>
      Available workers
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        phpfpm_total_processes
      </code>
    </td>
    
    <td>
      Total worker count
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        phpfpm_max_children_reached
      </code>
    </td>
    
    <td>
      Times max limit reached
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        phpfpm_slow_requests
      </code>
    </td>
    
    <td>
      Slow request count
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        phpfpm_accepted_connections
      </code>
    </td>
    
    <td>
      Total connections
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        phpfpm_listen_queue
      </code>
    </td>
    
    <td>
      Pending requests in queue
    </td>
  </tr>
</tbody>
</table>

Next, use Uptrace or [Grafana Alternatives](/comparisons/grafana-alternatives) to create dashboards and graphs based on the PHP-FPM metrics collected by OpenTelemetry Collector.

## Troubleshooting Common Issues

### Max Children Reached

If `phpfpm_max_children_reached` counter increases, all workers are busy and new requests are queued.

**Fix:** Increase worker pool size in PHP-FPM configuration:

```conf
pm.max_children = 50
pm.start_servers = 10
pm.min_spare_servers = 5
pm.max_spare_servers = 15
```

### High Memory Usage

Monitor `phpfpm_memory_usage` to detect memory leaks or improper configuration.

**Fix:** Restart workers periodically:

```conf
pm.max_requests = 500
```

### Slow Requests

Enable slow request logging to identify performance bottlenecks:

```conf
request_slowlog_timeout = 5s
slowlog = /var/log/php-fpm/slow.log
```

## OpenTelemetry Backend

Once the metrics are collected and exported, you can visualize them using a compatible backend system. For example, you can use Uptrace to create dashboards that display metrics from the OpenTelemetry Collector.

Uptrace is a [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues. For PHP monitoring, compare with [top APM tools](/tools/top-apm-tools) and see the [OpenTelemetry PHP guide](/get/opentelemetry-php).

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## What's next?

By setting up the PHP-FPM Exporter and integrating it with Uptrace, you can gain insights into the performance and health of your PHP-FPM instances and make informed decisions regarding optimizations or troubleshooting.

**Related guides:**

- [OpenTelemetry PHP tracing](/get/opentelemetry-php/tracing) - Instrument PHP applications
- [Laravel monitoring](/guides/opentelemetry-laravel) - Monitor Laravel applications
- [Symfony monitoring](/guides/opentelemetry-symfony) - Symfony observability
- [MySQL monitoring](/guides/opentelemetry-mysql) - Database performance
