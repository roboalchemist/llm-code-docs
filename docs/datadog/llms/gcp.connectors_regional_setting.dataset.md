# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.connectors_regional_setting.dataset.md

---
title: Regional Setting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Regional Setting
---

# Regional Setting

Defines the geographical region where Google Cloud resources are deployed and managed. A regional setting determines data residency, latency, and redundancy by associating resources with a specific Google Cloud region. It ensures that services and workloads operate within the selected region's infrastructure for compliance and performance optimization.

```
gcp.connectors_regional_setting
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
