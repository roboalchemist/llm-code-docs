# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataplex_environment.dataset.md

---
title: Dataplex Environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataplex Environment
---

# Dataplex Environment

A Dataplex Environment in Google Cloud is a managed compute resource that provides the infrastructure for running data processing tasks, notebooks, and analytics within Dataplex. It offers preconfigured execution environments with security, networking, and data access controls, enabling users to explore, transform, and analyze data stored across lakes, zones, and assets in a governed and scalable way.

```
gcp.dataplex_environment
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Environment creation time.                                                                                                                             |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the environment.                                                                                                                           |
| endpoints            | core | json          | Output only. URI Endpoints to access sessions associated with the Environment.                                                                                      |
| gcp_display_name     | core | string        | Optional. User friendly display name.                                                                                                                               |
| infrastructure_spec  | core | json          | Required. Infrastructure specification for the Environment.                                                                                                         |
| labels               | core | array<string> | Optional. User defined labels for the environment.                                                                                                                  |
| name                 | core | string        | Output only. The relative resource name of the environment, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id} |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| session_spec         | core | json          | Optional. Configuration for sessions created for this environment.                                                                                                  |
| session_status       | core | json          | Output only. Status of sessions created for this environment.                                                                                                       |
| state                | core | string        | Output only. Current state of the environment.                                                                                                                      |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. System generated globally unique ID for the environment. This ID will be different if the environment is deleted and re-created with the same name.    |
| update_time          | core | timestamp     | Output only. The time when the environment was last updated.                                                                                                        |
| zone_id              | core | string        |
