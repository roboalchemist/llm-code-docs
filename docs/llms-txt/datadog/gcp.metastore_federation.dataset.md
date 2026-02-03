# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.metastore_federation.dataset.md

---
title: Dataproc Metastore Federation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataproc Metastore Federation
---

# Dataproc Metastore Federation

Dataproc Metastore Federation in Google Cloud allows you to access and manage metadata from multiple Hive Metastores and Dataproc Metastores through a single unified interface. It simplifies data discovery and governance by providing a consistent view of metadata across different environments, enabling seamless integration with analytics and data processing tools.

```
gcp.metastore_federation
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time when the metastore federation was created.                                                                                      |
| datadog_display_name | core | string        |
| endpoint_uri         | core | string        | Output only. The federation endpoint.                                                                                                                 |
| labels               | core | array<string> | User-defined labels for the metastore federation.                                                                                                     |
| name                 | core | string        | Immutable. The relative resource name of the federation, of the form: projects/{project_number}/locations/{location_id}/federations/{federation_id}`. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The current state of the federation.                                                                                                     |
| state_message        | core | string        | Output only. Additional information about the current state of the metastore federation, if available.                                                |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. The globally unique resource identifier of the metastore federation.                                                                     |
| update_time          | core | timestamp     | Output only. The time when the metastore federation was last updated.                                                                                 |
| version              | core | string        | Immutable. The Apache Hive metastore version of the federation. All backend metastore versions must be compatible with the federation version.        |
| zone_id              | core | string        |
