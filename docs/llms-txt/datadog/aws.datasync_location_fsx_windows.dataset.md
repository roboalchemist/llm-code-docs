# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_fsx_windows.dataset.md

---
title: DataSync FSx for Windows File Server Location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > DataSync FSx for Windows File Server
  Location
---

# DataSync FSx for Windows File Server Location

DataSync FSx for Windows File Server Location in AWS represents a configured endpoint that allows AWS DataSync to transfer data to and from an Amazon FSx for Windows File Server file system. It stores connection details such as the file system ARN, domain, user credentials, and security group settings. This resource is used to automate and accelerate data movement between on-premises storage, other AWS services, or different FSx file systems while maintaining compatibility with Windows file system features like access control lists and SMB protocol support.

```
aws.datasync_location_fsx_windows
```

## Fields

| Title               | ID   | Type          | Data Type                                                                                                                                                                                                                                | Description |
| ------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| creation_time       | core | timestamp     | The time that the FSx for Windows File Server location was created.                                                                                                                                                                      |
| domain              | core | string        | The name of the Microsoft Active Directory domain that the FSx for Windows File Server file system belongs to.                                                                                                                           |
| location_arn        | core | string        | The ARN of the FSx for Windows File Server location.                                                                                                                                                                                     |
| location_uri        | core | string        | The uniform resource identifier (URI) of the FSx for Windows File Server location.                                                                                                                                                       |
| security_group_arns | core | array<string> | The ARNs of the Amazon EC2 security groups that provide access to your file system's preferred subnet. For information about configuring security groups for file system access, see the Amazon FSx for Windows File Server User Guide . |
| tags                | core | hstore_csv    |
| user                | core | string        | The user with the permissions to mount and access the FSx for Windows File Server file system.                                                                                                                                           |
