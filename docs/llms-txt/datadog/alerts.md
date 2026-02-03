# Source: https://docs.datadoghq.com/watchdog/alerts.md

---
title: Watchdog Alerts
description: >-
  View and interpret Watchdog Alerts that proactively detect anomalies on your
  systems and applications using AI-powered monitoring.
breadcrumbs: Docs > Datadog Watchdogâ¢ > Watchdog Alerts
---

# Watchdog Alerts

## Overview{% #overview %}

Watchdog proactively looks for anomalies on your systems and applications. Each anomaly is then displayed in the [Watchdog Alert Explorer](https://docs.datadoghq.com/watchdog) with more information about what happened, the possible impact on other systems, and the root cause.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/watchdog.764cd47e3927b6742a16238848b11171.png?auto=format"
   alt="The Watchdog Alerts page with one ongoing log anomaly alert for error logs, one resolved log anomaly alert for error logs, and one resolved error rate alert resolved through root cause analysis" /%}

## Watchdog Alert details{% #watchdog-alert-details %}

An alert overview card contains the sections below:

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/alerts/alerts_overview.db3ef881bd05e9f274be666fe5bcf461.png?auto=format"
   alt="Screenshot of a Watchdog alert card, showing an elevated error rate on the send-sms endpoint in sms-service" /%}

1. **Status**: The anomaly can be `ongoing`, `resolved`, or `expired`. (An anomaly is `expired` if it has been ongoing for over 48 hours.)
1. **Timeline**: Describes the time period over which the anomaly occurs.
1. **Message**: Describes the anomaly.
1. **Graph**: Visually represents the anomaly.
1. **Tags**: Shows the scope of the anomaly.
1. [**Impact**](https://docs.datadoghq.com/watchdog/impact_analysis/) (when available): Describes which users, views, or services the anomaly affects.

Clicking anywhere on an alert overview card opens the alerts details pane.

In addition to repeating the information in the alert overview card, the **Overview** tab may contain one or more of the following fields:

- **Expected Bounds**: Click the **Show expected bounds** checkbox. The graph changes color to differentiate between expected and anomalous behavior.
- **Suggested Next Steps**: Describes steps for investigation and triage of the anomalous behavior.
- **Monitors**: Lists monitors associated with your alert. Each monitor displayed has the metric of the current alert and its associated tags included in its scope.

Additionally, Watchdog suggests one or more monitors you can create to notify you if the anomaly happens again. These monitors do not exist yet, so the table lists their status as `suggested`. Click **Enable Monitor** to enable the suggested monitor for your organization. A series of icons pops up allowing you to open, edit, clone, mute, or delete the new monitor.

## Watchdog Alert Explorer{% #watchdog-alert-explorer %}

You can use the time range, search bar, or facets to filter your Watchdog Alerts feed.

- **Time range**: Use the time range selector in the upper right to view alerts detected in a specific time range. You can view any alert that happened in the last 6 months.
- **Search bar**: Enter text in the **Filter alerts** search box to search over alert titles.
- **Facets**: The left side of the Watchdog Alerts feed contains the search facets below. Check the corresponding boxes to filter your alerts by facet.

Available facets:

| All Alerts Group  | Description                                                                                                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alert Category    | Display all `apm`, `infrastructure`, or `logs` alerts.                                                                                                                                       |
| Alert Type        | Select alerts using metrics from APM or infrastructure integrations.                                                                                                                         |
| Alert Status      | Select alerts based on their status (`ongoing`, `resolved`, or `expired`).                                                                                                                   |
| APM Primary Tag   | The [defined APM primary tag](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/) to display alerts from.                                                               |
| Environment       | The environment to display alerts from. See [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) for more information about the `env` tag. |
| Service           | The service to display alerts from. See [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) for more information about the `service` tag. |
| End User Impacted | (Requires RUM). If Watchdog found any end users impacted. See [Impact Analysis](https://docs.datadoghq.com/watchdog/impact_analysis/) for more information.                                  |
| Root Cause        | (Requires APM). If Watchdog found the root cause of the anomaly or the critical failure. See [Root Cause Analysis](https://docs.datadoghq.com/watchdog/rca/) for more information.           |
| Team              | The team owning the impacted services. Enriched from the [Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/).                                                           |
| Log Anomaly Type  | Only display log anomalies of this type. The supported types are new log patterns and increases in existing log patterns.                                                                    |
| Log Source        | Only display alerts containing logs from this source.                                                                                                                                        |
| Log Status        | Only display alerts containing logs of this log status.                                                                                                                                      |

## Watchdog Alerts coverage{% #watchdog-alerts-coverage %}

Watchdog Alerts cover multiple application and infrastructure metrics:

{% tab title="Log Management" %}
Ingested logs are analyzed at the intake level where Watchdog performs aggregations on detected patterns as well as `environment`, `service`, `source`, and `status` tags. These aggregated logs are scanned for anomalous behaviors, such as the following:

- An emergence of logs with a warning or error status.
- A sudden increase of logs with a warning or error status.

All log anomalies are surfaced as [Insights](https://docs.datadoghq.com/watchdog/insights?tab=logmanagement#explore-insights) in the Log Explorer, matching the search context and any restrictions applied to your role. Log anomalies that Watchdog determines to be particularly `severe` are surfaced in the [Watchdog Alert Explorer](https://app.datadoghq.com/watchdog) and can be alerted on by setting up a [Watchdog logs monitor](https://docs.datadoghq.com/monitors/types/watchdog/). A `severe` anomaly is defined as:

- Containing error logs.
- Lasting at least 10 minutes (to avoid transient errors).
- Having a significant increase (to avoid small increases).
- Having a low `noise` score (to avoid having a lot of alerts for a given service). The `noise` score is calculated at the service level by:
  - Looking at the number of error patterns (the higher, the noisier).
  - Computing how close the patterns are to each other (the closer, the noisier).

#### Required data history{% #required-data-history %}

Watchdog requires some data to establish a baseline of expected behavior. For log anomalies, the minimum history is 24 hours. Watchdog starts finding anomalies after the minimum required history is available, and Watchdog improves as history grows. Best performances are obtained with six weeks of history.

#### Disabling log anomaly detection{% #disabling-log-anomaly-detection %}

To disable log anomaly detection, go to the [Log Management pipeline page](https://app.datadoghq.com/logs/pipelines) and click the Log Anomalies toggle.
{% /tab %}

{% tab title="APM" %}
Watchdog scans all services and resources to look for anomalies on the following metrics:

- Error rate
- Latency
- Hits (request rate)

Watchdog filters out barely-used endpoints or services to reduce noise and avoid anomalies on small amounts of traffic. Watchdog requires at least 0.5 requests per second for an endpoint to be monitored. Additionally, if an anomaly on hit rate is detected but has no impact on latency or error rate, the anomaly is then ignored.

#### Required data history{% #required-data-history %}

Watchdog requires some data to establish a baseline of expected behavior. For metric anomalies, the minimum history is two weeks. Watchdog starts finding anomalies after the minimum required history is available, and Watchdog improves as history grows. Best performances are obtained with six weeks of history.
{% /tab %}

{% tab title="USM" %}
Watchdog scans all services and resources to look for anomalies on the following metrics:

- Error rate
- Latency
- Hits (request rate)

Watchdog filters out minimally-used endpoints and services to reduce noise and avoid anomalies on small amounts of traffic. Additionally, if an anomaly on hit rate is detected but has no impact on latency or error rate, the anomaly is ignored.

#### Required data history{% #required-data-history %}

Watchdog requires data to establish a baseline of expected behavior. For metric anomalies, the minimum history is two weeks. Watchdog starts finding anomalies after the minimum required history is available, and Watchdog improves as history grows. Best performances are obtained with six weeks of history.
{% /tab %}

{% tab title="Infrastructure" %}
Watchdog looks at infrastructure metrics from the following integrations:

- [System](https://docs.datadoghq.com/integrations/system/), for host-level memory usage (memory leaks) and TCP retransmit rate.
- [Redis](https://docs.datadoghq.com/integrations/redisdb/)
- [PostgreSQL](https://docs.datadoghq.com/integrations/postgres/)
- [MySQL](https://docs.datadoghq.com/integrations/mysql/)
- [SQLServer](https://docs.datadoghq.com/integrations/sqlserver/)
- [Cassandra](https://docs.datadoghq.com/integrations/cassandra/)
- [Oracle Database](https://docs.datadoghq.com/integrations/oracle/)
- [NGINX](https://docs.datadoghq.com/integrations/nginx/)
- [Docker](https://docs.datadoghq.com/containers/docker/?tab=standard)
- [Kubernetes](https://docs.datadoghq.com/containers/kubernetes/installation/?tab=operator)
- [Amazon Web Services](https://docs.datadoghq.com/integrations/amazon_web_services/):
  - [S3](https://docs.datadoghq.com/integrations/amazon_s3/)
  - [ELB/ALB/NLB](https://docs.datadoghq.com/integrations/amazon_elb/)
  - [CloudFront](https://docs.datadoghq.com/integrations/amazon_cloudfront/)
  - [DynamoDB](https://docs.datadoghq.com/integrations/amazon_dynamodb/)
  - [RDS](https://docs.datadoghq.com/integrations/amazon_rds/)
  - [ECS](https://docs.datadoghq.com/containers/amazon_ecs/?tab=awscli)
  - [Lambda](https://docs.datadoghq.com/serverless/)

#### Required data history{% #required-data-history %}

Watchdog requires some data to establish a baseline of expected behavior. For metric anomalies, the minimum history is two weeks. Watchdog starts finding anomalies after the minimum required history is available, and Watchdog improves as history grows. Best performances are obtained with six weeks of history.
{% /tab %}

### Custom anomaly detection{% #custom-anomaly-detection %}

Watchdog uses the same seasonal algorithms that power monitors and dashboards. To look for anomalies on other metrics or to customize the sensitivity, the following algorithms are available:

- [Anomaly monitors](https://docs.datadoghq.com/monitors/types/anomaly/)
- [Forecast monitors](https://docs.datadoghq.com/monitors/types/forecasts/?tab=linear)
- [Outlier monitors](https://docs.datadoghq.com/monitors/types/outlier/?tab=dbscan)

## Where to find Watchdog Alerts{% #where-to-find-watchdog-alerts %}

Watchdog Alerts appear in the following places within Datadog:

- The [Watchdog Alert Explorer](https://docs.datadoghq.com/watchdog)
- On any individual [APM Service Page](https://docs.datadoghq.com/tracing/services/service_page/)
- In the [Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/)
- In the [Watchdog Insights panel](https://docs.datadoghq.com/watchdog/insights?tab=logmanagement#explore-insights), available on all explorers

### Watchdog binoculars on APM pages{% #watchdog-binoculars-on-apm-pages %}

When Watchdog detects an irregularity in an APM metric, the pink Watchdog binoculars icon appears next to the impacted service in the [APM Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/).

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/service_list.af569edac3df23fbf166325736381f28.png?auto=format"
   alt="Screenshot of the Software Catalog, showing 5 services. A pink binoculars icon follows the name of the web-store service." /%}

You can see greater detail about a metric anomaly by navigating to the top of a [Service Page](https://docs.datadoghq.com/tracing/services/service_page/) with the [Watchdog Insights](https://docs.datadoghq.com/watchdog/insights?tab=logmanagement#explore-insights) carousel.

You can also find the Watchdog icon on metric graphs.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/latency_graph.9b8286d34d70b62a0d3d2c950b9ef9eb.png?auto=format"
   alt="A graph showing service latency, in seconds, on the y-axis and the time of day on the x-axis. The entire graph is highlighted in pink, and the words May 2: 13:31 Ongoing appear at the top" /%}

Click on the binoculars icon to see a Watchdog Alert card with more details.

## Manage archived alerts{% #manage-archived-alerts %}

To archive a Watchdog Alert, open the side panel and click the folder icon in the upper-right corner. Archiving hides the alert from the explorer, as well as other places in Datadog, like the home page. If an alert is archived, the pink Watchdog binoculars icon does not show up next to the relevant service or resource.

To see archived alerts, select the checkbox option to **Show *N* archived alerts** in the top left of the [Watchdog Alert Explorer](https://docs.datadoghq.com/watchdog). The option is only available if at least one alert is archived. You can see who archived each alert and when it was archived, and restore archived alerts to your feed.

**Note**: Archiving does not prevent Watchdog from flagging future issues related to the service or resource.
