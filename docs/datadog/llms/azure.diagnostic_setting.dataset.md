# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.diagnostic_setting.dataset.md

---
title: Diagnostic Setting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Diagnostic Setting
---

# Diagnostic Setting

This table represents the Diagnostic Setting resource from Microsoft Azure.

```
azure.diagnostic_setting
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                      | Description |
| ------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| event_hub_authorization_rule_id | core | string     | The resource Id for the event hub authorization rule.                                                                                                                                                                                                                                          |
| event_hub_name                  | core | string     | The name of the event hub. If none is specified, the default event hub will be selected.                                                                                                                                                                                                       |
| id                              | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}                                                                                                      |
| location                        | core | string     |
| log_analytics_destination_type  | core | string     | A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type constructed as follows: <normalized service identity>_<normalized category name>. Possible values are: Dedicated and null (null is default.) |
| logs                            | core | json       | The list of logs settings.                                                                                                                                                                                                                                                                     |
| marketplace_partner_id          | core | string     | The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs.                                                                                                                                                                                          |
| metrics                         | core | json       | The list of metric settings.                                                                                                                                                                                                                                                                   |
| name                            | core | string     | The name of the resource                                                                                                                                                                                                                                                                       |
| resource_group                  | core | string     |
| service_bus_rule_id             | core | string     | The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.                                                                                                                                                                                           |
| storage_account_id              | core | string     | The resource ID of the storage account to which you would like to send Diagnostic Logs.                                                                                                                                                                                                        |
| subscription_id                 | core | string     |
| subscription_name               | core | string     |
| system_data                     | core | json       | The system metadata related to this resource.                                                                                                                                                                                                                                                  |
| tags                            | core | hstore_csv |
| type                            | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                                                                                                                      |
| workspace_id                    | core | string     | The full ARM resource ID of the Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2                          |
