# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_fsx_lustre.dataset.md

---
title: DataSync FSx for Lustre Location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync FSx for Lustre Location
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.datasync_location_fsx_lustre.dataset/index.html
---

# DataSync FSx for Lustre Location

DataSync FSx for Lustre Location in AWS represents a connection point that allows AWS DataSync to transfer data to and from an Amazon FSx for Lustre file system. It defines the configuration details needed for DataSync to access the file system, enabling fast, secure, and automated data movement between FSx for Lustre and other storage services or on-premises systems.

```
aws.datasync_location_fsx_lustre
```

## Fields

| Title               | ID   | Type          | Data Type                                                                                                       | Description |
| ------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| creation_time       | core | timestamp     | The time that the FSx for Lustre location was created.                                                          |
| location_arn        | core | string        | The Amazon Resource Name (ARN) of the FSx for Lustre location that was described.                               |
| location_uri        | core | string        | The URI of the FSx for Lustre location that was described.                                                      |
| security_group_arns | core | array<string> | The Amazon Resource Names (ARNs) of the security groups that are configured for the FSx for Lustre file system. |
| tags                | core | hstore        |
