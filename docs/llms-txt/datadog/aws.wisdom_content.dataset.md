# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.wisdom_content.dataset.md

---
title: Amazon Connect Wisdom Content
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amazon Connect Wisdom Content
---

# Amazon Connect Wisdom Content

Amazon Connect Wisdom Content represents a knowledge item within Amazon Connect Wisdom, which helps contact center agents quickly find relevant information during customer interactions. It summarizes key details about a piece of content, such as its title, type, and relevance, enabling faster access to helpful resources and improving agent efficiency.

```
aws.wisdom_content
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                | Description |
| ------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| content_arn        | core | string     | The Amazon Resource Name (ARN) of the content.                                                                                                                                                                                                           |
| content_id         | core | string     | The identifier of the content.                                                                                                                                                                                                                           |
| content_type       | core | string     | The media type of the content.                                                                                                                                                                                                                           |
| knowledge_base_arn | core | string     | The Amazon Resource Name (ARN) of the knowledge base.                                                                                                                                                                                                    |
| knowledge_base_id  | core | string     | The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.                                                                                                          |
| metadata           | core | hstore     | A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Wisdom, you can store an external version identifier as metadata to utilize for determining drift. |
| name               | core | string     | The name of the content.                                                                                                                                                                                                                                 |
| revision_id        | core | string     | The identifier of the revision of the content.                                                                                                                                                                                                           |
| status             | core | string     | The status of the content.                                                                                                                                                                                                                               |
| tags               | core | hstore_csv |
| title              | core | string     | The title of the content.                                                                                                                                                                                                                                |
