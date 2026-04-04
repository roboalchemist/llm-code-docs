# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.role_definition.dataset.md

---
title: Role Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Role Definition
---

# Role Definition

This table represents the Role Definition resource from Microsoft Azure.

```
azure.role_definition
```

## Fields

| Title             | ID   | Type          | Data Type                                 | Description |
| ----------------- | ---- | ------------- | ----------------------------------------- | ----------- |
| _key              | core | string        |
| assignable_scopes | core | array<string> | Role definition assignable scopes.        |
| created_by        | core | string        | Id of the user who created the assignment |
| created_on        | core | string        | Time it was created                       |
| description       | core | string        | The role definition description.          |
| id                | core | string        | The role definition ID.                   |
| location          | core | string        |
| name              | core | string        | The role definition name.                 |
| permissions       | core | json          | Role definition permissions.              |
| properties_type   | core | string        | The role type.                            |
| resource_group    | core | string        |
| role_name         | core | string        | The role name.                            |
| subscription_id   | core | string        |
| subscription_name | core | string        |
| tags              | core | hstore_csv    |
| type              | core | string        | The role definition type.                 |
| updated_by        | core | string        | Id of the user who updated the assignment |
| updated_on        | core | string        | Time it was updated                       |
