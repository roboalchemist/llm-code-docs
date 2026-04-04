# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3tables_table_bucket.dataset.md

---
title: S3 Tables Table Bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > S3 Tables Table Bucket
---

# S3 Tables Table Bucket

This table represents the S3 Tables Table Bucket resource from Amazon Web Services.

```
aws.s3tables_table_bucket
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                         | Description |
| ---------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| arn              | core | string     | The Amazon Resource Name (ARN) of the table bucket.                                               |
| configuration    | core | string     | Details about the maintenance configuration for the table bucket.                                 |
| created_at       | core | timestamp  | The date and time the table bucket was created at.                                                |
| name             | core | string     | The name of the table bucket.                                                                     |
| owner_account_id | core | string     | The ID of the account that owns the table bucket.                                                 |
| table_bucket_arn | core | string     | The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration. |
| tags             | core | hstore_csv |
