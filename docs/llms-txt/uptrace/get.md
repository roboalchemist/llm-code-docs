# Source: https://uptrace.dev/raw/get.md

# Getting started with Uptrace

> Learn how to connect OpenTelemetry signals to Uptrace, read your DSN, and monitor infrastructure, Kubernetes, and logs from one place.

Uptrace is an open-source observability and APM platform that ingests distributed traces, metrics, and logs via [OpenTelemetry](/opentelemetry). This page explains how to provision an Uptrace project, find your DSN, and begin streaming telemetry from your services.

## Quick start

1. **Provision Uptrace**. Either [sign up for Uptrace Cloud](https://app.uptrace.dev/join) or [self-host Uptrace](/get/hosted/install). Both deployment options expose a project [DSN](#dsn) such as `https://secret@api.uptrace.dev?grpc=4317`.
2. **Configure OpenTelemetry**. Paste the DSN into the OpenTelemetry SDK for your language (see the distributions below) and start the application. Uptrace immediately begins receiving spans, metrics, and logs.

<home-distro-list>



</home-distro-list>

Questions? Reach the team on [Telegram](https://t.me/uptrace), [Slack](https://join.slack.com/t/uptracedev/shared_invite/zt-3e35d4b0m-zfAew95ymE5Fv31LwvyuoQ), or [GitHub Discussions](https://github.com/uptrace/uptrace/discussions).

## DSN

Every project has a DSN (Data Source Name) that packages the Uptrace endpoint and credentials into one connection string. You can reveal the DSN under **Project Settings â Connection details**.

![Uptrace DSN](/get/dsn.png)

### Anatomy of a DSN

Example: `http://project1_secret@localhost:14318?grpc=14317`

- `http` â Transport protocol. Use `https` when TLS is enabled.
- `localhost:14318` â Uptrace HTTP endpoint. Cloud projects use `api.uptrace.dev`.
- `project1_secret` â Write-only token that authenticates the project.
- `?grpc=14317` â Optional gRPC endpoint for native OpenTelemetry exporters.

Share the DSN only with collectors or services that must send data; it is not required to view your dashboards.

### Ports

Uptrace accepts data via OTLP/gRPC and OTLP/HTTP on separate ports:

<table>
<thead>
  <tr>
    <th>
      Protocol
    </th>
    
    <th>
      <a href="/pricing">
        Cloud
      </a>
    </th>
    
    <th>
      <a href="/get/hosted/config">
        Self-hosted
      </a>
      
       (default)
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      OTLP/gRPC
    </td>
    
    <td>
      <code>
        api.uptrace.dev:4317
      </code>
    </td>
    
    <td>
      <code>
        :4317
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      OTLP/HTTP
    </td>
    
    <td>
      <code>
        api.uptrace.dev:443
      </code>
    </td>
    
    <td>
      <code>
        :80
      </code>
    </td>
  </tr>
</tbody>
</table>

Most OpenTelemetry SDKs default to gRPC. Use HTTP when gRPC is blocked by firewalls or proxies.

Self-hosted ports are configured in `uptrace.yml` via `listen.grpc.addr` and `listen.http.addr`. You can also use `site.url` and `site.ingest_url` to customize DSN host.

## Monitoring capabilities

### Infrastructure

- **OpenTelemetry Collector** gathers host metrics, databases, and middleware signals before forwarding them to Uptrace.
- **Prometheus** scrapes metrics and exports them directly to Uptrace.
- **AWS** users can stream [CloudWatch Metrics](/ingest/cloudwatch#cloudwatch-metrics) for EC2, RDS, and other managed services.

### Kubernetes

Deploy the OpenTelemetry Collector as a DaemonSet or use the Operator to scrape kubelet, API server, and pod-level metrics. Enrich traces with `k8s.*` attributes, then forward the data via your DSN. Follow the [Kubernetes monitoring guide](/get/kubernetes) for Helm steps, RBAC rules, and sampling advice.

### Logs

- **Vector** provides high-throughput log shipping with filtering and enrichment.
- **Fluent Bit** offers a lightweight forwarder for containers and edge nodes.
- **AWS** environments can ingest [CloudWatch Logs](/ingest/cloudwatch#cloudwatch-logs) for centralized searching alongside traces.

Correlate logs with spans to jump directly from an error message to the distributed trace that produced it.

## Troubleshooting

### Data is missing

1. Confirm the [DSN](#dsn) matches the project and environment you are instrumenting.
2. Validate network routes between your service and the Uptrace endpoint (try `curl` against the DSN host).
3. Ensure the OpenTelemetry SDK initializes before your application starts handling requests.
4. Inspect application logs for exporter failures or authentication errors.
5. Run a minimal sample app to isolate whether the issue is in instrumentation or platform networking.

### High resource usage

1. Lower the [sampling rate](/opentelemetry/sampling) to reduce span volume.
2. Tune exporter batch sizes, timeouts, and concurrency.
3. Audit custom instrumentation for expensive synchronous work.
4. Use system monitors to confirm whether pressure comes from CPU, memory, or I/O.

### Slow queries in the UI

1. Simplify filters or [reshape the query](/features/querying/spans#performance) to scan less data.
2. Limit the time range or select a specific service/environment tag.
3. Verify ClickHouse configuration and retention policies for the dataset backing your project.
4. Rebuild indexes for frequently queried columns if you self-host ClickHouse.

## Next steps

1. Explore dashboards, service maps, error reports, and span tables.
2. Define alerts for latency, error rate, or infrastructure saturation.
3. Customize dashboards for specific teams or services.
4. Integrate Uptrace checks into CI/CD so every release is covered by tracing and metrics.
