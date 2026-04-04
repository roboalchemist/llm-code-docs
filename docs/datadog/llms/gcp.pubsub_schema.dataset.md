# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.pubsub_schema.dataset.md

---
title: Pub/Sub Schema
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Pub/Sub Schema
---

# Pub/Sub Schema

Pub/Sub Schema in Google Cloud defines the structure of messages published to and received from Pub/Sub topics. It ensures data consistency by enforcing a specific format, such as Avro or Protocol Buffers, for message payloads. Schemas help validate messages before publishing, reducing errors and improving data quality across systems.

```
gcp.pubsub_schema
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| definition           | core | string        | The definition of the schema. This should contain a string representing the full definition of the schema that is a valid schema definition of the type specified in `type`. |
| labels               | core | array<string> |
| name                 | core | string        | Required. Name of the schema. Format is `projects/{project}/schemas/{schema}`.                                                                                               |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| revision_create_time | core | timestamp     | Output only. The timestamp that the revision was created.                                                                                                                    |
| revision_id          | core | string        | Output only. Immutable. The revision ID of the schema.                                                                                                                       |
| tags                 | core | hstore_csv    |
| type                 | core | string        | The type of the schema definition.                                                                                                                                           |
| zone_id              | core | string        |
