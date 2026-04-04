# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.databricks_workspace.dataset.md

---
title: Azure Databricks Workspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Azure Databricks Workspace
---

# Azure Databricks Workspace

Azure Databricks Workspace is an analytics and machine learning platform built on Apache Spark, fully managed within Azure. It provides a collaborative environment for data engineers, data scientists, and analysts to process large-scale data, build AI models, and integrate with other Azure services. The workspace simplifies cluster management, offers interactive notebooks, and supports seamless scaling for big data and advanced analytics workloads.

```
azure.databricks_workspace
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                                                                      | Description |
| ---------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| authorizations               | core | json       | The workspace provider authorizations.                                                                                                                                                                                                         |
| created_by                   | core | json       | Provides details of the entity that created/updated the workspace.                                                                                                                                                                             |
| created_date_time            | core | string     | The date and time stamp when the workspace was created.                                                                                                                                                                                        |
| disk_encryption_set_id       | core | string     | The resource Id of the managed disk encryption set.                                                                                                                                                                                            |
| encryption                   | core | json       | Encryption properties for databricks workspace                                                                                                                                                                                                 |
| id                           | core | string     | Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}                                                      |
| location                     | core | string     | The geo-location where the resource lives                                                                                                                                                                                                      |
| managed_disk_identity        | core | json       | The Managed Identity details for storage account.                                                                                                                                                                                              |
| managed_resource_group_id    | core | string     | The managed resource group Id.                                                                                                                                                                                                                 |
| name                         | core | string     | The name of the resource                                                                                                                                                                                                                       |
| parameters                   | core | json       | Custom Parameters used for Cluster Creation.                                                                                                                                                                                                   |
| private_endpoint_connections | core | json       | Private endpoint connections created on the workspace                                                                                                                                                                                          |
| provisioning_state           | core | string     | Provisioning status of the workspace.                                                                                                                                                                                                          |
| public_network_access        | core | string     | The network access type for accessing workspace. Set value to disabled to access workspace only via private link.                                                                                                                              |
| required_nsg_rules           | core | string     | Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only. |
| resource_group               | core | string     |
| sku                          | core | json       | SKU for the resource.                                                                                                                                                                                                                          |
| storage_account_identity     | core | json       | The Managed Identity details for storage account.                                                                                                                                                                                              |
| subscription_id              | core | string     |
| subscription_name            | core | string     |
| system_data                  | core | json       | Metadata pertaining to creation and last modification of the resource.                                                                                                                                                                         |
| tags                         | core | hstore_csv |
| type                         | core | string     | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.                                                                                                                                          |
| ui_definition_uri            | core | string     | The blob URI where the UI definition file is located.                                                                                                                                                                                          |
| updated_by                   | core | json       | Provides details of the entity that created/updated the workspace.                                                                                                                                                                             |
| workspace_id                 | core | string     | The unique identifier of the databricks workspace in databricks control plane.                                                                                                                                                                 |
| workspace_url                | core | string     | The workspace URL which is of the format 'adb-{workspaceId}.{random}.azuredatabricks.net'                                                                                                                                                      |
