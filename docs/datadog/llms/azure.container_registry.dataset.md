# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.container_registry.dataset.md

---
title: Container Registry
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Container Registry
---

# Container Registry

This table represents the Container Registry resource from Microsoft Azure.

```
azure.container_registry
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                              | Description |
| ---------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| admin_user_enabled           | core | bool          | The value that indicates whether the admin user is enabled.                            |
| creation_date                | core | string        | The creation date of the container registry in ISO8601 format.                         |
| data_endpoint_enabled        | core | bool          | Enable a single data endpoint per region for serving data.                             |
| data_endpoint_host_names     | core | array<string> | List of host names that will serve data when dataEndpointEnabled is true.              |
| encryption                   | core | json          | The encryption settings of container registry.                                         |
| id                           | core | string        | The resource ID.                                                                       |
| identity                     | core | json          | The identity of the container registry.                                                |
| location                     | core | string        | The location of the resource. This cannot be changed after the resource is created.    |
| login_server                 | core | string        | The URL that can be used to log into the container registry.                           |
| name                         | core | string        | The name of the resource.                                                              |
| network_rule_bypass_options  | core | string        | Whether to allow trusted Azure services to access a network restricted registry.       |
| network_rule_set             | core | json          | The network rule set for a container registry.                                         |
| policies                     | core | json          | The policies for a container registry.                                                 |
| private_endpoint_connections | core | json          | List of private endpoint connections for a container registry.                         |
| provisioning_state           | core | string        | The provisioning state of the container registry at the time the operation was called. |
| public_network_access        | core | string        | Whether or not public network access is allowed for the container registry.            |
| resource_group               | core | string        |
| sku                          | core | json          | The SKU of the container registry.                                                     |
| status                       | core | json          | The status of the container registry at the time the operation was called.             |
| subscription_id              | core | string        |
| subscription_name            | core | string        |
| system_data                  | core | json          | Metadata pertaining to creation and last modification of the resource.                 |
| tags                         | core | hstore_csv    |
| type                         | core | string        | The type of the resource.                                                              |
| zone_redundancy              | core | string        | Whether or not zone redundancy is enabled for this container registry                  |
