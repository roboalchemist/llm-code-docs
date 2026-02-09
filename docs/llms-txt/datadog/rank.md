# Source: https://docs.datadoghq.com/dashboards/functions/rank.md

---
title: Rank
description: >-
  Select and display top or bottom metric series using various aggregation
  methods like max, mean, sum, and area.
breadcrumbs: Docs > Dashboards > Functions > Rank
---

# Rank

## Top{% #top %}

| Function | Description               | Example                                              |
| -------- | ------------------------- | ---------------------------------------------------- |
| `top()`  | Graph the top N elements. | `top(<METRIC_NAME>{*}, <LIMIT_TO>, '<BY>', '<DIR>')` |

The `top()` function has three parameters:

- `LIMIT_TO`: The number of series to be displayed; choose from:

  - `5`
  - `10`
  - `25`
  - `50`
  - `100`

- `BY`: Aggregation method; choose from:

  - `max`: Maximum of all metrics values.
  - `mean`: Mean of all metrics values.
  - `min`: Min of all metrics values.
  - `sum`: Sum of all metrics values.
  - `last`: Last metrics value.
  - `l2norm`: Uses the [norm](http://en.wikipedia.org/wiki/Norm_%28mathematics%29) of the timeseries, which is always positive, to rank the series.
  - `area`: Signed area under the curve being graphed, which can be negative

- `DIR`: The direction of ranking; choose between:

  - `asc`: Rank the results in ascending order.
  - `desc`: Rank the results in descending order.

The `top()` method also has convenience functions of the following form, all of which take a single series list as input:

`[top, bottom][5, 10, 15, 20]_[mean, min, max, last, area, l2norm][2]`

For example, `bottom10_min()` retrieves the 10 lowest-valued series using the `min` metric.

## Other functions{% #other-functions %}

- [Algorithmic: Implement Anomaly or Outlier detection on your metric.](https://docs.datadoghq.com/dashboards/functions/algorithms)
- [Arithmetic: Perform Arithmetic operation on your metric.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Count: Count non zero or non null value of your metric.](https://docs.datadoghq.com/dashboards/functions/count)
- [Exclusion: Exclude certain values of your metric.](https://docs.datadoghq.com/dashboards/functions/exclusion)
- [Interpolation: Fill or set default values for your metric.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rate: Calculate custom derivative over your metric.](https://docs.datadoghq.com/dashboards/functions/rate)
- [Regression: Apply some machine learning function to your metric.](https://docs.datadoghq.com/dashboards/functions/regression)
- [Rollup: Control the number of raw points used in your metric.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Smoothing: Smooth your metric variations.](https://docs.datadoghq.com/dashboards/functions/smoothing)
- [Timeshift: Shift your metric data point along the timeline.](https://docs.datadoghq.com/dashboards/functions/timeshift)
