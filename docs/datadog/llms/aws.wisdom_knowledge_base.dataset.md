# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.wisdom_knowledge_base.dataset.md

---
title: Amazon Connect Wisdom Knowledge Base
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amazon Connect Wisdom Knowledge Base
---

# Amazon Connect Wisdom Knowledge Base

Amazon Connect Wisdom Knowledge Base is a managed knowledge repository that helps contact center agents quickly find relevant information during customer interactions. It integrates with Amazon Connect Wisdom to surface answers and guidance from multiple data sources, improving response accuracy and reducing handling time.

```
aws.wisdom_knowledge_base
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ------------------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                 | core | string     |
| account_id                           | core | string     |
| description                          | core | string     | The description of the knowledge base.                                                                                                                                                                                                                                                                                                                                                     |
| knowledge_base_arn                   | core | string     | The Amazon Resource Name (ARN) of the knowledge base.                                                                                                                                                                                                                                                                                                                                      |
| knowledge_base_id                    | core | string     | The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.                                                                                                                                                                                                                                            |
| knowledge_base_type                  | core | string     | The type of knowledge base.                                                                                                                                                                                                                                                                                                                                                                |
| name                                 | core | string     | The name of the knowledge base.                                                                                                                                                                                                                                                                                                                                                            |
| rendering_configuration              | core | json       | Information about how to render the content.                                                                                                                                                                                                                                                                                                                                               |
| server_side_encryption_configuration | core | json       | The configuration information for the customer managed key used for encryption. This KMS key must have a policy that allows kms:CreateGrant, kms:DescribeKey, kms:Decrypt/kms:GenerateDataKey permissions to the IAM identity using the key to invoke Wisdom. For more information about setting up a customer managed key for Wisdom, see Enable Amazon Connect Wisdom for your instance. |
| source_configuration                 | core | json       | Configuration information about the external data source.                                                                                                                                                                                                                                                                                                                                  |
| status                               | core | string     | The status of the knowledge base summary.                                                                                                                                                                                                                                                                                                                                                  |
| tags                                 | core | hstore_csv |
