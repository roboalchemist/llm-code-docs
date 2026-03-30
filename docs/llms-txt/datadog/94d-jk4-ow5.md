# Source: https://docs.datadoghq.com/security/default_rules/94d-jk4-ow5.md

---
title: >-
  Account should have a configured activity log alert for PostgreSQL database
  updates
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Account should have a configured
  activity log alert for PostgreSQL database updates
---

# Account should have a configured activity log alert for PostgreSQL database updates

## Description{% #description %}

Create an activity log alert for the Create or Update PostgreSQL Database event.

## Rationale{% #rationale %}

By implementing alerting on significant infrastructure changes in Microsoft Azure, you can detect unauthorized or unwanted activity.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Navigate to **Monitor**.
1. Select **Activity Logs**.
1. Search the operation name **Create/Update PostgreSQL Database**.
1. Click **On New Alert Rule**.
1. Under **Scope**, select the Subscription and any Resource Groups that need monitoring.
1. Configure Action groups if needed.
1. In **Details**, provide a descriptive Alert rule name and description.
1. Go to **Tags** and enter relevant tags.
1. Click **Review + create**.

### From the command line{% #from-the-command-line %}

```bash
az account get-access-token --query "{subscription:subscription,accessToken:accessToken}" --out tsv | xargs -L1 bash -c 'curl -X PUT -H "AuthorizationBearer $1" -H "Content-Typeapplication/json" https://management.azure.com/subscriptions/$0/resourceGroups/<Resource_Group_To Create_Alert_In>/providers/microsoft.insights/activityLogAlerts/<Unique_Alert_Name>?api-version=2017-04-01 -d@"input.json"'
```

`input.json` contains the request body JSON data mentioned below.

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
          "equals": "Microsoft.DBforPostgreSQL/servers/databases/write",
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

**Using PowerShell AZ cmdlets**:

```powershell
$ComplianceName = 'Create/Update PostgreSQL Database'
$Signal = 'Microsoft.DBforPostgreSQL/servers/databases/write'
$Category = 'Administrative'
$ResourceGroupName = 'MyResourceGroup'
$actiongroup = (Get-AzActionGroup -Name corenotifications -ResourceGroupName $ResourceGroupName)
$ActionGroupId = (New-Object Microsoft.Azure.Management.Monitor.Models.ActivityLogAlertActionGroup $ActionGroup.Id)
$Subscription = (Get-AzContext).Subscription
$location = 'Global'
$scope = "/subscriptions/$($Subscription.Id)"
$alertName = "$($Subscription.Name) - $($ComplianceName)"
$conditions = @(
  New-AzActivityLogAlertCondition -Field 'category' -Equal $Category
  New-AzActivityLogAlertCondition -Field 'operationName' -Equal $Signal
)
Set-AzActivityLogAlert -Location $location -Name $alertName -ResourceGroupName $ResourceGroupName -Scope $scope -Action $ActionGroupId -Condition $conditions
```

## References{% #references %}

1. [https://docs.microsoft.com/en-us/azure/postgresql/overview](https://docs.microsoft.com/en-us/azure/postgresql/overview)
1. [https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log](https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log)
1. [https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/createorupdate](https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/createorupdate)
1. [https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/listbysubscriptionid](https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/listbysubscriptionid)
1. [https://docs.microsoft.com/en-us/azure/security/benchmarks/security-controls-v2-logging-threat-detection#lt-4-enable-logging-for-azure-resources](https://docs.microsoft.com/en-us/azure/security/benchmarks/security-controls-v2-logging-threat-detection#lt-4-enable-logging-for-azure-resources)

## CIS Controls{% #cis-controls %}

Version 7: *6.3 Enable Detailed Logging*. Enable system logging to include detailed information such as an event source, date, user, timestamp, source addresses, destination addresses, and other useful elements.
