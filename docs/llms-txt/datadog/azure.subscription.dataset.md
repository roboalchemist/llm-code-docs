# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.subscription.dataset.md

---
title: Azure Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Azure Subscription
---

# Azure Subscription

An Azure Subscription is the fundamental unit for managing resources in Microsoft Azure. It defines a logical container that holds resources such as virtual machines, storage accounts, and databases. Each subscription has its own billing and access management boundaries, allowing organizations to separate workloads, environments, or departments. Subscriptions are tied to an Azure Active Directory tenant and can be governed with policies, role-based access control, and cost management tools.

```
azure.subscription
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                   | Description |
| --------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| authorization_source  | core | string     | The authorization source of the request. Valid values are one or more combinations of Legacy, RoleBased, Bypassed, Direct and Management. For example, 'Legacy, RoleBased'. |
| id                    | core | string     | The fully qualified ID for the subscription. For example, /subscriptions/8d65815f-a5b6-402f-9298-045155da7d74                                                               |
| location              | core | string     |
| managed_by_tenants    | core | json       | An array containing the tenants managing the subscription.                                                                                                                  |
| resource_group        | core | string     |
| state                 | core | string     | The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.                                                                                |
| subscription_id       | core | string     | The subscription ID.                                                                                                                                                        |
| subscription_name     | core | string     |
| subscription_policies | core | json       | Subscription policies.                                                                                                                                                      |
| tags                  | core | hstore_csv |
| tenant_id             | core | string     | The subscription tenant ID.                                                                                                                                                 |
