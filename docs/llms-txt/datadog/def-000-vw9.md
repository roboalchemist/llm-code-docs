# Source: https://docs.datadoghq.com/security/default_rules/def-000-vw9.md

---
title: >-
  A log metric filter and alert should exist for VPC network firewall rule
  changes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A log metric filter and alert should
  exist for VPC network firewall rule changes
---

# A log metric filter and alert should exist for VPC network firewall rule changes

## Description{% #description %}

It is recommended that a metric filter and alarm be established for Virtual Private Cloud (VPC) network firewall rule changes.

## Rationale{% #rationale %}

Monitoring create or update firewall rule events gives insight to network access changes and may reduce the time it takes to detect suspicious activity.

### Impact{% #impact %}

Enabling logging may result in your project being charged for the additional logs usage.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

#### Create the prescribed log metric{% #create-the-prescribed-log-metric %}

1. Go to Logging/Logs-based Metrics by visiting [https://console.cloud.google.com/logs/metrics](https://console.cloud.google.com/logs/metrics) and click **CREATE METRIC**.
1. Click the down arrow symbol on the **Filter Bar** at the rightmost corner and select **Convert to Advanced Filter**.
1. Clear any text and add:

```gdscript3
   resource.type="gce_firewall_rule"
   AND (protoPayload.methodName:"compute.firewalls.patch"
   OR protoPayload.methodName:"compute.firewalls.insert"
   OR protoPayload.methodName:"compute.firewalls.delete")
```
Click **Submit Filter**. Display logs appear based on the filter text entered by the user.In the **Metric Editor** menu on the right, fill out the name field. Set **Units** to **1** (default) and Type to Counter. This ensures that the log metric counts the number of log entries matching the advanced logs query.Click **Create Metric**.
#### Create a prescribed alert policy{% #create-a-prescribed-alert-policy %}

1. Go to [https://console.cloud.google.com/logs/metrics](https://console.cloud.google.com/logs/metrics). Under the **User-defined Metrics** section, identify the newly created metric.
1. Click the kebab icon in the rightmost column for the new metric and select **Create alert from Metric**.
1. Fill out the alert policy configuration and click **Save**. Choose the alerting threshold and configuration that makes sense for the user's organization. For example, a threshold of zero(0) for the most recent value ensures that a notification is triggered for every owner change in the project:

```mysql
   Set `Aggregator` to `Count`
   Set `Configuration`:
   - Condition: above
   - Threshold: 0
   - For: most recent value
```
Configure the desired notifications channels in the section **Notifications**.Name the policy and click **Save**.
### From the command line{% #from-the-command-line %}

#### Create a prescribed log metric{% #create-a-prescribed-log-metric %}

Use the command: `gcloud logging metrics create` Reference for command usage: [https://cloud.google.com/sdk/gcloud/reference/beta/logging/metrics/create](https://cloud.google.com/sdk/gcloud/reference/beta/logging/metrics/create)

#### Create a prescribed alert policy{% #create-a-prescribed-alert-policy-1 %}

Use the command: `gcloud alpha monitoring policies create` Reference for command usage: [https://cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/create](https://cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/create)

## References{% #references %}

1. [https://cloud.google.com/logging/docs/logs-based-metrics/](https://cloud.google.com/logging/docs/logs-based-metrics/)
1. [https://cloud.google.com/monitoring/custom-metrics/](https://cloud.google.com/monitoring/custom-metrics/)
1. [https://cloud.google.com/monitoring/alerts/](https://cloud.google.com/monitoring/alerts/)
1. [https://cloud.google.com/logging/docs/reference/tools/gcloud-logging](https://cloud.google.com/logging/docs/reference/tools/gcloud-logging)
1. [https://cloud.google.com/vpc/docs/firewalls](https://cloud.google.com/vpc/docs/firewalls)
