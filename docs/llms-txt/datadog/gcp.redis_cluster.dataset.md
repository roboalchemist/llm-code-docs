# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.redis_cluster.dataset.md

---
title: Redis Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redis Cluster
---

# Redis Cluster

Redis Cluster on Google Cloud is a managed in-memory data store service based on open-source Redis. It provides high availability, automatic sharding, and horizontal scaling to handle large datasets with low latency. This service is ideal for caching, real-time analytics, session management, and high-throughput workloads, while reducing the operational overhead of managing Redis infrastructure.

```
gcp.redis_cluster
```

## Fields

| Title                                    | ID   | Type          | Data Type                                                                                                                                                                                                                               | Description |
| ---------------------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                     | core | string        |
| ancestors                                | core | array<string> |
| async_cluster_endpoints_deletion_enabled | core | bool          | Optional. If true, cluster endpoints that are created and registered by customers can be deleted asynchronously. That is, such a cluster endpoint can be de-registered before the forwarding rules in the cluster endpoint are deleted. |
| authorization_mode                       | core | string        | Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.                                                                                                                       |
| automated_backup_config                  | core | json          | Optional. The automated backup config for the cluster.                                                                                                                                                                                  |
| backup_collection                        | core | string        | Optional. Output only. The backup collection full resource name. Example: projects/{project}/locations/{location}/backupCollections/{collection}                                                                                        |
| cluster_endpoints                        | core | json          | Optional. A list of cluster endpoints.                                                                                                                                                                                                  |
| create_time                              | core | timestamp     | Output only. The timestamp associated with the cluster creation request.                                                                                                                                                                |
| cross_cluster_replication_config         | core | json          | Optional. Cross cluster replication config.                                                                                                                                                                                             |
| datadog_display_name                     | core | string        |
| deletion_protection_enabled              | core | bool          | Optional. The delete operation will fail when the value is set to true.                                                                                                                                                                 |
| discovery_endpoints                      | core | json          | Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.                                                                                  |
| encryption_info                          | core | json          | Output only. Encryption information of the data at rest of the cluster.                                                                                                                                                                 |
| gcs_source                               | core | json          | Optional. Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters. Read permission is required to import from the provided Cloud Storage objects.                                 |
| labels                                   | core | array<string> | Optional. Labels to represent user-provided metadata.                                                                                                                                                                                   |
| maintenance_policy                       | core | json          | Optional. ClusterMaintenancePolicy determines when to allow or deny updates.                                                                                                                                                            |
| maintenance_schedule                     | core | json          | Output only. ClusterMaintenanceSchedule Output only Published maintenance schedule.                                                                                                                                                     |
| managed_backup_source                    | core | json          | Optional. Backups generated and managed by memorystore service.                                                                                                                                                                         |
| name                                     | core | string        | Required. Identifier. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`                                                    |
| node_type                                | core | string        | Optional. The type of a redis node in the cluster. NodeType determines the underlying machine-type of a redis node.                                                                                                                     |
| organization_id                          | core | string        |
| parent                                   | core | string        |
| persistence_config                       | core | json          | Optional. Persistence config (RDB, AOF) for the cluster.                                                                                                                                                                                |
| precise_size_gb                          | core | float64       | Output only. Precise value of redis memory size in GB for the entire cluster.                                                                                                                                                           |
| project_id                               | core | string        |
| project_number                           | core | string        |
| psc_configs                              | core | json          | Optional. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.                          |
| psc_connections                          | core | json          | Output only. The list of PSC connections that are auto-created through service connectivity automation.                                                                                                                                 |
| psc_service_attachments                  | core | json          | Output only. Service attachment details to configure Psc connections                                                                                                                                                                    |
| region_id                                | core | string        |
| replica_count                            | core | int64         | Optional. The number of replica nodes per shard.                                                                                                                                                                                        |
| resource_name                            | core | string        |
| shard_count                              | core | int64         | Optional. Number of shards for the Redis cluster.                                                                                                                                                                                       |
| size_gb                                  | core | int64         | Output only. Redis memory size in GB for the entire cluster rounded up to the next integer.                                                                                                                                             |
| state                                    | core | string        | Output only. The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED                                                                                                                                |
| state_info                               | core | json          | Output only. Additional information about the current state of the cluster.                                                                                                                                                             |
| tags                                     | core | hstore_csv    |
| transit_encryption_mode                  | core | string        | Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.                                                                                                                     |
| uid                                      | core | string        | Output only. System assigned, unique identifier for the cluster.                                                                                                                                                                        |
| zone_distribution_config                 | core | json          | Optional. This config will be used to determine how the customer wants us to distribute cluster resources within the region.                                                                                                            |
| zone_id                                  | core | string        |
