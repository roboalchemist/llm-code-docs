# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.schemas_schema.dataset.md

---
title: EventBridge Schema
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EventBridge Schema
---

# EventBridge Schema

EventBridge Schema in AWS defines the structure of events used within Amazon EventBridge. It provides a formal description of the event's format, including its fields and data types, making it easier to validate, discover, and integrate events across applications.

```
aws.schemas_schema
```

## Fields

| Title                | ID   | Type       | Data Type                                   | Description |
| -------------------- | ---- | ---------- | ------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| content              | core | string     | The source of the schema definition.        |
| description          | core | string     | The description of the schema.              |
| last_modified        | core | timestamp  | The date and time that schema was modified. |
| schema_arn           | core | string     | The ARN of the schema.                      |
| schema_name          | core | string     | The name of the schema.                     |
| schema_version       | core | string     | The version number of the schema            |
| tags                 | core | hstore_csv |
| type                 | core | string     | The type of the schema.                     |
| version_created_date | core | timestamp  | The date the schema version was created.    |
