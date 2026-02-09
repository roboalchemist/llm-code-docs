# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.redis.dataset.md

---
title: Azure Managed Redis
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Azure Managed Redis
---

# Azure Managed Redis

Azure Managed Redis is a fully managed in-memory data store based on the open-source Redis engine. It provides high-performance caching, session storage, and real-time data processing with built-in scalability, security, and monitoring. This service removes the need to manage infrastructure, offering automated updates, patching, and high availability options.

```
azure.redis
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                                                                        | Description |
| ---------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| enable_non_ssl_port          | core | bool          | Specifies whether the non-ssl Redis server port (6379) is enabled.                                                                                                                                                                                               |
| host_name                    | core | string        | Redis host name.                                                                                                                                                                                                                                                 |
| id                           | core | string        | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"                                                                      |
| identity                     | core | json          | Managed service identity (system assigned and/or user assigned identities)                                                                                                                                                                                       |
| instances                    | core | json          | List of the Redis instances associated with the cache                                                                                                                                                                                                            |
| linked_servers               | core | json          | List of the linked servers associated with the cache                                                                                                                                                                                                             |
| location                     | core | string        | The geo-location where the resource lives                                                                                                                                                                                                                        |
| minimum_tls_version          | core | string        | Optional: requires clients to use a specified TLS version (or higher) to connect (e,g, '1.0', '1.1', '1.2')                                                                                                                                                      |
| name                         | core | string        | The name of the resource                                                                                                                                                                                                                                         |
| port                         | core | int64         | Redis non-SSL port.                                                                                                                                                                                                                                              |
| private_endpoint_connections | core | json          | List of private endpoint connection associated with the specified redis cache                                                                                                                                                                                    |
| provisioning_state           | core | string        | Redis instance provisioning status.                                                                                                                                                                                                                              |
| public_network_access        | core | string        | Whether or not public endpoint access is allowed for this cache. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. If 'Disabled', private endpoints are the exclusive access method. Default value is 'Enabled'                               |
| redis_configuration          | core | json          | All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta, maxmemory-policy,notify-keyspace-events, aof-backup-enabled, aof-storage-connection-string-0, aof-storage-connection-string-1 etc. |
| redis_version                | core | string        | Redis version. This should be in the form 'major[.minor]' (only 'major' is required) or the value 'latest' which refers to the latest stable Redis version that is available. Supported versions: 4.0, 6.0 (latest). Default value is 'latest'.                  |
| replicas_per_master          | core | int64         | The number of replicas to be created per primary.                                                                                                                                                                                                                |
| replicas_per_primary         | core | int64         | The number of replicas to be created per primary.                                                                                                                                                                                                                |
| resource_group               | core | string        |
| shard_count                  | core | int64         | The number of shards to be created on a Premium Cluster Cache.                                                                                                                                                                                                   |
| sku                          | core | json          | SKU parameters supplied to the create Redis operation.                                                                                                                                                                                                           |
| ssl_port                     | core | int64         | Redis SSL port.                                                                                                                                                                                                                                                  |
| static_ip                    | core | string        | Static IP address. Optionally, may be specified when deploying a Redis cache inside an existing Azure Virtual Network; auto assigned by default.                                                                                                                 |
| subnet_id                    | core | string        | The full resource ID of a subnet in a virtual network to deploy the Redis cache in. Example format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1                  |
| subscription_id              | core | string        |
| subscription_name            | core | string        |
| tags                         | core | hstore_csv    |
| type                         | core | string        | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                                                                                        |
| update_channel               | core | string        | Optional: Specifies the update channel for the monthly Redis updates your Redis Cache will receive. Caches using 'Preview' update channel get latest Redis updates at least 4 weeks ahead of 'Stable' channel caches. Default value is 'Stable'.                 |
| zones                        | core | array<string> | The availability zones.                                                                                                                                                                                                                                          |
