# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.backup_plan.dataset.md

---
title: Backup Plan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup Plan
---

# Backup Plan

This table represents the Backup Plan resource from Amazon Web Services.

```
aws.backup_plan
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                                                                                         | Description |
| ------------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| advanced_backup_settings | core | json       | Contains a list of <code>BackupOptions</code> for a resource type.                                                                                                                                                                                                                |
| backup_plan_arn          | core | string     | An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, <code>arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50</code>.                                                                                                  |
| backup_plan_id           | core | string     | Uniquely identifies a backup plan.                                                                                                                                                                                                                                                |
| backup_plan_name         | core | string     | The display name of a saved backup plan.                                                                                                                                                                                                                                          |
| creation_date            | core | timestamp  | The date and time a resource backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.          |
| creator_request_id       | core | string     | A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.                                  |
| deletion_date            | core | timestamp  | The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of <code>DeletionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.                   |
| last_execution_date      | core | timestamp  | The last time this backup plan was run. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastExecutionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM. |
| tags                     | core | hstore_csv |
| version_id               | core | string     | Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.                                                                                                                                                       |
