# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qbusiness_index.dataset.md

---
title: Q Business Index
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Q Business Index
---

# Q Business Index

Q Business Index in AWS is part of the Amazon Q Business service, which helps organizations create and manage enterprise search and generative AI experiences. An index stores and organizes data from connected sources, making it searchable and accessible to Q Business applications. It enables efficient retrieval of relevant information across multiple repositories, supporting secure and context-aware responses for business users.

```
aws.qbusiness_index
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                                                                                                                                                                                        | Description |
| --------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| application_id                    | core | string     | The identifier of the Amazon Q Business application associated with the index.                                                                                                                                                                                   |
| capacity_configuration            | core | json       | The storage capacity units chosen for your Amazon Q Business index.                                                                                                                                                                                              |
| created_at                        | core | timestamp  | The Unix timestamp when the Amazon Q Business index was created.                                                                                                                                                                                                 |
| description                       | core | string     | The description for the Amazon Q Business index.                                                                                                                                                                                                                 |
| document_attribute_configurations | core | json       | Configuration information for document attributes or metadata. Document metadata are fields associated with your documents. For example, the company department name associated with each document. For more information, see Understanding document attributes. |
| error                             | core | json       | When the Status field value is FAILED, the ErrorMessage field contains a message that explains why.                                                                                                                                                              |
| index_arn                         | core | string     | The Amazon Resource Name (ARN) of the Amazon Q Business index.                                                                                                                                                                                                   |
| index_id                          | core | string     | The identifier of the Amazon Q Business index.                                                                                                                                                                                                                   |
| index_statistics                  | core | json       | Provides information about the number of documents indexed.                                                                                                                                                                                                      |
| status                            | core | string     | The current status of the index. When the value is ACTIVE, the index is ready for use. If the Status field value is FAILED, the ErrorMessage field contains a message that explains why.                                                                         |
| tags                              | core | hstore_csv |
| type                              | core | string     | The type of index attached to your Amazon Q Business application.                                                                                                                                                                                                |
| updated_at                        | core | timestamp  | The Unix timestamp when the Amazon Q Business index was last updated.                                                                                                                                                                                            |
