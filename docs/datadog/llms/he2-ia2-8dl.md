# Source: https://docs.datadoghq.com/security/default_rules/he2-ia2-8dl.md

---
title: >-
  Account should have a activity log alert configured for deallocating virtual
  machines
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Account should have a activity log
  alert configured for deallocating virtual machines
---

# Account should have a activity log alert configured for deallocating virtual machines

## Description{% #description %}

Create an activity log alert for the Deallocate Virtual Machine event.

## Rationale{% #rationale %}

By implementing alerting on significant infrastructure changes in Microsoft Azure, you can detect unauthorized or unwanted activity.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Using the Azure Portal search bar, search for **Monitor**.
1. Select **Alerts** from the left-hand panel.
1. Click **Create** and from the drop down select **Alert rule**.
1. Under **Scope**, click **Select scope**.
1. Select the appropriate subscription under **Filter by subscription**.
1. Select **Virtual machines** under **Filter by resource type**.
1. Select **All** for **Filter by location**.
1. Click on the subscription resource from the entries populated under **Resource**.
1. Click **Done**.
1. Verify that **Selection preview** shows your selected Virtual Machine(s) and subscription name.
1. Under **Condition**, click **Add Condition**.
1. Select **Deallocate Virtual Machine** signal name.
1. Navigate to **Actions**.
1. Under **Action group**, select **Add action groups** and either complete the creation process, or select the appropriate action group.
1. Navigate to **Details** and select the appropriate resource group to save the alert to.
1. Enter **Alert rule name** and **Alert rule description**.
1. Under the **Advanced options** drop-down menu, click on the **Enable alert rule upon creation** checkbox.
1. Click **Review + create** and verify all of the alert settings are correct.
1. Click **Create**.

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
          "equals": "Microsoft.Compute/virtualMachines/deallocate",
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
$ComplianceName = 'Deallocatete Virtual Machine'
$Signal = 'Microsoft.Compute/virtualMachines/deallocate'
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

1. [https://docs.microsoft.com/en-us/azure/virtual-machines/windows/overview](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/overview)
1. [https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log](https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log)
1. [https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/createorupdate](https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/createorupdate)
1. [https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/listbysubscriptionid](https://docs.microsoft.com/en-in/rest/api/monitor/activitylogalerts/listbysubscriptionid)
1. [https://docs.microsoft.com/en-us/azure/security/benchmarks/security-controls-v2-logging-threat-detection#lt-4-enable-logging-for-azure-resources](https://docs.microsoft.com/en-us/azure/security/benchmarks/security-controls-v2-logging-threat-detection#lt-4-enable-logging-for-azure-resources)
