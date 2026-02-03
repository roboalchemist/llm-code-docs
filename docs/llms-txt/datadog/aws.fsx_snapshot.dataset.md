# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.fsx_snapshot.dataset.md

---
title: FSx Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > FSx Snapshot
---

# FSx Snapshot

An FSx Snapshot in AWS is a point-in-time backup of an Amazon FSx file system. It captures the state of the file system at the moment the snapshot is taken, allowing you to restore data or create new file systems from it. Snapshots are incremental, meaning only changes since the last snapshot are saved, which helps reduce storage costs.

```
aws.fsx_snapshot
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                              | Description |
| --------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| administrative_actions      | core | json       | A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system.                                                                                                                                                 |
| creation_time               | core | timestamp  | The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.                                                                                                                                                                                                              |
| lifecycle                   | core | string     | The lifecycle status of the snapshot. PENDING - Amazon FSx hasn't started creating the snapshot. CREATING - Amazon FSx is creating the snapshot. DELETING - Amazon FSx is deleting the snapshot. AVAILABLE - The snapshot is fully available.                                                                          |
| lifecycle_transition_reason | core | json       | Describes why a resource lifecycle state changed.                                                                                                                                                                                                                                                                      |
| name                        | core | string     | The name of the snapshot.                                                                                                                                                                                                                                                                                              |
| resource_arn                | core | string     | The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference. |
| snapshot_id                 | core | string     | The ID of the snapshot.                                                                                                                                                                                                                                                                                                |
| tags                        | core | hstore_csv |
| volume_id                   | core | string     | The ID of the volume that the snapshot is of.                                                                                                                                                                                                                                                                          |
