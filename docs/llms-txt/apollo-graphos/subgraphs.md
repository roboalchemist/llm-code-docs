# Source: https://www.apollographql.com/docs/rover/commands/subgraphs.md

# Source: https://www.apollographql.com/docs/graphos/platform/insights/subgraphs.md

# Subgraph Metrics in GraphOS

All plans can access subgraph metrics. Metrics respect data retention policies defined on the [pricing page](https://www.apollographql.com/pricing).

Subgraph and connector-level insights give you visibility into how each service contributes to your supergraph's performance. You can use subgraph insights to:

* **Identify top traffic sources**: identify the clients or operations driving the highest error and request rates so you can prioritize fixes.

* **Detect performance bottlenecks**:  target operations with the slowest p95 service times to eliminate lag for your heaviest consumers.

* **Analyze trends**: uncover recurring patterns using latency heatmaps, error rate, and request rate charts across different time ranges.

* **Compare subgraphs**: rank and contrast subgraphs by request volume, latency, and error rates to understand performance differences.

## Set up subgraph metrics

Enable subgraph metric collection in your router configuration file by setting subgraph\_metrics to true:

```yaml title=router.yaml
telemetry:
  apollo:
    subgraph_metrics: true
```

If you're using the private preview on Router v2.6.2, use the configuration key `telemetry.apollo.experimental_subgraph_metrics` instead.

If you're using the public preview on Router v2.7.0, use the configuration key `telemetry.apollo.preview_subgraph_metrics` instead.

This feature supports cardinality up to 2000 per metric send interval. For high-traffic graphs with many subgraphs, [learn how to manage high cardinality](https://www.apollographql.com/docs/graphos/routing/observability/graphos/graphos-reporting#cardinality-limitations).

## View subgraph insights

Navigate to the **Insights** page in [Studio](https://studio.apollographql.com/?referrer=docs-content) and choose the **Subgraphs** option in the dropdown to start exploring subgraph and Connector-level insights.

This page shows you:

1. Your list of subgraphs ranked by fetch data, latency percentiles, error data, and total duration
2. The top clients and operations with the highest fetch, error, and latency rates
3. A time series charts for:
   * fetches and errors displayed as counts or rates
   * performance displayed as a latency heatmap, latency distribution, or p50, 95, 90, and 99 service times
4. Error information, including the error rates, codes, and standard paths
5. Owner information for the selected subgraph
