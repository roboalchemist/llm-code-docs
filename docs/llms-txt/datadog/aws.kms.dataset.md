# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kms.dataset.md

---
title: Key Management Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Key Management Service
---

# Key Management Service

This table represents the Key Management Service resource from Amazon Web Services.

```
aws.kms
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ----------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| key_arn                       | core | string     |
| key_id                        | core | string     |
| key_metadata                  | core | json       | Metadata associated with the key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| key_rotation_enabled          | core | bool       | A Boolean value that specifies whether key rotation is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| next_rotation_date            | core | timestamp  | The next date that KMS will automatically rotate the key material.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| on_demand_rotation_start_date | core | timestamp  | Identifies the date and time that an in progress on-demand rotation was initiated. The KMS API follows an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html">eventual consistency</a> model due to the distributed nature of the system. As a result, there might be a slight delay between initiating on-demand key rotation and the rotation's completion. Once the on-demand rotation is complete, use <a>ListKeyRotations</a> to view the details of the on-demand rotation. |
| rotation_period_in_days       | core | int64      | The number of days between each automatic rotation. The default value is 365 days.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags                          | core | hstore_csv |
