# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.authorization_role_eligibility_schedule_instance.dataset.md

---
title: Role Eligibility Schedule Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Role Eligibility Schedule Instance
---

# Role Eligibility Schedule Instance

A Role Eligibility Schedule Instance in Azure represents a specific assignment that makes a user or service principal eligible to activate a privileged role within Azure Active Directory. It is part of Privileged Identity Management (PIM) and defines when and how a user can become active in a role, including start and end times. This resource helps enforce just-in-time access, reducing standing privileges and improving security by ensuring elevated permissions are only available when needed.

```
azure.authorization_role_eligibility_schedule_instance
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                                                       | Description |
| ---------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| condition                    | core | string     | The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container' |
| condition_version            | core | string     | Version of the condition. Currently accepted value is '2.0'                                                                                                                                                                     |
| created_on                   | core | string     | DateTime when role eligibility schedule was created                                                                                                                                                                             |
| end_date_time                | core | string     | The endDateTime of the role eligibility schedule instance                                                                                                                                                                       |
| expanded_properties          | core | json       | Additional properties of principal, scope and role definition                                                                                                                                                                   |
| id                           | core | string     | The role eligibility schedule instance ID.                                                                                                                                                                                      |
| location                     | core | string     |
| member_type                  | core | string     | Membership type of the role eligibility schedule                                                                                                                                                                                |
| name                         | core | string     | The role eligibility schedule instance name.                                                                                                                                                                                    |
| principal_id                 | core | string     | The principal ID.                                                                                                                                                                                                               |
| principal_type               | core | string     | The principal type of the assigned principal ID.                                                                                                                                                                                |
| resource_group               | core | string     |
| role_definition_id           | core | string     | The role definition ID.                                                                                                                                                                                                         |
| role_eligibility_schedule_id | core | string     | Id of the master role eligibility schedule                                                                                                                                                                                      |
| scope                        | core | string     | The role eligibility schedule scope.                                                                                                                                                                                            |
| start_date_time              | core | string     | The startDateTime of the role eligibility schedule instance                                                                                                                                                                     |
| status                       | core | string     | The status of the role eligibility schedule instance                                                                                                                                                                            |
| subscription_id              | core | string     |
| subscription_name            | core | string     |
| tags                         | core | hstore_csv |
| type                         | core | string     | The role eligibility schedule instance type.                                                                                                                                                                                    |
