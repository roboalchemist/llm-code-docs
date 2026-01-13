# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_local_gateway_virtual_interface.dataset.md

---
title: EC2 Local Gateway Virtual Interface
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Local Gateway Virtual Interface
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_local_gateway_virtual_interface.dataset/index.html
---

# EC2 Local Gateway Virtual Interface

An EC2 Local Gateway Virtual Interface is a resource that enables communication between an on-premises network and Amazon VPCs through a local gateway. It provides a virtual interface for routing traffic between your data center and VPC resources when using AWS Outposts, allowing low-latency connectivity and integration with local network infrastructure.

```
aws.ec2_local_gateway_virtual_interface
```

## Fields

| Title                              | ID   | Type   | Data Type                                                                                | Description |
| ---------------------------------- | ---- | ------ | ---------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string |
| account_id                         | core | string |
| local_address                      | core | string | The local address.                                                                       |
| local_bgp_asn                      | core | int64  | The Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the local gateway.   |
| local_gateway_id                   | core | string | The ID of the local gateway.                                                             |
| local_gateway_virtual_interface_id | core | string | The ID of the virtual interface.                                                         |
| owner_id                           | core | string | The ID of the Amazon Web Services account that owns the local gateway virtual interface. |
| peer_address                       | core | string | The peer address.                                                                        |
| peer_bgp_asn                       | core | int64  | The peer BGP ASN.                                                                        |
| tags                               | core | hstore |
| vlan                               | core | int64  | The ID of the VLAN.                                                                      |
