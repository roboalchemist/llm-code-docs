# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_target_vpn_gateway.dataset.md

---
title: Target VPN Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Target VPN Gateway
---

# Target VPN Gateway

A Target VPN Gateway in Google Cloud is a regional resource that represents the VPN endpoint on the Google Cloud side of a Classic VPN connection. It is used to establish secure IPsec tunnels between your Virtual Private Cloud (VPC) network and an external network, such as an on-premises data center.

```
gcp.compute_target_vpn_gateway
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| creation_timestamp   | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| forwarding_rules     | core | array<string> | [Output Only] A list of URLs to the ForwardingRule resources. ForwardingRules are created usingcompute.forwardingRules.insert and associated with a VPN gateway.                                                                                                                                                                                                                                                                                    |
| gcp_status           | core | string        | [Output Only] The status of the VPN gateway, which can be one of the following: CREATING, READY, FAILED, or DELETING. Possible values: ['CREATING', 'DELETING', 'FAILED', 'READY']. Values descriptions: ['', '', '', '']                                                                                                                                                                                                                           |
| id                   | core | string        | [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                                     |
| kind                 | core | string        | Output only. [Output Only] Type of resource. Alwayscompute#targetVpnGateway for target VPN gateways.                                                                                                                                                                                                                                                                                                                                                |
| labels               | core | array<string> | Labels for this resource. These can only be added or modified by thesetLabels method. Each label key/value pair must comply withRFC1035. Label values may be empty.                                                                                                                                                                                                                                                                                 |
| name                 | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| network              | core | string        | URL of the network to which this VPN gateway is attached. Provided by the client when the VPN gateway is created.                                                                                                                                                                                                                                                                                                                                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region               | core | string        | [Output Only] URL of the region where the target VPN gateway resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.                                                                                                                                                                                                                                                               |
| region_id            | core | string        |
| resource_name        | core | string        |
| self_link            | core | string        | [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags                 | core | hstore_csv    |
| tunnels              | core | array<string> | [Output Only] A list of URLs to VpnTunnel resources. VpnTunnels are created using the compute.vpntunnels.insert method and associated with a VPN gateway.                                                                                                                                                                                                                                                                                           |
| zone_id              | core | string        |
