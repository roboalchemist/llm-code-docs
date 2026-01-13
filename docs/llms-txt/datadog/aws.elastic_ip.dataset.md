# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elastic_ip.dataset.md

---
title: Elastic IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elastic IP
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.elastic_ip.dataset/index.html
---

# Elastic IP

This table represents the Elastic IP resource from Amazon Web Services.

```
aws.elastic_ip
```

## Fields

| Title                      | ID   | Type   | Data Type                                                                                                                                                            | Description |
| -------------------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string |
| account_id                 | core | string |
| allocation_id              | core | string | The ID representing the allocation of the address.                                                                                                                   |
| association_id             | core | string | The ID representing the association of the address with an instance.                                                                                                 |
| carrier_ip                 | core | string | The carrier IP address associated. This option is only available for network interfaces which reside in a subnet in a Wavelength Zone (for example an EC2 instance). |
| customer_owned_ip          | core | string | The customer-owned IP address.                                                                                                                                       |
| customer_owned_ipv4_pool   | core | string | The ID of the customer-owned address pool.                                                                                                                           |
| domain                     | core | string | The network (<code>vpc</code>).                                                                                                                                      |
| elastic_ip_arn             | core | string |
| instance_id                | core | string | The ID of the instance that the address is associated with (if any).                                                                                                 |
| network_border_group       | core | string | The name of the unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.                           |
| network_interface_id       | core | string | The ID of the network interface.                                                                                                                                     |
| network_interface_owner_id | core | string | The ID of the Amazon Web Services account that owns the network interface.                                                                                           |
| private_ip_address         | core | string | The private IP address associated with the Elastic IP address.                                                                                                       |
| public_ip                  | core | string | The Elastic IP address.                                                                                                                                              |
| public_ipv4_pool           | core | string | The ID of an address pool.                                                                                                                                           |
| tags                       | core | hstore |
