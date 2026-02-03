# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_vnet.dataset.md

---
title: Network VNET
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network VNET
---

# Network VNET

This table represents the Network VNET resource from Microsoft Azure.

```
azure.network_vnet
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                        | Description |
| ----------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| address_space           | core | json       | The AddressSpace that contains an array of IP address ranges that can be used by subnets.                                                                        |
| bgp_communities         | core | json       | Bgp Communities sent over ExpressRoute with each route corresponding to a prefix in this VNET.                                                                   |
| dhcp_options            | core | json       | The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network.                                                          |
| enable_ddos_protection  | core | bool       | Indicates if DDoS protection is enabled for all the protected resources in the virtual network. It requires a DDoS protection plan associated with the resource. |
| enable_vm_protection    | core | bool       | Indicates if VM protection is enabled for all the subnets in the virtual network.                                                                                |
| encryption              | core | json       | Indicates if encryption is enabled on virtual network and if VM without encryption is allowed in encrypted VNet.                                                 |
| etag                    | core | string     | A unique read-only string that changes whenever the resource is updated.                                                                                         |
| extended_location       | core | json       | The extended location of the virtual network.                                                                                                                    |
| flow_timeout_in_minutes | core | int64      | The FlowTimeout value (in minutes) for the Virtual Network                                                                                                       |
| id                      | core | string     | Resource ID.                                                                                                                                                     |
| location                | core | string     | Resource location.                                                                                                                                               |
| name                    | core | string     | Resource name.                                                                                                                                                   |
| provisioning_state      | core | string     | The provisioning state of the virtual network resource.                                                                                                          |
| resource_group          | core | string     |
| resource_guid           | core | string     | The resourceGuid property of the Virtual Network resource.                                                                                                       |
| subscription_id         | core | string     |
| subscription_name       | core | string     |
| tags                    | core | hstore_csv |
| type                    | core | string     | Resource type.                                                                                                                                                   |
