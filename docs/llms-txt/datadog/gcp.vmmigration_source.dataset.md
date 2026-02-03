# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmmigration_source.dataset.md

---
title: VM Migration Source
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VM Migration Source
---

# VM Migration Source

VM Migration Source in Google Cloud represents the origin environment from which virtual machines are discovered and migrated into Google Cloud. It defines the connection details and configuration needed to access on-premises or other cloud environments, enabling assessment, replication, and migration of workloads into GCP.

```
gcp.vmmigration_source
```

## Fields

| Title                | ID   | Type          | Data Type                                                                             | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| aws                  | core | json          | AWS type source details.                                                              |
| azure                | core | json          | Azure type source details.                                                            |
| create_time          | core | timestamp     | Output only. The create time timestamp.                                               |
| datadog_display_name | core | string        |
| description          | core | string        | User-provided description of the source.                                              |
| encryption           | core | json          | Optional. Immutable. The encryption details of the source data stored by the service. |
| labels               | core | array<string> | The labels of the source.                                                             |
| name                 | core | string        | Output only. The Source name.                                                         |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The update time timestamp.                                               |
| vmware               | core | json          | Vmware type source details.                                                           |
| zone_id              | core | string        |
