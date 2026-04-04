# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.schemas_aws_schema.dataset.md

---
title: Schema
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Schema
---

# Schema

Schema in AWS refers to the structure definition used within AWS EventBridge Schemas. It describes the format, properties, and data types of events, enabling applications to understand and validate event data. The DescribeSchemaResponse provides details about a specific schema, such as its name, version, and content. This helps developers integrate and process events consistently across services.

```
aws.schemas_aws_schema
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
