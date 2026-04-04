# Source: https://docs.datadoghq.com/dashboards/functions/exclusion.md

---
title: Exclusion
description: >-
  Exclude null values and apply threshold-based filtering using clamp and cutoff
  functions on metrics.
breadcrumbs: Docs > Dashboards > Functions > Exclusion
---

# Exclusion

## Exclude null{% #exclude-null %}

| Function         | Description                                                    | Example                                        |
| ---------------- | -------------------------------------------------------------- | ---------------------------------------------- |
| `exclude_null()` | Remove groups with N/A tag values from your graph or top list. | `exclude_null(avg:system.load.1{*} by {host})` |

For example, say you have a metric with two tags: `account` and `region`. `account` has three possible values (`prod`, `build` and `N/A`) while `region` has four possible values (`us-east-1`, `us-west-1`, `eu-central-1`, and `N/A`).

When you graph this metric as a timeseries, you would have 3 x 4 = 12 lines on your graph. Applying `exclude_null()` removes lines with tag combinations containing *any* N/A values, leaving you with 2 x 3 = 6 groups.

## Clamp{% #clamp %}

| Function      | Description                                                          | Example                                |
| ------------- | -------------------------------------------------------------------- | -------------------------------------- |
| `clamp_min()` | Set any metric values *under* a threshold value to equal that value. | `clamp_min(avg:system.load.1{*}, 100)` |
| `clamp_max()` | Set any metric values *over* a threshold value to equal that value.  | `clamp_max(avg:system.load.1{*}, 100)` |

Add a threshold value. The `clamp_min()` sets all datapoints below the threshold to equal that value, while `clamp_max()` limits datapoints above the threshold.

Note: `clamp_min(values, threshold)` and `clamp_max(values, threshold)` sets any `NaN` in values to `threshold`.

To avoid this behavior, apply the `default_zero()` before the `clamp_min()` / `clamp_max()` function.

## Cutoff{% #cutoff %}

| Function       | Description                                               | Example                                 |
| -------------- | --------------------------------------------------------- | --------------------------------------- |
| `cutoff_min()` | Replace metric values *under* a threshold value with NaN. | `cutoff_min(avg:system.load.1{*}, 100)` |
| `cutoff_max()` | Replace metric values *over* a threshold value with NaN.  | `cutoff_max(avg:system.load.1{*}, 100)` |

Add a threshold value. The `cutoff_min()` replaces all metric values lower than this threshold value with `NaN`, while `cutoff_max()` replaces all metric values higher than this threshold value with `NaN`. The cutoff functions do not replace values that are **equal to** the threshold value.

**Tip**: For both the clamp and cutoff functions, it may be helpful to see the threshold value you have chosen. You can [set a horizontal marker](https://www.datadoghq.com/blog/customize-graphs-dashboards-graph-markers/) in Dashboards to indicate this value.

## Other functions{% #other-functions %}

- [Arithmetic: Perform Arithmetic operation on your metric.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Algorithmic: Implement Anomaly or Outlier detection on your metric.](https://docs.datadoghq.com/dashboards/functions/algorithms)
- [Count: Count non zero or non null value of your metric.](https://docs.datadoghq.com/dashboards/functions/count)
- [Interpolation: Fill or set default values for your metric.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rank: Select only a subset of metrics.](https://docs.datadoghq.com/dashboards/functions/rank)
- [Rate: Calculate custom derivative over your metric.](https://docs.datadoghq.com/dashboards/functions/rate)
- [Regression: Apply some machine learning function to your metric.](https://docs.datadoghq.com/dashboards/functions/regression)
- [Rollup: Control the number of raw points used in your metric.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Smoothing: Smooth your metric variations.](https://docs.datadoghq.com/dashboards/functions/smoothing)
- [Timeshift: Shift your metric data point along the timeline.](https://docs.datadoghq.com/dashboards/functions/timeshift)
