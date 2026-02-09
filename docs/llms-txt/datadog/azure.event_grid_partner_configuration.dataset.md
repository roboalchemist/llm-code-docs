# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.event_grid_partner_configuration.dataset.md

---
title: Event Grid Partner Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Event Grid Partner Configuration
---

# Event Grid Partner Configuration

This table represents the event_grid_partner_configuration resource from Microsoft Azure.

```
azure.event_grid_partner_configuration
```

## Fields

| Title                 | ID   | Type       | Data Type                                                       | Description |
| --------------------- | ---- | ---------- | --------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| id                    | core | string     | Fully qualified identifier of the resource.                     |
| location              | core | string     | Location of the resource.                                       |
| name                  | core | string     | Name of the resource.                                           |
| partner_authorization | core | json       | The details of authorized partners.                             |
| provisioning_state    | core | string     | Provisioning state of the partner configuration.                |
| resource_group        | core | string     |
| subscription_id       | core | string     |
| subscription_name     | core | string     |
| system_data           | core | json       | The system metadata relating to partner configuration resource. |
| tags                  | core | hstore_csv |
| type                  | core | string     | Type of the resource.                                           |
