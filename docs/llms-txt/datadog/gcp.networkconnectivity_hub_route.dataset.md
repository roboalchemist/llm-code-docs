# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkconnectivity_hub_route.dataset.md

---
title: Hub Route
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Hub Route
---

# Hub Route

A Hub Route in Google Cloud is a network route resource within a Network Connectivity Center hub. It defines how traffic is directed between spokes or external networks connected to the hub. Hub Routes enable centralized routing control, allowing administrators to manage connectivity policies, route priorities, and next-hop targets across hybrid and multi-cloud environments.

```
gcp.networkconnectivity_hub_route
```

## Fields

| Title                              | ID   | Type          | Data Type                                                                                                                                                                                                                                        | Description |
| ---------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                               | core | string        |
| ancestors                          | core | array<string> |
| create_time                        | core | timestamp     | Output only. The time the route was created.                                                                                                                                                                                                     |
| datadog_display_name               | core | string        |
| description                        | core | string        | An optional description of the route.                                                                                                                                                                                                            |
| ip_cidr_range                      | core | string        | The destination IP address range.                                                                                                                                                                                                                |
| labels                             | core | array<string> | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).                                                |
| location                           | core | string        | Output only. The origin location of the route. Uses the following form: "projects/{project}/locations/{location}" Example: projects/1234/locations/us-central1                                                                                   |
| name                               | core | string        | Immutable. The name of the route. Route names must be unique. Route names use the following form: `projects/{project_number}/locations/global/hubs/{hub}/routeTables/{route_table_id}/routes/{route_id}`                                         |
| next_hop_interconnect_attachment   | core | json          | Immutable. The next-hop VLAN attachment for packets on this route.                                                                                                                                                                               |
| next_hop_router_appliance_instance | core | json          | Immutable. The next-hop Router appliance instance for packets on this route.                                                                                                                                                                     |
| next_hop_vpc_network               | core | json          | Immutable. The destination VPC network for packets on this route.                                                                                                                                                                                |
| next_hop_vpn_tunnel                | core | json          | Immutable. The next-hop VPN tunnel for packets on this route.                                                                                                                                                                                    |
| organization_id                    | core | string        |
| parent                             | core | string        |
| priority                           | core | int64         | Output only. The priority of this route. Priority is used to break ties in cases where a destination matches more than one route. In these cases the route with the lowest-numbered priority value wins.                                         |
| project_id                         | core | string        |
| project_number                     | core | string        |
| region_id                          | core | string        |
| resource_name                      | core | string        |
| spoke                              | core | string        | Immutable. The spoke that this route leads to. Example: projects/12345/locations/global/spokes/SPOKE                                                                                                                                             |
| state                              | core | string        | Output only. The current lifecycle state of the route.                                                                                                                                                                                           |
| tags                               | core | hstore_csv    |
| type                               | core | string        | Output only. The route's type. Its type is determined by the properties of its IP address range.                                                                                                                                                 |
| uid                                | core | string        | Output only. The Google-generated UUID for the route. This value is unique across all Network Connectivity Center route resources. If a route is deleted and another with the same name is created, the new route is assigned a different `uid`. |
| update_time                        | core | timestamp     | Output only. The time the route was last updated.                                                                                                                                                                                                |
| zone_id                            | core | string        |
