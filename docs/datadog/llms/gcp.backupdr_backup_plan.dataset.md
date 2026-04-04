# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.backupdr_backup_plan.dataset.md

---
title: Backup and DR Backup Plan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup and DR Backup Plan
---

# Backup and DR Backup Plan

A Backup and DR Backup Plan in Google Cloud defines how data is backed up, stored, and recovered across Google Cloud services. It specifies backup schedules, retention policies, and recovery objectives to ensure business continuity. This resource helps automate and manage backup operations for databases, virtual machines, and other workloads, providing centralized control and compliance support.

```
gcp.backupdr_backup_plan
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                       | Description |
| ---------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| ancestors                    | core | array<string> |
| backup_rules                 | core | json          | Optional. The backup rules for this `BackupPlan`.                                                                                                                                                                                                                                                                                               |
| backup_vault                 | core | string        | Required. Resource name of backup vault which will be used as storage location for backups. Format: projects/{project}/locations/{location}/backupVaults/{backupvault}                                                                                                                                                                          |
| backup_vault_service_account | core | string        | Output only. The Google Cloud Platform Service Account to be used by the BackupVault for taking backups. Specify the email address of the Backup Vault Service Account.                                                                                                                                                                         |
| create_time                  | core | timestamp     | Output only. When the `BackupPlan` was created.                                                                                                                                                                                                                                                                                                 |
| datadog_display_name         | core | string        |
| description                  | core | string        | Optional. The description of the `BackupPlan` resource. The description allows for additional details about `BackupPlan` and its use cases to be provided. An example description is the following: "This is a backup plan that performs a daily backup at 6pm and retains data for 3 months". The description must be at most 2048 characters. |
| etag                         | core | string        | Optional. `etag` is returned from the service in the response. As a user of the service, you may provide an etag value in this field to prevent stale resources.                                                                                                                                                                                |
| labels                       | core | array<string> | Optional. This collection of key/value pairs allows for custom labels to be supplied by the user. Example, {"tag": "Weekly"}.                                                                                                                                                                                                                   |
| log_retention_days           | core | int64         | Optional. Applicable only for CloudSQL resource_type. Configures how long logs will be stored. It is defined in "days". This value should be greater than or equal to minimum enforced log retention duration of the backup vault.                                                                                                              |
| name                         | core | string        | Output only. Identifier. The resource name of the `BackupPlan`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`                                                                                                                                                                                                     |
| organization_id              | core | string        |
| parent                       | core | string        |
| project_id                   | core | string        |
| project_number               | core | string        |
| region_id                    | core | string        |
| resource_name                | core | string        |
| resource_type                | core | string        | Required. The resource type to which the `BackupPlan` will be applied. Examples include, "compute.googleapis.com/Instance", "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster", "compute.googleapis.com/Disk".                                                                                                                |
| revision_id                  | core | string        | Output only. The user friendly revision ID of the `BackupPlanRevision`. Example: v0, v1, v2, etc.                                                                                                                                                                                                                                               |
| revision_name                | core | string        | Output only. The resource id of the `BackupPlanRevision`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`                                                                                                                                                                                   |
| state                        | core | string        | Output only. The `State` for the `BackupPlan`.                                                                                                                                                                                                                                                                                                  |
| supported_resource_types     | core | array<string> | Output only. All resource types to which backupPlan can be applied.                                                                                                                                                                                                                                                                             |
| tags                         | core | hstore_csv    |
| update_time                  | core | timestamp     | Output only. When the `BackupPlan` was last updated.                                                                                                                                                                                                                                                                                            |
| zone_id                      | core | string        |
