# Source: https://docs.datadoghq.com/dashboards/functions/rate.md

---
title: Rate
description: >-
  Calculate rates, derivatives, and time differences to analyze metric changes
  per second, minute, or hour.
breadcrumbs: Docs > Dashboards > Functions > Rate
---

# Rate

## Per second{% #per-second %}

| Function       | Description                                                | Example                        |
| -------------- | ---------------------------------------------------------- | ------------------------------ |
| `per_second()` | Graph the rate at which the metric is changing per second. | `per_second(<METRIC_NAME>{*})` |

## Per minute{% #per-minute %}

| Function       | Description                                                | Example                        |
| -------------- | ---------------------------------------------------------- | ------------------------------ |
| `per_minute()` | Graph the rate at which the metric is changing per minute. | `per_minute(<METRIC_NAME>{*})` |

## Per hour{% #per-hour %}

| Function     | Description                                              | Example                      |
| ------------ | -------------------------------------------------------- | ---------------------------- |
| `per_hour()` | Graph the rate at which the metric is changing per hour. | `per_hour(<METRIC_NAME>{*})` |

## Time difference{% #time-difference %}

| Function | Description                                                    | Example                |
| -------- | -------------------------------------------------------------- | ---------------------- |
| `dt()`   | Graph the time difference in seconds between submitted points. | `dt(<METRIC_NAME>{*})` |

The dt() function returns only one timeseries regardless of how many groups are involved. Within that one timeseries, it considers the time difference of all the submitted points across the various groups.

## Value difference{% #value-difference %}

| Function | Description                    | Example                  |
| -------- | ------------------------------ | ------------------------ |
| `diff()` | Graph the delta of the metric. | `diff(<METRIC_NAME>{*})` |

Calculates the difference between each interval on a per interval basis. For example, a metric submits data points with a 15 second interval, the `diff()` modifier would show it over 15 second rate. **Note:** The calculation is done after applying time aggregation and before space aggregation takes place.

## Monotonic difference{% #monotonic-difference %}

| Function           | Description                                                                    | Example                            |
| ------------------ | ------------------------------------------------------------------------------ | ---------------------------------- |
| `monotonic_diff()` | Graph the delta of the metric like `diff()` but only if the delta is positive. | `monotonic_diff(<METRIC_NAME>{*})` |

## Derivative{% #derivative %}

| Function       | Description                                   | Example                        |
| -------------- | --------------------------------------------- | ------------------------------ |
| `derivative()` | Graph the derivative (diff/dt) of the metric. | `derivative(<METRIC_NAME>{*})` |

## Throughput{% #throughput %}

| Function       | Description                                                                                                                                       | Example                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `throughput()` | Converts a timeseries into a rate per second, by dividing each value by the number of seconds in the time bucket to produce the per-second value. | `throughput(<METRIC_NAME>{*})` |

## Other functions{% #other-functions %}

- [Algorithmic: Implement Anomaly or Outlier detection on your metric.](https://docs.datadoghq.com/dashboards/functions/algorithms)
- [Arithmetic: Perform Arithmetic operation on your metric.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Count: Count non zero or non null value of your metric.](https://docs.datadoghq.com/dashboards/functions/count)
- [Exclusion: Exclude certain values of your metric.](https://docs.datadoghq.com/dashboards/functions/exclusion)
- [Interpolation: Fill or set default values for your metric.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rank: Select only a subset of metrics.](https://docs.datadoghq.com/dashboards/functions/rank)
- [Regression: Apply some machine learning function to your metric.](https://docs.datadoghq.com/dashboards/functions/regression)
- [Rollup: Control the number of raw points used in your metric.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Smoothing: Smooth your metric variations.](https://docs.datadoghq.com/dashboards/functions/smoothing)
- [Timeshift: Shift your metric data point along the timeline.](https://docs.datadoghq.com/dashboards/functions/timeshift)

## Further Reading{% #further-reading %}

- [Alert on no change in value](https://docs.datadoghq.com/monitors/guide/alert-on-no-change-in-value/)
