# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_vpn_gateway.dataset.md

---
title: Cloud VPN Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud VPN Gateway
---

# Cloud VPN Gateway

Cloud VPN Gateway in Google Cloud is a virtual gateway that securely connects your on-premises network to your Virtual Private Cloud (VPC) using encrypted IPsec tunnels. It enables private communication between environments over the public internet, ensuring data confidentiality and integrity. This resource is typically used for hybrid cloud or multi-cloud setups where secure connectivity is required.

```
gcp.compute_vpn_gateway
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| creation_timestamp   | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| gateway_ip_version   | core | string        | The IP family of the gateway IPs for the HA-VPN gateway interfaces. If not specified, IPV4 will be used.                                                                                                                                                                                                                                                                                                                                            |
| id                   | core | string        | Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                        |
| kind                 | core | string        | Output only. [Output Only] Type of resource. Always compute#vpnGateway for VPN gateways.                                                                                                                                                                                                                                                                                                                                                            |
| labels               | core | array<string> | Labels for this resource. These can only be added or modified by thesetLabels method. Each label key/value pair must comply withRFC1035. Label values may be empty.                                                                                                                                                                                                                                                                                 |
| name                 | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| network              | core | string        | URL of the network to which this VPN gateway is attached. Provided by the client when the VPN gateway is created.                                                                                                                                                                                                                                                                                                                                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region               | core | string        | Output only. [Output Only] URL of the region where the VPN gateway resides.                                                                                                                                                                                                                                                                                                                                                                         |
| region_id            | core | string        |
| resource_name        | core | string        |
| self_link            | core | string        | Output only. [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                     |
| stack_type           | core | string        | The stack type for this VPN gateway to identify the IP protocols that are enabled. Possible values are: IPV4_ONLY,IPV4_IPV6, IPV6_ONLY. If not specified,IPV4_ONLY is used if the gateway IP version isIPV4, or IPV4_IPV6 if the gateway IP version isIPV6.                                                                                                                                                                                         |
| tags                 | core | hstore_csv    |
| vpn_interfaces       | core | json          | The list of VPN interfaces associated with this VPN gateway.                                                                                                                                                                                                                                                                                                                                                                                        |
| zone_id              | core | string        |
