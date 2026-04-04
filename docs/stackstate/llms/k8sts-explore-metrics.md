# Source: https://archivedocs.stackstate.com/metrics/k8sts-explore-metrics.md

# Explore Metrics

You can find the metrics explorer at the bottom of the StackState main menu. Use it to execute any PromQL query and visualize the resulting time series. The query result is shown in a chart for the selected time range and in a table that shows the last value together with the labels for the time series.

![Metrics Explorer](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-427fb0b8a38dbaa9d0abb6c479408dec23db2086%2Fk8s-metrics-explorer.png?alt=media)

## PromQL queries

The query input field has auto-suggestions for metric names, label names and values, and supported PromQL functions. See the Prometheus documentation for a complete [PromQL guide and reference](https://prometheus.io/docs/prometheus/latest/querying/basics/). StackState also adds 2 default parameters that can be used in any query: `${__interval}` and `${__rate_interval}`. They can be used to scale the aggregation interval automatically with the chart resolution ([more details](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-writing-promql-for-charts)).

## See also

* [Writing PromQL queries for representative charts](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-writing-promql-for-charts)
* [PromQL documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/)
* [PromQL operators](https://prometheus.io/docs/prometheus/latest/querying/operators/)
* [PromQL functions](https://prometheus.io/docs/prometheus/latest/querying/functions/)
* [Anatomy of a PromQL Query](https://promlabs.com/blog/2020/06/18/the-anatomy-of-a-promql-query/)
* [Selecting Data in PromQL](https://promlabs.com/blog/2020/07/02/selecting-data-in-promql/)
* [How to join multiple metrics](https://iximiuz.com/en/posts/prometheus-vector-matching/)
* [Aggregation over time](https://iximiuz.com/en/posts/prometheus-functions-agg-over-time/)
