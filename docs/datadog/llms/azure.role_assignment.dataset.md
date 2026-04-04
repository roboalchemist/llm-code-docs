# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.role_assignment.dataset.md

---
title: Role Assignment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Role Assignment
---

# Role Assignment

This table represents the Role Assignment resource from Microsoft Azure.

```
azure.role_assignment
```

## Fields

| Title                                  | ID   | Type       | Data Type                                                                                                                                                                                                                       | Description |
| -------------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                   | core | string     |
| condition                              | core | string     | The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container' |
| condition_version                      | core | string     | Version of the condition. Currently the only accepted value is '2.0'                                                                                                                                                            |
| created_by                             | core | string     | Id of the user who created the assignment                                                                                                                                                                                       |
| created_on                             | core | string     | Time it was created                                                                                                                                                                                                             |
| delegated_managed_identity_resource_id | core | string     | Id of the delegated managed identity resource                                                                                                                                                                                   |
| description                            | core | string     | Description of role assignment                                                                                                                                                                                                  |
| id                                     | core | string     | The role assignment ID.                                                                                                                                                                                                         |
| location                               | core | string     |
| name                                   | core | string     | The role assignment name.                                                                                                                                                                                                       |
| principal_id                           | core | string     | The principal ID.                                                                                                                                                                                                               |
| principal_type                         | core | string     | The principal type of the assigned principal ID.                                                                                                                                                                                |
| resource_group                         | core | string     |
| role_definition_id                     | core | string     | The role definition ID.                                                                                                                                                                                                         |
| scope                                  | core | string     | The role assignment scope.                                                                                                                                                                                                      |
| subscription_id                        | core | string     |
| subscription_name                      | core | string     |
| tags                                   | core | hstore_csv |
| type                                   | core | string     | The role assignment type.                                                                                                                                                                                                       |
| updated_by                             | core | string     | Id of the user who updated the assignment                                                                                                                                                                                       |
| updated_on                             | core | string     | Time it was updated                                                                                                                                                                                                             |
