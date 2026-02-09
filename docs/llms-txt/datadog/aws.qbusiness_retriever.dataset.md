# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qbusiness_retriever.dataset.md

---
title: Q Business Retriever
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Q Business Retriever
---

# Q Business Retriever

Q Business Retriever in AWS is part of the Amazon Q Business service, which helps applications access and retrieve relevant business data. A retriever defines how information is fetched from connected data sources, enabling more accurate and context-aware responses for business queries. It is typically used to configure and manage retrieval logic so that Amazon Q Business can surface the most useful information to end users.

```
aws.qbusiness_retriever
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                                      | Description |
| -------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| application_id | core | string     | The identifier of the Amazon Q Business application using the retriever.                                       |
| configuration  | core | json       | Provides information on how the retriever used for your Amazon Q Business application is configured.           |
| created_at     | core | timestamp  | The Unix timestamp when the retriever was created.                                                             |
| retriever_arn  | core | string     | The Amazon Resource Name (ARN) of the IAM role associated with the retriever.                                  |
| retriever_id   | core | string     | The identifier of the retriever.                                                                               |
| role_arn       | core | string     | The Amazon Resource Name (ARN) of the role with the permission to access the retriever and required resources. |
| status         | core | string     | The status of the retriever.                                                                                   |
| tags           | core | hstore_csv |
| type           | core | string     | The type of the retriever.                                                                                     |
| updated_at     | core | timestamp  | The Unix timestamp when the retriever was last updated.                                                        |
