# Source: https://docs.datadoghq.com/security/default_rules/def-000-d1v.md

---
title: '''Delete Policy Assignment'' activity log alert should be configured'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'Delete Policy Assignment' activity log
  alert should be configured
---

# 'Delete Policy Assignment' activity log alert should be configured

## Description{% #description %}

To enhance the detection of unsolicited changes and streamline the monitoring of modifications made in the **Policy - Assignments** page, it is advised to create an activity log alert specifically for the "Delete Policy Assignment" event. This alert will provide valuable insights into any deletions of policy assignments, allowing for quick detection and response to unauthorized changes.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Navigate to the **Monitor** blade.
1. Select **Alerts** > **Create** > **Alert rule**.
1. Under **Filter by subscription**, choose a subscription.
1. Under **Filter by resource type**, select **Policy Assignment**.
1. Under **Filter by location**, select **All**.
1. From the results, select the subscription, then click **Done**.
1. Select the **Condition** tab.
1. Under Signal name, click Delete **Delete policy assignment (Microsoft.Authorization/policyAssignments)**.
1. Select the **Actions** tab.
1. To use an existing action group, click **Select action groups**. To create a new action group, click **Create action group**. Fill out the appropriate details for the selection.
1. Select the **Details** tab.
1. Select a **Resource group**, provide an **Alert rule name** and an optional **Alert rule description**.
1. Click **Review + create**.
1. Click **Create**.
