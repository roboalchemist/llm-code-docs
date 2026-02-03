# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.efs_access_point.dataset.md

---
title: EFS Access Point
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EFS Access Point
---

# EFS Access Point

An EFS Access Point is an application-specific entry point into an Amazon Elastic File System. It simplifies access management by providing a unique access path with enforced user and group identities, as well as root directory settings. This allows multiple applications or tenants to securely share the same file system while maintaining isolation and consistent permissions.

```
aws.efs_access_point
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                                                                         | Description |
| ---------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| access_point_arn | core | string     | The unique Amazon Resource Name (ARN) associated with the access point.                                                                                                           |
| access_point_id  | core | string     | The ID of the access point, assigned by Amazon EFS.                                                                                                                               |
| account_id       | core | string     |
| client_token     | core | string     | The opaque string specified in the request to ensure idempotent creation.                                                                                                         |
| file_system_id   | core | string     | The ID of the EFS file system that the access point applies to.                                                                                                                   |
| life_cycle_state | core | string     | Identifies the lifecycle phase of the access point.                                                                                                                               |
| name             | core | string     | The name of the access point. This is the value of the Name tag.                                                                                                                  |
| owner_id         | core | string     | Identifies the Amazon Web Services account that owns the access point resource.                                                                                                   |
| posix_user       | core | json       | The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point. |
| root_directory   | core | json       | The directory on the EFS file system that the access point exposes as the root directory to NFS clients using the access point.                                                   |
| tags             | core | hstore_csv |
