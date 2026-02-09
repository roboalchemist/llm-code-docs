# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.billingconductor_billinggroup.dataset.md

---
title: Billingconductor Billinggroup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Billingconductor Billinggroup
---

# Billingconductor Billinggroup

This table represents the billingconductor_billinggroup resource from Amazon Web Services.

```
aws.billingconductor_billinggroup
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                              | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string     |
| account_grouping       | core | json       | Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled. |
| account_id             | core | string     |
| arn                    | core | string     | The Amazon Resource Number (ARN) that can be used to uniquely identify the billing group.              |
| computation_preference | core | json       |
| creation_time          | core | int64      | The time when the billing group was created.                                                           |
| description            | core | string     | The description of the billing group.                                                                  |
| last_modified_time     | core | int64      | The most recent time when the billing group was modified.                                              |
| name                   | core | string     | The name of the billing group.                                                                         |
| primary_account_id     | core | string     | The account ID that serves as the main account in a billing group.                                     |
| size                   | core | int64      | The number of accounts in the particular billing group.                                                |
| status                 | core | string     | The billing group status. Only one of the valid values can be used.                                    |
| status_reason          | core | string     | The reason why the billing group is in its current status.                                             |
| tags                   | core | hstore_csv |
