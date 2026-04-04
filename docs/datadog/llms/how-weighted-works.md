# Source: https://docs.datadoghq.com/dashboards/guide/how-weighted-works.md

---
title: How does weighted() work?
description: >-
  Understand how the weighted() function prevents artificial spikes when summing
  gauge metrics with transient tags.
breadcrumbs: Docs > Dashboards > Graphing Guides > How does weighted() work?
---

# How does weighted() work?

Every metrics query has a standard order of evaluation (see the [Anatomy of a query](https://docs.datadoghq.com/metrics/#anatomy-of-a-metric-query) for a quick review). For example, the following query is calculated as follows: `sum:kubernetes.cpu.requests{*} by {kube_container_name}.rollup(avg, 10)`

1. Time aggregation â Sum the values for each timeseries (defined by a unique tag value combination) in time for each 10s rollup time interval. The number of unique tag value combinations is determined by the most volatile / high granularity tag, let's say `container_id`, on this metric.
1. Then, per `kube_container_name` (space aggregation), take the sum of all averaged values as a single representative value. The summed values for each `kube_container_name` is dependent upon the number of unique `container_id`s there are for each rollup interval.

The `weighted()` function accounts for the short lifespan of the `container_id` tag values when summing by `kube_container_name` for this gauge metric.

#### Example{% #example %}

Consider this query with the following assumptions:`sum:kubernetes_state.pod.uptime{*} by {version}.rollup(avg, 10)`

- The gauge metric's submission interval is defined at 10 seconds.
- A datapoint is graphed every 60 seconds in time.
- There is a Kubernetes pod with 2 versions at any given time. Each version is labeled with an app and there is only ever 1 version per app.

The raw data over 60 seconds could resemble:

| Time                 | 0s  | 10s | 20s | 30s | 40s | 50s |
| -------------------- | --- | --- | --- | --- | --- | --- |
| `app:a`, `version:1` | 12  | NAN | NAN | NAN | NAN | NAN |
| `app:b`, `version:1` | NAN | 12  | 12  | 12  | NAN | NAN |
| `app:c`, `version:1` | NAN | NAN | NAN | NAN | 12  | 12  |
| `app:d`, `version:2` | 12  | NAN | NAN | NAN | NAN | NAN |
| `app:e`, `version:2` | NAN | 16  | 16  | 16  | NAN | NAN |
| `app:f`, `version:2` | NAN | NAN | NAN | NAN | 18  | 18  |

1. *Time Aggregation â Rolling up data* With time aggregation, we're rolling up data either `avg` (without weighted) or the proposed `weighted` average:

| Time aggregation     | .rollup(avg) | With .weighted() |
| -------------------- | ------------ | ---------------- |
| `app:a`, `version:1` | 12           | 2.0              |
| `app:b`, `version:1` | 12           | 6.0              |
| `app:c`, `version:1` | 12           | 4.0              |
| `app:d`, `version:2` | 12           | 2.0              |
| `app:e`, `version:2` | 16           | 8.0              |
| `app:f`, `version:2` | 18           | 6.0              |

1. *Space Aggregation* Finally, the metric is aggregated by version to get the final values below:

| Space aggregation by version | .rollup(avg) | With .weighted() |
| ---------------------------- | ------------ | ---------------- |
| `version:1`                  | 36           | 12               |
| `version:2`                  | 46           | 16               |

The `weighted()` function remedies any inconsistent behavior with short-lived tags by weighing the values against their submission rate

## Further reading{% #further-reading %}

- [Smoothing](https://docs.datadoghq.com/dashboards/functions/smoothing)
