# Source: https://docs.datadoghq.com/dashboards/guide/quick-graphs.md

---
title: Quick Graphs
description: >-
  Create graphs quickly from anywhere in Datadog using the Quick Graphs editor
  with keyboard shortcuts or global search.
breadcrumbs: Docs > Dashboards > Graphing Guides > Quick Graphs
---

# Quick Graphs

## Overview{% #overview %}

You can use Quick Graphs to graph your data from anywhere in Datadog.

Open the Quick Graphs editor with any of the following:

- Pressing `G` on any page.
- The global search (`Cmd+K` on MacOS, `Ctrl+K` on Windows) menu.
- The dashboards submenu.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/quick_graph_editor.03aae673c89fda9c3f43754c42da5d12.png?auto=format"
   alt="quick graph editor" /%}

## Graph your data{% #graph-your-data %}

### Graphing metrics{% #graphing-metrics %}

To query metrics, follow this process outlined in [Dashboard Querying](https://docs.datadoghq.com/dashboards/querying/#define-the-metric):

1. [Choose the metric to graph](https://docs.datadoghq.com/dashboards/querying/#define-the-metric).
1. [Filter](https://docs.datadoghq.com/dashboards/querying/#filter).
1. [Aggregate and rollup](https://docs.datadoghq.com/dashboards/querying/#aggregate-and-rollup).
1. [Apply additional functions](https://docs.datadoghq.com/dashboards/querying/#advanced-graphing).

### Graphing events{% #graphing-events %}

This section provides a brief overview of querying event platform data sources such as [Logs](https://docs.datadoghq.com/logs/explorer/), [APM](https://docs.datadoghq.com/tracing/trace_explorer/), [RUM](https://docs.datadoghq.com/real_user_monitoring/explorer/search/), [Security](https://docs.datadoghq.com/security/), [Events](https://docs.datadoghq.com/events/), [CI Pipelines](https://docs.datadoghq.com/continuous_integration/pipelines/), [CI Tests](https://docs.datadoghq.com/continuous_integration/tests/), and [Findings](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/findings/). Choose the event data source using the dropdown which is defaulted to **Metrics**.

To query event data, follow this process:

1. **Filter:** Narrow down, broaden, or shift your focus on the subset of data of current interest. The top field allows you to input a search query mixing key:value and full-text search.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/quick_graph_event_filter.c9b65700b37081026037c61346bbd85d.png?auto=format"
   alt="event filtering" /%}
**Choose the measure or facet:** Measure lets you choose the aggregation function whereas facet displays the unique count.
{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/quick_graph_event_measure.db22f58615d6d2eb589a38a47963d2c7.png?auto=format"
   alt="choosing measure" /%}
**Aggregate:** If you are graphing a measure, select the aggregation function for the measure you want to graph and use a facet to split your graph.
{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/quick_graph_event_group.42676a6f11ebadf142d36ce7baa8a8d3.png?auto=format"
   alt="choosing aggregation" /%}

**Rollup:** Choose the time interval for your graph. Changing the global timeframe changes the list of available timestep values.

**[Apply additional functions](https://docs.datadoghq.com/dashboards/querying/#advanced-graphing)** (same as metrics).

## Select a visualization{% #select-a-visualization %}

Quick Graphs supports:

- [Timeseries](https://docs.datadoghq.com/dashboards/widgets/timeseries/)
- [Top List](https://docs.datadoghq.com/dashboards/widgets/top_list/)
- [Query value](https://docs.datadoghq.com/dashboards/widgets/query_value/)
- [Geomap](https://docs.datadoghq.com/dashboards/widgets/geomap/)

## Give your graph title{% #give-your-graph-title %}

If you do not enter a title, one is automatically generated based on your selections. However, it is recommended that you create a title that describes the purpose of the graph.

## Export & share{% #export--share %}

Click **Export** to save your work to a Dashboard or Notebook. You can always come back to the editor to change the graph. If want to share a link directly to your graph without a Dashboard or Notebook, click **Copy to Clipboard**.
