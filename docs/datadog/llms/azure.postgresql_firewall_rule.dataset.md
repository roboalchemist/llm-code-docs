# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.postgresql_firewall_rule.dataset.md

---
title: PostgreSQL Firewall Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > PostgreSQL Firewall Rule
---

# PostgreSQL Firewall Rule

This table represents the PostgreSQL Firewall Rule resource from Microsoft Azure.

```
azure.postgresql_firewall_rule
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| end_ip_address    | core | string     | The end IP address of the server firewall rule. Must be IPv4 format.                                                                                                                      |
| id                | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| location          | core | string     |
| name              | core | string     | The name of the resource                                                                                                                                                                  |
| resource_group    | core | string     |
| start_ip_address  | core | string     | The start IP address of the server firewall rule. Must be IPv4 format.                                                                                                                    |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| type              | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
