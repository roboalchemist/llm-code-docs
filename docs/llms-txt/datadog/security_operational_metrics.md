# Source: https://docs.datadoghq.com/security/cloud_siem/respond_and_report/security_operational_metrics.md

---
title: Security Operational Metrics
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Respond (SOAR) and Report > Security
  Operational Metrics
---

# Security Operational Metrics

## Overview{% #overview %}

Cloud SIEM provides security operational metrics to help you determine the effectiveness of your team in responding to and resolving security threats to your cloud environments. These metrics are shown in the out-of-the-box [Cloud SIEM dashboard](https://app.datadoghq.com/dash/integration/30378/cloud-siem-overview) and are sent in the Cloud SIEM [weekly digest reports](https://app.datadoghq.com/security/configuration/reports). You can also create dashboards and monitors for them.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/secops_metrics.7f0478a2cc9f843c6134986ddb2f8f96.png?auto=format"
   alt="The security operational metrics section of the Cloud SIEM Overview dashboard" /%}

## Operational metrics{% #operational-metrics %}

{% dl %}

{% dt %}
`datadog.security.siem_signal.time_to_detect`
{% /dt %}

{% dd %}
**Name**: Time to Detect (TTD)
{% /dd %}

{% dd %}
**Description**: The time (in seconds) between when a matching log is triggered and when a signal is generated.
{% /dd %}

{% dd %}
**Metric type**: [DISTRIBUTION](https://docs.datadoghq.com/metrics/types/?tab=distribution#metric-types)
{% /dd %}

{% dt %}
`datadog.security.siem_signal.time_to_acknowledge`
{% /dt %}

{% dd %}
**Name**: Time to Acknowledge (TTA)
{% /dd %}

{% dd %}
**Description**: The time (in seconds) between when a signal is triggered and when an investigation on the signal begins.
{% /dd %}

{% dd %}
**Metric type**: [DISTRIBUTION](https://docs.datadoghq.com/metrics/types/?tab=distribution#metric-types)
{% /dd %}

{% dt %}
`datadog.security.siem_signal.time_to_investigate`
{% /dt %}

{% dd %}
**Name**: Time to Investigate (TTI)
{% /dd %}

{% dd %}
**Description**: The time (in seconds) between when an investigation on the signal begins and when the signal is archived.
{% /dd %}

{% dd %}
**Metric type**: [DISTRIBUTION](https://docs.datadoghq.com/metrics/types/?tab=distribution#metric-types)
{% /dd %}

{% dt %}
`datadog.security.siem_signal.time_to_resolve`
{% /dt %}

{% dd %}
**Name**: Time to Resolve (TTR)
{% /dd %}

{% dd %}
**Description**: The time (in seconds) it takes to archive a signal starting from the time when you are first notified of the detection.
{% /dd %}

{% dd %}
**Metric type**: [DISTRIBUTION](https://docs.datadoghq.com/metrics/types/?tab=distribution#metric-types)
{% /dd %}

{% /dl %}

## How the metrics are calculated{% #how-the-metrics-are-calculated %}

The TTD, TTA, and TTR metrics are calculated based on these timestamps:

1. The timestamp (`T0`) of the log that triggers a security signal.
1. The timestamp (`T1`) of when the signal is generated.
1. The timestamp (`T2`) of when the signal status is changed to `under_review`.
1. The timestamp (`T3`) of when the signal status is changed to `archived`.

| Metric                                                                      | How the metric is calculated |
| --------------------------------------------------------------------------- | ---------------------------- |
| Time to Detect (TTD)`datadog.security.siem_signal.time_to_detect`           | `T1 - T0`                    |
| Time to Acknowledge (TTA)`datadog.security.siem_signal.time_to_acknowledge` | `T2 - T1`                    |
| Time to Investigate (TTI)`datadog.security.siem_signal.time_to_investigate` | `T3 - T2`                    |
| Time to Resolve (TTR)`datadog.security.siem_signal.time_to_resolve`         | `T3 - T1`                    |

## Explore, visualize, and monitor the metrics{% #explore-visualize-and-monitor-the-metrics %}

Use the [Metrics Summary](https://docs.datadoghq.com/metrics/types/?tab=distribution#metric-types) to see metadata and tags for the operational metrics. You can also see which dashboards, notebooks, monitors, and SLOs are using those metrics.

Use tags to filter the metrics to specific teams, sources, and environments. You can then create [dashboards](https://docs.datadoghq.com/getting_started/dashboards/) for those metrics to visualize the data or create [monitors](https://docs.datadoghq.com/getting_started/monitors/) to alert you if the metrics exceed a specified threshold.

## Further reading{% #further-reading %}

- [Investigate Cloud SIEM Security Signals](https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigate_security_signals)
- [Getting started with dashboards](https://docs.datadoghq.com/getting_started/dashboards)
- [Getting started with monitors](https://docs.datadoghq.com/getting_started/monitors)
- [Learn more about the Metrics Summary](https://docs.datadoghq.com/metrics/summary/)
