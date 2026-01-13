# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.glacier_vault.dataset.md

---
title: S3 Glacier Vault
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > S3 Glacier Vault
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.glacier_vault.dataset/index.html
---

# S3 Glacier Vault

An S3 Glacier Vault is a secure container for storing archives in Amazon S3 Glacier, designed for long-term, low-cost data storage. Each vault can hold unlimited archives and provides metadata such as creation date, number of archives, and total size. Vaults also support access policies and notifications, enabling fine-grained control over data retrieval and monitoring.

```
aws.glacier_vault
```

## Fields

| Title                     | ID   | Type   | Data Type                                                                                                                                                                                              | Description |
| ------------------------- | ---- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                      | core | string |
| account_id                | core | string |
| creation_date             | core | string | The Universal Coordinated Time (UTC) date when the vault was created. This value should be a string in the ISO 8601 date format, for example 2012-03-20T17:03:43.221Z.                                 |
| last_inventory_date       | core | string | The Universal Coordinated Time (UTC) date when Amazon S3 Glacier completed the last vault inventory. This value should be a string in the ISO 8601 date format, for example 2012-03-20T17:03:43.221Z.  |
| number_of_archives        | core | int64  | The number of archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.                |
| size_in_bytes             | core | int64  | Total size, in bytes, of the archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault. |
| tags                      | core | hstore |
| vault_arn                 | core | string | The Amazon Resource Name (ARN) of the vault.                                                                                                                                                           |
| vault_name                | core | string | The name of the vault.                                                                                                                                                                                 |
| vault_notification_config | core | json   | Returns the notification configuration set on the vault.                                                                                                                                               |
