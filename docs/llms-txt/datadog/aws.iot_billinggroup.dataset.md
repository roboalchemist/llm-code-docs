# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_billinggroup.dataset.md

---
title: Iot Billinggroup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iot Billinggroup
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iot_billinggroup.dataset/index.html
---

# Iot Billinggroup

This table represents the iot_billinggroup resource from Amazon Web Services.

```
aws.iot_billinggroup
```

## Fields

| Title                    | ID   | Type   | Data Type                                       | Description |
| ------------------------ | ---- | ------ | ----------------------------------------------- | ----------- |
| _key                     | core | string |
| account_id               | core | string |
| billing_group_arn        | core | string | The ARN of the billing group.                   |
| billing_group_id         | core | string | The ID of the billing group.                    |
| billing_group_metadata   | core | json   | Additional information about the billing group. |
| billing_group_name       | core | string | The name of the billing group.                  |
| billing_group_properties | core | json   | The properties of the billing group.            |
| tags                     | core | hstore |
| version                  | core | int64  | The version of the billing group.               |
