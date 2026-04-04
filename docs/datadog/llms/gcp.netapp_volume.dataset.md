# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.netapp_volume.dataset.md

---
title: NetApp Volume
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > NetApp Volume
---

# NetApp Volume

NetApp Volume on Google Cloud is a managed file storage resource that provides high-performance, scalable, and secure NFS volumes. It is built on NetApp technology and is ideal for workloads that require enterprise-grade data management features such as snapshots, cloning, and replication. This service is commonly used for applications needing shared file storage, including databases, analytics, and development environments.

```
gcp.netapp_volume
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                              | Description |
| ----------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                          | core | string        |
| active_directory              | core | string        | Output only. Specifies the ActiveDirectory name of a SMB volume.                                                                                                                                       |
| ancestors                     | core | array<string> |
| backup_config                 | core | json          | BackupConfig of the volume.                                                                                                                                                                            |
| capacity_gib                  | core | int64         | Required. Capacity in GIB of the volume                                                                                                                                                                |
| cold_tier_size_gib            | core | int64         | Output only. Size of the volume cold tier data rounded down to the nearest GiB.                                                                                                                        |
| create_time                   | core | timestamp     | Output only. Create time of the volume                                                                                                                                                                 |
| datadog_display_name          | core | string        |
| description                   | core | string        | Optional. Description of the volume                                                                                                                                                                    |
| encryption_type               | core | string        | Output only. Specified the current volume encryption key source.                                                                                                                                       |
| export_policy                 | core | json          | Optional. Export policy of the volume                                                                                                                                                                  |
| has_replication               | core | bool          | Output only. Indicates whether the volume is part of a replication relationship.                                                                                                                       |
| hybrid_replication_parameters | core | json          | Optional. The Hybrid Replication parameters for the volume.                                                                                                                                            |
| kerberos_enabled              | core | bool          | Optional. Flag indicating if the volume is a kerberos volume or not, export policy rules control kerberos security modes (krb5, krb5i, krb5p).                                                         |
| kms_config                    | core | string        | Output only. Specifies the KMS config to be used for volume encryption.                                                                                                                                |
| labels                        | core | array<string> | Optional. Labels as key value pairs                                                                                                                                                                    |
| large_capacity                | core | bool          | Optional. Flag indicating if the volume will be a large capacity volume or a regular volume.                                                                                                           |
| ldap_enabled                  | core | bool          | Output only. Flag indicating if the volume is NFS LDAP enabled or not.                                                                                                                                 |
| mount_options                 | core | json          | Output only. Mount options of this volume                                                                                                                                                              |
| multiple_endpoints            | core | bool          | Optional. Flag indicating if the volume will have an IP address per node for volumes supporting multiple IP endpoints. Only the volume with large_capacity will be allowed to have multiple endpoints. |
| name                          | core | string        | Identifier. Name of the volume                                                                                                                                                                         |
| network                       | core | string        | Output only. VPC Network name. Format: projects/{project}/global/networks/{network}                                                                                                                    |
| organization_id               | core | string        |
| parent                        | core | string        |
| project_id                    | core | string        |
| project_number                | core | string        |
| protocols                     | core | array<string> | Required. Protocols required for the volume                                                                                                                                                            |
| psa_range                     | core | string        | Output only. This field is not implemented. The values provided in this field are ignored.                                                                                                             |
| region_id                     | core | string        |
| replica_zone                  | core | string        | Output only. Specifies the replica zone for regional volume.                                                                                                                                           |
| resource_name                 | core | string        |
| restore_parameters            | core | json          | Optional. Specifies the source of the volume to be created from.                                                                                                                                       |
| restricted_actions            | core | array<string> | Optional. List of actions that are restricted on this volume.                                                                                                                                          |
| security_style                | core | string        | Optional. Security Style of the Volume                                                                                                                                                                 |
| service_level                 | core | string        | Output only. Service level of the volume                                                                                                                                                               |
| share_name                    | core | string        | Required. Share name of the volume                                                                                                                                                                     |
| smb_settings                  | core | array<string> | Optional. SMB share settings for the volume.                                                                                                                                                           |
| snap_reserve                  | core | float64       | Optional. Snap_reserve specifies percentage of volume storage reserved for snapshot storage. Default is 0 percent.                                                                                     |
| snapshot_directory            | core | bool          | Optional. Snapshot_directory if enabled (true) the volume will contain a read-only .snapshot directory which provides access to each of the volume's snapshots.                                        |
| snapshot_policy               | core | json          | Optional. SnapshotPolicy for a volume.                                                                                                                                                                 |
| state                         | core | string        | Output only. State of the volume                                                                                                                                                                       |
| state_details                 | core | string        | Output only. State details of the volume                                                                                                                                                               |
| storage_pool                  | core | string        | Required. StoragePool name of the volume                                                                                                                                                               |
| tags                          | core | hstore_csv    |
| tiering_policy                | core | json          | Tiering policy for the volume.                                                                                                                                                                         |
| unix_permissions              | core | string        | Optional. Default unix style permission (e.g. 777) the mount point will be created with. Applicable for NFS protocol types only.                                                                       |
| used_gib                      | core | int64         | Output only. Used capacity in GIB of the volume. This is computed periodically and it does not represent the realtime usage.                                                                           |
| zone                          | core | string        | Output only. Specifies the active zone for regional volume.                                                                                                                                            |
| zone_id                       | core | string        |
