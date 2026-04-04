# Source: https://docs.datadoghq.com/dashboards/functions/arithmetic.md

---
title: Arithmetic
description: >-
  Perform mathematical operations including absolute values, logarithms,
  exponents, and cumulative sums on metrics.
breadcrumbs: Docs > Dashboards > Functions > Arithmetic
---

# Arithmetic

## Absolute{% #absolute %}

| Function | Description                             | Example                 |
| -------- | --------------------------------------- | ----------------------- |
| `abs()`  | Graph the absolute value of the metric. | `abs(<METRIC_NAME>{*})` |

Transforms this sine timeseries `sin{*}`:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/arithmetic/sinus.720631d66fdcbb58a59a88dc1ac65be2.png?auto=format"
   alt="Sinus function" /%}

into this one `abs(sin{*})`:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/arithmetic/sinus_abs.9189bbd860bf76e21a5a0e38e9bb77d9.png?auto=format"
   alt="Sinus function with abs" /%}

## Exponent{% #exponent %}

| Function | Description                                                         | Example                                                                                                                                    |
| -------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `pow()`  | Graph all combinations of metric and constant using exponentiation. | `pow(<METRIC_NAME>{*}, CONSTANT)`, `pow(<METRIC_NAME>{*}, <METRIC_NAME>{*})`, `pow(CONSTANT, <METRIC_NAME>{*})`, `pow(CONSTANT, CONSTANT)` |

## Logarithm{% #logarithm %}

### Log base 2{% #log-base-2 %}

| Function | Description                                    | Example                  |
| -------- | ---------------------------------------------- | ------------------------ |
| `log2()` | Graph the Base-2 logarithm of the metric. | `log2(<METRIC_NAME>{*})` |

Example:

If a metric, `x{*}`, increments itself by 1 for each data point, then `log2(x{*})` has the following shape:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/arithmetic/log2.c396ddaca856da6646f6eee6719b3403.png?auto=format"
   alt=" log2 function" /%}

### Log base 10{% #log-base-10 %}

| Function  | Description                                     | Example                   |
| --------- | ----------------------------------------------- | ------------------------- |
| `log10()` | Graph the Base-10 logarithm of the metric. | `log10(<METRIC_NAME>{*})` |

Example:

If a metric, `x{*}`, increments itself by 1 for each data point, then `log10(x{*})` has the following shape:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/arithmetic/log10.5b6bcf8df6757f21a697857ba3060bb4.png?auto=format"
   alt="log10 function" /%}

## Cumulative sum{% #cumulative-sum %}

| Function   | Description                                                          | Example                    |
| ---------- | -------------------------------------------------------------------- | -------------------------- |
| `cumsum()` | Graph the cumulative sum of the metric over the visible time window. | `cumsum(<METRIC_NAME>{*})` |

Example:

If a metric, `const_1{*}`, is a constant with the value of `1`, then `cumsum(const_1{*})` has the following shape:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/arithmetic/cumsum.8e70c215c9310fe53a648f77de820084.png?auto=format"
   alt="cum sum function with abs" /%}

## Cumulative sum in monitors{% #cumulative-sum-in-monitors %}

Cumulative sum should be avoided in monitor queries, because the cumulative sum function is a visual function. When used in a dashboard or notebook, the points will reflect values based on the selected timeframe. This doesn't translate well in a monitor as the monitor doesn't have a sense of which timeframe to use.

Instead, configure [Cumulative Time Windows](https://docs.datadoghq.com/monitors/configuration/?tab=thresholdalert#cumulative-time-windows) in your monitor evaluation period.

## Integral{% #integral %}

| Function     | Description                       | Example                      |
| ------------ | --------------------------------- | ---------------------------- |
| `integral()` | Graph the integral of the metric. | `integral(<METRIC_NAME>{*})` |

**Note**: Datadog's `integral()` is the cumulative sum of `[time delta] x [value delta]` over all consecutive pairs of points in the visible time window for a given metric.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/arithmetic/integral.4cde1d678e5351e0286015c32616e7ad.png?auto=format"
   alt="integral function with abs" /%}

## Other functions{% #other-functions %}

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
