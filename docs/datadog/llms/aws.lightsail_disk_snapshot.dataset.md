# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lightsail_disk_snapshot.dataset.md

---
title: Lightsail Disk Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lightsail Disk Snapshot
---

# Lightsail Disk Snapshot

A Lightsail Disk Snapshot in AWS is a point-in-time backup of a Lightsail block storage disk. It captures the entire state of the disk, allowing you to create new disks from the snapshot or restore data if needed. Snapshots make it easy to back up, duplicate, and migrate storage volumes within Lightsail environments.

```
aws.lightsail_disk_snapshot
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                                                                      | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| arn                   | core | string     | The Amazon Resource Name (ARN) of the disk snapshot.                                                                                                                                                                           |
| created_at            | core | timestamp  | The date when the disk snapshot was created.                                                                                                                                                                                   |
| from_disk_arn         | core | string     | The Amazon Resource Name (ARN) of the source disk from which the disk snapshot was created.                                                                                                                                    |
| from_disk_name        | core | string     | The unique name of the source disk from which the disk snapshot was created.                                                                                                                                                   |
| from_instance_arn     | core | string     | The Amazon Resource Name (ARN) of the source instance from which the disk (system volume) snapshot was created.                                                                                                                |
| from_instance_name    | core | string     | The unique name of the source instance from which the disk (system volume) snapshot was created.                                                                                                                               |
| is_from_auto_snapshot | core | bool       | A Boolean value indicating whether the snapshot was created from an automatic snapshot.                                                                                                                                        |
| location              | core | json       | The AWS Region and Availability Zone where the disk snapshot was created.                                                                                                                                                      |
| name                  | core | string     | The name of the disk snapshot (my-disk-snapshot).                                                                                                                                                                              |
| progress              | core | string     | The progress of the snapshot.                                                                                                                                                                                                  |
| resource_type         | core | string     | The Lightsail resource type (DiskSnapshot).                                                                                                                                                                                    |
| size_in_gb            | core | int64      | The size of the disk in GB.                                                                                                                                                                                                    |
| state                 | core | string     | The status of the disk snapshot operation.                                                                                                                                                                                     |
| support_code          | core | string     | The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily. |
| tags                  | core | hstore_csv |
