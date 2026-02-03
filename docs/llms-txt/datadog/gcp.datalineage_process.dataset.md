# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.datalineage_process.dataset.md

---
title: Data Lineage Process
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Data Lineage Process
---

# Data Lineage Process

Data Lineage Process in GCP tracks the flow of data through various services, showing how data is created, transformed, and consumed. It helps users understand dependencies between datasets, pipelines, and transformations, improving data governance, troubleshooting, and compliance. This resource is part of Google Cloud Data Catalog and Dataplex lineage capabilities.

```
gcp.datalineage_process
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | Optional. A human-readable name you can set to display in a user interface. Must be not longer than 200 characters and only contain UTF-8 letters or numbers, spaces or characters like `_-:&.`                                                                       |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. The resource name of the lineage process. Format: `projects/{project}/locations/{location}/processes/{process}`. Can be specified or auto-assigned. {process} must be not longer than 200 characters and only contain characters in a set: `a-zA-Z0-9_-:.` |
| organization_id      | core | string        |
| origin               | core | json          | Optional. The origin of this process and its runs and lineage events.                                                                                                                                                                                                 |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
