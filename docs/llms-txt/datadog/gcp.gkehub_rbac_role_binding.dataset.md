# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkehub_rbac_role_binding.dataset.md

---
title: GKE Hub RBAC Role Binding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GKE Hub RBAC Role Binding
---

# GKE Hub RBAC Role Binding

GKE Hub RBAC Role Binding is a Google Cloud resource that defines role-based access control bindings for users, groups, or service accounts within a GKE Hub environment. It associates specific roles with members to manage permissions across registered clusters in a fleet. This helps ensure consistent access control and security policies across multiple Kubernetes clusters connected through GKE Hub.

```
gcp.gkehub_rbac_role_binding
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                      | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. When the rbacrolebinding was created.                                                                                                                                                                                             |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. When the rbacrolebinding was deleted.                                                                                                                                                                                             |
| group                | core | string        | group is the group, as seen by the kubernetes cluster.                                                                                                                                                                                         |
| labels               | core | array<string> | Optional. Labels for this RBACRolebinding.                                                                                                                                                                                                     |
| name                 | core | string        | The resource name for the rbacrolebinding `projects/{project}/locations/{location}/scopes/{scope}/rbacrolebindings/{rbacrolebinding}` or `projects/{project}/locations/{location}/memberships/{membership}/rbacrolebindings/{rbacrolebinding}` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| role                 | core | json          | Required. Role to bind to the principal                                                                                                                                                                                                        |
| state                | core | json          | Output only. State of the rbacrolebinding resource.                                                                                                                                                                                            |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Google-generated UUID for this resource. This is unique across all rbacrolebinding resources. If a rbacrolebinding resource is deleted and another resource with the same name is created, it gets a different uid.               |
| update_time          | core | timestamp     | Output only. When the rbacrolebinding was last updated.                                                                                                                                                                                        |
| user                 | core | string        | user is the name of the user as seen by the kubernetes cluster, example "alice" or "alice@domain.tld"                                                                                                                                          |
| zone_id              | core | string        |
