# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshift_integration.dataset.md

---
title: Redshift Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Integration
---

# Redshift Integration

Redshift Integration in AWS allows Amazon Redshift to connect and work seamlessly with other AWS services and external data sources. It enables data ingestion, transformation, and querying across different systems, making it easier to unify data for analytics and reporting. This resource helps streamline workflows by reducing the need for complex data pipelines and supports secure, scalable integration for business intelligence and data warehousing use cases.

```
aws.redshift_integration
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                   | Description |
| ----------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| additional_encryption_context | core | hstore     | The encryption context for the integration. For more information, see Encryption context in the Amazon Web Services Key Management Service Developer Guide. |
| create_time                   | core | timestamp  | The time (UTC) when the integration was created.                                                                                                            |
| description                   | core | string     | The description of the integration.                                                                                                                         |
| errors                        | core | json       | Any errors associated with the integration.                                                                                                                 |
| integration_arn               | core | string     | The Amazon Resource Name (ARN) of the integration.                                                                                                          |
| integration_name              | core | string     | The name of the integration.                                                                                                                                |
| kms_key_id                    | core | string     | The Key Management Service (KMS) key identifier for the key used to encrypt the integration.                                                                |
| source_arn                    | core | string     | The Amazon Resource Name (ARN) of the database used as the source for replication.                                                                          |
| status                        | core | string     | The current status of the integration.                                                                                                                      |
| tags                          | core | hstore_csv |
| target_arn                    | core | string     | The Amazon Resource Name (ARN) of the Amazon Redshift data warehouse to use as the target for replication.                                                  |
