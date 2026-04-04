# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkehub_membership_feature.dataset.md

---
title: GKE Hub Feature Membership
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GKE Hub Feature Membership
---

# GKE Hub Feature Membership

GKE Hub Feature Membership represents the association between a specific GKE cluster and a feature managed through the GKE Hub. It enables centralized management, configuration, and monitoring of features such as Anthos Service Mesh, Config Management, or Policy Controller across multiple clusters. This resource helps ensure consistent feature deployment and lifecycle management within a multi-cluster or hybrid environment.

```
gcp.gkehub_membership_feature
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| configmanagement     | core | json          | Config Management-specific spec.                                                                                                                                                                                    |
| datadog_display_name | core | string        |
| fleetobservability   | core | json          | Fleet observability membership spec                                                                                                                                                                                 |
| identityservice      | core | json          | Identity Service-specific spec.                                                                                                                                                                                     |
| labels               | core | array<string> |
| mesh                 | core | json          | Anthos Service Mesh-specific spec                                                                                                                                                                                   |
| organization_id      | core | string        |
| origin               | core | json          | Whether this per-Membership spec was inherited from a fleet-level default. This field can be updated by users by either overriding a Membership config (updated to USER implicitly) or setting to FLEET explicitly. |
| parent               | core | string        |
| policycontroller     | core | json          | Policy Controller spec.                                                                                                                                                                                             |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
