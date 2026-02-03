# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.authorization_role_assignment_schedule_instance.dataset.md

---
title: Role Assignment Schedule Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Role Assignment Schedule Instance
---

# Role Assignment Schedule Instance

Role Assignment Schedule Instance in Azure represents a specific occurrence of a role assignment that is governed by Privileged Identity Management (PIM). It defines when and how a role is active for a user or principal, including start and end times, scope, and eligibility. This resource helps manage just-in-time access and enforces least privilege by ensuring roles are only active when needed.

```
azure.authorization_role_assignment_schedule_instance
```

## Fields

| Title                                        | ID   | Type       | Data Type                                                                                                                                                                                                                       | Description |
| -------------------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                         | core | string     |
| assignment_type                              | core | string     | Assignment type of the role assignment schedule                                                                                                                                                                                 |
| condition                                    | core | string     | The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container' |
| condition_version                            | core | string     | Version of the condition. Currently accepted value is '2.0'                                                                                                                                                                     |
| created_on                                   | core | string     | DateTime when role assignment schedule was created                                                                                                                                                                              |
| end_date_time                                | core | string     | The endDateTime of the role assignment schedule instance                                                                                                                                                                        |
| expanded_properties                          | core | json       | Additional properties of principal, scope and role definition                                                                                                                                                                   |
| id                                           | core | string     | The role assignment schedule instance ID.                                                                                                                                                                                       |
| linked_role_eligibility_schedule_id          | core | string     | roleEligibilityScheduleId used to activate                                                                                                                                                                                      |
| linked_role_eligibility_schedule_instance_id | core | string     | roleEligibilityScheduleInstanceId linked to this roleAssignmentScheduleInstance                                                                                                                                                 |
| location                                     | core | string     |
| member_type                                  | core | string     | Membership type of the role assignment schedule                                                                                                                                                                                 |
| name                                         | core | string     | The role assignment schedule instance name.                                                                                                                                                                                     |
| origin_role_assignment_id                    | core | string     | Role Assignment Id in external system                                                                                                                                                                                           |
| principal_id                                 | core | string     | The principal ID.                                                                                                                                                                                                               |
| principal_type                               | core | string     | The principal type of the assigned principal ID.                                                                                                                                                                                |
| resource_group                               | core | string     |
| role_assignment_schedule_id                  | core | string     | Id of the master role assignment schedule                                                                                                                                                                                       |
| role_definition_id                           | core | string     | The role definition ID.                                                                                                                                                                                                         |
| scope                                        | core | string     | The role assignment schedule scope.                                                                                                                                                                                             |
| start_date_time                              | core | string     | The startDateTime of the role assignment schedule instance                                                                                                                                                                      |
| status                                       | core | string     | The status of the role assignment schedule instance.                                                                                                                                                                            |
| subscription_id                              | core | string     |
| subscription_name                            | core | string     |
| tags                                         | core | hstore_csv |
| type                                         | core | string     | The role assignment schedule instance type.                                                                                                                                                                                     |
