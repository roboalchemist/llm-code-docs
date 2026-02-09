# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.machine_learning_services_registry.dataset.md

---
title: Machine Learning Services Registry
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Machine Learning Services Registry
---

# Machine Learning Services Registry

This table represents the machine_learning_services_registry resource from Microsoft Azure.

```
azure.machine_learning_services_registry
```

## Fields

| Title                                 | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ------------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string     |
| discovery_url                         | core | string     | Discovery URL for the Registry                                                                                                                                                            |
| id                                    | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| identity                              | core | json       | Managed service identity (system assigned and/or user assigned identities)                                                                                                                |
| intellectual_property_publisher       | core | string     | IntellectualPropertyPublisher for the registry                                                                                                                                            |
| kind                                  | core | string     | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type.                                                                                    |
| location                              | core | string     | The geo-location where the resource lives                                                                                                                                                 |
| managed_resource_group                | core | json       | ResourceId of the managed RG if the registry has system created resources                                                                                                                 |
| ml_flow_registry_uri                  | core | string     | MLFlow Registry URI for the Registry                                                                                                                                                      |
| name                                  | core | string     | The name of the resource                                                                                                                                                                  |
| public_network_access                 | core | string     | Is the Registry accessible from the internet?Possible values: "Enabled" or "Disabled"                                                                                                     |
| region_details                        | core | json       | Details of each region the registry is in                                                                                                                                                 |
| registry_private_endpoint_connections | core | json       | Private endpoint connections info used for pending connections in private link portal                                                                                                     |
| resource_group                        | core | string     |
| sku                                   | core | json       | Sku details required for ARM contract for Autoscaling.                                                                                                                                    |
| subscription_id                       | core | string     |
| subscription_name                     | core | string     |
| system_data                           | core | json       | Azure Resource Manager metadata containing createdBy and modifiedBy information.                                                                                                          |
| tags                                  | core | hstore_csv |
| type                                  | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
