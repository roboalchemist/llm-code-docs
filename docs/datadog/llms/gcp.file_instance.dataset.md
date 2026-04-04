# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.file_instance.dataset.md

---
title: Filestore Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Filestore Instance
---

# Filestore Instance

Filestore Instance in Google Cloud is a managed network-attached storage service that provides high-performance file systems for applications requiring shared file storage. It is ideal for workloads like content management, media processing, and data analytics, offering scalable capacity and throughput with simple integration into Google Cloud services.

```
gcp.file_instance
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                            | Description |
| ---------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| ancestors                    | core | array<string> |
| create_time                  | core | timestamp     | Output only. The time when the instance was created.                                                                                                                                                 |
| custom_performance_supported | core | bool          | Output only. Indicates whether this instance supports configuring its performance. If true, the user can configure the instance's performance by using the 'performance_config' field.               |
| datadog_display_name         | core | string        |
| deletion_protection_enabled  | core | bool          | Optional. Indicates whether the instance is protected against deletion.                                                                                                                              |
| deletion_protection_reason   | core | string        | Optional. The reason for enabling deletion protection.                                                                                                                                               |
| description                  | core | string        | The description of the instance (2048 characters or less).                                                                                                                                           |
| etag                         | core | string        | Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.                                                                                         |
| file_shares                  | core | json          | File system shares on the instance. For this version, only a single file share is supported.                                                                                                         |
| kms_key_name                 | core | string        | KMS key name used for data encryption.                                                                                                                                                               |
| labels                       | core | array<string> | Resource labels to represent user provided metadata.                                                                                                                                                 |
| name                         | core | string        | Output only. The resource name of the instance, in the format `projects/{project}/locations/{location}/instances/{instance}`.                                                                        |
| networks                     | core | json          | VPC networks to which the instance is connected. For this version, only a single network is supported.                                                                                               |
| organization_id              | core | string        |
| parent                       | core | string        |
| performance_config           | core | json          | Optional. Used to configure performance.                                                                                                                                                             |
| performance_limits           | core | json          | Output only. Used for getting performance limits.                                                                                                                                                    |
| project_id                   | core | string        |
| project_number               | core | string        |
| protocol                     | core | string        | Immutable. The protocol indicates the access protocol for all shares in the instance. This field is immutable and it cannot be changed after the instance has been created. Default value: `NFS_V3`. |
| region_id                    | core | string        |
| replication                  | core | json          | Optional. Replication configuration.                                                                                                                                                                 |
| resource_name                | core | string        |
| satisfies_pzi                | core | bool          | Output only. Reserved for future use.                                                                                                                                                                |
| satisfies_pzs                | core | bool          | Output only. Reserved for future use.                                                                                                                                                                |
| state                        | core | string        | Output only. The instance state.                                                                                                                                                                     |
| status_message               | core | string        | Output only. Additional information about the instance state, if available.                                                                                                                          |
| suspension_reasons           | core | array<string> | Output only. Field indicates all the reasons the instance is in "SUSPENDED" state.                                                                                                                   |
| tags                         | core | hstore_csv    |
| tier                         | core | string        | The service tier of the instance.                                                                                                                                                                    |
| zone_id                      | core | string        |
