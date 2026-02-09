# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.policy_assignment.dataset.md

---
title: Policy Assignment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Policy Assignment
---

# Policy Assignment

This table represents the Policy Assignment resource from Microsoft Azure.

```
azure.policy_assignment
```

## Fields

| Title                | ID   | Type          | Data Type                                                                             | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| description          | core | string        | This message will be part of response in case of policy violation.                    |
| enforcement_mode     | core | string        | The policy assignment enforcement mode. Possible values are Default and DoNotEnforce. |
| id                   | core | string        | The ID of the policy assignment.                                                      |
| identity             | core | json          | The managed identity associated with the policy assignment.                           |
| location             | core | string        | The location of the policy assignment. Only required when utilizing managed identity. |
| name                 | core | string        | The name of the policy assignment.                                                    |
| not_scopes           | core | array<string> | The policy's excluded scopes.                                                         |
| parameters           | core | hstore        | The parameter values for the assigned policy rule. The keys are the parameter names.  |
| policy_definition_id | core | string        | The ID of the policy definition or policy set definition being assigned.              |
| resource_group       | core | string        |
| scope                | core | string        | The scope for the policy assignment.                                                  |
| subscription_id      | core | string        |
| subscription_name    | core | string        |
| tags                 | core | hstore_csv    |
| type                 | core | string        | The type of the policy assignment.                                                    |
