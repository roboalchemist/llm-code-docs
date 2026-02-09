# Source: https://docs.datadoghq.com/dashboards/functions/count.md

---
title: Count
description: >-
  Count non-zero and non-null metric values for grouped queries and time series
  analysis.
breadcrumbs: Docs > Dashboards > Functions > Count
---

# Count

## Count non zero{% #count-non-zero %}

| Function          | Description                           | Example                           |
| ----------------- | ------------------------------------- | --------------------------------- |
| `count_nonzero()` | Compute count of all non-zero values. | `count_nonzero(<METRIC_NAME>{*})` |

For a query grouped by one or more [tag keys](https://docs.datadoghq.com/getting_started/tagging/), count the number of tag values with non-zero metric values at each point.

Example: `count_nonzero(system.cpu.user{*} by {host})` returns a timeseries representing the number of hosts with non-zero system load at each point.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/count/count_nonzero.625956fc4a82202e35d80f4e203b82e8.png?auto=format"
   alt="count non zero" /%}

Note: `count_nonzero_finite()` can be used as an alias for `count_nonzero()`.

## Count not null{% #count-not-null %}

| Function           | Description                           | Example                            |
| ------------------ | ------------------------------------- | ---------------------------------- |
| `count_not_null()` | Compute count of all not null values. | `count_not_null(<METRIC_NAME>{*})` |

For a query grouped by one or more [tag keys](https://docs.datadoghq.com/getting_started/tagging/), count the number of tag values with non-null metric values at each point. A null metric value is when there is no finite value.

Example: `count_not_null(system.cpu.user{*} by {host})` returns a timeseries representing the number of hosts with non-null system load at each point.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/count/count_not_null.3950e1152b2ae482e5bfbe8378635dae.png?auto=format"
   alt="count not null" /%}

## Other functions{% #other-functions %}

- [Algorithmic: Implement Anomaly or Outlier detection on your metric.](https://docs.datadoghq.com/dashboards/functions/algorithms)
- [Arithmetic: Perform Arithmetic operation on your metric.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Exclusion: Exclude certain values of your metric.](https://docs.datadoghq.com/dashboards/functions/exclusion)
- [Interpolation: Fill or set default values for your metric.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rank: Select only a subset of metrics.](https://docs.datadoghq.com/dashboards/functions/rank)
- [Rate: Calculate custom derivative over your metric.](https://docs.datadoghq.com/dashboards/functions/rate)
- [Regression: Apply some machine learning function to your metric.](https://docs.datadoghq.com/dashboards/functions/regression)
- [Rollup: Control the number of raw points used in your metric.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Smoothing: Smooth your metric variations.](https://docs.datadoghq.com/dashboards/functions/smoothing)
- [Timeshift: Shift your metric data point along the timeline.](https://docs.datadoghq.com/dashboards/functions/timeshift)
