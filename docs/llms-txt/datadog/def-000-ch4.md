# Source: https://docs.datadoghq.com/security/default_rules/def-000-ch4.md

---
title: A log metric filter and alert should exist for audit configuration changes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A log metric filter and alert should
  exist for audit configuration changes
---

# A log metric filter and alert should exist for audit configuration changes

## Description{% #description %}

Google Cloud Platform (GCP) services write audit log entries to the Admin Activity and Data Access logs to help answer the question of "Who did what, where, and when?" within GCP projects. Cloud audit logging records information such as the identity of the API caller, the time of the API call, the source IP address of the API caller, the request parameters, and the response elements returned by GCP services. Cloud audit logging provides a history of GCP API calls for an account, including API calls made through the console, SDKs, command-line tools, and other GCP services.

## Rationale{% #rationale %}

Cloud audit logging to Admin Activity and Data Access logs enables security analysis, resource change tracking, and compliance auditing. Configuring the metric filter and alerts for audit configuration changes ensures that the recommended state of audit configuration is maintained so that all activities in the project can be audited at any point in time.

### Impact{% #impact %}

Enabling logging may result in your project being charged for the additional logs usage.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

#### Create the prescribed log metric{% #create-the-prescribed-log-metric %}

1. Go to Logging/Logs-based Metrics by visiting [https://console.cloud.google.com/logs/metrics](https://console.cloud.google.com/logs/metrics) and click **CREATE METRIC**.
1. Click the down arrow symbol on the Filter Bar at the rightmost corner and select **Convert to Advanced Filter**.
1. Clear any text and add:
   ```gdscript3
   protoPayload.methodName="SetIamPolicy" AND
   protoPayload.serviceData.policyDelta.auditConfigDeltas:*
   ```
1. Click **Submit Filter**. Display logs appear based on the filter text entered by the user.
1. In the **Metric Editor** menu on the right, fill out the name field. Set **Units** to 1 (default) and **Type** to **Counter**. This will ensure that the log metric counts the number of log entries matching the user's advanced logs query.
1. Click **Create Metric**.

#### Create a prescribed alert policy{% #create-a-prescribed-alert-policy %}

1. Go to [https://console.cloud.google.com/logs/metrics](https://console.cloud.google.com/logs/metrics). Under the **User-defined Metrics** section, identify the newly created metric.
1. Click the kebab icon in the rightmost column for the new metric and select **Create alert from Metric**.
1. Fill out the alert policy configuration and click **Save**. Choose the alerting threshold and configuration that makes sense for the organization. For example, a threshold of zero(0) for the most recent value will ensure that a notification is triggered for every owner change in the project:

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

Use the command: `gcloud beta logging metrics create` Reference for command usage: [https://cloud.google.com/sdk/gcloud/reference/beta/logging/metrics/create](https://cloud.google.com/sdk/gcloud/reference/beta/logging/metrics/create)

#### Create a prescribed alert policy{% #create-a-prescribed-alert-policy-1 %}

Use the command: `gcloud alpha monitoring policies create` Reference for command usage: [https://cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/create](https://cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies/create)

## References{% #references %}

1. [https://cloud.google.com/logging/docs/logs-based-metrics/](https://cloud.google.com/logging/docs/logs-based-metrics/)
1. [https://cloud.google.com/monitoring/custom-metrics/](https://cloud.google.com/monitoring/custom-metrics/)
1. [https://cloud.google.com/monitoring/alerts/](https://cloud.google.com/monitoring/alerts/)
1. [https://cloud.google.com/logging/docs/reference/tools/gcloud-logging](https://cloud.google.com/logging/docs/reference/tools/gcloud-logging)
1. [https://cloud.google.com/logging/docs/audit/configure-data-access#getiampolicy-setiampolicy](https://cloud.google.com/logging/docs/audit/configure-data-access#getiampolicy-setiampolicy)
