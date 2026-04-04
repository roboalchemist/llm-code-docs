# Source: https://docs.datadoghq.com/account_management/billing/usage_monitor_apm.md

---
title: View and Alert on APM Usage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Account Management > Billing > View and Alert on APM Usage
---

# View and Alert on APM Usage

Datadog has many pricing plans to fit your needs. For more information, see the [Pricing page](https://www.datadoghq.com/pricing). Read APM documentation on [APM Billing](https://docs.datadoghq.com/account_management/billing/apm_distributed_tracing/) to understand how billing works for APM and Distributed Tracing.

## Usage page{% #usage-page %}

If you are an admin of your account, you can view your account usage using the [Usage Page](https://app.datadoghq.com/account/usage) which gets updated every 24 hours.

| Dimension         | Description                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------- |
| APM Hosts         | Shows the 99th percentile of all distinct APM hosts over all hours in the current month.     |
| APM Fargate Tasks | Shows the average of distinct Fargate tasks over 5-minute time periods in the current month. |
| Ingested Spans    | Shows the sum of Ingested Bytes from spans ingested in the current month.                    |
| Indexed Spans     | Shows the sum of Indexed Spans indexed in the current month.                                 |

Each APM host and APM Fargate task grants you an allotment of ingested and indexed volume:

- Ingested spans: 150 GB ingested spans per APM host and 10 GB ingested spans per APM Fargate task.
- Indexed spans: 1M indexed spans per APM host and 65k spans indexed spans per APM Fargate task.

## Set alerts based on ingested/indexed volumes{% #set-alerts-based-on-ingestedindexed-volumes %}

### Set alerts on ingested bytes{% #set-alerts-on-ingested-bytes %}

To ensure that your ingested spans usage remains within the allocation that APM hosts and APM Fargate tasks grants you, set up monitors to alert when your monthly usage is close to your allocation.

1. Create a [metric monitor](https://app.datadoghq.com/monitors/create/metric).
1. Enter `datadog.estimated_usage.apm.ingested_bytes`for the metric query.
1. Define the monitor's evaluation window to `current month (MTD)`. This ensures that the monitor is looking at the month-to-date usage. Read more about cumulative time windows in the [monitors](https://docs.datadoghq.com/monitors/configuration/?tab=thresholdalert#cumulative-time-windows) documentation.
1. Define the **Alert threshold** and an optional **Warning threshold** to alert when the ingested volume reaches 80% or 90% of your allotment.
1. Enter a name for the monitor. Define the notification to send an alert to your team when the ingested volumes are too high.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/monitor_usage_apm.113c4b7fc6d98bd66c5f149a89f9578a.png?auto=format"
   alt="A metric monitor configuration page showing the datadog.estimated_usage.apm.ingested_bytes as the metric query" /%}

To effectively reduce your ingested volumes, see this [guide](https://docs.datadoghq.com/tracing/guide/trace_ingestion_volume_control/) or the [ingestion mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/) documentation.

### Set alerts on indexed spans{% #set-alerts-on-indexed-spans %}

Similarly, you can set alerts to ensure that your budget for you indexed spans remains within certain limits. Create a metric monitor using the `datadog.estimated_usage.apm.indexed_spans` metric to get alerted when your month-to-date indexed spans volume goes over a defined threshold.

To reduce the number of indexed spans, check your configuration for retention filters. Read more about retention filters in the [trace retention](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/) documentation.
