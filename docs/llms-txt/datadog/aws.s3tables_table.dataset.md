# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3tables_table.dataset.md

---
title: S3 Tables Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > S3 Tables Table
---

# S3 Tables Table

This table represents the S3 Tables Table resource from Amazon Web Services.

```
aws.s3tables_table
```

## Fields

| Title       | ID   | Type          | Data Type                                         | Description |
| ----------- | ---- | ------------- | ------------------------------------------------- | ----------- |
| _key        | core | string        |
| account_id  | core | string        |
| created_at  | core | timestamp     | The date and time the table was created at.       |
| modified_at | core | timestamp     | The date and time the table was last modified at. |
| name        | core | string        | The name of the table.                            |
| namespace   | core | array<string> | The name of the namespace.                        |
| table_arn   | core | string        | The Amazon Resource Name (ARN) of the table.      |
| tags        | core | hstore_csv    |
| type        | core | string        | The type of the table.                            |
