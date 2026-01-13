# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_efs.dataset.md

---
title: DataSync Amazon EFS Location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync Amazon EFS Location
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.datasync_location_efs.dataset/index.html
---

# DataSync Amazon EFS Location

DataSync Amazon EFS Location represents a configured endpoint that allows AWS DataSync to access an Amazon Elastic File System (EFS). It defines the connection details, such as the EFS file system and mount options, enabling secure and efficient data transfers between EFS and other storage systems or services supported by DataSync.

```
aws.datasync_location_efs
```

## Fields

| Title                       | ID   | Type      | Data Type                                                                                                                                                                                | Description |
| --------------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string    |
| access_point_arn            | core | string    | The ARN of the access point that DataSync uses to access the Amazon EFS file system. For more information, see Accessing restricted file systems.                                        |
| account_id                  | core | string    |
| creation_time               | core | timestamp | The time that the location was created.                                                                                                                                                  |
| ec2_config                  | core | json      | The subnet and security groups that DataSync uses to connect to one of your Amazon EFS file system's mount targets.                                                                      |
| file_system_access_role_arn | core | string    | The Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system. For more information, see Creating a DataSync IAM role for file system access. |
| in_transit_encryption       | core | string    | Indicates whether DataSync uses Transport Layer Security (TLS) encryption when transferring data to or from the Amazon EFS file system.                                                  |
| location_arn                | core | string    | The ARN of the Amazon EFS file system location.                                                                                                                                          |
| location_uri                | core | string    | The URL of the Amazon EFS file system location.                                                                                                                                          |
| tags                        | core | hstore    |
