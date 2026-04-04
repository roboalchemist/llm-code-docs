# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpn_connection.dataset.md

---
title: VPN Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPN Connection
---

# VPN Connection

This table represents the VPN Connection resource from Amazon Web Services.

```
aws.vpn_connection
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                     | Description |
| ------------------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| category                       | core | string     | The category of the VPN connection. A value of <code>VPN</code> indicates an Amazon Web Services VPN connection. A value of <code>VPN-Classic</code> indicates an Amazon Web Services Classic VPN connection.                                                                                                                                 |
| core_network_arn               | core | string     | The ARN of the core network.                                                                                                                                                                                                                                                                                                                  |
| core_network_attachment_arn    | core | string     | The ARN of the core network attachment.                                                                                                                                                                                                                                                                                                       |
| customer_gateway_configuration | core | string     | The configuration information for the VPN connection's customer gateway (in the native XML format). This element is always present in the <a>CreateVpnConnection</a> response; however, it's present in the <a>DescribeVpnConnections</a> response only if the VPN connection is in the <code>pending</code> or <code>available</code> state. |
| customer_gateway_id            | core | string     | The ID of the customer gateway at your end of the VPN connection.                                                                                                                                                                                                                                                                             |
| gateway_association_state      | core | string     | The current state of the gateway association.                                                                                                                                                                                                                                                                                                 |
| options                        | core | json       | The VPN connection options.                                                                                                                                                                                                                                                                                                                   |
| routes                         | core | json       | The static routes associated with the VPN connection.                                                                                                                                                                                                                                                                                         |
| state                          | core | string     | The current state of the VPN connection.                                                                                                                                                                                                                                                                                                      |
| tags                           | core | hstore_csv |
| transit_gateway_id             | core | string     | The ID of the transit gateway associated with the VPN connection.                                                                                                                                                                                                                                                                             |
| type                           | core | string     | The type of VPN connection.                                                                                                                                                                                                                                                                                                                   |
| vgw_telemetry                  | core | json       | Information about the VPN tunnel.                                                                                                                                                                                                                                                                                                             |
| vpn_connection_arn             | core | string     |
| vpn_connection_id              | core | string     | The ID of the VPN connection.                                                                                                                                                                                                                                                                                                                 |
| vpn_gateway_id                 | core | string     | The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection.                                                                                                                                                                                                                                                  |
