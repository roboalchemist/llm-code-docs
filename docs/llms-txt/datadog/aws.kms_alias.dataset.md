# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kms_alias.dataset.md

---
title: KMS Alias
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > KMS Alias
---

# KMS Alias

KMS Alias in AWS is a friendly name that you can assign to a customer master key (CMK) in AWS Key Management Service. Instead of using the key's unique identifier or ARN, you can reference the alias to simplify key management and usage in applications. Aliases make it easier to rotate keys or change the underlying CMK without updating all dependent resources or code.

```
aws.kms_alias
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                   | Description |
| ----------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| alias_arn         | core | string     | String that contains the key ARN.                                                                                           |
| alias_name        | core | string     | String that contains the alias. This value begins with alias/.                                                              |
| creation_date     | core | timestamp  | Date and time that the alias was most recently created in the account and Region. Formatted as Unix time.                   |
| last_updated_date | core | timestamp  | Date and time that the alias was most recently associated with a KMS key in the account and Region. Formatted as Unix time. |
| policies          | core | json       |
| policy            | core | string     | A key policy document in JSON format.                                                                                       |
| policy_name       | core | string     | The name of the key policy. The only valid value is default.                                                                |
| tags              | core | hstore_csv |
| target_key_id     | core | string     | String that contains the key identifier of the KMS key associated with the alias.                                           |
