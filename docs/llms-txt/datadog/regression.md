# Source: https://docs.datadoghq.com/dashboards/functions/regression.md

---
title: Regression
description: >-
  Apply regression analysis with robust trends, trend lines, and piecewise
  constant approximations to metric data.
breadcrumbs: Docs > Dashboards > Functions > Regression
---

# Regression

## Robust trend{% #robust-trend %}

| Function         | Description                                          | Example                              |
| ---------------- | ---------------------------------------------------- | ------------------------------------ |
| `robust_trend()` | Fit a robust regression trend line using Huber loss. | `robust_trend(avg:<METRIC_NAME>{*})` |

The most common type of linear regressionâordinary least squares (OLS)âcan be heavily influenced by a small number of points with extreme values. Robust regression is an alternative method for fitting a regression line; it is not influenced as strongly by a small number of extreme values. As an example, see the following plot.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/regression/robust_trend.7757410fb5307f28819bd19268c7c70a.png?auto=format"
   alt="robust trend" /%}

The original metric is shown as a solid blue line. The purple dashed line is an OLS regression line, and the yellow dashed line is a robust regression line. The one short-lived spike in the metric leads to the OLS regression line trending upward, but the robust regression line ignores the spike and does a better job fitting the overall trend in the metric.

## Trend line{% #trend-line %}

| Function       | Description                                                              | Example                            |
| -------------- | ------------------------------------------------------------------------ | ---------------------------------- |
| `trend_line()` | Fit an ordinary least squares regression line through the metric values. | `trend_line(avg:<METRIC_NAME>{*})` |

Example:

The function `sin(x) * x/2 + x` then `trend_line(sin(x) * x/2 + x)` has the following shape:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/regression/trend_line_function.6c25a8733d61b64446fda62ccde78e6e.png?auto=format"
   alt="Trend line function" /%}

## Piecewise constant{% #piecewise-constant %}

| Function               | Description                                                                            | Example                                    |
| ---------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------ |
| `piecewise_constant()` | Approximate the metric with a piecewise function composed of constant-valued segments. | `piecewise_constant(avg:<METRIC_NAME>{*})` |

Example:

The function `x` then `piecewise_constant(x)` has the following shape:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/regression/piecewise_constant.67997bf263158c55990b19c90e9ce0ee.png?auto=format"
   alt="piecewise constant" /%}

## Other functions{% #other-functions %}

- [Algorithmic: Implement Anomaly or Outlier detection on your metric.](https://docs.datadoghq.com/dashboards/functions/algorithms)
- [Arithmetic: Perform Arithmetic operation on your metric.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Count: Count non zero or non null value of your metric.](https://docs.datadoghq.com/dashboards/functions/count)
- [Exclusion: Exclude certain values of your metric.](https://docs.datadoghq.com/dashboards/functions/exclusion)
- [Interpolation: Fill or set default values for your metric.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rank: Select only a subset of metrics.](https://docs.datadoghq.com/dashboards/functions/rank)
- [Rate: Calculate custom derivative over your metric.](https://docs.datadoghq.com/dashboards/functions/rate)
- [Rollup: Control the number of raw points used in your metric.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Smoothing: Smooth your metric variations.](https://docs.datadoghq.com/dashboards/functions/smoothing)
- [Timeshift: Shift your metric data point along the timeline.](https://docs.datadoghq.com/dashboards/functions/timeshift)
