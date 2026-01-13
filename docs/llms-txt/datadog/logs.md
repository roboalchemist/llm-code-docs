# Source: https://docs.datadoghq.com/containers/amazon_ecs/logs.md

# Source: https://docs.datadoghq.com/agent/logs.md

# Source: https://docs.datadoghq.com/logs.md

---
title: Log Management
description: >-
  Configure your Datadog Agent to gather logs from your host, containers &
  services.
breadcrumbs: Docs > Log Management
source_url: https://docs.datadoghq.com/index.html
---

# Log Management

{% callout %}
##### Join an enablement webinar session

Join an introductory or intermediate enablement session to learn how Datadog Log Management unifies logs, metrics, and traces in a single view, giving you rich context for analyzing log data.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=Logs)
{% /callout %}

## Overview{% #overview %}

Logging the important parts of your system's operations is crucial for maintaining infrastructure health. Modern infrastructure has the capability to generate thousands of log events per minute. In this situation, you need to choose which logs to send to a log management solution, and which logs to archive. Filtering your logs before sending them, however, may lead to gaps in coverage or the accidental removal of valuable data.

Datadog Log Management, also referred to as Datadog logs or logging, removes these limitations by decoupling log ingestion from indexing. This enables you to cost-effectively collect, process, archive, explore, and monitor all of your logs without limitations, also known as Logging without Limits*.

Logging without Limits* enables a streamlined troubleshooting experience in the [Log Explorer](https://docs.datadoghq.com/logs/explorer/), which empowers you and your teams to quickly assess and fix your infrastructure issues. It provides intuitive archiving to support your security and IT teams during audits and assessments. Logging without Limits* also powers [Datadog Cloud SIEM](https://docs.datadoghq.com/security/cloud_siem/), which detects security threats in your environment, without requiring you to index logs.

## Collect{% #collect %}

Begin [ingesting logs](https://docs.datadoghq.com/logs/log_collection/) from your hosts, containers, cloud providers, and other sources to get started with Datadog Log Management.

## Configure{% #configure %}

{% image
   source="https://datadog-docs.imgix.net/images/logs/lwl_marketecture_20231030.79cbac078b66f8f5cc423a7d3b223175.png?auto=format"
   alt="Configure your logs all in one place" /%}

Once your logs are ingested, process and enrich all your logs with pipelines and processors, provide control of your log management budget with indexes, generate metrics from ingested logs, or manage your logs within storage-optimized archives with [Log Configuration options](https://docs.datadoghq.com/logs/log_configuration/).

## Connect{% #connect %}

{% image
   source="https://datadog-docs.imgix.net/images/logs/connect.1c3ff6a547ac0a235559fb5c18f98510.png?auto=format"
   alt="Correlate logs with metrics or traces" /%}

Leverage the pillars of observability by connecting your logs to metrics and traces:

- [Connect your logs and traces](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/) to gain observability into your applications.
- [Correlate your logs and metrics](https://docs.datadoghq.com/logs/guide/correlate-logs-with-metrics/) to gain context of an issue and map it throughout your service.

## Explore{% #explore %}

Start exploring your ingested logs in the [Log Explorer](https://docs.datadoghq.com/logs/explorer/).

**Tip**: To open the Log Explorer from Datadog's global search, press `Cmd`/`Ctrl` + `K` and search for `logs`.

{% image
   source="https://datadog-docs.imgix.net/images/logs/explore.b937574cd932232459c1c5746146a353.png?auto=format"
   alt="Explore your ingested logs" /%}

- [Search](https://docs.datadoghq.com/logs/explorer/search_syntax/): Search through all of your logs.
- [Live Tail](https://docs.datadoghq.com/logs/live_tail/): See your ingested logs in real time across all your environments.
- [Analytics](https://docs.datadoghq.com/logs/explorer/analytics/): Perform Log Analytics over your indexed logs.
- [Patterns](https://docs.datadoghq.com/logs/explorer/patterns/): Spot log patterns by clustering your indexed logs together.
- [Saved Views](https://docs.datadoghq.com/logs/explorer/saved_views/): Use saved views to automatically configure your Log Explorer.

{% callout %}
##### Try Introduction to Log Management in the Learning Center

Learn without cost on real cloud compute capacity and a Datadog trial account. Enroll today to learn more about log collection, querying, analytics, metrics, monitoring, processing, storage, and access control.

[ENROLL NOW](https://learn.datadoghq.com/courses/intro-to-log-management)
{% /callout %}

## Further Reading{% #further-reading %}



- [Check out the latest Datadog Log Management releases (App login required)](https://app.datadoghq.com/release-notes?category=Log%20Management)
- [Start collecting your logs](https://docs.datadoghq.com/logs/log_collection/)
- [Introduction to Log Management](https://learn.datadoghq.com/courses/intro-to-log-management)
- [Join an interactive session to optimize your Log Management](https://dtdg.co/fe)
- [Accelerate Incident Investigations with Log Anomaly Detection](https://www.datadoghq.com/blog/accelerate-incident-investigations-with-log-anomaly-detection/)
- [Monitor your IoT devices at scale with Datadog Log Management](https://www.datadoghq.com/blog/monitor-iot-devices-at-scale-with-log-management/)
- [Monitor your firewall logs with Datadog](https://www.datadoghq.com/blog/monitoring-firewall-logs-datadog/)
- [Use CIDR notation queries to filter your network traffic logs](https://www.datadoghq.com/blog/cidr-queries-datadog-log-management/)
- [Monitor 1Password with Datadog Cloud SIEM](https://www.datadoghq.com/blog/monitor-1password-datadog-cloud-siem/)
- [Filter and correlate logs dynamically using Subqueries](https://www.datadoghq.com/blog/filter-logs-by-subqueries-with-datadog/)
- [Monitor DNS logs for network and security analysis](https://www.datadoghq.com/blog/monitor-dns-logs-for-network-and-security-datadog/)
- [A guide to Log Management Indexing Strategies with Datadog](https://www.datadoghq.com/architecture/a-guide-to-log-management-indexing-strategies-with-datadog/)
- [Search your historical logs more efficiently with Datadog Archive Search](https://www.datadoghq.com/blog/archive-search/)
\*Logging without Limits is a trademark of Datadog, Inc.

