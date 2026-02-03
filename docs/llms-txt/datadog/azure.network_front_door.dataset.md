# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_front_door.dataset.md

---
title: Network Front Door
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Front Door
---

# Network Front Door

This table represents the Network Front Door resource from Microsoft Azure.

```
azure.network_front_door
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                        | Description |
| ----------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------ | ----------- |
| _key                    | core | string     |
| backend_pools           | core | json       | Backend pools available to routing rules.                                                        |
| backend_pools_settings  | core | json       | Settings for all backendPools                                                                    |
| cname                   | core | string     | The host that each frontendEndpoint must CNAME to.                                               |
| enabled_state           | core | string     | Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled' |
| friendly_name           | core | string     | A friendly name for the frontDoor                                                                |
| frontdoor_id            | core | string     | The Id of the frontdoor.                                                                         |
| frontend_endpoints      | core | json       | Frontend endpoints available to routing rules.                                                   |
| health_probe_settings   | core | json       | Health probe settings associated with this Front Door instance.                                  |
| id                      | core | string     | Resource ID.                                                                                     |
| load_balancing_settings | core | json       | Load balancing settings associated with this Front Door instance.                                |
| location                | core | string     | Resource location.                                                                               |
| name                    | core | string     | Resource name.                                                                                   |
| provisioning_state      | core | string     | Provisioning state of the Front Door.                                                            |
| resource_group          | core | string     |
| resource_state          | core | string     | Resource status of the Front Door.                                                               |
| routing_rules           | core | json       | Routing rules associated with this Front Door.                                                   |
| rules_engines           | core | json       | Rules Engine Configurations available to routing rules.                                          |
| subscription_id         | core | string     |
| subscription_name       | core | string     |
| tags                    | core | hstore_csv |
| type                    | core | string     | Resource type.                                                                                   |
