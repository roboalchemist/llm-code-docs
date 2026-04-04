# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.mysql_flexible_server_configuration.dataset.md

---
title: MySQL Flexible Server Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MySQL Flexible Server Configuration
---

# MySQL Flexible Server Configuration

This table represents the MySQL Flexible Server Configuration resource from Microsoft Azure.

```
azure.mysql_flexible_server_configuration
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| allowed_values            | core | string     | Allowed values of the configuration.                                                                                                                                                      |
| data_type                 | core | string     | Data type of the configuration.                                                                                                                                                           |
| default_value             | core | string     | Default value of the configuration.                                                                                                                                                       |
| description               | core | string     | Description of the configuration.                                                                                                                                                         |
| id                        | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| is_config_pending_restart | core | string     | If is the configuration pending restart or not.                                                                                                                                           |
| is_dynamic_config         | core | string     | If is the configuration dynamic.                                                                                                                                                          |
| is_read_only              | core | string     | If is the configuration read only.                                                                                                                                                        |
| location                  | core | string     |
| name                      | core | string     | The name of the resource                                                                                                                                                                  |
| resource_group            | core | string     |
| subscription_id           | core | string     |
| subscription_name         | core | string     |
| system_data               | core | json       | The system metadata relating to this resource.                                                                                                                                            |
| tags                      | core | hstore_csv |
| type                      | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
| value                     | core | string     | Value of the configuration.                                                                                                                                                               |
