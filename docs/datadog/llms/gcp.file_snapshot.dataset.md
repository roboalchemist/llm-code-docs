# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.file_snapshot.dataset.md

---
title: Filestore Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Filestore Snapshot
---

# Filestore Snapshot

Filestore Snapshot in Google Cloud is a point-in-time copy of a Filestore instance. It allows you to preserve the state of your file system data for backup, recovery, or cloning purposes. Snapshots are stored independently from the source instance, enabling you to restore data to a new or existing Filestore instance without impacting the original.

```
gcp.file_snapshot
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                      | Description |
| --------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| create_time           | core | timestamp     | Output only. The time when the snapshot was created.                                                                                                           |
| datadog_display_name  | core | string        |
| description           | core | string        | A description of the snapshot with 2048 characters or less. Requests with longer descriptions will be rejected.                                                |
| filesystem_used_bytes | core | int64         | Output only. The amount of bytes needed to allocate a full copy of the snapshot content                                                                        |
| labels                | core | array<string> | Resource labels to represent user provided metadata.                                                                                                           |
| name                  | core | string        | Output only. The resource name of the snapshot, in the format `projects/{project_id}/locations/{location_id}/instances/{instance_id}/snapshots/{snapshot_id}`. |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| state                 | core | string        | Output only. The snapshot state.                                                                                                                               |
| tags                  | core | hstore_csv    |
| zone_id               | core | string        |
