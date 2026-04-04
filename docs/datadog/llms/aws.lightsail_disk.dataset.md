# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lightsail_disk.dataset.md

---
title: Lightsail Disk
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lightsail Disk
---

# Lightsail Disk

Lightsail Disk is a block storage resource in Amazon Lightsail that provides persistent storage for Lightsail instances and containers. It offers scalable, high-performance SSD-based storage that can be attached to instances, detached, and reattached as needed. Disks are designed for durability and availability, with automatic replication within an Availability Zone.

```
aws.lightsail_disk
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                           | Description |
| ----------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| add_ons           | core | json       | An array of objects representing the add-ons enabled on the disk.                                                                                                                                                                                   |
| arn               | core | string     | The Amazon Resource Name (ARN) of the disk.                                                                                                                                                                                                         |
| attached_to       | core | string     | The resources to which the disk is attached.                                                                                                                                                                                                        |
| attachment_state  | core | string     | (Discontinued) The attachment state of the disk. In releases prior to November 14, 2017, this parameter returned attached for system disks in the API response. It is now discontinued, but still included in the response. Use isAttached instead. |
| auto_mount_status | core | string     | The status of automatically mounting a storage disk to a virtual computer. This parameter only applies to Lightsail for Research resources.                                                                                                         |
| created_at        | core | timestamp  | The date when the disk was created.                                                                                                                                                                                                                 |
| gb_in_use         | core | int64      | (Discontinued) The number of GB in use by the disk. In releases prior to November 14, 2017, this parameter was not included in the API response. It is now discontinued.                                                                            |
| iops              | core | int64      | The input/output operations per second (IOPS) of the disk.                                                                                                                                                                                          |
| is_attached       | core | bool       | A Boolean value indicating whether the disk is attached.                                                                                                                                                                                            |
| is_system_disk    | core | bool       | A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).                                                                                                                                               |
| location          | core | json       | The AWS Region and Availability Zone where the disk is located.                                                                                                                                                                                     |
| name              | core | string     | The unique name of the disk.                                                                                                                                                                                                                        |
| path              | core | string     | The disk path.                                                                                                                                                                                                                                      |
| resource_type     | core | string     | The Lightsail resource type (Disk).                                                                                                                                                                                                                 |
| size_in_gb        | core | int64      | The size of the disk in GB.                                                                                                                                                                                                                         |
| state             | core | string     | Describes the status of the disk.                                                                                                                                                                                                                   |
| support_code      | core | string     | The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.                      |
| tags              | core | hstore_csv |
