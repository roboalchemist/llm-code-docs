# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_knowledge_base.dataset.md

---
title: Bedrock Knowledge Base
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Knowledge Base
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_knowledge_base.dataset/index.html
---

# Bedrock Knowledge Base

This table represents the Bedrock Knowledge Base resource from Amazon Web Services.

```
aws.bedrock_knowledge_base
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ---------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| account_id                   | core | string        |
| created_at                   | core | timestamp     | The time the knowledge base was created.                                                                                                                                                                                                                                                                                                                                                       |
| description                  | core | string        | The description of the knowledge base.                                                                                                                                                                                                                                                                                                                                                         |
| failure_reasons              | core | array<string> | A list of reasons that the API operation on the knowledge base failed.                                                                                                                                                                                                                                                                                                                         |
| knowledge_base_arn           | core | string        | The Amazon Resource Name (ARN) of the knowledge base.                                                                                                                                                                                                                                                                                                                                          |
| knowledge_base_configuration | core | json          | Contains details about the embeddings configuration of the knowledge base.                                                                                                                                                                                                                                                                                                                     |
| knowledge_base_id            | core | string        | The unique identifier of the knowledge base.                                                                                                                                                                                                                                                                                                                                                   |
| name                         | core | string        | The name of the knowledge base.                                                                                                                                                                                                                                                                                                                                                                |
| role_arn                     | core | string        | The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.                                                                                                                                                                                                                                                                                |
| status                       | core | string        | The status of the knowledge base. The following statuses are possible: <ul> <li> CREATING â The knowledge base is being created. </li> <li> ACTIVE â The knowledge base is ready to be queried. </li> <li> DELETING â The knowledge base is being deleted. </li> <li> UPDATING â The knowledge base is being updated. </li> <li> FAILED â The knowledge base API operation failed. </li> </ul> |
| storage_configuration        | core | json          | Contains details about the storage configuration of the knowledge base.                                                                                                                                                                                                                                                                                                                        |
| tags                         | core | hstore        |
| updated_at                   | core | timestamp     | The time the knowledge base was last updated.                                                                                                                                                                                                                                                                                                                                                  |
