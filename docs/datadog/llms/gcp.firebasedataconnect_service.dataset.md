# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.firebasedataconnect_service.dataset.md

---
title: Firebase Data Connect Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Firebase Data Connect Service
---

# Firebase Data Connect Service

Firebase Data Connect Service is a managed service in Google Cloud that provides a secure and scalable way to connect Firebase applications to relational databases. It simplifies data access by automatically generating APIs and handling authentication, authorization, and query optimization. This service helps developers integrate structured data into their Firebase apps without managing backend infrastructure or complex data pipelines.

```
gcp.firebasedataconnect_service
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                  | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Stores small amounts of arbitrary data.                                                                                                                                                                                                                                                                          |
| create_time          | core | timestamp     | Output only. [Output only] Create time stamp.                                                                                                                                                                                                                                                                              |
| datadog_display_name | core | string        |
| etag                 | core | string        | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. [AIP-154](https://google.aip.dev/154)                                                                               |
| gcp_display_name     | core | string        | Optional. Mutable human-readable name. 63 character limit.                                                                                                                                                                                                                                                                 |
| labels               | core | array<string> | Optional. Labels as key value pairs.                                                                                                                                                                                                                                                                                       |
| name                 | core | string        | Identifier. The relative resource name of the Firebase Data Connect service, in the format: ``` projects/{project}/locations/{location}/services/{service} ``` Note that the service ID is specific to Firebase Data Connect and does not correspond to any of the instance IDs of the underlying data source connections. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. A field that if true, indicates that the system is working update the service.                                                                                                                                                                                                                                |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. System-assigned, unique identifier.                                                                                                                                                                                                                                                                           |
| update_time          | core | timestamp     | Output only. [Output only] Update time stamp.                                                                                                                                                                                                                                                                              |
| zone_id              | core | string        |
