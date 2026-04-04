# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cleanrooms_configuredtableassociation.dataset.md

---
title: Cleanrooms Configuredtableassociation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Cleanrooms
  Configuredtableassociation
---

# Cleanrooms Configuredtableassociation

This table represents the cleanrooms_configuredtableassociation resource from Amazon Web Services.

```
aws.cleanrooms_configuredtableassociation
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| account_id           | core | string        |
| analysis_rule_types  | core | array<string> | The analysis rule types for the configured table association.                                                                                                |
| arn                  | core | string        | The unique ARN for the configured table association.                                                                                                         |
| configured_table_arn | core | string        | The unique ARN for the configured table that the association refers to.                                                                                      |
| configured_table_id  | core | string        | The unique ID for the configured table that the association refers to.                                                                                       |
| create_time          | core | timestamp     | The time the configured table association was created.                                                                                                       |
| description          | core | string        | A description of the configured table association.                                                                                                           |
| id                   | core | string        | The unique ID for the configured table association.                                                                                                          |
| membership_arn       | core | string        | The unique ARN for the membership this configured table association belongs to.                                                                              |
| membership_id        | core | string        | The unique ID for the membership this configured table association belongs to.                                                                               |
| name                 | core | string        | The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data. |
| role_arn             | core | string        | The service will assume this role to access catalog metadata and query the table.                                                                            |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | The time the configured table association was last updated.                                                                                                  |
