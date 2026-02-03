# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_interface.dataset.md

---
title: Network Interface
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Interface
---

# Network Interface

A Network Interface in Azure is a networking resource that connects a virtual machine to a virtual network. It defines how a VM communicates with external resources, other VMs, and the internet. Each network interface can have one or more IP configurations, including private and optional public IP addresses, and can be associated with network security groups for traffic filtering.

```
azure.network_interface
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                           | Description |
| ----------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string        |
| auxiliary_mode                | core | string        | Auxiliary mode of Network Interface resource.                                                                                       |
| dns_settings                  | core | json          | DNS settings of a network interface.                                                                                                |
| dscp_configuration            | core | json          | Reference to another subresource.                                                                                                   |
| enable_accelerated_networking | core | bool          | If the network interface is configured for accelerated networking. Not applicable to VM sizes which require accelerated networking. |
| enable_ip_forwarding          | core | bool          | Indicates whether IP forwarding is enabled on this network interface.                                                               |
| etag                          | core | string        | A unique read-only string that changes whenever the resource is updated.                                                            |
| extended_location             | core | json          | ExtendedLocation complex type.                                                                                                      |
| hosted_workloads              | core | array<string> | A list of references to linked BareMetal resources.                                                                                 |
| id                            | core | string        | Resource ID.                                                                                                                        |
| ip_configurations             | core | json          | A list of IPConfigurations of the network interface.                                                                                |
| location                      | core | string        | Resource location.                                                                                                                  |
| mac_address                   | core | string        | The MAC address of the network interface.                                                                                           |
| migration_phase               | core | string        | Migration phase of Network Interface resource.                                                                                      |
| name                          | core | string        | Resource name.                                                                                                                      |
| nic_type                      | core | string        | Type of Network Interface resource.                                                                                                 |
| primary                       | core | bool          | Whether this is a primary network interface on a virtual machine.                                                                   |
| provisioning_state            | core | string        | The current provisioning state.                                                                                                     |
| resource_group                | core | string        |
| resource_guid                 | core | string        | The resource GUID property of the network interface resource.                                                                       |
| subscription_id               | core | string        |
| subscription_name             | core | string        |
| tags                          | core | hstore_csv    |
| tap_configurations            | core | json          | A list of TapConfigurations of the network interface.                                                                               |
| type                          | core | string        | Resource type.                                                                                                                      |
| virtual_machine               | core | json          | Reference to another subresource.                                                                                                   |
| vnet_encryption_supported     | core | bool          | Whether the virtual machine this nic is attached to supports encryption.                                                            |
| workload_type                 | core | string        | WorkloadType of the NetworkInterface for BareMetal resources                                                                        |
