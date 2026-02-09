# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.apigateway_api.dataset.md

---
title: API Gateway API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway API
---

# API Gateway API

API Gateway API in Google Cloud is a managed service that allows you to create, secure, and monitor APIs for your backend services. It provides a centralized entry point for managing traffic, authentication, and access control, while integrating with other GCP services. This helps developers expose and manage APIs efficiently without handling infrastructure or scaling concerns.

```
gcp.apigateway_api
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Created time.                                                                                                                                                                                                         |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | Optional. Display name.                                                                                                                                                                                                            |
| labels               | core | array<string> | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources                                                   |
| managed_service      | core | string        | Optional. Immutable. The name of a Google Managed Service ( https://cloud.google.com/service-infrastructure/docs/glossary#managed). If not specified, a new Service will automatically be created in the same project as this API. |
| name                 | core | string        | Output only. Resource name of the API. Format: projects/{project}/locations/global/apis/{api}                                                                                                                                      |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. State of the API.                                                                                                                                                                                                     |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Updated time.                                                                                                                                                                                                         |
| zone_id              | core | string        |
