# Source: https://docs.datadoghq.com/dashboards/functions.md

---
title: Functions
description: >-
  Apply mathematical and statistical functions to modify metric query results in
  Datadog dashboards and visualizations.
breadcrumbs: Docs > Dashboards > Functions
---

# Functions

## Overview{% #overview %}

Functions can modify how the results of a metric query are returned for visualizations. Most functions are applied after the results of the metric query are returned, but functions can also change the parameters before the query is made.

For example, the Rollup function changes the time aggregation of a query before the results are returned. Alternatively, arithmetic functions apply changes to the returned results of the metric query. See the [Metrics](https://docs.datadoghq.com/metrics/#anatomy-of-a-metric-query) page to learn more about querying metrics. To learn more about the different functions, see the function types.

## Add a function{% #add-a-function %}

Functions can be applied to your queries by clicking the Add Function `Î£` icon in the graphing editor. Most of the functions are applied after [time](https://docs.datadoghq.com/metrics/#time-aggregation) and [space aggregation](https://docs.datadoghq.com/metrics/#space-aggregation).

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/functions/sigmaaddingfunctions.7e2ae3adca1aa0115074bc6f44c651d9.png?auto=format"
   alt="Capital Sigma symbol for Add Function" /%}

## Function types{% #function-types %}

- [Algorithmic: Implement anomaly or outlier detection.](https://docs.datadoghq.com/dashboards/functions/algorithms)
- [Arithmetic: Perform arithmetic operations.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Count: Count non-zero or non-null values.](https://docs.datadoghq.com/dashboards/functions/count)
- [Exclusion: Exclude certain values of your metric.](https://docs.datadoghq.com/dashboards/functions/exclusion)
- [Interpolation: Fill or set default values.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rank: Select only a subset of metrics.](https://docs.datadoghq.com/dashboards/functions/rank)
- [Rate: Calculate a custom derivative over your metric.](https://docs.datadoghq.com/dashboards/functions/rate)
- [Regression: Apply a machine learning function.](https://docs.datadoghq.com/dashboards/functions/regression)
- [Rollup: Control the number of raw data points used.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Smoothing: Smooth your metric variations.](https://docs.datadoghq.com/dashboards/functions/smoothing)
- [Timeshift: Shift your metric data point along the timeline.](https://docs.datadoghq.com/dashboards/functions/timeshift)
- [Beta: Compute the rolling average of a metric.](https://docs.datadoghq.com/dashboards/functions/beta)

## Further Reading{% #further-reading %}

- [Querying metrics](https://docs.datadoghq.com/metrics/#querying-metrics)
