# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.iam_role.dataset.md

---
title: IAM Role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM Role
---

# IAM Role

An IAM Role in Google Cloud is a collection of permissions that define what actions a user or service account can perform on specific resources. Roles can be predefined by Google or custom-built to fit specific needs. They simplify access management by grouping permissions together, allowing administrators to assign them to users, groups, or service accounts instead of managing individual permissions.

```
gcp.iam_role
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| deleted              | core | bool          | The current deleted state of the role. This field is read only. It will be ignored in calls to CreateRole and UpdateRole.                                                                                                                                                                                                                                                                                                |
| description          | core | string        | Optional. A human-readable description for the role.                                                                                                                                                                                                                                                                                                                                                                     |
| included_permissions | core | array<string> | The names of the permissions this role grants when bound in an IAM policy.                                                                                                                                                                                                                                                                                                                                               |
| labels               | core | array<string> |
| name                 | core | string        | The name of the role. When `Role` is used in `CreateRole`, the role name must not be set. When `Role` is used in output and other input such as `UpdateRole`, the role name is the complete path. For example, `roles/logging.viewer` for predefined roles, `organizations/{ORGANIZATION_ID}/roles/myRole` for organization-level custom roles, and `projects/{PROJECT_ID}/roles/myRole` for project-level custom roles. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| stage                | core | string        | The current launch stage of the role. If the `ALPHA` launch stage has been selected for a role, the `stage` field will not be included in the returned definition for the role.                                                                                                                                                                                                                                          |
| tags                 | core | hstore_csv    |
| title                | core | string        | Optional. A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes.                                                                                                                                                                                                                                                                                                                             |
| zone_id              | core | string        |
