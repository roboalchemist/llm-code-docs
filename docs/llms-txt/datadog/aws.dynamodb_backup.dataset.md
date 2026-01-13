# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dynamodb_backup.dataset.md

---
title: DynamoDB Backup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DynamoDB Backup
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.dynamodb_backup.dataset/index.html
---

# DynamoDB Backup

DynamoDB Backup in AWS provides information about on-demand and continuous backups of DynamoDB tables. It allows you to view details such as backup creation time, status, size, and the table it was created from. This helps ensure data protection, point-in-time recovery, and compliance by enabling you to restore tables to a specific state when needed.

```
aws.dynamodb_backup
```

## Fields

| Title                        | ID   | Type   | Data Type                                                                                                                     | Description |
| ---------------------------- | ---- | ------ | ----------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string |
| account_id                   | core | string |
| backup_details               | core | json   | Contains the details of the backup created for the table.                                                                     |
| source_table_details         | core | json   | Contains the details of the table when the backup was created.                                                                |
| source_table_feature_details | core | json   | Contains the details of the features enabled on the table when the backup was created. For example, LSIs, GSIs, streams, TTL. |
| tags                         | core | hstore |
