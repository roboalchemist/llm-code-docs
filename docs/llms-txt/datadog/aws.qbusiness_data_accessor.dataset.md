# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qbusiness_data_accessor.dataset.md

---
title: Q Business Data Accessor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Q Business Data Accessor
---

# Q Business Data Accessor

Q Business Data Accessor in AWS provides access details for retrieving data within the Amazon Q Business service. It defines how applications or users can securely connect to and use data sources integrated with Q Business, ensuring proper permissions and configurations are applied. This resource helps manage and control data access for business intelligence and search use cases.

```
aws.qbusiness_data_accessor
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                 | Description |
| --------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| action_configurations | core | json       | The list of action configurations specifying the allowed actions and any associated filters.              |
| application_id        | core | string     | The unique identifier of the Amazon Q Business application associated with this data accessor.            |
| created_at            | core | timestamp  | The timestamp when the data accessor was created.                                                         |
| data_accessor_arn     | core | string     | The Amazon Resource Name (ARN) of the data accessor.                                                      |
| data_accessor_id      | core | string     | The unique identifier of the data accessor.                                                               |
| idc_application_arn   | core | string     | The Amazon Resource Name (ARN) of the IAM Identity Center application associated with this data accessor. |
| principal             | core | string     | The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.            |
| tags                  | core | hstore_csv |
| updated_at            | core | timestamp  | The timestamp when the data accessor was last updated.                                                    |
