# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.virtual_network_gateway.dataset.md

---
title: Virtual Network Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Virtual Network Gateway
---

# Virtual Network Gateway

This table represents the Virtual Network Gateway resource from Microsoft Azure.

```
azure.virtual_network_gateway
```

## Fields

| Title                                 | ID   | Type       | Data Type                                                                                                                                                                         | Description |
| ------------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string     |
| active_active                         | core | bool       | ActiveActive flag.                                                                                                                                                                |
| admin_state                           | core | string     | Property to indicate if the Express Route Gateway serves traffic when there are multiple Express Route Gateways in the vnet                                                       |
| allow_remote_vnet_traffic             | core | bool       | Configure this gateway to accept traffic from other Azure Virtual Networks. This configuration does not support connectivity to Azure Virtual WAN.                                |
| allow_virtual_wan_traffic             | core | bool       | Configures this gateway to accept traffic from remote Virtual WAN networks.                                                                                                       |
| auto_scale_configuration              | core | json       | Autoscale configuration for virutal network gateway                                                                                                                               |
| bgp_settings                          | core | json       | Virtual network gateway's BGP speaker settings.                                                                                                                                   |
| custom_routes                         | core | json       | The reference to the address space resource which represents the custom routes address space specified by the customer for virtual network gateway and VpnClient.                 |
| disable_ip_sec_replay_protection      | core | bool       | disableIPSecReplayProtection flag.                                                                                                                                                |
| enable_bgp                            | core | bool       | Whether BGP is enabled for this virtual network gateway or not.                                                                                                                   |
| enable_bgp_route_translation_for_nat  | core | bool       | EnableBgpRouteTranslationForNat flag.                                                                                                                                             |
| enable_dns_forwarding                 | core | bool       | Whether dns forwarding is enabled or not.                                                                                                                                         |
| enable_private_ip_address             | core | bool       | Whether private IP needs to be enabled on this gateway for connections or not.                                                                                                    |
| etag                                  | core | string     | A unique read-only string that changes whenever the resource is updated.                                                                                                          |
| extended_location                     | core | json       | The extended location of type local virtual network gateway.                                                                                                                      |
| gateway_default_site                  | core | json       | The reference to the LocalNetworkGateway resource which represents local network site having default routes. Assign Null value in case of removing existing default site setting. |
| gateway_type                          | core | string     | The type of this virtual network gateway.                                                                                                                                         |
| id                                    | core | string     | Resource ID.                                                                                                                                                                      |
| inbound_dns_forwarding_endpoint       | core | string     | The IP address allocated by the gateway to which dns requests can be sent.                                                                                                        |
| ip_configurations                     | core | json       | IP configurations for virtual network gateway.                                                                                                                                    |
| location                              | core | string     | Resource location.                                                                                                                                                                |
| name                                  | core | string     | Resource name.                                                                                                                                                                    |
| nat_rules                             | core | json       | NatRules for virtual network gateway.                                                                                                                                             |
| provisioning_state                    | core | string     | The provisioning state of the virtual network gateway resource.                                                                                                                   |
| resource_group                        | core | string     |
| resource_guid                         | core | string     | The resource GUID property of the virtual network gateway resource.                                                                                                               |
| sku                                   | core | json       | The reference to the VirtualNetworkGatewaySku resource which represents the SKU selected for Virtual network gateway.                                                             |
| subscription_id                       | core | string     |
| subscription_name                     | core | string     |
| tags                                  | core | hstore_csv |
| type                                  | core | string     | Resource type.                                                                                                                                                                    |
| v_net_extended_location_resource_id   | core | string     | Customer vnet resource id. VirtualNetworkGateway of type local gateway is associated with the customer vnet.                                                                      |
| virtual_network_gateway_policy_groups | core | json       | The reference to the VirtualNetworkGatewayPolicyGroup resource which represents the available VirtualNetworkGatewayPolicyGroup for the gateway.                                   |
| vpn_client_configuration              | core | json       | The reference to the VpnClientConfiguration resource which represents the P2S VpnClient configurations.                                                                           |
| vpn_gateway_generation                | core | string     | The generation for this VirtualNetworkGateway. Must be None if gatewayType is not VPN.                                                                                            |
| vpn_type                              | core | string     | The type of this virtual network gateway.                                                                                                                                         |
