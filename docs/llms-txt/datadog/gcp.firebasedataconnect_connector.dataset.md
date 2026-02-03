# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.firebasedataconnect_connector.dataset.md

---
title: Firebase Data Connect Connector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Firebase Data Connect Connector
---

# Firebase Data Connect Connector

Firebase Data Connect Connector is a managed service in Google Cloud that enables secure and efficient access to relational data from Firebase applications. It provides a seamless way to connect Firebase apps to databases like Cloud SQL, allowing developers to query and manage structured data using familiar Firebase tools. The connector handles authentication, scaling, and performance optimization automatically.

```
gcp.firebasedataconnect_connector
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Stores small amounts of arbitrary data.                                                                                                                                                                                            |
| create_time          | core | timestamp     | Output only. [Output only] Create time stamp.                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| etag                 | core | string        | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. [AIP-154](https://google.aip.dev/154) |
| gcp_display_name     | core | string        | Optional. Mutable human-readable name. 63 character limit.                                                                                                                                                                                   |
| gcp_source           | core | json          | Required. The source files that comprise the connector.                                                                                                                                                                                      |
| labels               | core | array<string> | Optional. Labels as key value pairs.                                                                                                                                                                                                         |
| name                 | core | string        | Identifier. The relative resource name of the connector, in the format: ``` projects/{project}/locations/{location}/services/{service}/connectors/{connector} ```                                                                            |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. A field that if true, indicates that the system is working to compile and deploy the connector.                                                                                                                                 |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. System-assigned, unique identifier.                                                                                                                                                                                             |
| update_time          | core | timestamp     | Output only. [Output only] Update time stamp.                                                                                                                                                                                                |
| zone_id              | core | string        |
