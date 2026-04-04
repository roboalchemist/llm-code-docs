# Source: https://uptrace.dev/raw/features/querying/promql-compat.md

# PromQL compatibility

> See how Uptrace extends PromQL, which functions are supported, and how to adapt Prometheus queries or Grafana dashboards.

## Introduction

Uptrace aims to be compatible with the Prometheus query language while extending it in a meaningful way. Most Prometheus queries can be used in Uptrace with minimal modifications, for example, the following Prometheus queries are also valid in Uptrace:

- `$metric_name{foo="xxx",bar~"yyy"}`
- `increase($metric_name)` and `delta($metric_name)`
- `rate($metric_name[5m])` and `irate($metric_name[5m])`
- `avg_over_time($go_goroutines[5m])`
- `avg by (foo)(sum by(foo, bar)($metric_name))`
- `$metric_name offset 1w`
- Math between series with automatic many-to-one/one-to-many vector matching, for example, `sum($mem by (type)) / sum($mem) as mem`.

But there are also some differences between the systems that don't allow you to just copy and paste queries from Prometheus. To ease the migration, you can use Uptrace as a [Prometheus data source in Grafana](/features/grafana#prometheus-metrics), which is 100% compatible with the original Prometheus and allows you to use existing Grafana dashboards.

## Aliases

Because metric names can be quite long, Uptrace requires you to provide a short metric alias that starts with the dollar sign:

```yaml
metrics:
  - node_memory_MemFree_bytes as $mem_free
  - node_memory_Cached_bytes as $cached
```

Such aliases will be used as the resulting timeseries names when querying metrics:

```yaml
query:
  - $mem_free
  - $cached
  - $mem_free + $cached
```

Uptrace also allows to explicitly specify aliases for expressions:

```shell
$mem_free + $cached as total_mem
```

Because Uptrace queries can contain multiple expressions separated with the `|`, you can reference other expressions using their aliases:

```shell
$mem_free + $cached as total_mem | 1 - ($mem_free / total_mem) as mem_utilization
```

## Grouping

Just like Prometheus, Uptrace allows to customize grouping, for example, the following queries return the same result in Uptrace and Prometheus:

```shell
sum by (cpu, mode)(node_cpu_seconds_total)
sum(node_cpu_seconds_total) by (cpu, mode)

avg by (cpu)(sum by (cpu, mode)(node_cpu_seconds_total))
avg(sum(node_cpu_seconds_total) by (cpu, mode)) by (cpu)
```

<partial path="querying-metrics">



</partial>

## Rate interval

Uptrace automatically picks and applies a suitable `$__rate_interval` just like Grafana does:

```shell
# Grafana and Prometheus
irate(node_cpu_seconds_total[$__rate_interval])

# Uptrace
irate(node_cpu_seconds_total)
```

You can specify the lookbehind window in square brackets, e.g. `irate($metric[5i])` where `i` is equal to the current **i**nterval. When omitted, the default lookbehind window is `10i`.

## Range vs instant vectors

Because Uptrace does not distinguish between range and instant vectors, you should omit the lookbehind window and let Uptrace pick a default for you:

```shell
# Omit the window by default.
irate(node_cpu_seconds_total)

# Only specify it when needed.
max_over_time(process_resident_memory_bytes[1d])
```
