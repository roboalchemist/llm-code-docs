# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmmigration_migrating_vm.dataset.md

---
title: Migrating VM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Migrating VM
---

# Migrating VM

A Migrating VM in Google Cloud is a virtual machine that is in the process of being moved from one host or environment to another. This typically occurs during live migration, maintenance, or resource optimization. The VM continues running while its memory and state are transferred, minimizing downtime and ensuring workload continuity.

```
gcp.vmmigration_migrating_vm
```

## Fields

| Title                                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                        | Description |
| ------------------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                 | core | string        |
| ancestors                            | core | array<string> |
| aws_source_vm_details                | core | json          | Output only. Details of the VM from an AWS source.                                                                                                                                                                                                                                               |
| azure_source_vm_details              | core | json          | Output only. Details of the VM from an Azure source.                                                                                                                                                                                                                                             |
| compute_engine_disks_target_defaults | core | json          | Details of the target Persistent Disks in Compute Engine.                                                                                                                                                                                                                                        |
| compute_engine_target_defaults       | core | json          | Details of the target VM in Compute Engine.                                                                                                                                                                                                                                                      |
| create_time                          | core | timestamp     | Output only. The time the migrating VM was created (this refers to this resource and not to the time it was installed in the source).                                                                                                                                                            |
| current_sync_info                    | core | json          | Output only. Details of the current running replication cycle.                                                                                                                                                                                                                                   |
| cutover_forecast                     | core | json          | Output only. Provides details of future CutoverJobs of a MigratingVm. Set to empty when cutover forecast is unavailable.                                                                                                                                                                         |
| datadog_display_name                 | core | string        |
| description                          | core | string        | The description attached to the migrating VM by the user.                                                                                                                                                                                                                                        |
| error                                | core | json          | Output only. Provides details on the state of the Migrating VM in case of an error in replication.                                                                                                                                                                                               |
| gcp_display_name                     | core | string        | The display name attached to the MigratingVm by the user.                                                                                                                                                                                                                                        |
| group                                | core | string        | Output only. The group this migrating vm is included in, if any. The group is represented by the full path of the appropriate Group resource.                                                                                                                                                    |
| labels                               | core | array<string> | The labels of the migrating VM.                                                                                                                                                                                                                                                                  |
| last_replication_cycle               | core | json          | Output only. Details of the last replication cycle. This will be updated whenever a replication cycle is finished and is not to be confused with last_sync which is only updated on successful replication cycles.                                                                               |
| last_sync                            | core | json          | Output only. The most updated snapshot created time in the source that finished replication.                                                                                                                                                                                                     |
| name                                 | core | string        | Output only. The identifier of the MigratingVm.                                                                                                                                                                                                                                                  |
| organization_id                      | core | string        |
| parent                               | core | string        |
| policy                               | core | json          | The replication schedule policy.                                                                                                                                                                                                                                                                 |
| project_id                           | core | string        |
| project_number                       | core | string        |
| recent_clone_jobs                    | core | json          | Output only. The recent clone jobs performed on the migrating VM. This field holds the vm's last completed clone job and the vm's running clone job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request.       |
| recent_cutover_jobs                  | core | json          | Output only. The recent cutover jobs performed on the migrating VM. This field holds the vm's last completed cutover job and the vm's running cutover job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request. |
| region_id                            | core | string        |
| resource_name                        | core | string        |
| source_vm_id                         | core | string        | The unique ID of the VM in the source. The VM's name in vSphere can be changed, so this is not the VM's name but rather its moRef id. This id is of the form vm-.                                                                                                                                |
| state                                | core | string        | Output only. State of the MigratingVm.                                                                                                                                                                                                                                                           |
| state_time                           | core | timestamp     | Output only. The last time the migrating VM state was updated.                                                                                                                                                                                                                                   |
| tags                                 | core | hstore_csv    |
| update_time                          | core | timestamp     | Output only. The last time the migrating VM resource was updated.                                                                                                                                                                                                                                |
| vmware_source_vm_details             | core | json          | Output only. Details of the VM from a Vmware source.                                                                                                                                                                                                                                             |
| zone_id                              | core | string        |
