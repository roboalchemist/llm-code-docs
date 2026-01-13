# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.backup_legalhold.dataset.md

---
title: Backup Legalhold
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup Legalhold
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.backup_legalhold.dataset/index.html
---

# Backup Legalhold

This table represents the Backup Legalhold resource from Amazon Web Services.

```
aws.backup_legalhold
```

## Fields

| Title                    | ID   | Type      | Data Type                                                                                           | Description |
| ------------------------ | ---- | --------- | --------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string    |
| account_id               | core | string    |
| cancel_description       | core | string    | The reason for removing the legal hold.                                                             |
| cancellation_date        | core | timestamp | The time when the legal hold was cancelled.                                                         |
| creation_date            | core | timestamp | The time when the legal hold was created.                                                           |
| description              | core | string    | The description of the legal hold.                                                                  |
| legal_hold_arn           | core | string    | The framework ARN for the specified legal hold. The format of the ARN depends on the resource type. |
| legal_hold_id            | core | string    | The ID of the legal hold.                                                                           |
| recovery_point_selection | core | json      | The criteria to assign a set of resources, such as resource types or backup vaults.                 |
| retain_record_until      | core | timestamp | The date and time until which the legal hold record is retained.                                    |
| status                   | core | string    | The status of the legal hold.                                                                       |
| tags                     | core | hstore    |
| title                    | core | string    | The title of the legal hold.                                                                        |
