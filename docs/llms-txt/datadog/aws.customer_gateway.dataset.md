# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.customer_gateway.dataset.md

---
title: Customer Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Customer Gateway
---

# Customer Gateway

This table represents the Customer Gateway resource from Amazon Web Services.

```
aws.customer_gateway
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                | Description |
| -------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| bgp_asn              | core | string     | The customer gateway device's Border Gateway Protocol (BGP) Autonomous System Number (ASN). Valid values: <code>1</code> to <code>2,147,483,647</code>                                                                                                                                                                                                                   |
| bgp_asn_extended     | core | string     | The customer gateway device's Border Gateway Protocol (BGP) Autonomous System Number (ASN). Valid values: <code>2,147,483,648</code> to <code>4,294,967,295</code>                                                                                                                                                                                                       |
| certificate_arn      | core | string     | The Amazon Resource Name (ARN) for the customer gateway certificate.                                                                                                                                                                                                                                                                                                     |
| customer_gateway_arn | core | string     |
| customer_gateway_id  | core | string     | The ID of the customer gateway.                                                                                                                                                                                                                                                                                                                                          |
| device_name          | core | string     | The name of customer gateway device.                                                                                                                                                                                                                                                                                                                                     |
| ip_address           | core | string     | IPv4 address for the customer gateway device's outside interface. The address must be static. If <code>OutsideIpAddressType</code> in your VPN connection options is set to <code>PrivateIpv4</code>, you can use an RFC6598 or RFC1918 private IPv4 address. If <code>OutsideIpAddressType</code> is set to <code>PublicIpv4</code>, you can use a public IPv4 address. |
| state                | core | string     | The current state of the customer gateway (<code>pending | available | deleting | deleted</code>).                                                                                                                                                                                                                                                                       |
| tags                 | core | hstore_csv |
| type                 | core | string     | The type of VPN connection the customer gateway supports (<code>ipsec.1</code>).                                                                                                                                                                                                                                                                                         |
