# Source: https://docs.datadoghq.com/dashboards/graph_insights/correlations.md

---
title: Metric Correlations
description: >-
  Find potential root causes by discovering metrics with irregular behavior that
  correlate with observed issues.
breadcrumbs: Docs > Dashboards > Graph Insights > Metric Correlations
---

# Metric Correlations

## Overview{% #overview %}

{% alert level="info" %}
Metric Correlations is available for [Timeseries widgets](https://docs.datadoghq.com/dashboards/widgets/timeseries/) with the **Metric** data source.
{% /alert %}

Metric Correlations can help you find potential root causes for an observed issue by searching for other metrics that exhibited irregular behavior around the same time. Correlations scans your metrics from different sources such as dashboards, integrations, APM, and custom metrics.

## Find correlated metrics{% #find-correlated-metrics %}

You can start your metric correlations exploration from any of your dashboards, notebooks, APM, Watchdog alerts, or monitor status pages.

- Left click on any graph and select **Find correlated metrics**.
- From a full-screen graph, click the **Correlations** tab.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/correlations/find_correlated_metrics.f3d011516bbb57ab3dfe3cda321e58e2.png?auto=format"
   alt="Dashboard graph menu option find correlated metrics" /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/correlations/correlations_tab.f645bbc5e143989e1fc1944cd9a96077.png?auto=format"
   alt="Dashboard search" /%}

Correlations *tries* to automatically detect the area of interest (anomalous behavior) for your metric. If the area of interest is not selected automatically or needs adjustment, you can manually draw the area of interest from the edit search option. Datadog searches for other metrics that exhibit anomalous behavior at times matching the area of interest.

**Note**: Correlation searches are available for a single metric. For graphs with multiple metrics, select the series of interest. From a full-screen graph, select one series on the graph legend, then click the **Correlations** tab.

## Customize your search{% #customize-your-search %}

You can customize the default search parameters of correlations. From a full-screen graph, on the *Correlations* tab, click the **Edit Search** button, or click directly on the graph.

1. Click and drag on the graph to set the time frame for your correlations search.
1. Define the sources you want correlations to search from (APM services, integrations, dashboards, or custom metrics).
1. Select **Auto-select** or **Custom select** from specific categories. For custom metrics, at least one selection is required.
   - Custom metrics is the only category not selected by default. Choose metric namespaces or single metrics to search correlations upon.
1. Use the tag filter box to scope the search by a tag.

A list of search results is displayed below the search graph with the following:

- **Type**: A graphic representing the source type (APM service, integration, dashboard, or custom metric).
- **Source**: The name of the source for the correlated metrics.
- **Correlations**: The number of correlated metrics found.
- **Preview**: A preview graph of the correlated metrics.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/correlations/search_results.0d211a5b0427b53eb23ef702253ca5aa.png?auto=format"
   alt="Search results" /%}

As results load, you can explore the details without waiting for all results.

## Investigate{% #investigate %}

From the results list, select a row to investigate the details of that correlation.

- Similar to dashboards, hovering over a graph creates a time-synced line on all other graphs.
- To view all sources, remove the filter in the menu.
- Sources for each metric are linked by name. For example, dashboard names link to the dashboard.
- Use the export icon to export the graph to a dashboard, notebook, or copy the query.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/correlations/correlated_metric_source_details.c7a3277009c05f8095610746d7d32222.png?auto=format"
   alt="Detail view of correlated metric source" /%}

## Further Reading{% #further-reading %}

- [Datadog Dashboards](https://docs.datadoghq.com/dashboards/)
- [Datadog Notebooks](https://docs.datadoghq.com/notebooks/)
- [APM Service Page](https://docs.datadoghq.com/tracing/services/service_page/)
- [Watchdog](https://docs.datadoghq.com/watchdog/)
- [Anomaly detection, predictive correlations - Using AI-assisted metrics monitoring](https://www.datadoghq.com/blog/ai-powered-metrics-monitoring/)
- [Improve SLO accuracy and performance with Datadog Synthetic Monitoring](https://www.datadoghq.com/blog/slo-synthetic-monitoring/)
