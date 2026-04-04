# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.backup_gateway_hypervisor.dataset.md

---
title: Backup Gateway Hypervisor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup Gateway Hypervisor
---

# Backup Gateway Hypervisor

This table represents the Backup Gateway Hypervisor resource from Amazon Web Services.

```
aws.backup_gateway_hypervisor
```

## Fields

| Title                               | ID   | Type       | Data Type                                                                                                                                                              | Description |
| ----------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| account_id                          | core | string     |
| host                                | core | string     | The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).                                                           |
| hypervisor_arn                      | core | string     | The Amazon Resource Name (ARN) of the hypervisor.                                                                                                                      |
| kms_key_arn                         | core | string     | The Amazon Resource Name (ARN) of the KMS used to encrypt the hypervisor.                                                                                              |
| last_successful_metadata_sync_time  | core | timestamp  | This is the time when the most recent successful sync of metadata occurred.                                                                                            |
| latest_metadata_sync_status         | core | string     | This is the most recent status for the indicated metadata sync.                                                                                                        |
| latest_metadata_sync_status_message | core | string     | This is the most recent status for the indicated metadata sync.                                                                                                        |
| log_group_arn                       | core | string     | The Amazon Resource Name (ARN) of the group of gateways within the requested log.                                                                                      |
| name                                | core | string     | This is the name of the specified hypervisor.                                                                                                                          |
| state                               | core | string     | This is the current state of the specified hypervisor. The possible states are <code>PENDING</code>, <code>ONLINE</code>, <code>OFFLINE</code>, or <code>ERROR</code>. |
| tags                                | core | hstore_csv |
