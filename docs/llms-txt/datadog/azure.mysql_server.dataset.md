# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.mysql_server.dataset.md

---
title: Azure Database for MySQL Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Azure Database for MySQL Server
---

# Azure Database for MySQL Server

Azure Database for MySQL Server is a fully managed relational database service based on the MySQL engine. It handles maintenance, backups, and security automatically, allowing users to focus on application development. The service offers built-in high availability, scaling options, and performance tuning. It supports multiple compute and storage tiers to match workload requirements.

```
azure.mysql_server
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ---------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| administrator_login          | core | string     | The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).                                                        |
| byok_enforcement             | core | string     | Status showing whether the server data encryption is enabled with customer-managed keys.                                                                                                  |
| earliest_restore_date        | core | string     | Earliest restore point creation time (ISO8601 format)                                                                                                                                     |
| fully_qualified_domain_name  | core | string     | The fully qualified domain name of a server.                                                                                                                                              |
| id                           | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| identity                     | core | json       | Properties to configure Identity for Bring your Own Keys                                                                                                                                  |
| infrastructure_encryption    | core | string     | Status showing whether the server enabled infrastructure encryption.                                                                                                                      |
| location                     | core | string     | The geo-location where the resource lives                                                                                                                                                 |
| master_server_id             | core | string     | The master server id of a replica server.                                                                                                                                                 |
| minimal_tls_version          | core | string     | Enforce a minimal Tls version for the server.                                                                                                                                             |
| name                         | core | string     | The name of the resource                                                                                                                                                                  |
| private_endpoint_connections | core | json       | List of private endpoint connections on a server                                                                                                                                          |
| public_network_access        | core | string     | Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'                                                      |
| replica_capacity             | core | int64      | The maximum number of replicas that a primary server can have.                                                                                                                            |
| replication_role             | core | string     | The replication role.                                                                                                                                                                     |
| resource_group               | core | string     |
| sku                          | core | json       | Billing information related properties of a server.                                                                                                                                       |
| ssl_enforcement              | core | string     | Enable ssl enforcement or not when connect to server.                                                                                                                                     |
| storage_profile              | core | json       | Storage profile of a server.                                                                                                                                                              |
| subscription_id              | core | string     |
| subscription_name            | core | string     |
| tags                         | core | hstore_csv |
| type                         | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
| user_visible_state           | core | string     | A state of a server that is visible to user.                                                                                                                                              |
| version                      | core | string     | The version of a server.                                                                                                                                                                  |
