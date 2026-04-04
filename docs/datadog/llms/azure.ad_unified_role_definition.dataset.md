# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.ad_unified_role_definition.dataset.md

---
title: Active Directory Unified Role Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Active Directory Unified Role
  Definition
---

# Active Directory Unified Role Definition

This table represents the Active Directory Unified Role Definition resource from Microsoft Azure.

```
azure.ad_unified_role_definition
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                             | Description |
| ------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| description               | core | string        | The description for the unifiedRoleDefinition. Read-only when isBuiltIn is true.                                                                                                                                      |
| id                        | core | string        | The unique identifier for an entity. Read-only.                                                                                                                                                                       |
| inherits_permissions_from | core | json          | Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.                              |
| is_built_in               | core | bool          | Flag indicating whether the role definition is part of the default set included in Microsoft Entra or a custom definition. Read-only. Supports $filter (eq, in).                                                      |
| is_enabled                | core | bool          | Flag indicating whether the role is enabled for assignment. If false the role is not available for assignment. Read-only when isBuiltIn is true.                                                                      |
| location                  | core | string        |
| name                      | core | string        |
| resource_group            | core | string        |
| resource_scopes           | core | array<string> | List of the scopes or permissions the role definition applies to. Currently only / is supported. Read-only when isBuiltIn is true. DO NOT USE. This will be deprecated soon. Attach scope to role assignment.         |
| role_permissions          | core | json          | List of permissions included in the role. Read-only when isBuiltIn is true. Required.                                                                                                                                 |
| subscription_id           | core | string        |
| subscription_name         | core | string        |
| tags                      | core | hstore_csv    |
| template_id               | core | string        | Custom template identifier that can be set when isBuiltIn is false but is read-only when isBuiltIn is true. This identifier is typically used if one needs an identifier to be the same across different directories. |
| version                   | core | string        | Indicates version of the role definition. Read-only when isBuiltIn is true.                                                                                                                                           |
