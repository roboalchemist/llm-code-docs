# Source: https://uptrace.dev/raw/get/opentelemetry-swift/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-rust/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-ruby/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-python/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-php/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-js/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-java/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-go/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-erlang/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-dotnet/metrics.md

# Source: https://uptrace.dev/raw/get/opentelemetry-cpp/metrics.md

# Source: https://uptrace.dev/raw/features/querying/metrics.md

# Querying Metrics

> Write PromQL inspired metric queries with aliases, joins, and expressions that feed dashboards built in the UI or YAML.

<alert type="info">

To learn about metrics, see [OpenTelemetry Metrics](/opentelemetry/metrics) documentation.

</alert>

Uptrace provides a powerful query language that supports joining, grouping, and aggregating multiple metrics in a single query. The Uptrace query language is backwards compatible with Prometheus (PromQL), so you can use your existing PromQL queries with Uptrace.

If you're already familiar with PromQL, read [PromQL compatibility](promql-compat) guide to learn more.

## Writing queries

Uptrace allows you to create dashboards using UI or YAML configuration files. This documentation uses the more compact YAML format, but you can achieve the same with the UI.

YAML:

```yaml
metrics:
  - postgresql_commits as $commits

query:
  - sum($commits)
```

UI:

![Grid item form](/features/querying-metrics/grid-item-form.png)

## Aliases

Because metric names can be quite long, Uptrace requires you to provide a short metric alias that must start with the dollar sign:

```yaml
metrics:
  # metric aliases always start with the dollar sign
  - system_filesystem_usage as $fs_usage
  - system_network_packets as $packets
```

You must then use the alias instead of the metric name when writing queries:

```yaml
query:
  - sum($fs_usage)
```

Uptrace also allows to specify an alias for expressions:

```yaml
query:
  - $fs_usage{state="used"} as used_space
  - $fs_usage{host_name='host1', device='/dev/sdd1'} as host1_sdd1
```

You can then reference the expression using the alias:

```yaml
metrics:
  - service_cache_redis as $redis
query:
  - $redis{type="hits"} as hits
  - $redis{type="misses"} as misses
  - hits / (hits + misses) as hit_rate
```

## Grouping

Uptrace allows to customize grouping on a function level:

```shell
sum($metric) by (attr1, attr2)
avg(sum($metric) by (attr1, attr2)) by (attr1)
```

<partial path="querying-metrics">



</partial>

## Instruments

OpenTelemetry offers various [instruments](/opentelemetry/metrics#instruments), each with its own set of aggregate functions:

<table>
<thead>
  <tr>
    <th>
      Instrument Name
    </th>
    
    <th>
      Timeseries kind
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <a href="/opentelemetry/metrics#counter">
        Counter
      </a>
      
      , <a href="/opentelemetry/metrics#counterobserver">
        CounterObserver
      </a>
    </td>
    
    <td>
      <a href="#counter">
        Counter
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/opentelemetry/metrics#updowncounter">
        UpDownCounter
      </a>
      
      , <a href="/opentelemetry/metrics#updowncounterobserver">
        UpDownCounterObserver
      </a>
    </td>
    
    <td>
      <a href="#additive">
        Additive
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/opentelemetry/metrics#gaugeobserver">
        GaugeObserver
      </a>
    </td>
    
    <td>
      <a href="#gauge">
        Gauge
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/opentelemetry/metrics#histogram">
        Histogram
      </a>
    </td>
    
    <td>
      <a href="#histogram">
        Histogram
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="/ingest/cloudwatch#metrics">
        AWS CloudWatch
      </a>
    </td>
    
    <td>
      <a href="#summary">
        Summary
      </a>
    </td>
  </tr>
</tbody>
</table>

### Counter

Counter is a timeseries kind that measures additive non-decreasing values, for example, the **total** number of:

- processed requests
- received bytes
- disk reads

Uptrace supports the following functions to aggregate `counter` timeseries:

<table>
<thead>
  <tr>
    <th>
      Expression
    </th>
    
    <th>
      Result timeseries
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        sum($metric)
      </code>
    </td>
    
    <td>
      Sum of timeseries
    </td>
  </tr>
</tbody>
</table>

### Gauge

Gauge is a timeseries kind that measures non-additive values for which sum does not produce a meaningful correct result, for example:

- error rate
- memory utilization
- cache hit rate

Uptrace supports the following functions to aggregate `gauge` timeseries:

<table>
<thead>
  <tr>
    <th>
      Expression
    </th>
    
    <th>
      Result timeseries
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        avg($metric)
      </code>
    </td>
    
    <td>
      Avg of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        min($metric)
      </code>
    </td>
    
    <td>
      Min of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        max($metric)
      </code>
    </td>
    
    <td>
      Max of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        sum($metric)
      </code>
    </td>
    
    <td>
      Sum of timeseries
    </td>
  </tr>
</tbody>
</table>

* Note that the `sum` functions should not be normally used with this instrument and was added only for compatibility with Prometheus and AWS metrics.

### Additive

Additive is a timeseries kind which measures additive values that increase or decrease with time, for example, the number of:

- active requests
- open connections
- memory in use (megabytes)

Uptrace supports the following functions to aggregate `additive` timeseries:

<table>
<thead>
  <tr>
    <th>
      Expression
    </th>
    
    <th>
      Result timeseries
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        sum($metric)
      </code>
    </td>
    
    <td>
      Sum of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        avg($metric)
      </code>
    </td>
    
    <td>
      Avg of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        min($metric)
      </code>
    </td>
    
    <td>
      Min of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        max($metric)
      </code>
    </td>
    
    <td>
      Max of timeseries
    </td>
  </tr>
</tbody>
</table>

### Histogram

Histogram is a timeseries kind that contains a histogram from recorded values, for example:

- request latency
- request size

Uptrace supports the following functions to aggregate `histogram` timeseries:

<table>
<thead>
  <tr>
    <th>
      Expression
    </th>
    
    <th>
      Result timeseries
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        histogram_count($metric)
      </code>
    </td>
    
    <td>
      Number of observed values in timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        p50($metric)
      </code>
    </td>
    
    <td>
      P50 of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        p75($metric)
      </code>
    </td>
    
    <td>
      P75 of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        p90($metric)
      </code>
    </td>
    
    <td>
      P90 of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        p95($metric)
      </code>
    </td>
    
    <td>
      P95 of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        p99($metric)
      </code>
    </td>
    
    <td>
      P99 of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        histogram_quantile(0.5, $metric)
      </code>
    </td>
    
    <td>
      Same as <code>
        p50($metric)
      </code>
      
       (PromQL-compatible)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        avg($metric)
      </code>
    </td>
    
    <td>
      <code>
        sum($metric) / histogram_count($metric)
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        min($metric)
      </code>
    </td>
    
    <td>
      Min observed value in the histogram
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        max($metric)
      </code>
    </td>
    
    <td>
      Max observed value in the histogram
    </td>
  </tr>
</tbody>
</table>

### Summary

Sum is a timeseries kind that exists for compatibility with Prometheus and AWS Cloud Watch. It stores the `min`, `max`, `sum`, and `count` aggregates of observed values.

<table>
<thead>
  <tr>
    <th>
      Expression
    </th>
    
    <th>
      Result timeseries
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        sum($metric)
      </code>
    </td>
    
    <td>
      Sum of timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        histogram_count($metric)
      </code>
    </td>
    
    <td>
      Number of observed values in timeseries
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        avg($metric)
      </code>
    </td>
    
    <td>
      <code>
        sum($metric) / count($metric)
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        min($metric)
      </code>
    </td>
    
    <td>
      Min observed value
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        max($metric)
      </code>
    </td>
    
    <td>
      Max observed value
    </td>
  </tr>
</tbody>
</table>

## Misc

### What are timeseries?

A timeseries is a metric with an unique set of attributes, for example, each host has a separate timeseries for the same metric name:

```yaml
# metric_name{ attr1, attr2... }
system_filesystem_usage{host_name='host1'} # timeseries 1
system_filesystem_usage{host_name='host2'} # timeseries 2
```

You can add more attributes to create more detailed and rich timeseries, for example, you can use `state` attribute to report the number of free and used bytes in a filesystem:

```yaml
system_filesystem_usage{host_name='host1', state='free'} # timeseries 1
system_filesystem_usage{host_name='host1', state='used'} # timeseries 2

system_filesystem_usage{host_name='host2', state='free'} # timeseries 3
system_filesystem_usage{host_name='host2', state='used'} # timeseries 4
```

With just 2 attributes, you can write a number of useful queries:

```yaml
# the filesystem size (free+used bytes) on each host
query:
  - sum($fs_usage) group by host_name

# the number of free bytes on each host
query:
  - sum($fs_usage{state='free'}) as free group by host_name

# fs utilization on each host
query:
  - sum($fs_usage{state='used'}) / sum($fs_usage) as fs_util group by host_name

# the size of your dataset on all hosts
query:
  - sum($fs_usage{state='used'}) as dataset_size
```

### Binary operator precedence

The following list shows the precedence of binary operators in Uptrace, from highest to lowest.

- `^`
- `*`, `/`, `%`
- `+`, `-`
- `==`, `!=`, `<=`, `<`, `>=`, `>`
- `and`, `unless`
- `or`

Operators on the same precedence level are left-associative. For example, `2 * 3 % 2` is equivalent to `(2 * 3) % 2`.

## See also

- [OpenTelemetry Metrics](/opentelemetry/metrics)
- [OpenTelemetry PostgreSQL metrics](/guides/opentelemetry-postgresql)
- [OpenTelemetry Redis metrics](/guides/opentelemetry-redis)
