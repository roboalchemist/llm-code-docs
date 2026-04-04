# Source: https://docs.datadoghq.com/security/default_rules/def-000-2sc.md

---
title: '''Delete Public Ip Address Rule'' activity log alert should be configured'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'Delete Public Ip Address Rule'
  activity log alert should be configured
---

# 'Delete Public Ip Address Rule' activity log alert should be configured

## Description{% #description %}

To enhance network security monitoring and expedite the detection of suspicious activity, it is recommended to create an activity log alert specifically for the "Delete Public IP Addresses Rule" event. By enabling this alert, you gain valuable insights into the deletions of public IP addresses rules. It is important to note that enabling this alert may result in a substantial increase in log size, particularly if there are numerous administrative actions performed on a server. However, the benefits of improved security monitoring outweigh the potential impact on log size.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Navigate to the **Monitor** blade.
1. Select **Alerts** > **Create** > **Alert rule**.
1. Under **Filter by subscription**, choose a subscription.
1. Under **Filter by resource type**, select **Public IP addresses**.
1. Under **Filter by location**, select **All**.
1. From the results, select the subscription, then click **Done**.
1. Select the **Condition** tab.
1. Under Signal name, click Delete **Delete Public Ip Address (Microsoft.Network/publicIPAddresses)**.
1. Select the **Actions** tab.
1. To use an existing action group, click **Select action groups**. To create a new action group, click **Create action group**. Fill out the appropriate details for the selection.
1. Select the **Details** tab.
1. Select a **Resource group**, provide an **Alert rule name** and an optional **Alert rule description**.
1. Click **Review + create**.
1. Click **Create**.
