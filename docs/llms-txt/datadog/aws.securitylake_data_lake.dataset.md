# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.securitylake_data_lake.dataset.md

---
title: Security Lake Data Lake
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Security Lake Data Lake
---

# Security Lake Data Lake

This table represents the Security Lake Data Lake resource from Amazon Web Services.

```
aws.securitylake_data_lake
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                 | Description |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| create_status             | core | string     | Retrieves the status of the <code>CreateDatalake</code> API call for an account in Amazon Security Lake.                                                                                                                                                                                  |
| data_lake_arn             | core | string     | The Amazon Resource Name (ARN) created by you to provide to the subscriber. For more information about ARNs and how to use them in policies, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html">Amazon Security Lake User Guide</a>. |
| encryption_configuration  | core | json       | Provides encryption details of Amazon Security Lake object.                                                                                                                                                                                                                               |
| lifecycle_configuration   | core | json       | Provides lifecycle details of Amazon Security Lake object.                                                                                                                                                                                                                                |
| region                    | core | string     | The Amazon Web Services Regions where Security Lake is enabled.                                                                                                                                                                                                                           |
| replication_configuration | core | json       | Provides replication details of Amazon Security Lake object.                                                                                                                                                                                                                              |
| s3_bucket_arn             | core | string     | The ARN for the Amazon Security Lake Amazon S3 bucket.                                                                                                                                                                                                                                    |
| tags                      | core | hstore_csv |
| update_status             | core | json       | The status of the last <code>UpdateDataLake </code>or <code>DeleteDataLake</code> API request.                                                                                                                                                                                            |
