# Source: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention.md

---
title: Trace Retention
description: Learn how to control trace retention with retention filters.
breadcrumbs: Docs > APM > The Trace Pipeline > Trace Retention
source_url: https://docs.datadoghq.com/trace_pipeline/trace_retention/index.html
---

# Trace Retention

{% image
   source="https://datadog-docs.imgix.net/images/tracing/apm_lifecycle/retention_filters.563d0e7036a2c2588675936cb819b81d.png?auto=format"
   alt="Retention filters" /%}

With Datadog APM, [the ingestion and the retention of traces for 15 days](https://docs.datadoghq.com/tracing/trace_pipeline/) are fully customizable.

To track or monitor your volume of ingested and indexed data, see the [Usage Metrics](https://docs.datadoghq.com/tracing/trace_pipeline/metrics) documentation.

## Retention filters{% #retention-filters %}

After spans have been ingested, some are kept for 15 days according to the retention filters that are set up on your account:

1. The **Intelligent Retention Filter** retains spans for every environment, service, operation, and resource for different latency distributions.
1. Several **Default Retention Filters** are created to ensure that you keep visibility over all of your services and endpoints, as well as errors and high-latency traces.
1. You can create any number of additional **Custom Retention Filters** for your services, to capture the traces that matters the most to your business, based on any span attribute or tag filter.

**Note**: The permission `apm_retention_filter_write` is required to create, delete, modify, enable, or disable retention filters.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/retention_filters/retention_filters.ce63b8a6f88f53352e3bccbaa1a7750d.png?auto=format"
   alt="Retention Filters Page" /%}

In Datadog, on the [Retention Filters](https://app.datadoghq.com/apm/traces/retention-filters) settings page, you can see a list of all retention filters:

{% dl %}

{% dt %}
Filter Name
{% /dt %}

{% dd %}
The name of each retention filter used to index spans.
{% /dd %}

{% dt %}
Filter Query
{% /dt %}

{% dd %}
The tag-based query for each filter.
{% /dd %}

{% dt %}
Retention Rate
{% /dt %}

{% dd %}
A percentage from 0 to 100% of how many matching spans are indexed. The retained spans are uniformly chosen from among spans that match the filter query.
{% /dd %}

{% dt %}
Spans Indexed
{% /dt %}

{% dd %}
The number of spans indexed by the filter over the selected time period.
{% /dd %}

{% dt %}
Last Updated
{% /dt %}

{% dd %}
The date and user who last modified the retention filter.
{% /dd %}

{% dt %}
Enabled toggle
{% /dt %}

{% dd %}
Allows filters to be turned on and off.
{% /dd %}

{% /dl %}

**Note**: The order of the retention filter list changes indexing behavior. If a span matches a retention filter early in the list, the span is either kept or dropped. Any matching custom retention filter lower on the list does not catch the already-processed span.

The `Spans Indexed` column for each retention filter is powered by the `datadog.estimated_usage.apm.indexed_spans` metric, which you can use to track your indexed span usage. For more information, read [Usage Metrics](https://docs.datadoghq.com/tracing/trace_pipeline/metrics), or explore the [out-of-the-box usage dashboard](https://app.datadoghq.com/dash/integration/30337/app-analytics-usage) available in your account.

{% alert level="info" %}
Retention filters do not affect what traces are collected by the Agent and sent to Datadog ("ingested"). To control ingestion, use dedicated [ingestion controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/).
{% /alert %}

### Retention filter types{% #retention-filter-types %}

There are two types of retention filters:

1. **Span-level retention filters** - Index only the specific spans that match your filter criteria.
1. **Trace-level retention filters** - Index entire traces that contain spans matching your filter criteria, making the complete traces searchable in Trace Queries.

| Feature                   | Standard retention filters       | Trace-level retention filters                                       |
| ------------------------- | -------------------------------- | ------------------------------------------------------------------- |
| **Configuration**         | Span query + Span retention rate | Span query + Span retention rate + Trace retention rate             |
| **What is indexed**       | Only spans targeted by the query | All spans belonging to traces that contain spans matching the query |
| **Where it is queryable** | Span Explorer                    | Span Explorer and Trace Queries                                     |

**Note**: Indirectly indexed spans retained by trace-level retention filters (that is, spans that don't match the query directly but belong to traces that do) are not evaluated by [trace analytics monitors](https://docs.datadoghq.com/monitors/types/apm/?tab=traceanalytics).

### Default retention filters{% #default-retention-filters %}

The following retention filters are enabled by default:

- The `Error Default` retention filter indexes error spans with `status:error`. The retention rate and the query are configurable. For example, to capture production errors, set the query to `status:error, env:production`. Disable the retention filter if you do not want to capture the errors by default.
- The `App and API Protection Default` retention filter is enabled if you are using [App and API Protection](https://docs.datadoghq.com/security/application_security/). It ensures the retention of all spans in traces that have been identified as having an application security impact (an attack attempt).
- The `Synthetics Default` retention filter is enabled if you are using Synthetic Monitoring. It ensures that traces generated from synthetic API and browser tests remain available by default. See [Synthetic APM](https://docs.datadoghq.com/synthetics/apm/) for more information, including how to correlate traces with synthetic tests.
- The `Dynamic Instrumentation Default` retention filter is enabled if you are using [Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/). It ensures spans created dynamically with Dynamic instrumentation remain available in the long term by default.

### Datadog intelligent retention filter{% #datadog-intelligent-retention-filter %}

The Datadog intelligent retention filter is always active for your services, and it keeps a representative selection of traces without requiring you to create dozens of custom retention filters. It is composed of:

- Diversity sampling
- One percent flat sampling

**Note:** [Trace Queries](https://docs.datadoghq.com/tracing/trace_explorer/trace_queries) are based on the data indexed by the Intelligent Retention filter.

Spans indexed by the Intelligent retention filter (diversity sampling and 1% flat sampling) are **not counted towards the usage** of indexed spans, and so **do not impact your bill**.

If there are specific tags or attributes for which you want to index more spans than what the Intelligent Retention filter retains, then create your own retention filter.

#### Diversity sampling{% #diversity-sampling %}

Diversity sampling scans through the **service entry spans** and retains for 30 days:

- At least one span (and the associated trace) for each combination of environment, service, operation, and resource every 15 minutes at most, to ensure that you can always find example traces in [service](https://docs.datadoghq.com/tracing/services/service_page/) and [resource](https://docs.datadoghq.com/tracing/services/resource_page/) pages, even for low traffic endpoints.
- High latency spans for the `p75`, `p90`, and `p95` percentile spans (and the associated trace) for each combination of environment, service, operation, and resource.
- A representative selection of errors, ensuring error diversity (for example, response status code 400s, 500s).

The set of data captured by diversity sampling is not uniformly sampled (that is, it is not proportionally representative of the full traffic). It is biased towards errors and high latency traces.

#### One percent flat sampling{% #one-percent-flat-sampling %}

The flat 1% sampling captures:

1. All **traces correlated with 1% of ingested RUM sessions**, ensuring all indexed sessions have associated trace data. This improves [correlation between APM and RUM](https://docs.datadoghq.com/tracing/other_telemetry/rum/), allowing you to debug user issues by viewing both frontend sessions and backend traces together. The sample is applied based on the `session_id`, meaning all traces linked to the same RUM session share a consistent indexing decision.
1. A **uniform 1% sample** of [ingested spans](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/), applied based on the `trace_id` so all spans in the same trace share the same sampling decision. Use this sample for general system health monitoring and trend analysis.

This sampling mechanism is uniform, and it is proportionally representative of the full ingested traffic. As a result, low-traffic services and endpoints might be missing from that dataset if you filter on a short time frame.

### Create your own retention filter{% #create-your-own-retention-filter %}

Create custom retention filters to retain specific trace data for 15 days. Use any span tag or attribute in the filter query to target and retain the spans that matter the most to your business.

For example, you can create filters to keep all traces for:

- Credit card transactions over $100: `@transaction_amount:>100`
- Checkout operation spans that have a duration longer than 2 seconds on the production environment: `resource_name:"GET /checkout" @duration:>2s env:prod`
- Specific versions of an online delivery service application: `service:delivery-api @version:v2.0`

When you index a span using a retention filter:

- **Searchability**: The indexed span can be found in Trace Explorer, dashboards, and monitored for 15 days.

- **Visualization context**: When you click on any indexed span in the Trace Explorer, you always see its complete trace context (all parent and child spans) in flame graph or waterfall view, regardless of whether those other spans were indexed.

- **Search context**: Although you can visualize a complete trace, only the spans that were specifically indexed by retention filters will be searchable in the Trace Explorer.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/retention_filters/retention_filter_create.4426e6a0384c180c17e6943a7353647f.png?auto=format"
   alt="Create Retention Filter" /%}

To create a retention filter:

1. Go to [**APM** > **Retention Filters**](https://app.datadoghq.com/apm/traces/retention-filters).
1. Click **Add Retention Filter**.
1. Define the **Retention Query** to target the spans you wish to retain. Use any span or attribute to filter spans, as you would write a query in the [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/?tab=listview#indexed-spans-search-with-15-day-retention).
1. Set a **Span rate** to define the percentage of spans matching this query that should be indexed.
1. Optionally, set a **Trace rate** to define the percentage of full traces associated with the spans that should be indexed. This ensures that other spans from traces associated with the span targeted by the retention query are also indexed, so that the indexed data is queryable in [Trace Queries](https://docs.datadoghq.com/tracing/trace_explorer/trace_queries).
1. Set a name for the filter.
1. Click **Add Filter** to save the filter.

{% alert level="warning" %}
Configuring a trace rate can significantly increase your indexed spans usage.
{% /alert %}

For example, if you configure a retention filter to index spans from `service:my-service`:

- Configuring a span rate of `100%` ensures that all spans matching `service:my-service` are indexed.
- Configuring a trace rate of `50%` ensures that all spans from all traces with a span from `service:my-service` are indexed. Assuming traces have 100 spans in average and 5 spans from `service:my-service`, configuring a trace rate indexes the remaining 95 spans of the trace, for the trace rate percentage being configured.

When you create a new filter or edit the retention rate of an existing filter, Datadog displays an estimate of the percentage change in global indexing volume.

Filters are retained in a serial order. If you have an upstream filter that retains spans with the `resource:POST /hello_world` tag, those spans do not show up in the **Edit** window of a downstream filter that searches for spans with the same tag because they have been retained by the upstream filter.

## Trace search and analytics on indexed spans{% #trace-search-and-analytics-on-indexed-spans %}

### In the Trace Explorer, dashboards, and notebooks{% #in-the-trace-explorer-dashboards-and-notebooks %}

By default, spans indexed by custom retention filters **and** the intelligent retention filter are included in the Trace Explorer [aggregated views](https://docs.datadoghq.com/tracing/trace_explorer/?tab=timeseriesview#indexed-spans-search-with-15-day-retention) (timeseries, toplist, table), as well as in dashboards and notebook queries.

The `retained_by` attribute is present on all retained spans. Its value is:

- `retained_by:retention_filter` if the span was captured by a custom retention filter, including the default retention filters and **no trace rate** was configured. These spans are not included in Trace Queries as trace queries require all spans of a trace to be indexed.
- `retained_by:trace_retention_filter` if the span is captured by a retention filter for which a trace rate was configured.
- `retained_by:diversity_sampling` if the span was captured by diversity sampling (part of the Intelligent retention filter).
- `retained_by:flat_sampled` if the span was indexed by the 1% flat sampling. Filter further by retention reason:
  - `@retention_reason:rum` for traces linked to RUM sessions sampled based on the `session_id`. Use this to analyze traces correlated with user sessions.
  - `@retention_reason:apm` for traces sampled uniformly based on the `trace_id`. Use this for general performance trends and system-wide analysis.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/retention_filters/trace_analytics.3ad6f52206b269d6d19edf7f88239772.png?auto=format"
   alt="Retained By facet" /%}

### In trace analytics monitors{% #in-trace-analytics-monitors %}

Spans indexed by the intelligent retention filter are **excluded** from APM trace analytics monitor evaluation.

## Further Reading{% #further-reading %}

- [Ingestion Mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms)
- [Ingestion Controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/)
- [Usage Metrics](https://docs.datadoghq.com/tracing/trace_pipeline/metrics/)
