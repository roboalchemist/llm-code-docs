# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.apihub_api_hub_instance.dataset.md

---
title: Apihub Api Hub Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Apihub Api Hub Instance
---

# Apihub Api Hub Instance

This table represents the apihub_api_hub_instance resource from Google Cloud Platform.

```
gcp.apihub_api_hub_instance
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| config               | core | json          | Required. Config of the ApiHub instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| create_time          | core | timestamp     | Output only. Creation timestamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the ApiHub instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| labels               | core | array<string> |
| name                 | core | string        | Identifier. Format: `projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The current state of the ApiHub instance. Possible values: ['STATE_UNSPECIFIED', 'INACTIVE', 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'FAILED']. Values descriptions: ['The default value. This value is used if the state is omitted.', 'The ApiHub instance has not been initialized or has been deleted.', 'The ApiHub instance is being created.', 'The ApiHub instance has been created and is ready for use.', 'The ApiHub instance is being updated.', 'The ApiHub instance is being deleted.', 'The ApiHub instance encountered an error during a state change.'] |
| state_message        | core | string        | Output only. Extra information about ApiHub instance state. Currently the message would be populated when state is `FAILED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Last update timestamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| zone_id              | core | string        |
