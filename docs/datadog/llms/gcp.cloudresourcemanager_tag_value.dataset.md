# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudresourcemanager_tag_value.dataset.md

---
title: TagValue
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > TagValue
---

# TagValue

TagValue in Google Cloud represents a specific value within a TagKey, used for organizing and managing resources through labels. It helps apply consistent metadata across projects, folders, and organizations, enabling better resource grouping, access control, and cost tracking. Each TagValue is associated with a TagKey and can be attached to supported resources for policy enforcement and organization.

```
gcp.cloudresourcemanager_tag_value
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                        | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Creation time.                                                                                                                                                                                                                                                                                                      |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. User-assigned description of the TagValue. Must not exceed 256 characters. Read-write.                                                                                                                                                                                                                                 |
| etag                 | core | string        | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagValueRequest for details.                                                                                                                                                                       |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. Resource name for TagValue in the format `tagValues/456`.                                                                                                                                                                                                                                                             |
| namespaced_name      | core | string        | Output only. The namespaced name of the TagValue. Can be in the form `{organization_id}/{tag_key_short_name}/{tag_value_short_name}` or `{project_id}/{tag_key_short_name}/{tag_value_short_name}` or `{project_number}/{tag_key_short_name}/{tag_value_short_name}`.                                                            |
| organization_id      | core | string        |
| parent               | core | string        | Immutable. The resource name of the new TagValue's parent TagKey. Must be of the form `tagKeys/{tag_key_id}`.                                                                                                                                                                                                                    |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| short_name           | core | string        | Required. Immutable. User-assigned short name for TagValue. The short name should be unique for TagValues within the same parent TagKey. The short name must be 256 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Update time.                                                                                                                                                                                                                                                                                                        |
| zone_id              | core | string        |
