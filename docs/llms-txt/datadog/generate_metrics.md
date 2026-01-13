# Source: https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics.md

---
title: Generate Custom Metrics from Spans and Traces
description: Generate custom metrics from ingested spans and complete traces.
breadcrumbs: >-
  Docs > APM > The Trace Pipeline > Generate Custom Metrics from Spans and
  Traces
source_url: https://docs.datadoghq.com/trace_pipeline/generate_metrics/index.html
---

# Generate Custom Metrics from Spans and Traces

{% image
   source="https://datadog-docs.imgix.net/images/tracing/apm_lifecycle/span_based_metrics.3446bb76b0ca9495ce454e75105ba1b6.png?auto=format"
   alt="Span-based metrics" /%}

Generate custom metrics from ingested spans to track trends, power dashboards, and trigger monitorsâeven for spans and traces that are not retained for full trace analysis.

Custom metrics are created from spans ingested by Datadog APM, regardless of whether a [retention filter](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention) indexes those spans. Extract numeric values from spans (such as counts, durations, or custom tags) or traces (end-to-end trace duration) and store them as long-lived [custom metrics](https://docs.datadoghq.com/metrics/#overview) with 15-month retention.

**Notes:**

- Datadog automatically generates [Trace Metrics](https://docs.datadoghq.com/tracing/metrics/metrics_namespace/) that capture request counts, error rates, and latency distributions for 100% of your application traffic.
- Available spans for custom metric generation depend on your [APM ingestion control settings](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls). Dropped spans from sampling or filtering cannot generate metrics.

Use custom metrics from spans for:

- Fine-grained visibility into span-level latency, error rates, or tag-level performance
- Powering [anomaly](https://docs.datadoghq.com/monitors/types/anomaly/#overview) or [forecast](https://docs.datadoghq.com/monitors/types/forecasts/) monitors with low-latency, high-resolution metrics.
- Extracting key signals for trending or alerting without retaining the full span.

#### When to use custom metrics from traces{% #when-to-use-custom-metrics-from-traces %}

Datadog allows you to generate metrics from [Trace Queries](https://docs.datadoghq.com/tracing/trace_explorer/trace_queries).

{% callout %}
##### Request access to the Preview!

Custom metrics from traces are in Preview. To request access, submit a ticket to the APM Support team and provide a short description of your use case.

[Request Access](https://help.datadoghq.com/hc/en-us/requests/new)
{% /callout %}

Use custom metrics from traces for:

- Metrics derived from complete trace context, such as total trace duration or operations per trace.
- Alerting on conditions requiring full trace knowledge (for example, N+1 query detection or fan-out patterns).
- Extracting key signals for trending or alerting without retaining the full trace.

## Create a metric from spans or traces{% #create-a-metric-from-spans-or-traces %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/span_to_metrics/createspantometrics.409869c81f5800360caf1dc5abd53b7e.png?auto=format"
   alt="How to create a metric" /%}

1. Navigate to [**APM** > **Generate Metrics**](https://app.datadoghq.com/apm/traces/generate-metrics).
1. Click **New Metric**.
1. Name your metric following the [metric naming convention](https://docs.datadoghq.com/metrics/#naming-metrics). Metric names starting with `trace.*` are not allowed.
1. Select the metric type: **Spans** or **Traces**. Both use the same [query syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/) as APM Search and Analytics.
1. Define the metric query to filter and include only the spans or traces you want to measure.
1. Choose the value to aggregate:
   - Select `*` to count all matching spans or traces.
   - Enter a numeric attribute (for example, `@cassandra_row_count`) to aggregate and track the count, min, max, sum, or percentiles.
1. Set grouping dimensions. By default, metrics have no tags unless you add them. Use any span attribute or tag to create metric tags.
1. Preview the result to view the real-time impact of your query through the data visualization and matching spans or traces in the live preview.
1. Click **Create Metric**.

{% alert level="danger" %}
Span-based metrics are considered [custom metrics](https://docs.datadoghq.com/metrics/custom_metrics/) and billed accordingly. Avoid grouping by unbounded or extremely high cardinality attributes like timestamps, user IDs, request IDs, or session IDs to avoid impacting your billing.
{% /alert %}

## Update existing metrics{% #update-existing-metrics %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/span_to_metrics/editspantometrics.1e303220430ba648ef11ff71a32ec0a3.png?auto=format"
   alt="Edit an existing metrics" /%}

After a metric is created, only two fields can be updated:

| Field               | Reason                                                          |
| ------------------- | --------------------------------------------------------------- |
| Stream filter query | Change the set of matching spans to be aggregated into metrics. |
| Aggregation groups  | Update the tags to manage the cardinality of generated metrics. |

**Note**: To change the metric type or name, create a new metric and delete the old one.

## Data availability{% #data-availability %}

Metrics generated from traces are emitted after a trace completes. For long-running traces, the delay increases accordingly (for example, a 45-minute trace's metric cannot be emitted until trace completion).

When using custom metrics from traces in monitors, account for this latency to avoid false positives.

## Further Reading{% #further-reading %}

- [Customize trace ingestion and retain important traces](https://docs.datadoghq.com/tracing/trace_pipeline)
- [Use Analytics queries and monitors based on retained traces](https://docs.datadoghq.com/tracing/trace_search_and_analytics/query_syntax)
- [Use advanced trace queries to create metrics from specific traces](https://docs.datadoghq.com/tracing/trace_explorer/trace_queries)
- [Monitor 100% of your application traffic with trace metrics](https://docs.datadoghq.com/tracing/metrics/metrics_namespace)
- [Create and manage span-based metrics with Terraform](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/spans_metric)
