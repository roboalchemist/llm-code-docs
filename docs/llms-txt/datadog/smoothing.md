# Source: https://docs.datadoghq.com/dashboards/functions/smoothing.md

---
title: Smoothing
description: >-
  Reduce noise in metric data using autosmooth, exponentially weighted moving
  averages, median filters, and weighted functions.
breadcrumbs: Docs > Dashboards > Functions > Smoothing
---

# Smoothing

## Autosmooth{% #autosmooth %}

| Function       | Description                                                           | Example                        |
| -------------- | --------------------------------------------------------------------- | ------------------------------ |
| `autosmooth()` | Automatically removes noise while preserving the trend of the metric. | `autosmooth(<METRIC_NAME>{*})` |

The `autosmooth()` function applies a moving average with an automatically selected span. It smooths a timeseries while preserving its trend. In this example, the function chooses the optimal span to smooth the timeseries:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/smoothing/autosmooth_illustration.8d449617c46e8a9c6fb36202b985987e.png?auto=format"
   alt="autosmooth illustration" /%}

When used on a `group by` query, such as `avg by`, the same span is applied on all the timeseries. If used on several metrics in the same graph, different spans can be selected to optimally smooth each one of the metric timeseries.

The algorithm is inspired by the [ASAP algorithm](https://github.com/stanford-futuredata/ASAP)-you can read more about it in this [blog post](https://www.datadoghq.com/blog/auto-smoother-asap).

The `autosmooth()` function cannot be used in monitors. Being that the span is chosen dynamically, the result of applying the function could change from minute to minute, making threshold setting difficult and leading to alert flapping.

## Exponentially weighted moving average{% #exponentially-weighted-moving-average %}

### Ewma 3{% #ewma-3 %}

| Function   | Description                                                         | Example                    |
| ---------- | ------------------------------------------------------------------- | -------------------------- |
| `ewma_3()` | Compute the exponentially weighted moving average over a span of 3. | `ewma_3(<METRIC_NAME>{*})` |

Note: The span value is twice the weighted average age of the series. So `ewma_3()` is comparable to a 3-day rolling average.

Example:

If a metric `10 + x%10 {*}` increments itself by 1 starting from 10 until it drops back to 10 after 10 data points, then `ewma3(10 + x%10 {*})` has the following shape:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/smoothing/ewma3.6eac30799393ef10b5b05220fe092b25.png?auto=format"
   alt="EWMA3" /%}

### Ewma 5{% #ewma-5 %}

| Function   | Description                                                         | Example                    |
| ---------- | ------------------------------------------------------------------- | -------------------------- |
| `ewma_5()` | Compute the exponentially weighted moving average over a span of 5. | `ewma_5(<METRIC_NAME>{*})` |

Note: The span value is twice the weighted average age of the series. So `ewma_5()` is comparable to a 5-day rolling average.

Example:

If a metric `10 + x%10 {*}` increments itself by 1 starting from 10 until it drops back to 10 after 10 data points, then `ewma5(10 + x%10 {*})` has the following shape:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/smoothing/ewma5.df9df1fad29834caa5a5df3036ce7151.png?auto=format"
   alt="EWMA5" /%}

### Ewma 7{% #ewma-7 %}

| Function   | Description                                                         | Example                    |
| ---------- | ------------------------------------------------------------------- | -------------------------- |
| `ewma_7()` | Compute the exponentially weighted moving average over a span of 7. | `ewma_7(<METRIC_NAME>{*})` |

Note: The span value is twice the weighted average age of the series. So `ewma_7()` is comparable to a 7-day rolling average.

### Ewma 10{% #ewma-10 %}

| Function    | Description                                                          | Example                     |
| ----------- | -------------------------------------------------------------------- | --------------------------- |
| `ewma_10()` | Compute the exponentially weighted moving average over a span of 10. | `ewma_10(<METRIC_NAME>{*})` |

Note: The span value is twice the weighted average age of the series. So `ewma_10()` is comparable to a 10-day rolling average.

Example:

If a metric `10 + x%10 {*}` increments itself by 1 starting from 10 until it drops back to 10 after 10 data points, then `ewma10(10 + x%10 {*})` has the following shape:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/smoothing/ewma10.931f28d6d5a49060e40a64588298db58.png?auto=format"
   alt="EWMA10" /%}

### Ewma 20{% #ewma-20 %}

| Function    | Description                                                          | Example                     |
| ----------- | -------------------------------------------------------------------- | --------------------------- |
| `ewma_20()` | Compute the exponentially weighted moving average over a span of 20. | `ewma_20(<METRIC_NAME>{*})` |

Note: The span value is twice the weighted average age of the series. So `ewma_20()` is comparable to a 20-day rolling average.

Example:

If a metric `10 + x%10 {*}` increments itself by 1 starting from 10 until it drops back to 10 after 10 data points, then `ewma20(10 + x%10 {*})` has the following shape:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/smoothing/ewma20.ae7ee8fa57421c5190aed48fa170f619.png?auto=format"
   alt="EWMA20" /%}

## Median{% #median %}

### Median 3{% #median-3 %}

| Function     | Description                      | Example                      |
| ------------ | -------------------------------- | ---------------------------- |
| `median_3()` | Rolling median with a span of 3. | `median_3(<METRIC_NAME>{*})` |

Note: The span value is the number of data points. So `median_3()` uses the last 3 data points to calculate the median.

### Median 5{% #median-5 %}

| Function     | Description                      | Example                      |
| ------------ | -------------------------------- | ---------------------------- |
| `median_5()` | Rolling median with a span of 5. | `median_5(<METRIC_NAME>{*})` |

Note: The span value is the number of data points. So `median_5()` uses the last 5 data points to calculate the median.

### Median 7{% #median-7 %}

| Function     | Description                      | Example                      |
| ------------ | -------------------------------- | ---------------------------- |
| `median_7()` | Rolling median with a span of 7. | `median_7(<METRIC_NAME>{*})` |

Note: The span value is the number of data points. So `median_7()` uses the last 7 data points to calculate the median.

### Median 9{% #median-9 %}

| Function     | Description                      | Example                      |
| ------------ | -------------------------------- | ---------------------------- |
| `median_9()` | Rolling median with a span of 9. | `median_9(<METRIC_NAME>{*})` |

Note: The span value is the number of data points. So `median_9()` uses the last 9 data points to calculate the median.

## Weighted{% #weighted %}

{% alert level="info" %}
Weighted() is only available when querying `SUM BY` on gauge type metrics.
{% /alert %}

| Function     | Description                                                                       | Example                                   |
| ------------ | --------------------------------------------------------------------------------- | ----------------------------------------- |
| `weighted()` | Automatically removes noise while preserving the proper weight of transient tags. | `sum:(<GAUGE_METRIC_NAME>{*}).weighted()` |

The `weighted()` function accounts for the short-lived lifespan of transient, churning tag values when summing gauge metrics in space to prevent artificial spikes.

This function is automatically appended to queries on gauge metrics if both of the following conditions are met:

1. The metric has a regular, consistent submission interval that is also specified on Metrics Summary
1. The metric is aggregated with `SUM by` (for example, `sum: mygaugemetric{*}`)

Here is an example graph of the original query with inaccurate spikes (in purple) and the query with the properly weighted calculation (in green):

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/smoothing/weighted.bb548961a20cad1af2ada9cb5d04e453.png?auto=format"
   alt="Example graph comparing queries with and without the weighted modifier" /%}

For more information on the weighted() modifier, see [How does weighted() work?](https://docs.datadoghq.com/dashboards/guide/how-weighted-works).

## Other functions{% #other-functions %}

- [Algorithmic: Implement Anomaly or Outlier detection on your metric.](https://docs.datadoghq.com/dashboards/functions/algorithms)
- [Arithmetic: Perform Arithmetic operation on your metric.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Count: Count non zero or non null value of your metric.](https://docs.datadoghq.com/dashboards/functions/count)
- [Exclusion: Exclude certain values of your metric.](https://docs.datadoghq.com/dashboards/functions/exclusion)
- [Interpolation: Fill or set default values for your metric.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rank: Select only a subset of metrics.](https://docs.datadoghq.com/dashboards/functions/rank)
- [Rate: Calculate custom derivative over your metric.](https://docs.datadoghq.com/dashboards/functions/rate)
- [Regression: Apply some machine learning function to your metric.](https://docs.datadoghq.com/dashboards/functions/regression)
- [Rollup: Control the number of raw points used in your metric.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Timeshift: Shift your metric data point along the timeline.](https://docs.datadoghq.com/dashboards/functions/timeshift)
