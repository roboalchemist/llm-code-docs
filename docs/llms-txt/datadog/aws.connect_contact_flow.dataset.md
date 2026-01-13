# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_contact_flow.dataset.md

---
title: Connect Contact Flow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Contact Flow
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.connect_contact_flow.dataset/index.html
---

# Connect Contact Flow

Connect Contact Flow in AWS is a resource within Amazon Connect that defines the customer experience during an interaction. It is essentially a workflow that controls how calls or chats are routed, what prompts are played, and how agents or automated actions handle the interaction. This resource allows you to design and manage customer journeys, integrating with other AWS services for personalization and automation.

```
aws.connect_contact_flow
```

## Fields

| Title                | ID   | Type      | Data Type                                                                                                                                                                                     | Description |
| -------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string    |
| account_id           | core | string    |
| arn                  | core | string    | The Amazon Resource Name (ARN) of the flow.                                                                                                                                                   |
| content              | core | string    | The JSON string that represents the content of the flow. For an example, see Example flow in Amazon Connect Flow language. Length Constraints: Minimum length of 1. Maximum length of 256000. |
| description          | core | string    | The description of the flow.                                                                                                                                                                  |
| flow_content_sha256  | core | string    | Indicates the checksum value of the flow content.                                                                                                                                             |
| id                   | core | string    | The identifier of the flow.                                                                                                                                                                   |
| last_modified_region | core | string    | The region in which the flow was last modified                                                                                                                                                |
| last_modified_time   | core | timestamp | The time at which the flow was last modified.                                                                                                                                                 |
| name                 | core | string    | The name of the flow.                                                                                                                                                                         |
| state                | core | string    | The type of flow.                                                                                                                                                                             |
| status               | core | string    | The status of the flow.                                                                                                                                                                       |
| tags                 | core | hstore    |
| type                 | core | string    | The type of the flow. For descriptions of the available types, see Choose a flow type in the Amazon Connect Administrator Guide.                                                              |
| version              | core | int64     | The identifier of the flow version.                                                                                                                                                           |
| version_description  | core | string    | The description of the flow version.                                                                                                                                                          |
