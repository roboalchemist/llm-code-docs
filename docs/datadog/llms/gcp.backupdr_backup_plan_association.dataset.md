# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.backupdr_backup_plan_association.dataset.md

---
title: Backup and DR Backup Plan Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Backup and DR Backup Plan
  Association
---

# Backup and DR Backup Plan Association

Associates a backup plan with a specific resource in Google Cloud Backup and DR service. It defines which workloads or data sources are protected under a given backup plan, ensuring consistent backup scheduling, retention, and recovery policies. This association enables automated protection and centralized management of backup operations across Google Cloud environments.

```
gcp.backupdr_backup_plan_association
```

## Fields

| Title                                                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                      | Description |
| ----------------------------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                                  | core | string        |
| ancestors                                             | core | array<string> |
| backup_plan                                           | core | string        | Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId}                                                                                                                                                                                       |
| backup_plan_revision_id                               | core | string        | Output only. The user friendly revision ID of the `BackupPlanRevision`. Example: v0, v1, v2, etc.                                                                                                                                                                                                                                              |
| backup_plan_revision_name                             | core | string        | Output only. The resource id of the `BackupPlanRevision`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`                                                                                                                                                                                  |
| cloud_sql_instance_backup_plan_association_properties | core | json          | Output only. Cloud SQL instance's backup plan association properties.                                                                                                                                                                                                                                                                          |
| create_time                                           | core | timestamp     | Output only. The time when the instance was created.                                                                                                                                                                                                                                                                                           |
| data_source                                           | core | string        | Output only. Resource name of data source which will be used as storage location for backups taken. Format : projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}                                                                                                                                       |
| datadog_display_name                                  | core | string        |
| labels                                                | core | array<string> |
| name                                                  | core | string        | Output only. Identifier. The resource name of BackupPlanAssociation in below format Format : projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}                                                                                                                                                          |
| organization_id                                       | core | string        |
| parent                                                | core | string        |
| project_id                                            | core | string        |
| project_number                                        | core | string        |
| region_id                                             | core | string        |
| resource                                              | core | string        | Required. Immutable. Resource name of workload on which the backup plan is applied. The format can either be the resource name (e.g., "projects/my-project/zones/us-central1-a/instances/my-instance") or the full resource URI (e.g., "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance"). |
| resource_name                                         | core | string        |
| resource_type                                         | core | string        | Required. Immutable. Resource type of workload on which backupplan is applied                                                                                                                                                                                                                                                                  |
| rules_config_info                                     | core | json          | Output only. The config info related to backup rules.                                                                                                                                                                                                                                                                                          |
| state                                                 | core | string        | Output only. The BackupPlanAssociation resource state.                                                                                                                                                                                                                                                                                         |
| tags                                                  | core | hstore_csv    |
| update_time                                           | core | timestamp     | Output only. The time when the instance was updated.                                                                                                                                                                                                                                                                                           |
| zone_id                                               | core | string        |
