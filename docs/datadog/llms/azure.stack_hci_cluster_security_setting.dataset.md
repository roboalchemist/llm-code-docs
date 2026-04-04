# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.stack_hci_cluster_security_setting.dataset.md

---
title: Stack Hci Cluster Security Setting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Stack Hci Cluster Security Setting
---

# Stack Hci Cluster Security Setting

This table represents the stack_hci_cluster_security_setting resource from Microsoft Azure.

```
azure.stack_hci_cluster_security_setting
```

## Fields

| Title                              | ID   | Type       | Data Type                                                                                                                                                                                   | Description |
| ---------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string     |
| id                                 | core | string     | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| location                           | core | string     |
| name                               | core | string     | The name of the resource                                                                                                                                                                    |
| provisioning_state                 | core | string     | The status of the last operation.                                                                                                                                                           |
| resource_group                     | core | string     |
| secured_core_compliance_assignment | core | string     | Secured Core Compliance Assignment                                                                                                                                                          |
| security_compliance_status         | core | json       | Security Compliance Status                                                                                                                                                                  |
| subscription_id                    | core | string     |
| subscription_name                  | core | string     |
| system_data                        | core | json       | Azure Resource Manager metadata containing createdBy and modifiedBy information.                                                                                                            |
| tags                               | core | hstore_csv |
| type                               | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                   |
| wdac_compliance_assignment         | core | string     | WDAC Compliance Assignment                                                                                                                                                                  |
