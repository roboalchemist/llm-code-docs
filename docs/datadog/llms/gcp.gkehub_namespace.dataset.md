# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkehub_namespace.dataset.md

---
title: GKE Hub Namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GKE Hub Namespace
---

# GKE Hub Namespace

GKE Hub Namespace is a Google Cloud resource that represents a logical namespace within a registered Kubernetes cluster managed through GKE Hub. It enables consistent configuration, policy management, and service discovery across multiple clusters in a fleet. This resource helps organize workloads and apply configurations at the namespace level for multi-cluster environments.

```
gcp.gkehub_namespace
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. When the namespace was created.                                                                                                                                                                         |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. When the namespace was deleted.                                                                                                                                                                         |
| labels               | core | array<string> | Optional. Labels for this Namespace.                                                                                                                                                                                 |
| name                 | core | string        | The resource name for the namespace `projects/{project}/locations/{location}/namespaces/{namespace}`                                                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| scope                | core | string        | Required. Scope associated with the namespace                                                                                                                                                                        |
| state                | core | json          | Output only. State of the namespace resource.                                                                                                                                                                        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Google-generated UUID for this resource. This is unique across all namespace resources. If a namespace resource is deleted and another resource with the same name is created, it gets a different uid. |
| update_time          | core | timestamp     | Output only. When the namespace was last updated.                                                                                                                                                                    |
| zone_id              | core | string        |
