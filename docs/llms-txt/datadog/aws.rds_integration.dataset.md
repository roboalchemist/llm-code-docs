# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_integration.dataset.md

---
title: RDS Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Integration
---

# RDS Integration

This table represents the RDS Integration resource from Amazon Web Services.

```
aws.rds_integration
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                   | Description |
| ----------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| additional_encryption_context | core | hstore     | The encryption context for the integration. For more information, see Encryption context in the Amazon Web Services Key Management Service Developer Guide. |
| create_time                   | core | timestamp  | The time when the integration was created, in Universal Coordinated Time (UTC).                                                                             |
| data_filter                   | core | string     | Data filters for the integration. These filters determine which tables from the source database are sent to the target Amazon Redshift data warehouse.      |
| description                   | core | string     | A description of the integration.                                                                                                                           |
| errors                        | core | json       | Any errors associated with the integration.                                                                                                                 |
| integration_arn               | core | string     | The ARN of the integration.                                                                                                                                 |
| integration_name              | core | string     | The name of the integration.                                                                                                                                |
| kms_key_id                    | core | string     | The Amazon Web Services Key Management System (Amazon Web Services KMS) key identifier for the key used to to encrypt the integration.                      |
| source_arn                    | core | string     | The Amazon Resource Name (ARN) of the database used as the source for replication.                                                                          |
| status                        | core | string     | The current status of the integration.                                                                                                                      |
| tags                          | core | hstore_csv |
| target_arn                    | core | string     | The ARN of the Redshift data warehouse used as the target for replication.                                                                                  |
