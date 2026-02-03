# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.discoveryengine_collection.dataset.md

---
title: Discovery Engine Collection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Discovery Engine Collection
---

# Discovery Engine Collection

Discovery Engine Collection in Google Cloud is a container for organizing and managing data used by Discovery Engine services, such as search and recommendation systems. It groups related data sources, schemas, and configurations to enable efficient indexing, querying, and personalization across datasets.

```
gcp.discoveryengine_collection
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Timestamp the Collection was created at.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| data_connector       | core | json          | Output only. The data connector, if present, manages the connection for data stores in the Collection. To set up the connector, use DataConnectorService.SetUpDataConnector method, which creates a new Collection while setting up the DataConnector singleton resource. Setting up connector on an existing Collection is not supported. This output only field contains a subset of the DataConnector fields, including `name`, `data_source`, `entities.entity_name` and `entities.data_store`. To get more details about a data connector, use the DataConnectorService.GetDataConnector method. |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | Required. The Collection display name. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. The full resource name of the Collection. Format: `projects/{project}/locations/{location}/collections/{collection_id}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters.                                                                                                                                                                                                                                                                                                                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
