# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.databricks_access_connector.dataset.md

---
title: Azure Databricks Access Connector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Azure Databricks Access Connector
---

# Azure Databricks Access Connector

Azure Databricks Access Connector is a managed identity resource that enables secure access from Azure Databricks to other Azure services without requiring credentials. It simplifies authentication by using Azure Active Directory and provides a secure way for Databricks to interact with resources like storage accounts or key vaults.

```
azure.databricks_access_connector
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| id                 | core | string     | Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| identity           | core | json       | Managed service identity (system assigned and/or user assigned identities)                                                                                                                |
| location           | core | string     | The geo-location where the resource lives                                                                                                                                                 |
| name               | core | string     | The name of the resource                                                                                                                                                                  |
| provisioning_state | core | string     | Provisioning status of the accessConnector.                                                                                                                                               |
| resource_group     | core | string     |
| subscription_id    | core | string     |
| subscription_name  | core | string     |
| system_data        | core | json       | Metadata pertaining to creation and last modification of the resource.                                                                                                                    |
| tags               | core | hstore_csv |
| type               | core | string     | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.                                                                                     |
