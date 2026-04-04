# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_address_list.dataset.md

---
title: SES Address List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Address List
---

# SES Address List

This table represents the SES Address List resource from Amazon Web Services.

```
aws.ses_address_list
```

## Fields

| Title                  | ID   | Type       | Data Type                                                | Description |
| ---------------------- | ---- | ---------- | -------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| address_list_arn       | core | string     | The Amazon Resource Name (ARN) of the address list.      |
| address_list_id        | core | string     | The identifier of the address list.                      |
| address_list_name      | core | string     | The user-friendly name of the address list.              |
| created_timestamp      | core | timestamp  | The timestamp of when the address list was created.      |
| last_updated_timestamp | core | timestamp  | The timestamp of when the address list was last updated. |
| tags                   | core | hstore_csv |
