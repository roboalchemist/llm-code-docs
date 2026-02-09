# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qbusiness_data_source.dataset.md

---
title: Q Business Data Source
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Q Business Data Source
---

# Q Business Data Source

Q Business Data Source in AWS is part of the Amazon Q Business service, which enables integration of external data sources into the Q Business environment. A data source represents a connection to an external system where business data is stored, allowing Q Business to retrieve, index, and use that information for search, insights, and generative AI applications. This resource provides details about the configuration and status of a connected data source.

```
aws.qbusiness_data_source
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                                                                                                                         | Description |
| --------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| application_id                    | core | string     | The identifier of the Amazon Q Business application.                                                                                                                                              |
| configuration                     | core | json       | The details of how the data source connector is configured.                                                                                                                                       |
| created_at                        | core | timestamp  | The Unix timestamp when the data source connector was created.                                                                                                                                    |
| data_source_arn                   | core | string     | The Amazon Resource Name (ARN) of the data source.                                                                                                                                                |
| data_source_id                    | core | string     | The identifier of the data source connector.                                                                                                                                                      |
| description                       | core | string     | The description for the data source connector.                                                                                                                                                    |
| document_enrichment_configuration | core | json       | Provides the configuration information for altering document metadata and content during the document ingestion process. For more information, see Custom document enrichment.                    |
| error                             | core | json       | When the Status field value is FAILED, the ErrorMessage field contains a description of the error that caused the data source connector to fail.                                                  |
| index_id                          | core | string     | The identifier of the index linked to the data source connector.                                                                                                                                  |
| media_extraction_configuration    | core | json       | The configuration for extracting information from media in documents for the data source.                                                                                                         |
| role_arn                          | core | string     | The Amazon Resource Name (ARN) of the role with permission to access the data source and required resources.                                                                                      |
| status                            | core | string     | The current status of the data source connector. When the Status field value is FAILED, the ErrorMessage field contains a description of the error that caused the data source connector to fail. |
| sync_schedule                     | core | string     | The schedule for Amazon Q Business to update the index.                                                                                                                                           |
| tags                              | core | hstore_csv |
| type                              | core | string     | The type of the data source connector. For example, S3.                                                                                                                                           |
| updated_at                        | core | timestamp  | The Unix timestamp when the data source connector was last updated.                                                                                                                               |
| vpc_configuration                 | core | json       | Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source.                                                                                               |
