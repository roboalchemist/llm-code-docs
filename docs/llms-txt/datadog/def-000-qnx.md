# Source: https://docs.datadoghq.com/security/default_rules/def-000-qnx.md

---
title: '''Create Policy Assignment'' activity log alert should be configured'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'Create Policy Assignment' activity log
  alert should be configured
---

# 'Create Policy Assignment' activity log alert should be configured
 
## Description{% #description %}

To improve detection of unsolicited changes and gain insight into modifications made in "Azure policy - assignments," it is recommended to create an activity log alert specifically for the Create Policy Assignment event. This alert will help monitor and track any occurrences of policy assignment creation, reducing the time it takes to identify and respond to any unauthorized changes.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **Monitor** and select **Alerts**.
1. Click **New Alert Rule**.
1. Under **Scope**, click **Select Resource**.
1. Under **Filter by Subscription**, select the appropriate subscription.
1. Under **Filter by Resource Type**, select **Policy Assignment**.
1. Select **All** for **Filter by Location**.
1. Click the subscription resource from the entries populated under **Resource**. Verify that the selection preview shows **All Policy** assignment (policyAssignments) and the selected subscription name.
1. Click **Done**.
1. Under **Condition**, click **Add Condition**, then select the **Create Policy Assignment** signal.
1. Click **Done**.
1. Under **Action Group**, select **Add Action Groups** and complete the creation process or select the appropriate action group.
1. Under **Alert Rule Details**, enter the **Alert Rule Name** and **Description**.
1. Select the appropriate resource group to save the alert to.
1. Select the **Enable alert rule upon creation** checkbox.
1. Click **Create Alert Rule**.
