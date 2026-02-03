# Source: https://docs.datadoghq.com/security/default_rules/ur9-gbd-pl9.md

---
title: >-
  The account should have a configured activity log alert for firewall rule
  creation or update
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The account should have a configured
  activity log alert for firewall rule creation or update
---

# The account should have a configured activity log alert for firewall rule creation or update
 
## Warning: This rule will be deprecated 18 December 2023 as part of the update to Azure CIS version 2.0.0{% #warning-this-rule-will-be-deprecated-18-december-2023-as-part-of-the-update-to-azure-cis-version-200 %}

## Description{% #description %}

Create an activity log alert for the Create or Update SQL Server Firewall Rule event.

### Default value{% #default-value %}

By default, no monitoring alerts are created or active.

## Rationale{% #rationale %}

Monitoring for Create or Update SQL Server Firewall Rule events gives insight into network access changes and may reduce the time it takes to detect suspicious activity.

### Impact{% #impact %}

There will be a substantial increase in log size if there are a large number of administrative actions on a server.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Navigate to `Monitor` blade.
1. Select `Alerts`.
1. Click `Create`.
1. Click on `Alert rule`.
1. Under the Scope tab, click `Select scope`.
1. In the `Select a resource` window, select the appropriate filters:
   - Filter by subscription: `< choose the subscription alerts are needed for >`
   - Filter by resource type: **Server Firewall Rule (servers/firewallRules)**
   - Filter by location: `All`
   - Click on the `subscription name` or `resource group` that the Log Alert Rule will be applied to
1. Verify that the selection preview shows:
   - **All server firewall rule (servers/firewallrules)** or `< your selected resource >`
   - `< Resource Name >` - The subscription, group, or resource you selected
1. Click `Done`.
1. Under the Condition tab, click `Add Condition`. The `Select a signal` window may automatically open without clicking.
1. In the `Select a signal` window, under the "Signal Name" heading, click **Create/Update server firewall rule (Microsoft.Sql/servers/firewallRules)**.
1. Under the Actions tab, choose appropriately:
   - Select action groups - If you have an existing action group to notify the necessary personnel.
   - Create action group - If you do not have an existing action group or want to create a new one.
1. Under the Details tab, fill in:
   - Resource group - Select the resource group you want the alert rule to reside in
   - Alert rule name - Give your alert a recognizable and standardized name
   - Alert rule description - (Optional)
1. Click `Review + create` then verify the summary details.
1. Click `Create`.

### From the command line{% #from-the-command-line %}

```
az account get-access-token --query "{subscription:subscription,accessToken:accessToken}" --out tsv | xargs -L1 bash -c 'curl -X PUT -H "AuthorizationBearer $1" -H "Content-Typeapplication/json" https://management.azure.com/subscriptions/$0/resourceGroups/<Resource_Group_To Create_Alert_In>/providers/microsoft.insights/activityLogAlerts/<Unique_Alert_Name>?api-version=2017-04-01 -d@"input.json"'
```

`input.json` contains the following request body JSON data:

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
          "equals": "Microsoft.Sql/servers/firewallRules/write",
          "field": "operationName"
        }
      ]
    },
    "actions": {
      "actionGroups": [
        {
          "actionGroupId": "/subscriptions/<Subscription_ID>/resourceGroups/<Resource_Group_For_Alert_Group>/providers/microsoft.insights/actionGroups/<Alert_Group>",
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
1. [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-logging-threat-detection#lt-3-enable-logging-for-security-investigation](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-logging-threat-detection#lt-3-enable-logging-for-security-investigation)
