# Source: https://docs.datadoghq.com/dashboards/graph_insights.md

---
title: Graph Insights
description: >-
  Discover potential root causes using Metric Correlations and Watchdog Explains
  to analyze irregular metric behavior.
breadcrumbs: Docs > Dashboards > Graph Insights
---

# Graph Insights

## Overview{% #overview %}

Graph insights can help you find potential root causes for an observed issue by searching for other metrics that exhibited irregular behavior around the same time. Metric Correlations scans your metrics from different sources, such as dashboards, integrations, APM, and custom metrics.

## Metric Correlations{% #metric-correlations %}

{% alert level="info" %}
Metric Correlations is available for [Timeseries widgets](https://docs.datadoghq.com/dashboards/widgets/timeseries/) with the **Metric** data source.
{% /alert %}

To target the search more effectively, Metric Correlations uses information about related dashboards and services. Correlations can sift through metrics from various sources, including APM, integrations, and dashboards, as well as arbitrary metric namespaces you select. It searches for irregularities in other metrics over the corresponding time period, enabling Datadog to automatically provide clues that facilitate a more efficient root cause analysis.

For more information, see the [Metric Correlations](https://docs.datadoghq.com/dashboards/graph_insights/correlations/) documentation.

## Watchdog Explains{% #watchdog-explains %}

{% alert level="info" %}
Watchdog Explains is available for [Timeseries widgets](https://docs.datadoghq.com/dashboards/widgets/timeseries/) with the **Metric** data source.
{% /alert %}

Datadog collects various types of data to provide insights into application performance, including metrics, traces, and logs, which tell you what, how, and why something is happening. Watchdog Explains analyzes high-level trends such as latency, error rates, or request count evolution to detect critical signals. Upon observing a spike in these graphs, Watchdog Explains helps you investigate the immediate questions:

- What is the source of the spike?
- Does this anomaly affect everyone or is an isolated incident?

For more information, see the [Watchdog Explains](https://docs.datadoghq.com/dashboards/graph_insights/watchdog_explains/) documentation.

## Further reading{% #further-reading %}

- [Learn more about Watchdog Insights](https://docs.datadoghq.com/watchdog/insights/)
- [Anomaly detection, predictive correlations - Using AI-assisted metrics monitoring](https://www.datadoghq.com/blog/ai-powered-metrics-monitoring/)
