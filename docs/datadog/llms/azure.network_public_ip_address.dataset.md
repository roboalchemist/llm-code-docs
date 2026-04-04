# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_public_ip_address.dataset.md

---
title: Public IP Address
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Public IP Address
---

# Public IP Address

A Public IP Address in Azure is a resource that allows Azure services, such as virtual machines, load balancers, or application gateways, to communicate with the internet or external networks. It provides a unique, routable IP address that can be static or dynamic, and supports both IPv4 and IPv6. Public IPs are often used to enable inbound and outbound connectivity, DNS name resolution, and secure access to applications.

```
azure.network_public_ip_address
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                   | Description |
| --------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| ddos_settings               | core | json          | Contains the DDoS protection settings of the public IP.                                     |
| delete_option               | core | string        | Specify what happens to the public IP address when the VM using it is deleted               |
| dns_settings                | core | json          | Contains FQDN of the DNS record associated with the public IP address.                      |
| etag                        | core | string        | A unique read-only string that changes whenever the resource is updated.                    |
| extended_location           | core | json          | ExtendedLocation complex type.                                                              |
| id                          | core | string        | Resource ID.                                                                                |
| idle_timeout_in_minutes     | core | int64         | The idle timeout of the public IP address.                                                  |
| ip_address                  | core | string        | The IP address associated with the public IP address resource.                              |
| ip_tags                     | core | json          | The list of tags associated with the public IP address.                                     |
| location                    | core | string        | Resource location.                                                                          |
| migration_phase             | core | string        | Migration phase of Public IP Address.                                                       |
| name                        | core | string        | Resource name.                                                                              |
| nat_gateway                 | core | json          | Nat Gateway resource.                                                                       |
| provisioning_state          | core | string        | The current provisioning state.                                                             |
| public_ip_address_version   | core | string        | IP address version.                                                                         |
| public_ip_allocation_method | core | string        | IP address allocation method.                                                               |
| resource_group              | core | string        |
| resource_guid               | core | string        | The resource GUID property of the public IP address resource.                               |
| sku                         | core | json          | SKU of a public IP address.                                                                 |
| subscription_id             | core | string        |
| subscription_name           | core | string        |
| tags                        | core | hstore_csv    |
| type                        | core | string        | Resource type.                                                                              |
| zones                       | core | array<string> | A list of availability zones denoting the IP allocated for the resource needs to come from. |
