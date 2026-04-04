# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.k8s_pod.dataset.md

---
title: K8s Pod
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > K8s Pod
---

# K8s Pod

This table represents the k8s_pod resource from Google Cloud Platform.

```
gcp.k8s_pod
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| api_version          | core | string        | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  |
| datadog_display_name | core | string        |
| gcp_status           | core | json          | Most recently observed status of the pod. This data may not be up to date. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status                                                                      |
| kind                 | core | string        | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| labels               | core | array<string> |
| metadata             | core | json          | Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata                                                                                                                                                                |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| spec                 | core | json          | Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status                                                                                                                                   |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
