# Source: https://docs.datadoghq.com/developers/integrations/create-an-integration-monitor-template.md

---
title: Create a Monitor Template
description: Learn how to create a monitor for your integration.
breadcrumbs: Docs > Developers > Datadog Integrations > Create a Monitor Template
---

# Create a Monitor Template

## Overview{% #overview %}

This page guides Technology Partners through creating and packaging monitor templates with their official Datadog integration.

[Datadog Monitors](https://docs.datadoghq.com/monitors/) continuously evaluate data (such as metrics, logs, and events) to detect conditions that indicate performance issues and availability risks. They act as proactive alerting tools that automatically notify users when behavior deviates from expected thresholds, enabling teams to take action before incidents impact customers.

For Technology Partners, monitors transform the telemetry your integration collects into actionable insights. When you package monitor templates, users can enable them directly from the [**Monitors > Templates**](https://app.datadoghq.com/monitors/templates) page for faster setup and time to value.

At least one monitor template is required if your integration collects metrics.

## Building a monitor template{% #building-a-monitor-template %}

These steps assume you've [joined the Datadog Partner Network](https://docs.datadoghq.com/developers/integrations/?tab=integrations#join-the-datadog-partner-network), have access to a partner developer organization, and have already [created a listing in the Developer Platform](https://docs.datadoghq.com/developers/integrations/build_integration/#create-a-listing).

1. Determine which telemetry you want to monitor.
1. Create and configure a monitor in your partner developer organization.
1. Test your monitor.
1. Add your monitor to your integration.

### Determine which telemetry to monitor{% #determine-which-telemetry-to-monitor %}

Start by reviewing the [full list of monitor types](https://docs.datadoghq.com/monitors/types/) to understand what kinds of telemetry you can alert on. Determine the insights that matter most to your users. Refer to the examples below for common use cases and examples.

#### Monitor your service's RED (rate, errors, duration) metrics{% #monitor-your-services-red-rate-errors-duration-metrics %}

- **Rate**: Monitor the number of requests your service receives.
- **Errors**: Track how many of those requests fail.
- **Duration**: Measure how long those requests take (latency).

#### Monitor your infrastructure{% #monitor-your-infrastructure %}

- **CPU utilization**: Track CPU usage to ensure they're neither under nor over-utilized, to prevent system slowdowns or application failures.
- **Memory utilization**: Monitor how much system memory is being used to detect and prevent issues like memory leaks or crashes.
- **Storage**: Monitor disk space to prevent problems such as data loss, service interruptions, or write failures.

#### Monitor your logs{% #monitor-your-logs %}

- **Error spikes**: Alert when error logs exceed a threshold, such as repeated `connection refused` or `timeout` messages within a short period.
- **Missing activity**: Detect when expected logs stop appearing, indicating a stalled process or failed service.

### Create your monitor{% #create-your-monitor %}

[Create and configure your monitor](https://docs.datadoghq.com/getting_started/monitors/#create-a-monitor) within your partner developer organization. These monitors serve as reusable templates that integration users can enable directly in their own Datadog organizations.

### Test your monitor{% #test-your-monitor %}

1. Ingest telemetry that triggers your monitor.
1. Navigate to the [Monitor list](https://app.datadoghq.com/monitors/manage) page and select your monitor.
1. Confirm that your monitor is triggered as expected. Use [Status Events](https://docs.datadoghq.com/monitors/status/events/) to view when your monitor was triggered and review details for each event.

## Add your monitor to your integration{% #add-your-monitor-to-your-integration %}

After you've created and tested your monitor, add it to your listing in the Developer Platform. When your integration is published, the monitor becomes a searchable template linked to your integration.

{% image
   source="https://datadog-docs.imgix.net/images/developers/integrations/content_tab.5b98536823cb5877d0a7e8757393296c.png?auto=format"
   alt="The Content tab in the Integration Developer Platform" /%}

1. In the Developer Platform, go to the **Content** tab.
1. Click **Import Monitor**.
1. Search for and select the monitor you created. You can include up to 10 monitors per integration.
1. For each monitor, provide a **Display Name** and **Description**. These appear on the [**Monitors > Templates**](https://app.datadoghq.com/monitors/templates) page:
   - **Display Name**: A concise title that clearly communicates what the alert covers. Use active voice (for example, `Database latency exceeds threshold`).
   - **Description**: A short explanation that helps users decide whether the monitor is relevant to them. Describe why this alert matters and what impact it addresses.
1. Click **Import**, then **Save Changes**.

## Further Reading{% #further-reading %}

- [Configure Monitors](https://docs.datadoghq.com/monitors/configuration/)
