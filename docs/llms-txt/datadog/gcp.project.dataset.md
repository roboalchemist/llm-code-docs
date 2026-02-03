# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.project.dataset.md

---
title: Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Project
---

# Project

This table represents the Project resource from Google Cloud Platform.

```
gcp.project
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Creation time.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. The time at which this resource was requested for deletion.                                                                                                                                                                                                                                                                                                                                                                        |
| etag                 | core | string        | Output only. A checksum computed by the server based on the current value of the Project resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.                                                                                                                                                                                                                               |
| gcp_display_name     | core | string        | Optional. A user-assigned display name of the project. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `My Project`                                                                                                                                                                            |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The unique resource name of the project. It is an int64 generated number prefixed by "projects/". Example: `projects/415104041262`                                                                                                                                                                                                                                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The project lifecycle state. Possible values: ['STATE_UNSPECIFIED', 'ACTIVE', 'DELETE_REQUESTED']. Values descriptions: ['Unspecified state. This is only used/useful for distinguishing unset values.', 'The normal and active state.', 'The project has been marked for deletion by the user (by invoking DeleteProject) or by the system (Google Cloud Platform). This can generally be reversed by invoking UndeleteProject.'] |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The most recent time this resource was modified.                                                                                                                                                                                                                                                                                                                                                                                   |
| zone_id              | core | string        |
