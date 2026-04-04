# Source: https://docs.datadoghq.com/developers/service_checks.md

---
title: Service Check
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Developers > Service Check
---

# Service Check

## Overview{% #overview %}

Service checks allow you to characterize the status of a service to monitor it within Datadog. Service checks monitor the up or down status of the specific service. You are alerted whenever the monitoring Agent fails to connect to that service in a specified number of consecutive checks. For example, you can get an alert any time the monitoring Agent on a Redis host reports three consecutive failed attempts to connect to Redis and collect metrics.

Service checks at the cluster level offer another effective way to monitor distributed or redundant systems that can withstand some failures. Use these alerts for architectures where individual hosts run multiple services, because they can surface the degradation of the service even if the hosts running that service remain available (and would pass a host-level health check).

You can set up monitoring and an alert for when a critical, non-redundant service is lost, or if a cluster is on the verge of failure due to widespread node loss. Other critical alerts could be a drop in request throughput or an increase in request latency.

You might need to set up a service check if an integration does not have one natively or for an internal service that you want to monitor for up or down status.

To use service checks, first set up the check:

- [Submit a custom Agent Check.](https://docs.datadoghq.com/developers/service_checks/agent_service_checks_submission)
- [Submit a Service Check with DogStatsD.](https://docs.datadoghq.com/developers/service_checks/dogstatsd_service_checks_submission)
- [Submit a Service Check through Datadog API.](https://docs.datadoghq.com/api/v1/service-checks/)

Once the service check is sending data, check out your check summary and set up dashboards, monitors, and alerts:

## Visualize your service check in Datadog{% #visualize-your-service-check-in-datadog %}

Service checks can be visualized and used in 3 Datadog sections:

- [Check Summary](https://app.datadoghq.com/check/summary)
- [Screenboards](https://app.datadoghq.com/dashboard)
- [Service Check Monitor](https://app.datadoghq.com/monitors/create/custom)

### Check summary{% #check-summary %}

The [Check Summary](https://app.datadoghq.com/check/summary) page lists all checks reported across your infrastructure in the past day. Select a check to get insights on the status and tags associated with the check.

{% image
   source="https://datadog-docs.imgix.net/images/developers/service_checks/check_summary.c05dcac33fda50f1b1385f19783536c6.png?auto=format"
   alt="Check summary" /%}

### Screenboards{% #screenboards %}

You can visualize service checks with a **Check status** widget in a screenboard:

{% image
   source="https://datadog-docs.imgix.net/images/developers/service_checks/check_status_widget.e01615cf84f2de4dd4b2fe688355c456.png?auto=format"
   alt="Check status widget" /%}

After clicking on the **Check status** widget icon, the following pop-up appears:

{% image
   source="https://datadog-docs.imgix.net/images/developers/service_checks/check_widget_config.ea84dda9d70523cee9fe8d8ba856314e.png?auto=format"
   alt="Check widget config" /%}

In this form, you can:

- **Check Name**: Select your service check name.
- **Reporting Timeframe**: Select the time frame on which you want to aggregate your status.
- **Scoping**: Select a single check or a cluster of check statuses reported by a single tag value or a tag key.
- **Widget Title**: Set your widget title.

## Service check monitor{% #service-check-monitor %}

Even if you can't graph a service check over time as you would for metrics, you can still monitor it with a [Service Check Monitor](https://app.datadoghq.com/monitors/create/custom).

{% image
   source="https://datadog-docs.imgix.net/images/developers/service_checks/service_check_monitor.c285c67fd9e219f17715b0798b846861.png?auto=format"
   alt="Check monitor" /%}

In this form, you can:

- **Pick a service check**: Select the check status name to monitor.
- **Pick monitor scope**: Select the context for your monitor (including/excluding tags).
- **Set alert conditions**: Choose between a simple check alert or a cluster alert.
- **Configure notifications and automations**: Choose who this monitor should notify and edit the notifications sent (find more about [Datadog notifications](https://docs.datadoghq.com/monitors/notify/)).
- **Define permissions and audit notifications**: Edit access permissions for your monitor and set audit notifications.

For more information on creating a service check, see [Service Check Monitor](https://docs.datadoghq.com/monitors/types/service_check/).
