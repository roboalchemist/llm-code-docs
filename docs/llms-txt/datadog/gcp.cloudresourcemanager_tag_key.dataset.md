# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudresourcemanager_tag_key.dataset.md

---
title: TagKey
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > TagKey
---

# TagKey

TagKey in Google Cloud is a resource that defines a key within the tagging system used for organizing and managing cloud resources. It represents the key part of a key-value pair that can be applied across projects, folders, or organizations to categorize and control access to resources consistently.

```
gcp.cloudresourcemanager_tag_key
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Creation time.                                                                                                                                                                                                                                                                                                                           |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. User-assigned description of the TagKey. Must not exceed 256 characters. Read-write.                                                                                                                                                                                                                                                        |
| etag                 | core | string        | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagKeyRequest for details.                                                                                                                                                                                              |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. The resource name for a TagKey. Must be in the format `tagKeys/{tag_key_id}`, where `tag_key_id` is the generated numeric id for the TagKey.                                                                                                                                                                                               |
| namespaced_name      | core | string        | Output only. Immutable. Namespaced name of the TagKey.                                                                                                                                                                                                                                                                                                |
| organization_id      | core | string        |
| parent               | core | string        | Immutable. The resource name of the TagKey's parent. A TagKey can be parented by an Organization or a Project. For a TagKey parented by an Organization, its parent must be in the form `organizations/{org_id}`. For a TagKey parented by a Project, its parent can be in the form `projects/{project_id}` or `projects/{project_number}`.           |
| project_id           | core | string        |
| project_number       | core | string        |
| purpose              | core | string        | Optional. A purpose denotes that this Tag is intended for use in policies of a specific policy engine, and will involve that policy engine in management operations involving this Tag. A purpose does not grant a policy engine exclusive rights to the Tag, and it may be referenced by other policy engines. A purpose cannot be changed once set. |
| region_id            | core | string        |
| resource_name        | core | string        |
| short_name           | core | string        | Required. Immutable. The user friendly name for a TagKey. The short name should be unique for TagKeys within the same tag namespace. The short name must be 1-256 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.                                |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Update time.                                                                                                                                                                                                                                                                                                                             |
| zone_id              | core | string        |
