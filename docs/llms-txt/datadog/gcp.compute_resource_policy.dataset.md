# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_resource_policy.dataset.md

---
title: Compute Resource Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Compute Resource Policy
---

# Compute Resource Policy

A Compute Resource Policy in Google Cloud is a configuration that defines rules for managing compute resources such as VM instances and disks. It allows you to automate tasks like snapshot schedules, disk replication, and instance placement policies. By applying a resource policy, you can ensure consistent management of resources, improve availability, and simplify operational tasks.

```
gcp.compute_resource_policy
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ----------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                          | core | string        |
| ancestors                     | core | array<string> |
| creation_timestamp            | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                                     |
| datadog_display_name          | core | string        |
| description                   | core | string        |
| disk_consistency_group_policy | core | json          | Resource policy for disk consistency groups.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| gcp_status                    | core | string        | [Output Only] The status of resource policy creation. Possible values: ['CREATING', 'DELETING', 'EXPIRED', 'INVALID', 'READY']. Values descriptions: ['Resource policy is being created.', 'Resource policy is being deleted.', 'Resource policy is expired and will not run again.', '', 'Resource policy is ready to be used.']                                                                                                                                        |
| group_placement_policy        | core | json          | Resource policy for instances for placement configuration.                                                                                                                                                                                                                                                                                                                                                                                                               |
| id                            | core | string        | Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                                             |
| instance_schedule_policy      | core | json          | Resource policy for scheduling instance operations.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| kind                          | core | string        | Output only. [Output Only] Type of the resource. Alwayscompute#resource_policies for resource policies.                                                                                                                                                                                                                                                                                                                                                                  |
| labels                        | core | array<string> |
| name                          | core | string        | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id               | core | string        |
| parent                        | core | string        |
| project_id                    | core | string        |
| project_number                | core | string        |
| region                        | core | string        |
| region_id                     | core | string        |
| resource_name                 | core | string        |
| resource_status               | core | json          | Output only. [Output Only] The system status of the resource policy.                                                                                                                                                                                                                                                                                                                                                                                                     |
| self_link                     | core | string        | Output only. [Output Only] Server-defined fully-qualified URL for this resource.                                                                                                                                                                                                                                                                                                                                                                                         |
| snapshot_schedule_policy      | core | json          | Resource policy for persistent disks for creating snapshots.                                                                                                                                                                                                                                                                                                                                                                                                             |
| tags                          | core | hstore_csv    |
| zone_id                       | core | string        |
