# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.folder.dataset.md

---
title: Folder
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Folder
---

# Folder

This table represents the Folder resource from Google Cloud Platform.

```
gcp.folder
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Timestamp when the folder was created.                                                                                                                                                                                                                                                                                                                                                                                         |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. Timestamp when the folder was requested to be deleted.                                                                                                                                                                                                                                                                                                                                                                         |
| etag                 | core | string        | Output only. A checksum computed by the server based on the current value of the folder resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.                                                                                                                                                                                                                            |
| gcp_display_name     | core | string        | The folder's display name. A folder's display name must be unique amongst its siblings. For example, no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters. This is captured by the regular expression: `[\p{L}\p{N}]([\p{L}\p{N}_- ]{0,28}[\p{L}\p{N}])?`. |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The resource name of the folder. Its format is `folders/{folder_id}`, for example: "folders/1234".                                                                                                                                                                                                                                                                                                                             |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The lifecycle state of the folder. Updates to the state must be performed using DeleteFolder and UndeleteFolder. Possible values: ['STATE_UNSPECIFIED', 'ACTIVE', 'DELETE_REQUESTED']. Values descriptions: ['Unspecified state.', 'The normal and active state.', 'The folder has been marked for deletion by the user.']                                                                                                     |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Timestamp when the folder was last modified.                                                                                                                                                                                                                                                                                                                                                                                   |
| zone_id              | core | string        |
