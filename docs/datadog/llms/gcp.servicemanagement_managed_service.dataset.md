# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.servicemanagement_managed_service.dataset.md

---
title: Managed Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Managed Service
---

# Managed Service

A Managed Service in Google Cloud is a fully managed offering where Google handles infrastructure, scaling, patching, and maintenance tasks. It allows users to focus on application logic and business needs instead of operational overhead. Examples include managed databases, data processing services, and AI platforms.

```
gcp.servicemanagement_managed_service
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                           | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| organization_id      | core | string        |
| parent               | core | string        |
| producer_project_id  | core | string        | ID of the project that produces and owns this service.                                                                              |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| service_name         | core | string        | The name of the service. See the [overview](https://cloud.google.com/service-infrastructure/docs/overview) for naming requirements. |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
