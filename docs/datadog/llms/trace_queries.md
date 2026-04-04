# Source: https://docs.datadoghq.com/tracing/trace_explorer/trace_queries.md

---
title: Trace Queries
description: Trace Queries
breadcrumbs: Docs > APM > Trace Explorer > Trace Queries
---

# Trace Queries

## Overview{% #overview %}

With Trace Queries, you can find entire traces based on the properties of multiple spans and the relationships between those spans within the structure of the trace. To create a trace query, you define two or more [span queries](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/) and then specify the relationship within the searched-for trace structure of the spans that are returned by each span query.

You can search, filter, group, and visualize the traces from the Trace Query explorer.

With structure-based trace querying, you can answer questions such as:

- Which traces include a dependency between two services (`service A` has a downstream call to `service B`)?
- What API endpoints are affected by my erroring backend service?

Use Trace Queries to accelerate your investigations and find relevant traces.

## Trace query editor{% #trace-query-editor %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_queries/trace_query_editor.daba8723b654f496cb72b12e38b1c97d.png?auto=format"
   alt="Trace Query editor" /%}

A trace query is composed of two or more span queries, joined by trace query operators.

### Span queries{% #span-queries %}

Query for spans from a specific environment, service, or endpoint using the [Span query syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/). Use autocomplete suggestions to view facets and recent queries.

Click **Add another span query** to add a span query and use it in the trace query statement.

### Trace query operators{% #trace-query-operators %}

Combine multiple span queries, labeled `a`, `b`, `c`, and so on, into a trace query in the **Traces matching** field, using operators between the letters that represent each span query:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_queries/traces_matching.70dcd85a1656eb9e5b0e35b1d40e4041.png?auto=format"
   alt="Span queries combined into a trace query" /%}

| Operator | Description                                                                                                                              | Example                                                                                                                                           |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `&&`     | **And**: Both spans are in the trace                                                                                                     | Traces that contain spans from the service `web-store` and spans from the service `payments-go`:`service:web-store && service:payments-go`        |
| `||`     | **Or**: One or the other span are in the trace                                                                                           | Traces that contain spans from the service `web-store` or from the service `mobile-store`:`service:web-store || service:mobile-store`             |
| `->`     | **Indirect relationship**: Traces that contain a span matching the left query that is upstream of spans matching the right query         | Traces where the service `checkoutservice` is upstream of the service `quoteservice`:`service:checkoutservice -> service:quoteservice`            |
| `=>`     | **Direct relationship**: Traces that contain a span matching the left query that is the direct parent of a span matching the right query | Traces where the service `checkoutservice` is directly calling the service `shippingservice`:`service:checkoutservice => service:shippingservice` |
| `NOT`    | **Exclusion**: Traces that **do not** contain spans matching the query                                                                   | Traces that contain spans from the service `web-store`, but not from the service `payments-go`:`service:web-store && NOT(service:payments-go)`    |

### Trace-level filters{% #trace-level-filters %}

Filter the result set of traces further by applying filters on trace-level attributes like the number of spans or the end-to-end duration of the trace in the **Where** statement:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_queries/where_statement.bdbce3f65e1f7282aea6db3bff5204c8.png?auto=format"
   alt="Trace-level filters example" /%}

| Filter             | Description                     | Example                                                                                                                                                                                       |
| ------------------ | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `span_count(a)`    | Number of occurrences of a span | Traces that contain more than 10 calls to a mongo database:- **queryA**:`service:web-store-mongo @db.statement:"SELECT * FROM stores`- **Traces matching**:`a`- **Where**:`span_count(a):>10` |
| `total_span_count` | Number of spans in the trace    | Traces that contain more than 1000 spans:**Where**`total_span_count:>1000`                                                                                                                    |
| `trace_duration`   | End to end trace duration       | Traces for which the end-to-end execution time is more than 5 seconds :**Where**:`trace_duration:>5s`                                                                                         |

## Flow Map{% #flow-map %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_queries/trace_flow_map.d05ebd5306ff35a55d07968b909fbb0b.png?auto=format"
   alt="Trace Flow Map" /%}

The Flow Map helps you understand the request path and service dependencies from the resulting traces that match the Trace Query. Use the map to identify error paths, unusual service dependencies, or abnormally high request rates to a database.

**Note**: The Flow Map is powered by a sample of the ingested traffic.

Service nodes that match span queries are highlighted to show you which parts of the trace your query conditions are targeting.

To get more information about **a single service**, hover on the service's node to see its metrics for request rate and error rate. To see metrics for the request rate and the error rate **between two services**, hover on an edge connecting the two services.

To filter out traces that do not contain a dependency on a particular service, click on the service's node on the map.

## Trace list{% #trace-list %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_queries/trace_list.ab883f1d0c092510922c052699a17a13.png?auto=format"
   alt="Trace List" /%}

The Trace list shows up to fifty sample traces that match the query and are within the selected time range. Hover on the Latency Breakdown to get a sense of where (in which services) time is spent during the request execution.

**Note**: Information displayed in the table are attributes from the root span of the trace, including the duration, which **does not** represent the end-to-end duration of the trace.

## Analytics{% #analytics %}

Select one of the other visualizations, such as `Timeseries`, `Top List`, or `Table` to aggregate results over time, grouped by one or multiple dimensions. Read [Span Visualizations](https://docs.datadoghq.com/tracing/trace_explorer/visualize/#timeseries) for more information on the aggregation options.

In addition to those aggregation options, you must also select which span query (`a`, `b`, `c`, and so on) you want to aggregate the spans from. Select the query that matches the spans from which you're using the tags and attributes in the aggregation options.

For example, if you query for traces that contain a span from the service `web-store` (query `a`) and a span from the service `payments-go` with some errors (query `b`), and you visualize a count of spans grouped by `@merchant.tier`, use spans from query `a`, because `merchant.tier` is an attribute from the spans of the service `web-store`, not from the service `payments-go`.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_queries/timeseries_using_spans_from.c9facacd18ce707894388705c608314e.png?auto=format"
   alt="Timeseries view" /%}

## How Trace Queries source data{% #how-trace-queries-source-data %}

Trace Queries run on traces indexed by the [intelligent retention filter](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#datadog-intelligent-retention-filter) and [trace-level retention filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#create-your-own-retention-filter).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_queries/trace_queries_base_data.2fc2b2e527928ffd4af20fcb9cd5c75c.png?auto=format"
   alt="Flow showing where trace retention filters apply in the processing pipeline" /%}

The intelligent retention filter is enabled by default and includes:

- [Flat sampling](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#one-percent-flat-sampling): Retains all traces correlated with 1% of ingested RUM sessions, plus a uniform 1% sample of ingested spans, ensuring correlation between frontend sessions and backend traces.
- [Diversity sampling](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#diversity-sampling): Retains a diverse set of traces to maintain visibility across environments, services, operations, and resources.

Both Flat sampling and Diversity sampling capture **complete traces**, meaning all spans within a trace are indexed to ensure accurate results in Trace Queries.

Trace-level retention filters are configurable. Use a filter query to target spans by any tag or attribute and retain the most critical traces. Setting a trace rate ensures that the filter retains all spans of a trace so you can query those traces in Trace Queries.

## Further Reading{% #further-reading %}

- [Analyze the root causes and business impact of production issues with Trace Queries](https://www.datadoghq.com/blog/trace-queries/)
- [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer)
- [Span Query Syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/)
