# Source: https://uptrace.dev/raw/ingest.md

# Supported data ingestion methods

> Overview of every supported ingestion path including OpenTelemetry SDKs, Collector, Prometheus, CloudWatch, and log forwarders.

Uptrace supports multiple ingestion methods to collect traces, metrics, and logs from your applications and infrastructure. This guide helps you choose the right approach for your use case.

## Quick decision guide

**Starting fresh with observability?**<br />


Use the [OpenTelemetry SDK](/ingest/opentelemetry) for your programming language. It provides traces, metrics, and logs with full control over instrumentation.

**Need zero-code instrumentation?**<br />


Use [OpenTelemetry eBPF](/ingest/ebpf) to automatically capture HTTP, gRPC, SQL, and other traffic without code changes.

**Already using Prometheus or Grafana?**<br />


Use [Prometheus remote write](/ingest/prometheus) to forward metrics while keeping PromQL compatibility.

**Collecting infrastructure metrics?**<br />


Use the [OpenTelemetry Collector](/ingest/collector) to monitor host metrics, databases, and other systems.

**Forwarding logs from files or systems?**<br />


Use [Vector](/ingest/logs/vector) or [FluentBit](/ingest/logs/fluentbit) for high-performance log collection.

**Migrating from Sentry?**<br />


Use the [Sentry SDK](/ingest/sentry) integration to send error tracking data to Uptrace.

---

## OpenTelemetry native

These methods use OpenTelemetry Protocol (OTLP) natively and provide the most complete observability.

<table>
<thead>
  <tr>
    <th>
      Method
    </th>
    
    <th>
      Signals
    </th>
    
    <th>
      Best for
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/ingest/opentelemetry">
        OpenTelemetry SDK
      </a>
    </td>
    
    <td>
      Traces, Metrics, Logs
    </td>
    
    <td>
      Applications with code access. Configure SDKs for Go, Python, Java, JavaScript, Ruby, PHP, .NET, Rust, and more.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/collector">
        OpenTelemetry Collector
      </a>
    </td>
    
    <td>
      Traces, Metrics, Logs
    </td>
    
    <td>
      Infrastructure monitoring, data transformation, and routing. Acts as a central hub for telemetry.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/otelarrow">
        OTel Arrow
      </a>
    </td>
    
    <td>
      Traces, Metrics, Logs
    </td>
    
    <td>
      High-volume deployments. Uses Apache Arrow for 50-70% bandwidth reduction compared to standard OTLP.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/ebpf">
        OpenTelemetry eBPF
      </a>
    </td>
    
    <td>
      Traces, Metrics
    </td>
    
    <td>
      Zero-code instrumentation. Captures HTTP, gRPC, SQL at the kernel level for any language.
    </td>
  </tr>
</tbody>
</table>

## Metrics collection

These methods focus on collecting metrics from various sources.

<table>
<thead>
  <tr>
    <th>
      Method
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/ingest/prometheus">
        Prometheus
      </a>
    </td>
    
    <td>
      Forward Prometheus metrics via remote write or Collector receivers. Keeps PromQL queries compatible.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/cloudwatch">
        AWS CloudWatch
      </a>
    </td>
    
    <td>
      Ship AWS CloudWatch metrics and logs via Data Firehose or YACE exporter.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/telegraf">
        Telegraf
      </a>
    </td>
    
    <td>
      Output Telegraf metrics through the OpenTelemetry plugin.
    </td>
  </tr>
</tbody>
</table>

## Log forwarding

These methods specialize in collecting and forwarding logs to Uptrace.

<table>
<thead>
  <tr>
    <th>
      Method
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/ingest/logs/vector">
        Vector
      </a>
    </td>
    
    <td>
      High-performance log collection with VRL transforms. Blazingly fast and memory efficient.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/logs/fluentbit">
        FluentBit
      </a>
    </td>
    
    <td>
      Lightweight log processor with OpenTelemetry output. Great for containerized environments.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/logs/loki">
        Loki
      </a>
    </td>
    
    <td>
      Bridge Promtail or Grafana Agent logs via the Collector's Loki receiver.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/logs/heroku">
        Heroku
      </a>
    </td>
    
    <td>
      Collect Heroku platform logs using Logplex and Vector.
    </td>
  </tr>
</tbody>
</table>

## Error tracking and legacy protocols

<table>
<thead>
  <tr>
    <th>
      Method
    </th>
    
    <th>
      Signals
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/ingest/sentry">
        Sentry SDK
      </a>
    </td>
    
    <td>
      Traces, Errors
    </td>
    
    <td>
      Use existing Sentry SDKs with Uptrace. Good for JavaScript browser apps and error tracking.
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/legacy/jaeger">
        Jaeger
      </a>
    </td>
    
    <td>
      Traces
    </td>
    
    <td>
      Accept spans from existing Jaeger agents via Collector receiver.
    </td>
  </tr>
</tbody>
</table>

---

## Summary table

<table>
<thead>
  <tr>
    <th>
      Method
    </th>
    
    <th align="center">
      Traces
    </th>
    
    <th align="center">
      Metrics
    </th>
    
    <th align="center">
      Logs
    </th>
    
    <th align="center">
      Code changes
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/ingest/opentelemetry">
        OpenTelemetry SDK
      </a>
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      Required
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/collector">
        OpenTelemetry Collector
      </a>
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/otelarrow">
        OTel Arrow
      </a>
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/ebpf">
        OpenTelemetry eBPF
      </a>
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/prometheus">
        Prometheus
      </a>
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/cloudwatch">
        AWS CloudWatch
      </a>
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/telegraf">
        Telegraf
      </a>
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/logs/vector">
        Vector
      </a>
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/logs/fluentbit">
        FluentBit
      </a>
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/logs/loki">
        Loki
      </a>
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/logs/heroku">
        Heroku
      </a>
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/sentry">
        Sentry SDK
      </a>
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      Minimal
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/legacy/jaeger">
        Jaeger
      </a>
    </td>
    
    <td align="center">
      â
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      
    </td>
    
    <td align="center">
      None
    </td>
  </tr>
</tbody>
</table>
