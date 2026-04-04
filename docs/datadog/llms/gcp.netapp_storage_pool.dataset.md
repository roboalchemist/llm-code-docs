# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.netapp_storage_pool.dataset.md

---
title: NetApp Storage Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > NetApp Storage Pool
---

# NetApp Storage Pool

NetApp Storage Pool in Google Cloud is a managed storage resource that provides scalable, high-performance file storage for enterprise workloads. It is part of Cloud Volumes Service for NetApp, allowing users to create and manage storage pools that back volumes with flexible capacity and performance options. This resource is designed for applications requiring shared file storage, such as databases, analytics, and enterprise applications, while integrating with Google Cloud's security and management features.

```
gcp.netapp_storage_pool
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                  | Description |
| --------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string        |
| active_directory      | core | string        | Optional. Specifies the Active Directory to be used for creating a SMB volume.                                                                                                             |
| allow_auto_tiering    | core | bool          | Optional. True if the storage pool supports Auto Tiering enabled volumes. Default is false. Auto-tiering can be enabled after storage pool creation but it can't be disabled once enabled. |
| ancestors             | core | array<string> |
| capacity_gib          | core | int64         | Required. Capacity in GIB of the pool                                                                                                                                                      |
| create_time           | core | timestamp     | Output only. Create time of the storage pool                                                                                                                                               |
| datadog_display_name  | core | string        |
| description           | core | string        | Optional. Description of the storage pool                                                                                                                                                  |
| encryption_type       | core | string        | Output only. Specifies the current pool encryption key source.                                                                                                                             |
| global_access_allowed | core | bool          | Deprecated. Used to allow SO pool to access AD or DNS server from other regions.                                                                                                           |
| kms_config            | core | string        | Optional. Specifies the KMS config to be used for volume encryption.                                                                                                                       |
| labels                | core | array<string> | Optional. Labels as key value pairs                                                                                                                                                        |
| ldap_enabled          | core | bool          | Optional. Flag indicating if the pool is NFS LDAP enabled or not.                                                                                                                          |
| name                  | core | string        | Identifier. Name of the storage pool                                                                                                                                                       |
| network               | core | string        | Required. VPC Network name. Format: projects/{project}/global/networks/{network}                                                                                                           |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| psa_range             | core | string        | Optional. This field is not implemented. The values provided in this field are ignored.                                                                                                    |
| region_id             | core | string        |
| replica_zone          | core | string        | Optional. Specifies the replica zone for regional storagePool.                                                                                                                             |
| resource_name         | core | string        |
| satisfies_pzi         | core | bool          | Output only. Reserved for future use                                                                                                                                                       |
| satisfies_pzs         | core | bool          | Output only. Reserved for future use                                                                                                                                                       |
| service_level         | core | string        | Required. Service level of the storage pool                                                                                                                                                |
| state                 | core | string        | Output only. State of the storage pool                                                                                                                                                     |
| state_details         | core | string        | Output only. State details of the storage pool                                                                                                                                             |
| tags                  | core | hstore_csv    |
| volume_capacity_gib   | core | int64         | Output only. Allocated size of all volumes in GIB in the storage pool                                                                                                                      |
| volume_count          | core | int64         | Output only. Volume count of the storage pool                                                                                                                                              |
| zone                  | core | string        | Optional. Specifies the active zone for regional storagePool.                                                                                                                              |
| zone_id               | core | string        |
