# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_watcher.dataset.md

---
title: Network Watcher
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Watcher
---

# Network Watcher

This table represents the Network Watcher resource from Microsoft Azure.

```
azure.network_watcher
```

## Fields

| Title              | ID   | Type       | Data Type                                                                | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| etag               | core | string     | A unique read-only string that changes whenever the resource is updated. |
| flow_logs          | core | json       |
| id                 | core | string     | Resource ID.                                                             |
| location           | core | string     | Resource location.                                                       |
| name               | core | string     | Resource name.                                                           |
| provisioning_state | core | string     | The provisioning state of the network watcher resource.                  |
| resource_group     | core | string     |
| subscription_id    | core | string     |
| subscription_name  | core | string     |
| tags               | core | hstore_csv |
| type               | core | string     | Resource type.                                                           |
