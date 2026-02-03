# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_fsx_openzfs.dataset.md

---
title: DataSync Location FSx OpenZFS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync Location FSx OpenZFS
---

# DataSync Location FSx OpenZFS

This table represents the DataSync Location FSx OpenZFS resource from Amazon Web Services.

```
aws.datasync_location_fsx_openzfs
```

## Fields

| Title               | ID   | Type          | Data Type                                                                                                                                                                 | Description |
| ------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| creation_time       | core | timestamp     | The time that the FSx for OpenZFS location was created.                                                                                                                   |
| location_arn        | core | string        | The ARN of the FSx for OpenZFS location that was described.                                                                                                               |
| location_uri        | core | string        | The uniform resource identifier (URI) of the FSx for OpenZFS location that was described. Example: <code>fsxz://us-west-2.fs-1234567890abcdef02/fsx/folderA/folder</code> |
| protocol            | core | json          | The type of protocol that DataSync uses to access your file system.                                                                                                       |
| security_group_arns | core | array<string> | The ARNs of the security groups that are configured for the FSx for OpenZFS file system.                                                                                  |
| tags                | core | hstore_csv    |
