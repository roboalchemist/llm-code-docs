# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_vnet_peering.dataset.md

---
title: Network VNET Peering
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network VNET Peering
---

# Network VNET Peering

This table represents the Network VNET Peering resource from Microsoft Azure.

```
azure.network_vnet_peering
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                               | Description |
| ------------------------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string     |
| allow_forwarded_traffic              | core | bool       | Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.                                                                                                                                                                                                           |
| allow_gateway_transit                | core | bool       | If gateway links can be used in remote virtual networking to link to this virtual network.                                                                                                                                                                                                                                              |
| allow_virtual_network_access         | core | bool       | Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.                                                                                                                                                                                                                     |
| do_not_verify_remote_gateways        | core | bool       | If we need to verify the provisioning state of the remote gateway.                                                                                                                                                                                                                                                                      |
| etag                                 | core | string     | A unique read-only string that changes whenever the resource is updated.                                                                                                                                                                                                                                                                |
| id                                   | core | string     | Resource ID.                                                                                                                                                                                                                                                                                                                            |
| location                             | core | string     |
| name                                 | core | string     | The name of the resource that is unique within a resource group. This name can be used to access the resource.                                                                                                                                                                                                                          |
| peering_state                        | core | string     | The status of the virtual network peering.                                                                                                                                                                                                                                                                                              |
| peering_sync_level                   | core | string     | The peering sync status of the virtual network peering.                                                                                                                                                                                                                                                                                 |
| provisioning_state                   | core | string     | The provisioning state of the virtual network peering resource.                                                                                                                                                                                                                                                                         |
| remote_address_space                 | core | json       | The reference to the address space peered with the remote virtual network.                                                                                                                                                                                                                                                              |
| remote_bgp_communities               | core | json       | The reference to the remote virtual network's Bgp Communities.                                                                                                                                                                                                                                                                          |
| remote_virtual_network               | core | json       | The reference to the remote virtual network. The remote virtual network can be in the same or different region (preview). See here to register for the preview and learn more (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering).                                                                  |
| remote_virtual_network_address_space | core | json       | The reference to the current address space of the remote virtual network.                                                                                                                                                                                                                                                               |
| remote_virtual_network_encryption    | core | json       | The reference to the remote virtual network's encryption                                                                                                                                                                                                                                                                                |
| resource_group                       | core | string     |
| resource_guid                        | core | string     | The resourceGuid property of the Virtual Network peering resource.                                                                                                                                                                                                                                                                      |
| subscription_id                      | core | string     |
| subscription_name                    | core | string     |
| tags                                 | core | hstore_csv |
| type                                 | core | string     | Resource type.                                                                                                                                                                                                                                                                                                                          |
| use_remote_gateways                  | core | bool       | If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway. |
