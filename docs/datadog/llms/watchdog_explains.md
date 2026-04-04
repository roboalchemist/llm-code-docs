# Source: https://docs.datadoghq.com/dashboards/graph_insights/watchdog_explains.md

---
title: Watchdog Explains
description: >-
  Automatically detect anomalies in timeseries graphs and identify contributing
  tags for faster root cause analysis.
breadcrumbs: Docs > Dashboards > Graph Insights > Watchdog Explains
---

# Watchdog Explains

## Overview{% #overview %}

Watchdog Explains is an investigation assistant that detects anomalies on timeseries graphs and identifies which tags contribute to them. This allows you to immediately focus your investigation on problematic areas of your infrastructure or software stack.

To disable Watchdog Explains, see Disabling anomaly detection.

{% alert level="info" %}
Watchdog Explains is available for [Timeseries widgets](https://docs.datadoghq.com/dashboards/widgets/timeseries/) with **Metric** data (avg, sum, min, and max aggregation).
{% /alert %}

## How Watchdog Explains detects anomalies{% #how-watchdog-explains-detects-anomalies %}

Watchdog Explains applies anomaly detection to graphs on your dashboard by analyzing both the shape and value of the underlying timeseries. It identifies deviations from historical patterns, flagging spikes, dips, or gradual drifts that don't align with expected behavior.

To account for seasonality, the algorithm looks back up to three weeks in time. For example, if a spike appears on a Monday at 9:00 a.m., Watchdog compares that datapoint against previous Mondays at the same hour. If similar patterns appear consistently, the spike is treated as **seasonal** and not flagged as an anomaly. This helps reduce false positives and ensures that only unexpected deviations are surfaced.

Anomalies can be sharp spikes or drops, but may also be more subtle trends like step changes or slope shifts.

{% alert level="info" %}
Anomaly detection in Watchdog Explains works with **Metrics data** (avg, sum, min, and max aggregation).
{% /alert %}

## Watchdog Explains isolates the cause with dimensional analysis{% #watchdog-explains-isolates-the-cause-with-dimensional-analysis %}

You can start your investigation from any timeseries graph that uses metric data. When Watchdog Explains detects an anomaly, it highlights the affected region with a pink box. To begin investigating, click **Investigate Anomaly**.

This opens a full-screen investigation view. Watchdog analyzes the anomaly and surfaces any tag groups that significantly contributed to the shape or scale of the anomaly. Click on a tag to see how removing or isolating that dimension affects the graph. Use this to identify root causes like specific customers, services, or environments.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/graph_insights/watchdog_explains/isolation_tag_breakdown.2a2f3260352864de409a0a0e88197d0b.png?auto=format"
   alt="Tag breakdown in Watchdog Explains investigation" /%}

## Disabling anomaly detection{% #disabling-anomaly-detection %}

{% alert level="info" %}
You can disable anomaly scanning on any dashboard. This only affects your view, other dashboard viewers still see anomalies unless they turn it off.
{% /alert %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/graph_insights/watchdog_explains/disable_anomaly_detection.a9302b973b2442a13b77def87dc80276.png?auto=format"
   alt="Disabling anomaly detection in Watchdog Explains" /%}

To disable anomaly detection on a dashboard, open **Anomalies** at the top of the dashboard and click **Turn Off**.

## Further reading{% #further-reading %}

- [Learn more about Watchdog Insights](https://docs.datadoghq.com/watchdog/insights/)
- [Anomaly detection, predictive correlations - Using AI-assisted metrics monitoring](https://www.datadoghq.com/blog/ai-powered-metrics-monitoring/)
