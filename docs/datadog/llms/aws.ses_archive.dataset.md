# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_archive.dataset.md

---
title: SES Archive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Archive
---

# SES Archive

This table represents the SES Archive resource from Amazon Web Services.

```
aws.ses_archive
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                     | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| archive_arn            | core | string     | The Amazon Resource Name (ARN) of the archive.                                                                                                                                                                                                                                                                |
| archive_id             | core | string     | The unique identifier of the archive.                                                                                                                                                                                                                                                                         |
| archive_name           | core | string     | The unique name assigned to the archive.                                                                                                                                                                                                                                                                      |
| archive_state          | core | string     | The current state of the archive: <ul> <li> <code>ACTIVE</code> â The archive is ready and available for use. </li> <li> <code>PENDING_DELETION</code> â The archive has been marked for deletion and will be permanently deleted in 30 days. No further modifications can be made in this state. </li> </ul> |
| created_timestamp      | core | timestamp  | The timestamp of when the archive was created.                                                                                                                                                                                                                                                                |
| kms_key_arn            | core | string     | The Amazon Resource Name (ARN) of the KMS key used to encrypt the archive.                                                                                                                                                                                                                                    |
| last_updated_timestamp | core | timestamp  | The timestamp of when the archive was modified.                                                                                                                                                                                                                                                               |
| retention              | core | json       | The retention period for emails in this archive.                                                                                                                                                                                                                                                              |
| tags                   | core | hstore_csv |
