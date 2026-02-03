# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cleanrooms_configuredtable.dataset.md

---
title: Cleanrooms Configuredtable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cleanrooms Configuredtable
---

# Cleanrooms Configuredtable

This table represents the cleanrooms_configuredtable resource from Amazon Web Services.

```
aws.cleanrooms_configuredtable
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                   | Description |
| ------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| account_id                | core | string        |
| allowed_columns           | core | array<string> | The columns within the underlying Glue table that can be utilized within collaborations.                                                                                                                                                                                                                    |
| analysis_method           | core | string        | The analysis method for the configured table. <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table. <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table. <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table. |
| analysis_rule_types       | core | array<string> | The types of analysis rules associated with this configured table. Currently, only one analysis rule may be associated with a configured table.                                                                                                                                                             |
| arn                       | core | string        | The unique ARN for the configured table.                                                                                                                                                                                                                                                                    |
| create_time               | core | timestamp     | The time the configured table was created.                                                                                                                                                                                                                                                                  |
| description               | core | string        | A description for the configured table.                                                                                                                                                                                                                                                                     |
| id                        | core | string        | The unique ID for the configured table.                                                                                                                                                                                                                                                                     |
| name                      | core | string        | A name for the configured table.                                                                                                                                                                                                                                                                            |
| selected_analysis_methods | core | array<string> | The selected analysis methods for the configured table.                                                                                                                                                                                                                                                     |
| table_reference           | core | json          | The table that this configured table represents.                                                                                                                                                                                                                                                            |
| tags                      | core | hstore_csv    |
| update_time               | core | timestamp     | The time the configured table was last updated                                                                                                                                                                                                                                                              |
