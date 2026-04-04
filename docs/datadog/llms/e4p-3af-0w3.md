# Source: https://docs.datadoghq.com/security/default_rules/e4p-3af-0w3.md

---
title: >-
  Account should have a configured activity log alert for deleting policy
  assignments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Account should have a configured
  activity log alert for deleting policy assignments
---

# Account should have a configured activity log alert for deleting policy assignments

## Warning: This rule will be deprecated 18 December 2023 as part of the update to Azure CIS version 2.0.0{% #warning-this-rule-will-be-deprecated-18-december-2023-as-part-of-the-update-to-azure-cis-version-200 %}

## Description{% #description %}

Create an activity log alert for the Delete Policy Assignment event.

## Rationale{% #rationale %}

By monitoring delete policy assignment events, you gain insight into changes in the **Policy - Assignments** page and reduce the time it takes to detect unsolicited changes.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Navigate to **Monitor**.
1. Select **Alerts**.
1. Click **On New Alert Rule**.
1. Under **Scope**, click **Select resource**.
1. Select the appropriate subscription under **Filter by subscription**.
1. Select **Policy Assignment** under **Filter by resource type**.
1. Select **All** for **Filter by location**.
1. Click on the subscription from the entries populated under **Resource**.
1. Verify that **Selection preview** shows All Policy assignments (`policyAssignments`) and your selected subscription name.
1. Click **Done**.
1. Under **Condition**, click **Add Condition**.
1. Select **Delete policy assignment signal**.
1. Click **Done**.
1. Under **Action group**, select **Add action groups** and either complete the creation process or select the appropriate action group.
1. Under **Alert rule details**, enter **Alert rule name** and **Description**.
1. Select the appropriate resource group to save the alert to.
1. Click on the **Enable alert rule upon creation** checkbox.
1. Click **Create alert rule**.

### From the command line{% #from-the-command-line %}

```
az account get-access-token --query "{subscription:subscription,accessToken:accessToken}" --out tsv | xargs -L1 bash -c 'curl -X PUT -H "Authorization: Bearer $1" -H "Content-Type: application/json"
https://management.azure.com/subscriptions/$0/resourceGroups/<Resource_Group_To_Create_Alert_In>/providers/microsoft.insights/activityLogAlerts/<Unique_Alert_Name>?api-version=2017-04-01 -d@"input.json"
```

Where `input.json` contains the request body JSON data below:

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
            "allOf": [{
                    "containsAny": null,
                    "equals": "Administrative",
                    "field": "category"
                },
                {
                    "containsAny": null,
                    "equals": "Microsoft.Authorization/policyAssignments/delete",
                    "field": "operationName"
                }
            ]
        },
        "actions": {
            "actionGroups": [{
                "actionGroupId": "/subscriptions/<Subscription_ID>/resourceGroups/<Resource_Group_For_Alert_Group>/providers/microsoft.insights/actionGroups/<Alert_Group>",
                "webhookProperties": null
            }]
        }
    }
}
```

Configurable Parameters for command line:

- `<Resource_Group_To_Create_Alert_In>`
- `<Unique_Alert_Name>`

Configurable Parameters for `input.json`:

- `<Subscription_ID>` in scopes
- `<Subscription_ID>` in actionGroupId
- `<Resource_Group_For_Alert_Group>` in actionGroupId
- `<Alert_Group>` in actionGroupId

**Using PowerShell AZ cmdlets**:

```powershell
$ComplianceName = 'Delete Policy Assignment'
$Signal = 'Microsoft.Authorization/policyAssignments/delete'
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

1. [https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log](https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log)
1. [https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/createorupdate](https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/createorupdate)
1. [https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/listbysubscriptionid](https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/listbysubscriptionid)
1. [https://docs.microsoft.com/en-us/azure/security/benchmarks/security-controls-v2-logging-threat-detection#lt-4-enable-logging-for-azure-resources](https://docs.microsoft.com/en-us/azure/security/benchmarks/security-controls-v2-logging-threat-detection#lt-4-enable-logging-for-azure-resources)
1. [https://azure.microsoft.com/en-us/services/blueprints/](https://azure.microsoft.com/en-us/services/blueprints/)

## Additional Information{% #additional-information %}

- This log alert also applies for Azure Blueprints.
