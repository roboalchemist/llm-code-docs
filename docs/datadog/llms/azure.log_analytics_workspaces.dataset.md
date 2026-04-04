# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.log_analytics_workspaces.dataset.md

---
title: Log Analytics Workspaces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Log Analytics Workspaces
---

# Log Analytics Workspaces

This table represents the Log Analytics Workspaces resource from Microsoft Azure.

```
azure.log_analytics_workspaces
```

## Fields

| Title                               | ID   | Type       | Data Type | Description |
| ----------------------------------- | ---- | ---------- | --------- | ----------- |
| _key                                | core | string     |
| created_date                        | core | string     |
| customer_id                         | core | string     |
| etag                                | core | string     |
| features                            | core | json       |
| force_cmk_for_query                 | core | bool       |
| id                                  | core | string     |
| location                            | core | string     |
| modified_date                       | core | string     |
| name                                | core | string     |
| private_link_scoped_resources       | core | json       |
| provisioning_state                  | core | string     |
| public_network_access_for_ingestion | core | string     |
| public_network_access_for_query     | core | string     |
| resource_group                      | core | string     |
| retention_in_days                   | core | int64      |
| sku                                 | core | json       |
| subscription_id                     | core | string     |
| subscription_name                   | core | string     |
| tags                                | core | hstore_csv |
| type                                | core | string     |
| workspace_capping                   | core | json       |
