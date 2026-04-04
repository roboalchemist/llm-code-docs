# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.storagegateway_tapepool.dataset.md

---
title: Storage Gateway Tape Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Gateway Tape Pool
---

# Storage Gateway Tape Pool

This table represents the Storage Gateway Tape Pool resource from Amazon Web Services.

```
aws.storagegateway_tapepool
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                               | Description |
| --------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| pool_arn                    | core | string     | The Amazon Resource Name (ARN) of the custom tape pool. Use the <a>ListTapePools</a> operation to return a list of custom tape pools for your account and Amazon Web Services Region.                                                                                                                                                                                                   |
| pool_name                   | core | string     | The name of the custom tape pool. <code>PoolName</code> can use all ASCII characters, except '/' and '\'.                                                                                                                                                                                                                                                                               |
| pool_status                 | core | string     | Status of the custom tape pool. Pool can be <code>ACTIVE</code> or <code>DELETED</code>.                                                                                                                                                                                                                                                                                                |
| retention_lock_time_in_days | core | int64      | Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days).                                                                                                                                                                                                                                                                          |
| retention_lock_type         | core | string     | Tape retention lock type, which can be configured in two modes. When configured in governance mode, Amazon Web Services accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root Amazon Web Services account. |
| storage_class               | core | string     | The storage class that is associated with the custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.                                                                                                                                           |
| tags                        | core | hstore_csv |
