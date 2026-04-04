# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.contactcenterinsights_view.dataset.md

---
title: View
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > View
---

# View

A View in Google Cloud refers to a virtual table defined by a SQL query that presents data from one or more tables or other views. It does not store data itself but provides a way to simplify complex queries, enforce data access controls, and present consistent data representations. Views are commonly used in BigQuery and other GCP data services to manage and secure data access efficiently.

```
gcp.contactcenterinsights_view
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time at which this view was created.                                                                                               |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | The human-readable display name of the view.                                                                                                        |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. The resource name of the view. Format: projects/{project}/locations/{location}/views/{view}                                              |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The most recent time at which the view was updated.                                                                                    |
| value                | core | string        | A filter to reduce conversation results to a specific subset. Refer to https://cloud.google.com/contact-center/insights/docs/filtering for details. |
| zone_id              | core | string        |
