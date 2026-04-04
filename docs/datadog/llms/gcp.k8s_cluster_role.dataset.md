# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.k8s_cluster_role.dataset.md

---
title: K8s Cluster Role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > K8s Cluster Role
---

# K8s Cluster Role

This table represents the k8s_cluster_role resource from Google Cloud Platform.

```
gcp.k8s_cluster_role
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| aggregation_rule     | core | json          | AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.                                                                   |
| ancestors            | core | array<string> |
| api_version          | core | string        | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  |
| datadog_display_name | core | string        |
| kind                 | core | string        | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| labels               | core | array<string> |
| metadata             | core | json          | Standard object's metadata.                                                                                                                                                                                                                                                                        |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| rules                | core | json          | Rules holds all the PolicyRules for this ClusterRole                                                                                                                                                                                                                                               |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
