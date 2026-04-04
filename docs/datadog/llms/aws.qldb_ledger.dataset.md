# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qldb_ledger.dataset.md

---
title: QLDB Ledger
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QLDB Ledger
---

# QLDB Ledger

QLDB Ledger in AWS is a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log. It is designed for applications that need to maintain a complete and verifiable history of data changes without building complex audit systems.

```
aws.qldb_ledger
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                           | Description |
| ---------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The Amazon Resource Name (ARN) for the ledger.                                                                                                                                                                                                                                                                                                      |
| creation_date_time     | core | timestamp  | The date and time, in epoch time format, when the ledger was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)                                                                                                                                                                                   |
| deletion_protection    | core | bool       | Specifies whether the ledger is protected from being deleted by any user. If not defined during ledger creation, this feature is enabled (true) by default. If deletion protection is enabled, you must first disable it before you can delete the ledger. You can disable it by calling the UpdateLedger operation to set this parameter to false. |
| encryption_description | core | json       | Information about the encryption of data at rest in the ledger. This includes the current status, the KMS key, and when the key became inaccessible (in the case of an error). If this parameter is undefined, the ledger uses an Amazon Web Services owned KMS key for encryption.                                                                 |
| name                   | core | string     | The name of the ledger.                                                                                                                                                                                                                                                                                                                             |
| permissions_mode       | core | string     | The permissions mode of the ledger.                                                                                                                                                                                                                                                                                                                 |
| state                  | core | string     | The current status of the ledger.                                                                                                                                                                                                                                                                                                                   |
| tags                   | core | hstore_csv |
