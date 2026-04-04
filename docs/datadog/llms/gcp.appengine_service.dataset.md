# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.appengine_service.dataset.md

---
title: App Engine Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Engine Service
---

# App Engine Service

App Engine Service in Google Cloud is a logical component within App Engine that runs a specific application or microservice. Each service can have its own runtime, scaling configuration, and versioning, allowing developers to separate workloads, manage traffic routing, and deploy updates independently. It is useful for structuring applications into modular parts while leveraging App Engine's fully managed infrastructure.

```
gcp.appengine_service
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| id                   | core | string        | Output only. Relative name of the service within the application. Example: default.@OutputOnly                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| labels               | core | array<string> | A set of labels to apply to this service. Labels are key/value pairs that describe the service and all resources that belong to it (e.g., versions). The labels can be used to search and group resources, and are propagated to the usage and billing reports, enabling fine-grain analysis of costs. An example of using labels is to tag resources belonging to different environments (e.g., "env=prod", "env=qa"). Label keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, dashes, and international characters. Label keys must start with a lowercase letter or an international character. Each service can have at most 32 labels. |
| name                 | core | string        | Output only. Full path to the Service resource in the API. Example: apps/myapp/services/default.@OutputOnly                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| network_settings     | core | json          | Ingress settings for this service. Will apply to all versions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| split                | core | json          | Mapping that defines fractional HTTP traffic diversion to different versions within the service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
