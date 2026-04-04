# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.firebasedataconnect_schema.dataset.md

---
title: Firebase Data Connect Schema
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Firebase Data Connect Schema
---

# Firebase Data Connect Schema

Firebase Data Connect Schema defines the structure and relationships of data used by Firebase Data Connect, a service that enables secure and scalable access to relational data from Firebase applications. It specifies how data is organized, queried, and synchronized between Firebase and connected databases, ensuring consistency and efficient data operations.

```
gcp.firebasedataconnect_schema
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Stores small amounts of arbitrary data.                                                                                                                                                                                            |
| create_time          | core | timestamp     | Output only. [Output only] Create time stamp.                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| datasources          | core | json          | Required. The data sources linked in the schema.                                                                                                                                                                                             |
| etag                 | core | string        | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. [AIP-154](https://google.aip.dev/154) |
| gcp_display_name     | core | string        | Optional. Mutable human-readable name. 63 character limit.                                                                                                                                                                                   |
| gcp_source           | core | json          | Required. The source files that comprise the application schema.                                                                                                                                                                             |
| labels               | core | array<string> | Optional. Labels as key value pairs.                                                                                                                                                                                                         |
| name                 | core | string        | Identifier. The relative resource name of the schema, in the format: ``` projects/{project}/locations/{location}/services/{service}/schemas/{schema} ``` Right now, the only supported schema is "main".                                     |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. A field that if true, indicates that the system is working to compile and deploy the schema.                                                                                                                                    |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. System-assigned, unique identifier.                                                                                                                                                                                             |
| update_time          | core | timestamp     | Output only. [Output only] Update time stamp.                                                                                                                                                                                                |
| zone_id              | core | string        |
