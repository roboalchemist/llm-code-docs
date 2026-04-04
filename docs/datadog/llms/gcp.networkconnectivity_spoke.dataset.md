# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkconnectivity_spoke.dataset.md

---
title: Spoke
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Spoke
---

# Spoke

A Spoke in Google Cloud is a network resource used within the Network Connectivity Center. It represents a connection between a hub and various network resources such as VPN tunnels, VLAN attachments, or router appliance instances. Spokes simplify the management of large-scale network topologies by centralizing connectivity through a hub-and-spoke model, improving visibility and control over hybrid and multi-cloud networks.

```
gcp.networkconnectivity_spoke
```

## Fields

| Title                             | ID   | Type          | Data Type                                                                                                                                                                                                                  | Description |
| --------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string        |
| ancestors                         | core | array<string> |
| create_time                       | core | timestamp     | Output only. The time the spoke was created.                                                                                                                                                                               |
| datadog_display_name              | core | string        |
| description                       | core | string        | Optional. An optional description of the spoke.                                                                                                                                                                            |
| etag                              | core | string        | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.                        |
| field_paths_pending_update        | core | array<string> | Optional. The list of fields waiting for hub administration's approval.                                                                                                                                                    |
| group                             | core | string        | Optional. The name of the group that this spoke is associated with.                                                                                                                                                        |
| hub                               | core | string        | Immutable. The name of the hub that this spoke is attached to.                                                                                                                                                             |
| labels                            | core | array<string> | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).                          |
| linked_interconnect_attachments   | core | json          | Optional. VLAN attachments that are associated with the spoke.                                                                                                                                                             |
| linked_producer_vpc_network       | core | json          | Optional. The linked producer VPC that is associated with the spoke.                                                                                                                                                       |
| linked_router_appliance_instances | core | json          | Optional. Router appliance instances that are associated with the spoke.                                                                                                                                                   |
| linked_vpc_network                | core | json          | Optional. VPC network that is associated with the spoke.                                                                                                                                                                   |
| linked_vpn_tunnels                | core | json          | Optional. VPN tunnels that are associated with the spoke.                                                                                                                                                                  |
| name                              | core | string        | Immutable. The name of the spoke. Spoke names must be unique. They use the following form: `projects/{project_number}/locations/{region}/spokes/{spoke_id}`                                                                |
| organization_id                   | core | string        |
| parent                            | core | string        |
| project_id                        | core | string        |
| project_number                    | core | string        |
| reasons                           | core | json          | Output only. The reasons for current state of the spoke.                                                                                                                                                                   |
| region_id                         | core | string        |
| resource_name                     | core | string        |
| spoke_type                        | core | string        | Output only. The type of resource associated with the spoke.                                                                                                                                                               |
| state                             | core | string        | Output only. The current lifecycle state of this spoke.                                                                                                                                                                    |
| tags                              | core | hstore_csv    |
| unique_id                         | core | string        | Output only. The Google-generated UUID for the spoke. This value is unique across all spoke resources. If a spoke is deleted and another with the same name is created, the new spoke is assigned a different `unique_id`. |
| update_time                       | core | timestamp     | Output only. The time the spoke was last updated.                                                                                                                                                                          |
| zone_id                           | core | string        |
