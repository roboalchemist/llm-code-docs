# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_fsx_ontap.dataset.md

---
title: DataSync Location for Amazon FSx for NetApp ONTAP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > DataSync Location for Amazon FSx for
  NetApp ONTAP
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.datasync_location_fsx_ontap.dataset/index.html
---

# DataSync Location for Amazon FSx for NetApp ONTAP

DataSync Location for Amazon FSx for NetApp ONTAP is a resource that defines a connection point between AWS DataSync and an FSx for ONTAP file system. It enables secure, automated, and high-performance data transfers between ONTAP volumes and other storage systems or AWS services. This location is used as either a source or destination in DataSync tasks, helping to simplify large-scale data migrations, replication, or ongoing synchronization while maintaining ONTAP's enterprise-grade features.

```
aws.datasync_location_fsx_ontap
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                            | Description |
| --------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| creation_time               | core | timestamp     | The time that the location was created.                                                                              |
| fsx_filesystem_arn          | core | string        | The ARN of the FSx for ONTAP file system.                                                                            |
| location_arn                | core | string        | The ARN of the FSx for ONTAP file system location.                                                                   |
| location_uri                | core | string        | The uniform resource identifier (URI) of the FSx for ONTAP file system location.                                     |
| protocol                    | core | json          | Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.                       |
| security_group_arns         | core | array<string> | The security groups that DataSync uses to access your FSx for ONTAP file system.                                     |
| storage_virtual_machine_arn | core | string        | The ARN of the storage virtual machine (SVM) on your FSx for ONTAP file system where you're copying data to or from. |
| tags                        | core | hstore        |
