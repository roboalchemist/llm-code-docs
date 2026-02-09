# Source: https://docs.datadoghq.com/dashboards/functions/beta.md

---
title: Beta Functions
description: >-
  Use rolling average beta functions to smooth metric data over different time
  spans in dashboard queries.
breadcrumbs: Docs > Dashboards > Functions > Beta Functions
---

# Beta Functions

Beta functions are available by editing the query JSON directly.

## Rolling average{% #rolling-average %}

| Function          | Description                                    | Example                           |
| ----------------- | ---------------------------------------------- | --------------------------------- |
| `rollingavg_5()`  | Compute the rolling average over a span of 5.  | `rollingavg_5(system.load.1{*})`  |
| `rollingavg_13()` | Compute the rolling average over a span of 13. | `rollingavg_13(system.load.1{*})` |
| `rollingavg_21()` | Compute the rolling average over a span of 21. | `rollingavg_21(system.load.1{*})` |
| `rollingavg_29()` | Compute the rolling average over a span of 29. | `rollingavg_29(system.load.1{*})` |

## Other functions{% #other-functions %}

- [Arithmetic: Perform Arithmetic operation on your metric.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Algorithmic: Implement Anomaly or Outlier detection on your metric.](https://docs.datadoghq.com/dashboards/functions/algorithms)
- [Count: Count non zero or non null value of your metric.](https://docs.datadoghq.com/dashboards/functions/count)
- [Exclusion: Exclude certain values of your metric.](https://docs.datadoghq.com/dashboards/functions/exclusion)
- [Interpolation: Fill or set default values for your metric.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rank: Select only a subset of metrics.](https://docs.datadoghq.com/dashboards/functions/rank)
- [Rate: Calculate custom derivative over your metric.](https://docs.datadoghq.com/dashboards/functions/rate)
- [Regression: Apply some machine learning function to your metric.](https://docs.datadoghq.com/dashboards/functions/regression)
- [Rollup: Control the number of raw points used in your metric.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Smoothing: Smooth your metric variations.](https://docs.datadoghq.com/dashboards/functions/smoothing)
- [Timeshift: Shift your metric data point along the timeline.](https://docs.datadoghq.com/dashboards/functions/timeshift)
