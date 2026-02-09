# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_resource_configuration.dataset.md

---
title: VPC Lattice Resource Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Lattice Resource Configuration
---

# VPC Lattice Resource Configuration

This table represents the VPC Lattice Resource Configuration resource from Amazon Web Services.

```
aws.vpc_lattice_resource_configuration
```

## Fields

| Title                                          | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                 | Description |
| ---------------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                           | core | string        |
| account_id                                     | core | string        |
| allow_association_to_shareable_service_network | core | bool          | Specifies whether the resource configuration is associated with a sharable service network.                                                                                                                                                                                                                               |
| amazon_managed                                 | core | bool          | Indicates whether the resource configuration was created and is managed by Amazon.                                                                                                                                                                                                                                        |
| arn                                            | core | string        | The Amazon Resource Name (ARN) of the resource configuration.                                                                                                                                                                                                                                                             |
| created_at                                     | core | timestamp     | The date and time that the resource configuration was created, in ISO-8601 format.                                                                                                                                                                                                                                        |
| custom_domain_name                             | core | string        | The custom domain name of the resource configuration.                                                                                                                                                                                                                                                                     |
| failure_reason                                 | core | string        | The reason the create-resource-configuration request failed.                                                                                                                                                                                                                                                              |
| id                                             | core | string        | The ID of the resource configuration.                                                                                                                                                                                                                                                                                     |
| last_updated_at                                | core | timestamp     | The most recent date and time that the resource configuration was updated, in ISO-8601 format.                                                                                                                                                                                                                            |
| name                                           | core | string        | The name of the resource configuration.                                                                                                                                                                                                                                                                                   |
| port_ranges                                    | core | array<string> | The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30                                                                                                                                                                  |
| protocol                                       | core | string        | The TCP protocol accepted by the specified resource configuration.                                                                                                                                                                                                                                                        |
| resource_configuration_definition              | core | json          | The resource configuration.                                                                                                                                                                                                                                                                                               |
| resource_configuration_group_id                | core | string        | The ID of the group resource configuration.                                                                                                                                                                                                                                                                               |
| resource_gateway_id                            | core | string        | The ID of the resource gateway used to connect to the resource configuration in a given VPC. You can specify the resource gateway identifier only for resource configurations with type SINGLE, GROUP, or ARN.                                                                                                            |
| status                                         | core | string        | The status of the resource configuration.                                                                                                                                                                                                                                                                                 |
| tags                                           | core | hstore_csv    |
| type                                           | core | string        | The type of resource configuration. <ul> <li> <code>SINGLE</code> - A single resource. </li> <li> <code>GROUP</code> - A group of resources. </li> <li> <code>CHILD</code> - A single resource that is part of a group resource configuration. </li> <li> <code>ARN</code> - An Amazon Web Services resource. </li> </ul> |
