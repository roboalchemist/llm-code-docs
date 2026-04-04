# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.servicedirectory_namespace.dataset.md

---
title: Service Directory Namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Directory Namespace
---

# Service Directory Namespace

A Service Directory Namespace in Google Cloud is a container for organizing and managing services within Service Directory. It provides a logical grouping where services can be registered, discovered, and resolved by clients. Namespaces help isolate services across different environments or applications, making it easier to manage service endpoints and ensure consistent service discovery.

```
gcp.servicedirectory_namespace
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                 | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| labels               | core | array<string> | Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters. |
| name                 | core | string        | Immutable. The resource name for the namespace in the format `projects/*/locations/*/namespaces/*`.                                                                                       |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. The globally unique identifier of the namespace in the UUID4 format.                                                                                                         |
| zone_id              | core | string        |
