# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.osis_pipeline.dataset.md

---
title: OpenSearch Ingestion Pipeline
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > OpenSearch Ingestion Pipeline
---

# OpenSearch Ingestion Pipeline

OpenSearch Ingestion Pipeline in AWS is a managed service that lets you build and run data ingestion pipelines for Amazon OpenSearch Service. It enables you to collect, transform, and route streaming data from various sources into OpenSearch domains for search, analytics, and visualization. The service handles scaling, reliability, and integration with AWS data sources, reducing the need for custom ingestion infrastructure.

```
aws.osis_pipeline
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                                                                                 | Description |
| --------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| buffer_options              | core | json          | Options that specify the configuration of a persistent buffer. To configure how OpenSearch Ingestion encrypts this data, set the EncryptionAtRestOptions. For more information, see Persistent buffering. |
| created_at                  | core | timestamp     | The date and time when the pipeline was created.                                                                                                                                                          |
| destinations                | core | json          | Destinations to which the pipeline writes data.                                                                                                                                                           |
| encryption_at_rest_options  | core | json          | Options to control how OpenSearch encrypts buffer data.                                                                                                                                                   |
| ingest_endpoint_urls        | core | array<string> | The ingestion endpoints for the pipeline, which you can send data to.                                                                                                                                     |
| last_updated_at             | core | timestamp     | The date and time when the pipeline was last updated.                                                                                                                                                     |
| log_publishing_options      | core | json          | Key-value pairs that represent log publishing settings.                                                                                                                                                   |
| max_units                   | core | int64         | The maximum pipeline capacity, in Ingestion Compute Units (ICUs).                                                                                                                                         |
| min_units                   | core | int64         | The minimum pipeline capacity, in Ingestion Compute Units (ICUs).                                                                                                                                         |
| pipeline_arn                | core | string        | The Amazon Resource Name (ARN) of the pipeline.                                                                                                                                                           |
| pipeline_configuration_body | core | string        | The Data Prepper pipeline configuration in YAML format.                                                                                                                                                   |
| pipeline_name               | core | string        | The name of the pipeline.                                                                                                                                                                                 |
| service_vpc_endpoints       | core | json          | A list of VPC endpoints that OpenSearch Ingestion has created to other Amazon Web Services services.                                                                                                      |
| status                      | core | string        | The current status of the pipeline.                                                                                                                                                                       |
| status_reason               | core | json          | The reason for the current status of the pipeline.                                                                                                                                                        |
| tags                        | core | hstore_csv    |
| vpc_endpoint_service        | core | string        | The VPC endpoint service name for the pipeline.                                                                                                                                                           |
| vpc_endpoints               | core | json          | The VPC interface endpoints that have access to the pipeline.                                                                                                                                             |
