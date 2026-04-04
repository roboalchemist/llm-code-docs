# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.mysql_flexible_server.dataset.md

---
title: MySQL Flexible Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MySQL Flexible Server
---

# MySQL Flexible Server

This table represents the MySQL Flexible Server resource from Microsoft Azure.

```
azure.mysql_flexible_server
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| --------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| administrator_login         | core | string     | The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).                                                        |
| availability_zone           | core | string     | availability Zone information of the server.                                                                                                                                              |
| backup                      | core | json       | Backup related properties of a server.                                                                                                                                                    |
| create_mode                 | core | string     | The mode to create a new MySQL server.                                                                                                                                                    |
| data_encryption             | core | json       | The Data Encryption for CMK.                                                                                                                                                              |
| fully_qualified_domain_name | core | string     | The fully qualified domain name of a server.                                                                                                                                              |
| high_availability           | core | json       | High availability related properties of a server.                                                                                                                                         |
| id                          | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| identity                    | core | json       | The cmk identity for the server.                                                                                                                                                          |
| location                    | core | string     | The geo-location where the resource lives                                                                                                                                                 |
| maintenance_window          | core | json       | Maintenance window of a server.                                                                                                                                                           |
| name                        | core | string     | The name of the resource                                                                                                                                                                  |
| network                     | core | json       | Network related properties of a server.                                                                                                                                                   |
| replica_capacity            | core | int64      | The maximum number of replicas that a primary server can have.                                                                                                                            |
| replication_role            | core | string     | The replication role.                                                                                                                                                                     |
| resource_group              | core | string     |
| restore_point_in_time       | core | string     | Restore point creation time (ISO8601 format), specifying the time to restore from.                                                                                                        |
| sku                         | core | json       | The SKU (pricing tier) of the server.                                                                                                                                                     |
| source_server_resource_id   | core | string     | The source MySQL server id.                                                                                                                                                               |
| state                       | core | string     | The state of a server.                                                                                                                                                                    |
| storage                     | core | json       | Storage related properties of a server.                                                                                                                                                   |
| subscription_id             | core | string     |
| subscription_name           | core | string     |
| system_data                 | core | json       | The system metadata relating to this resource.                                                                                                                                            |
| tags                        | core | hstore_csv |
| type                        | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
| version                     | core | string     | Server version.                                                                                                                                                                           |
