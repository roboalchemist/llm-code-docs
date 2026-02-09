# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_private_endpoint.dataset.md

---
title: Private Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Private Endpoint
---

# Private Endpoint

A Private Endpoint in Azure is a network interface that securely connects you to an Azure service using a private IP address from your virtual network. This allows traffic between your virtual network and the service to travel entirely over the Microsoft backbone network, eliminating exposure to the public internet and enhancing security.

```
azure.network_private_endpoint
```

## Fields

| Title                                   | ID   | Type       | Data Type                                                                                                                                                              | Description |
| --------------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                    | core | string     |
| application_security_groups             | core | json       | Application security groups in which the private endpoint IP configuration is included.                                                                                |
| custom_dns_configs                      | core | json       | An array of custom dns configurations.                                                                                                                                 |
| custom_network_interface_name           | core | string     | The custom name of the network interface attached to the private endpoint.                                                                                             |
| etag                                    | core | string     | A unique read-only string that changes whenever the resource is updated.                                                                                               |
| extended_location                       | core | json       | ExtendedLocation complex type.                                                                                                                                         |
| id                                      | core | string     | Resource ID.                                                                                                                                                           |
| ip_configurations                       | core | json       | A list of IP configurations of the private endpoint. This will be used to map to the First Party Service's endpoints.                                                  |
| location                                | core | string     | Resource location.                                                                                                                                                     |
| manual_private_link_service_connections | core | json       | A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource. |
| name                                    | core | string     | Resource name.                                                                                                                                                         |
| network_interfaces                      | core | json       | An array of references to the network interfaces created for this private endpoint.                                                                                    |
| private_link_service_connections        | core | json       | A grouping of information about the connection to the remote resource.                                                                                                 |
| provisioning_state                      | core | string     | The current provisioning state.                                                                                                                                        |
| resource_group                          | core | string     |
| subnet                                  | core | json       | Subnet in a virtual network resource.                                                                                                                                  |
| subscription_id                         | core | string     |
| subscription_name                       | core | string     |
| tags                                    | core | hstore_csv |
| type                                    | core | string     | Resource type.                                                                                                                                                         |
