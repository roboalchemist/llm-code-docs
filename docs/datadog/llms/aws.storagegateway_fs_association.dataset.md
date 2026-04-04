# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.storagegateway_fs_association.dataset.md

---
title: Storage Gateway Fs Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Gateway Fs Association
---

# Storage Gateway Fs Association

This table represents the Storage Gateway Fs Association resource from Amazon Web Services.

```
aws.storagegateway_fs_association
```

## Fields

| Title                                  | ID   | Type       | Data Type                                                                                                                                                                                                                                      | Description |
| -------------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                   | core | string     |
| account_id                             | core | string     |
| audit_destination_arn                  | core | string     | The Amazon Resource Name (ARN) of the storage used for the audit logs.                                                                                                                                                                         |
| cache_attributes                       | core | json       |
| endpoint_network_configuration         | core | json       | Specifies network configuration information for the gateway associated with the Amazon FSx file system. <note> If multiple file systems are associated with this gateway, this parameter's <code>IpAddresses</code> field is required. </note> |
| file_system_association_arn            | core | string     | The Amazon Resource Name (ARN) of the file system association.                                                                                                                                                                                 |
| file_system_association_status         | core | string     | The status of the file system association. Valid Values: <code>AVAILABLE</code> | <code>CREATING</code> | <code>DELETING</code> | <code>FORCE_DELETING</code> | <code>UPDATING</code> | <code>ERROR</code>                                     |
| file_system_association_status_details | core | json       | An array containing the FileSystemAssociationStatusDetail data type, which provides detailed information on file system association status.                                                                                                    |
| gateway_arn                            | core | string     |
| location_arn                           | core | string     | The ARN of the backend Amazon FSx file system used for storing file data. For information, see <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_FileSystem.html">FileSystem</a> in the <i>Amazon FSx API Reference</i>.        |
| tags                                   | core | hstore_csv |
