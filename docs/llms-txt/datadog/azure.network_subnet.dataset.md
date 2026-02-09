# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_subnet.dataset.md

---
title: Subnet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Subnet
---

# Subnet

A Subnet in Azure is a logical subdivision of a virtual network that allows you to segment and organize resources within defined IP address ranges. It enables isolation, traffic control, and efficient use of network space while supporting features like network security groups, route tables, and service endpoints.

```
azure.network_subnet
```

## Fields

| Title                                 | ID   | Type          | Data Type                                                                                                                   | Description |
| ------------------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string        |
| address_prefix                        | core | string        | The address prefix for the subnet.                                                                                          |
| address_prefixes                      | core | array<string> | List of address prefixes for the subnet.                                                                                    |
| delegations                           | core | json          | An array of references to the delegations on the subnet.                                                                    |
| etag                                  | core | string        | A unique read-only string that changes whenever the resource is updated.                                                    |
| id                                    | core | string        | Resource ID.                                                                                                                |
| location                              | core | string        |
| name                                  | core | string        | The name of the resource that is unique within a resource group. This name can be used to access the resource.              |
| private_endpoint_network_policies     | core | string        | Enable or Disable apply network policies on private end point in the subnet.                                                |
| private_link_service_network_policies | core | string        | Enable or Disable apply network policies on private link service in the subnet.                                             |
| provisioning_state                    | core | string        | The current provisioning state.                                                                                             |
| purpose                               | core | string        | A read-only string identifying the intention of use for this subnet based on delegations and other user-defined properties. |
| resource_group                        | core | string        |
| service_endpoints                     | core | json          | An array of service endpoints.                                                                                              |
| subscription_id                       | core | string        |
| subscription_name                     | core | string        |
| tags                                  | core | hstore_csv    |
| type                                  | core | string        | Resource type.                                                                                                              |
