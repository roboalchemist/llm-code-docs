# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.sql_firewall_rule.dataset.md

---
title: SQL Firewall Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SQL Firewall Rule
---

# SQL Firewall Rule

This table represents the SQL Firewall Rule resource from Microsoft Azure.

```
azure.sql_firewall_rule
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                               | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| end_ip_address    | core | string     | The end IP address of the firewall rule. Must be IPv4 format. Must be greater than or equal to startIpAddress. Use value '0.0.0.0' for all Azure-internal IP addresses. |
| id                | core | string     | Resource ID.                                                                                                                                                            |
| location          | core | string     |
| name              | core | string     | Resource name.                                                                                                                                                          |
| resource_group    | core | string     |
| start_ip_address  | core | string     | The start IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' for all Azure-internal IP addresses.                                                |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| type              | core | string     | Resource type.                                                                                                                                                          |
