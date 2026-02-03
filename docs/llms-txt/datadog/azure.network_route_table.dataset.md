# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_route_table.dataset.md

---
title: Route Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Route Table
---

# Route Table

A Route Table in Azure is a networking resource that defines how traffic is directed within a virtual network. It contains user-defined routes that control the flow of network traffic, allowing customization beyond the system default routes. By associating a route table with subnets, you can manage traffic paths, enforce security boundaries, and direct traffic through network appliances such as firewalls or gateways.

```
azure.network_route_table
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                             | Description |
| ----------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| disable_bgp_route_propagation | core | bool       | Whether to disable the routes learned by BGP on that route table. True means disable. |
| etag                          | core | string     | A unique read-only string that changes whenever the resource is updated.              |
| id                            | core | string     | Resource ID.                                                                          |
| location                      | core | string     | Resource location.                                                                    |
| name                          | core | string     | Resource name.                                                                        |
| provisioning_state            | core | string     | The current provisioning state.                                                       |
| resource_group                | core | string     |
| resource_guid                 | core | string     | The resource GUID property of the route table.                                        |
| routes                        | core | json       | Collection of routes contained within a route table.                                  |
| subscription_id               | core | string     |
| subscription_name             | core | string     |
| tags                          | core | hstore_csv |
| type                          | core | string     | Resource type.                                                                        |
