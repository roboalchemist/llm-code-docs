# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.wisdom_quick_response.dataset.md

---
title: Amazon Connect Wisdom Quick Response
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amazon Connect Wisdom Quick Response
---

# Amazon Connect Wisdom Quick Response

Amazon Connect Wisdom Quick Response provides a summary of predefined quick responses used in Amazon Connect Wisdom. These quick responses help agents reply faster to customer inquiries by offering ready-to-use, consistent answers. The resource includes details such as identifiers, names, and content metadata for managing and retrieving quick responses efficiently within the contact center environment.

```
aws.wisdom_quick_response
```

## Fields

| Title              | ID   | Type          | Data Type                                                                                                                                                                                                                    | Description |
| ------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string        |
| account_id         | core | string        |
| channels           | core | array<string> | The Amazon Connect contact channels this quick response applies to. The supported contact channel types include Chat.                                                                                                        |
| content_type       | core | string        | The media type of the quick response content. Use application/x.quickresponse;format=plain for quick response written in plain text. Use application/x.quickresponse;format=markdown for quick response written in richtext. |
| created_time       | core | timestamp     | The timestamp when the quick response was created.                                                                                                                                                                           |
| description        | core | string        | The description of the quick response.                                                                                                                                                                                       |
| is_active          | core | bool          | Whether the quick response is active.                                                                                                                                                                                        |
| knowledge_base_arn | core | string        | The Amazon Resource Name (ARN) of the knowledge base.                                                                                                                                                                        |
| knowledge_base_id  | core | string        | The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.                                                                              |
| last_modified_by   | core | string        | The Amazon Resource Name (ARN) of the user who last updated the quick response data.                                                                                                                                         |
| last_modified_time | core | timestamp     | The timestamp when the quick response summary was last modified.                                                                                                                                                             |
| name               | core | string        | The name of the quick response.                                                                                                                                                                                              |
| quick_response_arn | core | string        | The Amazon Resource Name (ARN) of the quick response.                                                                                                                                                                        |
| quick_response_id  | core | string        | The identifier of the quick response.                                                                                                                                                                                        |
| status             | core | string        | The resource status of the quick response.                                                                                                                                                                                   |
| tags               | core | hstore_csv    |
