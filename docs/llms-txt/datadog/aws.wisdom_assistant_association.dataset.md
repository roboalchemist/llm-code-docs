# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.wisdom_assistant_association.dataset.md

---
title: Amazon Connect Wisdom Assistant Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Amazon Connect Wisdom Assistant
  Association
---

# Amazon Connect Wisdom Assistant Association

Amazon Connect Wisdom Assistant Association links a Wisdom assistant with another resource, such as a contact center instance or knowledge base, to provide agents with real-time recommendations and relevant information during customer interactions. It helps improve agent efficiency by surfacing contextually appropriate content from multiple data sources through the Wisdom service.

```
aws.wisdom_assistant_association
```

## Fields

| Title                     | ID   | Type       | Data Type                                                    | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------ | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| assistant_arn             | core | string     | The Amazon Resource Name (ARN) of the Wisdom assistant.      |
| assistant_association_arn | core | string     | The Amazon Resource Name (ARN) of the assistant association. |
| assistant_association_id  | core | string     | The identifier of the assistant association.                 |
| assistant_id              | core | string     | The identifier of the Wisdom assistant.                      |
| association_data          | core | json       | The association data.                                        |
| association_type          | core | string     | The type of association.                                     |
| tags                      | core | hstore_csv |
