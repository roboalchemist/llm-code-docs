# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.athena_prepared_statement.dataset.md

---
title: Athena Prepared Statement
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Athena Prepared Statement
---

# Athena Prepared Statement

An Athena Prepared Statement in AWS is a saved SQL query that can be parameterized and reused across multiple executions. It allows you to define queries once, store them in Athena, and run them later with different input values, improving efficiency and consistency. This helps reduce repetitive query writing, enforces query standardization, and can enhance security by controlling how queries are executed.

```
aws.athena_prepared_statement
```

## Fields

| Title              | ID   | Type       | Data Type                                                          | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| description        | core | string     | The description of the prepared statement.                         |
| last_modified_time | core | timestamp  | The last modified time of the prepared statement.                  |
| query_statement    | core | string     | The query string for the prepared statement.                       |
| statement_name     | core | string     | The name of the prepared statement.                                |
| tags               | core | hstore_csv |
| work_group_name    | core | string     | The name of the workgroup to which the prepared statement belongs. |
