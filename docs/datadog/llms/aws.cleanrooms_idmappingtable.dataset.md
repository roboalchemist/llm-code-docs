# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cleanrooms_idmappingtable.dataset.md

---
title: Cleanrooms Idmappingtable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cleanrooms Idmappingtable
---

# Cleanrooms Idmappingtable

This table represents the cleanrooms_idmappingtable resource from Amazon Web Services.

```
aws.cleanrooms_idmappingtable
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                | Description |
| -------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| arn                        | core | string     | The Amazon Resource Name (ARN) of the ID mapping table.                                  |
| collaboration_arn          | core | string     | The Amazon Resource Name (ARN) of the collaboration that contains this ID mapping table. |
| collaboration_id           | core | string     | The unique identifier of the collaboration that contains this ID mapping table.          |
| create_time                | core | timestamp  | The time at which the ID mapping table was created.                                      |
| description                | core | string     | The description of the ID mapping table.                                                 |
| id                         | core | string     | The unique identifier of the ID mapping table.                                           |
| input_reference_config     | core | json       | The input reference configuration for the ID mapping table.                              |
| input_reference_properties | core | json       | The input reference properties for the ID mapping table.                                 |
| kms_key_arn                | core | string     | The Amazon Resource Name (ARN) of the Amazon Web Services KMS key.                       |
| membership_arn             | core | string     | The Amazon Resource Name (ARN) of the membership resource for the ID mapping table.      |
| membership_id              | core | string     | The unique identifier of the membership resource for the ID mapping table.               |
| name                       | core | string     | The name of the ID mapping table.                                                        |
| tags                       | core | hstore_csv |
| update_time                | core | timestamp  | The most recent time at which the ID mapping table was updated.                          |
