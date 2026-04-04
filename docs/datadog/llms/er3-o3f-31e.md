# Source: https://docs.datadoghq.com/security/default_rules/er3-o3f-31e.md

---
title: >-
  Account should have a activity log alert configured for 'Create or Update
  Network Security Group'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Account should have a activity log
  alert configured for 'Create or Update Network Security Group'
---

# Account should have a activity log alert configured for 'Create or Update Network Security Group'

## Warning: This rule will be deprecated 18 December 2023 as part of the update to Azure CIS version 2.0.0{% #warning-this-rule-will-be-deprecated-18-december-2023-as-part-of-the-update-to-azure-cis-version-200 %}

## Description{% #description %}

Create an Activity Log Alert for the Create or Update Network Security Group event.

## Rationale{% #rationale %}

By monitoring for creation and updates to network security group events, you gain insight into network access changes and may reduce the time it takes to detect suspicious activity.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Navigate to **Monitor**.
1. Select **Alerts**.
1. Click **On New Alert Rule**.
1. Under **Scope**, click **Select resource**.
1. Select the appropriate subscription under **Filter by subscription**.
1. Select **Network Security Groups** under **Filter by resource type**.
1. Select **All** for **Filter by location**.
1. Click on the subscription resource from the entries populated under **Resource**.
1. Click **Done**.
1. Verify that **Selection preview** shows Network Security Groups and your selected subscription name.
1. Under **Condition**, click **Add Condition**.
1. Select **Create or Update Network Security Group** signal.
1. Click **Done**.
1. Under **Action group**, select **Add action groups** and either complete the creation process, or select the appropriate action group.
1. Under **Alert rule details**, enter **Alert rule name** and **Description**.
1. Select appropriate resource group to save the alert to.
1. Click on the **Enable alert rule upon creation** checkbox.
1. Click **Create alert rule**.

### From the command line{% #from-the-command-line %}

```bash
az account get-access-token --query "{subscription:subscription,accessToken:accessToken}" --out tsv | xargs -L1 bash -c 'curl -X PUT -H "Authorization: Bearer $1" -H "Content-Type: application/json" https://management.azure.com/subscriptions/$0/resourceGroups/<Resource_Group_ To_Create_Alert_In>/providers/microsoft.insights/activityLogAlerts/<Unique_Alert _Name>?api-version=2017-04-01 -d@"input.json"'
```

Where `input.json` contains the request body JSON data, as mentioned below.

```json
{
  "location": "Global",
  "tags": {},
  "properties": {
    "scopes": [
      "/subscriptions/<Subscription_ID>"
    ],
    "enabled": true,
    "condition": {
      "allOf": [
        {
          "containsAny": null,
          "equals": "Administrative",
          "field": "category"
        },
        {
          "containsAny": null,
          "field": "operationName",
          "equals": "Microsoft.Network/networkSecurityGroups/write"
        }
      ]
    },
    "actions": {
      "actionGroups": [
        {
          "actionGroupId": "/subscriptions/<Subscription_ID>/resourceGroups/<Resource_Group_For_Alert_Gr oup>/providers/microsoft.insights/actionGroups/<Alert_Group>",
          "webhookProperties": null
        }
      ]
    },
  }
}
```

## References{% #references %}

1. [https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement](https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement)
1. [https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log](https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log)
1. [https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/createorupdate](https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/createorupdate)
1. [https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/listbysubscriptionid](https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/listbysubscriptionid)
1. [https://docs.microsoft.com/en-us/azure/security/benchmarks/security-controls-v2-logging-threat-detection#lt-4-enable-logging-for-azure-resources](https://docs.microsoft.com/en-us/azure/security/benchmarks/security-controls-v2-logging-threat-detection#lt-4-enable-logging-for-azure-resources)

## CIS Controls{% #cis-controls %}

Version 7, 6.3 - Enable Detailed Logging: Enable system logging to include detailed information such as an event source, date, user, timestamp, source addresses, destination addresses, and other useful elements.
