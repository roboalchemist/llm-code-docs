# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkehub_membership_binding.dataset.md

---
title: GKE Hub MembershipBinding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GKE Hub MembershipBinding
---

# GKE Hub MembershipBinding

GKE Hub MembershipBinding is a Google Cloud resource that associates a GKE Hub Membership with a specific policy or configuration, such as fleet-level RBAC or workload identity settings. It defines how a cluster participates in fleet-wide features and enforces consistent access or management policies across multiple clusters within a fleet.

```
gcp.gkehub_membership_binding
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. When the membership binding was created.                                                                                                                                                                                |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. When the membership binding was deleted.                                                                                                                                                                                |
| labels               | core | array<string> | Optional. Labels for this MembershipBinding.                                                                                                                                                                                         |
| name                 | core | string        | The resource name for the membershipbinding itself `projects/{project}/locations/{location}/memberships/{membership}/bindings/{membershipbinding}`                                                                                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| scope                | core | string        | A Scope resource name in the format `projects/*/locations/*/scopes/*`.                                                                                                                                                               |
| state                | core | json          | Output only. State of the membership binding resource.                                                                                                                                                                               |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Google-generated UUID for this resource. This is unique across all membershipbinding resources. If a membershipbinding resource is deleted and another resource with the same name is created, it gets a different uid. |
| update_time          | core | timestamp     | Output only. When the membership binding was last updated.                                                                                                                                                                           |
| zone_id              | core | string        |
