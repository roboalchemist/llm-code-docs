# Source: https://docs.datadoghq.com/tracing/trace_explorer/visualize.md

---
title: Span Visualizations
description: View spans in a list, or aggregate spans into timeseries, top lists and more.
breadcrumbs: Docs > APM > Trace Explorer > Span Visualizations
---

# Span Visualizations

## Overview{% #overview %}

Visualizations define how the queried span data is displayed. Select relevant visualizations to surface valuable information, such as a **list** for individual events, or as **timeseries** or **top lists** for aggregates.

## List view{% #list-view %}

The list view displays a list of spans that match the selected context, defined by the [search bar query](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/#search-syntax) filter and a [time range](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/#time-range).

In the table, choose which information of interest to display as columns. Manage the columns by either:

- interacting with the table header row to **sort**, **rearrange**, or **remove** columns.
- selecting a facet from the facet panel on the left, or from the trace side panel after clicking on a specific span, to **add** a column for a field. You can also add columns from with the **Options** button.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/list_view_table_controls.mp4" /%}

The default sort for spans in the list visualization is by timestamp, with the most recent spans on top. To surface spans with lowest or highest value for a measure first, or to sort your spans lexicographically for the value of a tag, specify that column as the **by** column.

The configuration of the columns is stored alongside other elements of your troubleshooting context in saved views.

The `Latency Breakdown` of the trace might be missing for some spans if the trace is malformed or incomplete. For instance, the error and the rare samplers capture pieces of traces, without the guarantee of capturing the complete trace. In this case, the data is omitted to avoid displaying inconsistent or misleading latency information that would only make sense when the trace is complete.

When the query is filtered on error spans, select the **Group into Issues** option to visualize a list of [Error Tracking](https://docs.datadoghq.com/tracing/error_tracking/) issues instead of individual error spans. Click on any issue in the issue list to open the issue panel and access additional information about this group of errors.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/trace_explorer_issue_grouping.11cae3fc0491d4e1fc4b4bcc20f3bcbc.png?auto=format"
   alt="Error Tracking Issue Grouping" /%}

From the issue details, click `See all errors` to view individual error spans grouped under this issue.

**Note**:Switch back to the `Errors` grouping to view individual errors, including non fingerprinted errors, i.e. errors without associated issue.

## Timeseries{% #timeseries %}

Use timeseries to visualize the evolution of a [measure](https://docs.datadoghq.com/tracing/trace_explorer/facets/#quantitative-facets-measures) (or a count of unique tag values) over a selected time frame, and optionally split the data by up to three tags (grouping).

**Note**: The [Live Explorer](https://docs.datadoghq.com/tracing/trace_explorer/?tab=timeseriesview#live-search-for-15-minutes) (15 minutes) allows grouping by only one dimension.

Aggregated views use additional query options, to define the **measured tag dimension**, the dimensions to **group** the query by, and the **aggregation period**. For example:

1. Choose to view the `Duration` measure.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/group_by_measured_dimension.4568e1b385405165d4dfd1a503b040da.png?auto=format"
      alt="Measured Dimension" /%}

1. Select the aggregation function for the `Duration` measure. Selecting a measure lets you choose the aggregation function whereas selecting a qualitative attribute displays the unique count.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/group_by_aggregation_function.f3af097daa1dfe87e21344678fecb520.png?auto=format"
      alt="Aggregation Function" /%}

1. Group the query by a dimension, for example, `Resource`.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/group_by_dimension.9c53c2039c248f0fb3f39f85bf7e2306.png?auto=format"
      alt="Split Dimension" /%}

1. Choose to display a number of either top or bottom values according to the selected tag.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/group_by_top_bottom.d2f96909eb947b36add14714432b1350.png?auto=format"
      alt="Top Bottom X values" /%}

1. Choose the rollup period, for example, `10min`.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/group_by_rollup_period.22a04630adea45d774d598a67ec7dded.png?auto=format"
      alt="Rollup Period" /%}

The following Trace Explorer timeseries view shows the evolution of the top ten resource names of the service `shopist-web-ui` according to the 95th percentile of `Duration` over the past four hours:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/timeseries_view.b20d272a5a83387312a3e5dcd7cd81b8.png?auto=format"
   alt="Timeseries view" /%}

Choose additional display options for timeseries: the **roll-up interval**, whether you **display** results as **bars** (recommended for counts and unique counts), **lines** (recommended for statistical aggregations) or **areas**, and the **colorset**.

## Top list{% #top-list %}

Use a top list to visualize a span count, a count of unique tag values, or a measure split by one tag dimension.

For example, the following top list shows the top ten website customers that experienced an error at checkout over the past day, based on the span count.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/top_list_view.d0396b47ce8e482c1f6d52d7b9bce16c.png?auto=format"
   alt="Top list view" /%}

## Table{% #table %}

Use a table to visualize the top values from up to three dimension combinations according to a chosen measure or span count.

**Note**: A table visualization grouped by a single dimension is the same as a Top List, just with a different display.

The following table shows the error spans count by `Env`, `Service`, and `Error type`.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/visualize/table_view.11a181a8364195b69241adf35001c417.png?auto=format"
   alt="Table view" /%}

## Request Flow Map{% #request-flow-map %}

[Request flow maps](https://app.datadoghq.com/apm/flow-map) combine APM's [service map](https://docs.datadoghq.com/tracing/services/services_map/) and [live exploring](https://docs.datadoghq.com/tracing/trace_explorer/) features to illustrate request paths through your stack. Scope your traces to any combination of tags and generate a dynamic map that represents the flow of requests between every service.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/live_search_and_analytics/request_flow_map/Overview.234c34ed4fdff0152cde4978b6bd4f13.png?auto=format"
   alt="Request flow map showing the flow of requests between services, as well as request times and error rates" /%}

For example, you can use request flow maps to identify high-traffic services or track the number of database calls generated by a request to a specific endpoint. If you use [shadow deployments](https://docs.datadoghq.com/tracing/services/deployment_tracking/#shadow-deploys) or feature flags set as custom span tags, you can use request flow maps to compare request latencies between requests and anticipate how code changes will impact perforamnce.

### Navigating the request flow map{% #navigating-the-request-flow-map %}

- Hover over the edge that connects two services to see metrics for requests, errors, and latencies between those services. **Note**: Highlighted edges represent the highest throughput connections, or the most common paths.

- Click **Export** to save a PNG image of the current request flow map. Use this feature to generate a live architecture diagram or one scoped to a specific user flow.

- Click any service on the map to view health, performance, infrastructure, and runtime metrics for that service.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/live_search_and_analytics/request_flow_map/ServicePanel.00b6a22bd4b803054e54ac1c0dd8fda3.png?auto=format"
   alt="Request flow map side panel with metrics and metadata for the selected service" /%}

- The map automatically selects an appropriate layout based on the number of services present. Click **Cluster** or **Flow** to switch between the layouts.

- RUM Applications are represented on the request flow map if you have [connected RUM and Traces](https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm?tab=browserrum).

{% video
   url="https://datadog-docs.imgix.net/images/tracing/live_search_and_analytics/request_flow_map/RUMService.mp4" /%}

## Further Reading{% #further-reading %}

- [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/)
- [Learn more about Request Flow Maps](https://www.datadoghq.com/blog/apm-request-flow-map-datadog)
