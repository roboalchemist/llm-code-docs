# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.netapp_snapshot.dataset.md

---
title: NetApp Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > NetApp Snapshot
---

# NetApp Snapshot

NetApp Snapshot in Google Cloud is a point-in-time copy of a Cloud Volumes Service volume. It allows users to quickly back up and restore data without impacting performance or requiring additional storage management. Snapshots are space-efficient, incremental, and can be used for data protection, recovery, or cloning purposes within NetApp Cloud Volumes on GCP.

```
gcp.netapp_snapshot
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                        | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time when the snapshot was created.                                                                                             |
| datadog_display_name | core | string        |
| description          | core | string        | A description of the snapshot with 2048 characters or less. Requests with longer descriptions will be rejected.                                  |
| labels               | core | array<string> | Resource labels to represent user provided metadata.                                                                                             |
| name                 | core | string        | Identifier. The resource name of the snapshot. Format: `projects/{project_id}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}`. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The snapshot state.                                                                                                                 |
| state_details        | core | string        | Output only. State details of the storage pool                                                                                                   |
| tags                 | core | hstore_csv    |
| used_bytes           | core | float64       | Output only. Current storage usage for the snapshot in bytes.                                                                                    |
| zone_id              | core | string        |
