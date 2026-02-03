# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_contact_flow_module.dataset.md

---
title: Connect Contact Flow Module
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Contact Flow Module
---

# Connect Contact Flow Module

Connect Contact Flow Module in AWS is a reusable component within Amazon Connect that allows you to define and manage parts of a contact flow separately. It helps simplify complex flows by breaking them into smaller, modular pieces that can be reused across multiple contact flows. This improves maintainability, consistency, and efficiency when designing customer interaction experiences.

```
aws.connect_contact_flow_module
```

## Fields

| Title       | ID   | Type       | Data Type                                                                                                                  | Description |
| ----------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| arn         | core | string     | The Amazon Resource Name (ARN).                                                                                            |
| content     | core | string     | The JSON string that represents the content of the flow. For an example, see Example flow in Amazon Connect Flow language. |
| description | core | string     | The description of the flow module.                                                                                        |
| id          | core | string     | The identifier of the flow module.                                                                                         |
| name        | core | string     | The name of the flow module.                                                                                               |
| state       | core | string     | The type of flow module.                                                                                                   |
| status      | core | string     | The status of the flow module.                                                                                             |
| tags        | core | hstore_csv |
