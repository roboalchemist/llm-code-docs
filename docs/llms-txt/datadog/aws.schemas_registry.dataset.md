# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.schemas_registry.dataset.md

---
title: EventBridge Schema Registry
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Schema Registry
---

# EventBridge Schema Registry

EventBridge Schema Registry in AWS is a managed repository that stores and organizes event schemas used in EventBridge. It helps developers discover, create, and manage schemas for events, making it easier to understand event structure and generate code bindings for applications. This improves event-driven development by ensuring consistency and simplifying integration across services.

```
aws.schemas_registry
```

## Fields

| Title         | ID   | Type       | Data Type                 | Description |
| ------------- | ---- | ---------- | ------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| registry_arn  | core | string     | The ARN of the registry.  |
| registry_name | core | string     | The name of the registry. |
| tags          | core | hstore_csv |
