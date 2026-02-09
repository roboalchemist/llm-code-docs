# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.connectors_regional_settings.dataset.md

---
title: Regional Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Regional Settings
---

# Regional Settings

Regional Settings in Google Cloud Platform define configuration parameters that apply to resources within a specific region. These settings help manage aspects such as location preferences, data residency, and service availability. They ensure that workloads and data comply with regional requirements and optimize performance by keeping resources close to users or dependent services.

```
gcp.connectors_regional_settings
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                      | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| encryption_config    | core | json          | Optional. Regional encryption config to hold CMEK details.                                                     |
| labels               | core | array<string> |
| name                 | core | string        | Output only. Resource name of the Connection. Format: projects/{project}/locations/{location}/regionalSettings |
| network_config       | core | json          | Optional. Regional network config.                                                                             |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| provisioned          | core | bool          | Output only. Specifies whether the region is provisioned.                                                      |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
