# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.firebaserules_release.dataset.md

---
title: Firebase Rules Release
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Firebase Rules Release
---

# Firebase Rules Release

Firebase Rules Release is a Google Cloud resource that represents a specific deployment of Firebase security rules for services like Firestore, Storage, or Realtime Database. It defines the version of rules currently active in a Firebase project, allowing developers to manage, audit, and roll back rule configurations.

```
gcp.firebaserules_release
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Time the release was created.                                                                               |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | Required. Format: `projects/{project_id}/releases/{release_id}`                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| ruleset_name         | core | string        | Required. Name of the `Ruleset` referred to by this `Release`. The `Ruleset` must exist for the `Release` to be created. |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time the release was updated.                                                                               |
| zone_id              | core | string        |
