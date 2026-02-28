# Source: https://docs.datadoghq.com/security/default_rules/def-000-yp6.md

---
title: A log metric filter and alert should exist for VPC network route changes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A log metric filter and alert should
  exist for VPC network route changes
---

# A log metric filter and alert should exist for VPC network route changes

## Description{% #description %}

It is recommended that a metric filter and alarm be established for Virtual Private Cloud (VPC) network route changes.

## Rationale{% #rationale %}

Google Cloud Platform (GCP) routes define the paths taken by network traffic from a VM instance to another destination. The other destination can be inside the organization VPC network (such as another VM) or outside of it. Every route consists of a destination and a next hop. Traffic whose destination IP is within the destination range is sent to the next hop for delivery. Monitoring changes to route tables helps to ensure that all VPC traffic flows through an expected path.

### Impact{% #impact %}

Enabling of logging may result in your project being charged for the additional logs usage.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

#### Create the prescribed Log Metric{% #create-the-prescribed-log-metric %}

1. Go to [Logs-based Metrics](https://console.cloud.google.com/logs/metrics) within **Logging** in the Google Cloud console and click **CREATE METRIC**.
1. Click the down arrow symbol on the filter bar at the rightmost corner and select **Convert to Advanced Filter**.
1. Clear any text and add:
   ```gdscript3
   resource.type="gce_route"
   AND (protoPayload.methodName:"compute.routes.delete"
   OR protoPayload.methodName:"compute.routes.insert")
   ```
1. Click **Submit Filter**. Display logs appear based on the entered filter text.
1. In the `Metric Editor` menu on the right, fill out the name field. Set `Units` to `1` (default) and `Type` to `Counter`. This ensures that the log metric counts the number of log entries matching the advanced logs query.
1. Click **Create Metric**.

#### Create the prescribed alert policy{% #create-the-prescribed-alert-policy %}

1. Identify the newly created metric under the section `User-defined Metrics` in the [Logs-based Metrics](https://console.cloud.google.com/logs/metrics) page in the Google Cloud console.
1. Click the 3-dot icon in the rightmost column for the new metric and select `Create alert from Metric`. A new page appears.
1. Fill out the alert policy configuration and click **Save**. Choose the alerting threshold and configuration that makes sense for your organization. For example, a threshold of zero(0) for the most recent value ensures that a notification is triggered for every owner change in the project:
   ```mysql
   Set `Aggregator` to `Count`
   Set `Configuration`:
   - Condition: above
   - Threshold: 0
   - For: most recent value
   ```
1. Configure the desired notification channels in the section **Notifications**.
1. Name the `policy` and click **Save**.

### From the command line{% #from-the-command-line %}

#### Create the prescribed Log Metric{% #create-the-prescribed-log-metric-1 %}

Use the command `gcloud logging metrics create`. Read the [usage reference](https://cloud.google.com/sdk/gcloud/reference/beta/logging/metrics/create) in the Google Cloud documentation for more information.

#### Create the prescribed alert policy{% #create-the-prescribed-alert-policy-1 %}

Use the command `gcloud alpha monitoring policies create`. Read the [usage reference](https://cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/create) in the Google Cloud documentation for more information.

## References{% #references %}

1. [https://cloud.google.com/logging/docs/logs-based-metrics/](https://cloud.google.com/logging/docs/logs-based-metrics/)
1. [https://cloud.google.com/monitoring/custom-metrics/](https://cloud.google.com/monitoring/custom-metrics/)
1. [https://cloud.google.com/monitoring/alerts/](https://cloud.google.com/monitoring/alerts/)
1. [https://cloud.google.com/logging/docs/reference/tools/gcloud-logging](https://cloud.google.com/logging/docs/reference/tools/gcloud-logging)
1. [https://cloud.google.com/storage/docs/access-control/iam](https://cloud.google.com/storage/docs/access-control/iam)
