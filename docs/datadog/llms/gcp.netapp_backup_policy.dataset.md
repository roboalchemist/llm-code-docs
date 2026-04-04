# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.netapp_backup_policy.dataset.md

---
title: NetApp Backup Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > NetApp Backup Policy
---

# NetApp Backup Policy

A NetApp Backup Policy in Google Cloud defines automated backup schedules and retention rules for Cloud Volumes ONTAP or Cloud Volumes Service. It ensures data protection by managing when and how backups are created, stored, and deleted. This policy helps maintain compliance, supports disaster recovery, and simplifies backup management across NetApp storage environments in GCP.

```
gcp.netapp_backup_policy
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                              | Description |
| --------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| assigned_volume_count | core | int64         | Output only. The total number of volumes assigned by this backup policy.                                                                                                                               |
| create_time           | core | timestamp     | Output only. The time when the backup policy was created.                                                                                                                                              |
| daily_backup_limit    | core | int64         | Number of daily backups to keep. Note that the minimum daily backup limit is 2.                                                                                                                        |
| datadog_display_name  | core | string        |
| description           | core | string        | Description of the backup policy.                                                                                                                                                                      |
| enabled               | core | bool          | If enabled, make backups automatically according to the schedules. This will be applied to all volumes that have this policy attached and enforced on volume level. If not specified, default is true. |
| labels                | core | array<string> | Resource labels to represent user provided metadata.                                                                                                                                                   |
| monthly_backup_limit  | core | int64         | Number of monthly backups to keep. Note that the sum of daily, weekly and monthly backups should be greater than 1.                                                                                    |
| name                  | core | string        | Identifier. The resource name of the backup policy. Format: `projects/{project_id}/locations/{location}/backupPolicies/{backup_policy_id}`.                                                            |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| state                 | core | string        | Output only. The backup policy state.                                                                                                                                                                  |
| tags                  | core | hstore_csv    |
| weekly_backup_limit   | core | int64         | Number of weekly backups to keep. Note that the sum of daily, weekly and monthly backups should be greater than 1.                                                                                     |
| zone_id               | core | string        |
