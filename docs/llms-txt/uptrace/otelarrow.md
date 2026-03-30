# Source: https://uptrace.dev/raw/ingest/otelarrow.md

# Ingesting telemetry using OTel Arrow Protocol

> Send telemetry to Uptrace using OTel Arrow for up to 50% bandwidth reduction compared to standard OTLP.

OTel Arrow is an extension to OpenTelemetry Protocol (OTLP) that uses [Apache Arrow](https://arrow.apache.org/) columnar format for more efficient data transport. Uptrace accepts data in OTel Arrow format on its default OTLP endpoints without any additional configuration.

## What is OTel Arrow?

OTel Arrow (OpenTelemetry Protocol with Apache Arrow) is a high-performance telemetry transport protocol that converts OpenTelemetry data into Apache Arrow's columnar format. This approach provides significant bandwidth savings while maintaining full compatibility with the OpenTelemetry ecosystem.

The protocol was developed to address the bandwidth costs of large-scale telemetry collection. It is now part of the OpenTelemetry Collector Contrib distribution and is considered production-ready.

### Key benefits

- **50-70% bandwidth reduction** for logs and metrics compared to standard OTLP/gRPC with Zstd compression
- **30% bandwidth reduction** for traces compared to standard OTLP
- **Compression factors of 15x-30x** compared to uncompressed data
- **Zero-copy data exchange** across process boundaries using Arrow IPC
- **Full OTLP compatibility** - can fall back to standard OTLP when needed

### How it works

OTel Arrow achieves its efficiency through several techniques:

1. **Columnar format**: Converts OpenTelemetry data into Apache Arrow record batches, which organize data by columns rather than rows for better compression
2. **Streaming protocol**: Embeds Arrow IPC (Inter-Process Communication) within gRPC streams
3. **Deduplication**: Removes duplicate Resource and Scope values before encoding
4. **Zstd compression**: Applies Zstd compression at both gRPC and Arrow levels

## Production results

OTel Arrow has been running in production at large-scale deployments for over a year, handling 500,000-600,000 spans per second while exporting 250-300 MB/second of compressed data.

Cost analysis shows that while OTel Arrow increases CPU usage, the bandwidth savings more than compensate for it. In cloud environments, the compute cost is substantially less than the bandwidth savings.

## Configuring OTel Arrow exporter

<alert type="warning">

The last OpenTelemetry Collector version compatible with otelarrow is **v0.136.0**. Later versions fail due to a [known issue](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/43872).

</alert>

OTel Arrow is currently only available as an [OpenTelemetry Collector](/opentelemetry/collector) exporter. OpenTelemetry SDKs do not support OTel Arrow directly yet, so you need to send data from your application to the Collector using standard OTLP, and then configure the Collector to export data to Uptrace using OTel Arrow.

To use OTel Arrow with Uptrace, replace the standard `otlp` exporter with `otelarrow` in your OpenTelemetry Collector configuration.

### Cloud

To send data to [Uptrace Cloud](/) using OTel Arrow:

```yaml
processors:
  resourcedetection:
    detectors: [env, system]
  cumulativetodelta:
  batch:
    send_batch_size: 10000
    timeout: 10s

exporters:
  otelarrow/uptrace:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: '<FIXME>'

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otelarrow/uptrace]
    metrics:
      receivers: [otlp]
      processors: [cumulativetodelta, batch, resourcedetection]
      exporters: [otelarrow/uptrace]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otelarrow/uptrace]
```

### Self-hosted

For [self-hosted Uptrace](/get/hosted/install), point the exporter to your Uptrace instance:

```yaml
exporters:
  otelarrow/uptrace:
    endpoint: localhost:14317
    tls:
      insecure: true
    headers:
      uptrace-dsn: 'http://project1_secret_token@localhost:14317/1'
```

## Configuration options

The OTel Arrow exporter includes all standard OTLP exporter options plus Arrow-specific settings:

### Arrow settings

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
        arrow.disabled
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Disable Arrow encoding and use standard OTLP
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        arrow.num_streams
      </code>
    </td>
    
    <td>
      <code>
        max(1, NumCPU/2)
      </code>
    </td>
    
    <td>
      Number of concurrent Arrow streams
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        arrow.max_stream_lifetime
      </code>
    </td>
    
    <td>
      <code>
        30s
      </code>
    </td>
    
    <td>
      Maximum duration for each Arrow stream
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        arrow.prioritizer
      </code>
    </td>
    
    <td>
      <code>
        leastloaded
      </code>
    </td>
    
    <td>
      Load distribution strategy for streams
    </td>
  </tr>
</tbody>
</table>

### Compression settings

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
        compression
      </code>
    </td>
    
    <td>
      <code>
        zstd
      </code>
    </td>
    
    <td>
      gRPC-level compression (none, gzip, zstd, snappy)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        arrow.zstd
      </code>
    </td>
    
    <td>
      enabled
    </td>
    
    <td>
      Arrow-level Zstd compression
    </td>
  </tr>
</tbody>
</table>

### Example with tuned settings

```yaml
exporters:
  otelarrow/uptrace:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: '<FIXME>'
    compression: zstd
    arrow:
      num_streams: 4
      max_stream_lifetime: 60s
```

Longer stream lifetimes and larger batch sizes improve compression but require more memory. Tune these settings based on your workload and available resources.

## Falling back to OTLP

If you need to disable Arrow encoding and use standard OTLP, set `arrow.disabled: true`:

```yaml
exporters:
  otelarrow/uptrace:
    endpoint: api.uptrace.dev:4317
    headers:
      uptrace-dsn: '<FIXME>'
    arrow:
      disabled: true
```

This is useful for debugging or when Arrow encoding causes issues.

## When to use OTel Arrow

OTel Arrow is most beneficial when:

- **High telemetry volume**: The bandwidth savings become significant at scale
- **Cross-region or cloud egress**: Reducing data transfer saves on network costs
- **Constrained network bandwidth**: Arrow compression helps in bandwidth-limited environments

For small deployments with low telemetry volume, standard OTLP may be simpler and sufficient.

## What's next?

- Learn about [OpenTelemetry Collector](/opentelemetry/collector) configuration
- Explore [data ingestion methods](/ingest) supported by Uptrace
- Configure [host metrics](/opentelemetry/collector/host-metrics) collection
