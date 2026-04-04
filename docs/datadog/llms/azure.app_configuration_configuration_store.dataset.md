# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.app_configuration_configuration_store.dataset.md

---
title: App Configuration Configuration Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > App Configuration Configuration
  Store
---

# App Configuration Configuration Store

This table represents the app_configuration_configuration_store resource from Microsoft Azure.

```
azure.app_configuration_configuration_store
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ----------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| create_mode                   | core | string     | Indicates whether the configuration store need to be recovered.                                                                                                                           |
| creation_date                 | core | string     | The creation date of configuration store.                                                                                                                                                 |
| data_plane_proxy              | core | json       | Property specifying the configuration of data plane proxy for Azure Resource Manager (ARM).                                                                                               |
| disable_local_auth            | core | bool       | Disables all authentication methods other than AAD authentication.                                                                                                                        |
| enable_purge_protection       | core | bool       | Property specifying whether protection against purge is enabled for this configuration store.                                                                                             |
| encryption                    | core | json       | The encryption settings of the configuration store.                                                                                                                                       |
| endpoint                      | core | string     | The DNS endpoint where the configuration store API will be available.                                                                                                                     |
| id                            | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| identity                      | core | json       | The managed identity information, if configured.                                                                                                                                          |
| location                      | core | string     | The geo-location where the resource lives                                                                                                                                                 |
| name                          | core | string     | The name of the resource                                                                                                                                                                  |
| private_endpoint_connections  | core | json       | The list of private endpoint connections that are set up for this resource.                                                                                                               |
| provisioning_state            | core | string     | The provisioning state of the configuration store.                                                                                                                                        |
| public_network_access         | core | string     | Control permission for data plane traffic coming from public networks while private endpoint is enabled.                                                                                  |
| resource_group                | core | string     |
| sku                           | core | json       | The sku of the configuration store.                                                                                                                                                       |
| soft_delete_retention_in_days | core | int64      | The amount of time in days that the configuration store will be retained when it is soft deleted.                                                                                         |
| subscription_id               | core | string     |
| subscription_name             | core | string     |
| system_data                   | core | json       | Resource system metadata.                                                                                                                                                                 |
| tags                          | core | hstore_csv |
| type                          | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
