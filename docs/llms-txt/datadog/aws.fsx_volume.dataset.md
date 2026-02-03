# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.fsx_volume.dataset.md

---
title: FSx Volume
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > FSx Volume
---

# FSx Volume

An FSx Volume in AWS is a storage resource within Amazon FSx that provides scalable, high-performance file storage for workloads such as databases, analytics, and enterprise applications. It allows you to manage data at the volume level, supporting features like snapshots, backups, and access control.

```
aws.fsx_volume
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| --------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| administrative_actions      | core | json       | A list of administrative actions for the volume that are in process or waiting to be processed. Administrative actions describe changes to the volume that you have initiated using the UpdateVolume action.                                                                                                                                                                                                         |
| creation_time               | core | timestamp  | The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.                                                                                                                                                                                                                                                                                                            |
| file_system_id              | core | string     | The globally unique ID of the file system, assigned by Amazon FSx.                                                                                                                                                                                                                                                                                                                                                   |
| lifecycle                   | core | string     | The lifecycle status of the volume. AVAILABLE - The volume is fully available for use. CREATED - The volume has been created. CREATING - Amazon FSx is creating the new volume. DELETING - Amazon FSx is deleting an existing volume. FAILED - Amazon FSx was unable to create the volume. MISCONFIGURED - The volume is in a failed but recoverable state. PENDING - Amazon FSx hasn't started creating the volume. |
| lifecycle_transition_reason | core | json       | The reason why the volume lifecycle status changed.                                                                                                                                                                                                                                                                                                                                                                  |
| name                        | core | string     | The name of the volume.                                                                                                                                                                                                                                                                                                                                                                                              |
| ontap_configuration         | core | json       | The configuration of an Amazon FSx for NetApp ONTAP volume.                                                                                                                                                                                                                                                                                                                                                          |
| open_zfs_configuration      | core | json       | The configuration of an Amazon FSx for OpenZFS volume.                                                                                                                                                                                                                                                                                                                                                               |
| resource_arn                | core | string     | The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.                                                                                               |
| tags                        | core | hstore_csv |
| volume_id                   | core | string     | The system-generated, unique ID of the volume.                                                                                                                                                                                                                                                                                                                                                                       |
| volume_type                 | core | string     | The type of the volume.                                                                                                                                                                                                                                                                                                                                                                                              |
