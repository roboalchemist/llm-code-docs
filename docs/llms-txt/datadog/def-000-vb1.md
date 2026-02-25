# Source: https://docs.datadoghq.com/security/default_rules/def-000-vb1.md

---
title: '''Delete Security Solution'' activity log alert should be configured'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'Delete Security Solution' activity log
  alert should be configured
---

# 'Delete Security Solution' activity log alert should be configured

## Description{% #description %}

To enhance the detection of suspicious activity and gain insights into changes made to active security solutions, it is recommended to create an activity log alert specifically for the "Delete Security Solution" event. By monitoring these events, you can quickly detect any unauthorized deletions of security solutions, reducing the time it takes to identify and respond to potential security threats.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Navigate to the **Monitor** blade.
1. Select **Alerts** > **Create** > **Alert rule**.
1. Under **Filter by subscription**, choose a subscription.
1. Under **Filter by resource type**, select **Security Solutions (securitySolutions)**.
1. Under **Filter by location**, select **All**.
1. From the results, select the subscription, then click **Done**.
1. Click the **Condition** tab.
1. Under Signal name, click Delete **Delete Security Solutions (Microsoft.Security/securitySolutions)**.
1. Click the **Actions** tab.
1. To use an existing action group, click **Select action groups**. To create a new action group, click **Create action group**. Fill out the appropriate details for the selection.
1. Click the **Details** tab.
1. Select a **Resource group**, then provide an **Alert rule name** and an optional **Alert rule description**.
1. Click **Review + create**.
1. Click **Create**.
