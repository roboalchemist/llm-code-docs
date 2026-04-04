# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_endpoint.dataset.md

---
title: VPC Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Endpoint
---

# VPC Endpoint

This table represents the VPC Endpoint resource from Amazon Web Services.

```
aws.vpc_endpoint
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                  | Description |
| -------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string        |
| account_id                 | core | string        |
| arn                        | core | string        |
| creation_timestamp         | core | timestamp     | The date and time that the endpoint was created.                                                           |
| dns_entries                | core | json          | (Interface endpoint) The DNS entries for the endpoint.                                                     |
| dns_options                | core | json          | The DNS options for the endpoint.                                                                          |
| failure_reason             | core | string        | Reason for the failure.                                                                                    |
| groups                     | core | json          | (Interface endpoint) Information about the security groups that are associated with the network interface. |
| ip_address_type            | core | string        | The IP address type for the endpoint.                                                                      |
| ipv4_prefixes              | core | json          | Array of IPv4 prefixes.                                                                                    |
| ipv6_prefixes              | core | json          | Array of IPv6 prefixes.                                                                                    |
| last_error                 | core | json          | The last error that occurred for endpoint.                                                                 |
| network_interface_ids      | core | array<string> | (Interface endpoint) The network interfaces for the endpoint.                                              |
| owner_id                   | core | string        | The ID of the Amazon Web Services account that owns the endpoint.                                          |
| policies                   | core | json          |
| policy_document            | core | string        | The policy document associated with the endpoint, if applicable.                                           |
| private_dns_enabled        | core | bool          | (Interface endpoint) Indicates whether the VPC is associated with a private hosted zone.                   |
| requester_managed          | core | bool          | Indicates whether the endpoint is being managed by its service.                                            |
| resource_configuration_arn | core | string        | The Amazon Resource Name (ARN) of the resource configuration.                                              |
| route_table_ids            | core | array<string> | (Gateway endpoint) The IDs of the route tables associated with the endpoint.                               |
| service_name               | core | string        | The name of the service to which the endpoint is associated.                                               |
| service_network_arn        | core | string        | The Amazon Resource Name (ARN) of the service network.                                                     |
| service_region             | core | string        | The Region where the service is hosted.                                                                    |
| state                      | core | string        | The state of the endpoint.                                                                                 |
| subnet_ids                 | core | array<string> | (Interface endpoint) The subnets for the endpoint.                                                         |
| tags                       | core | hstore_csv    |
| vpc_endpoint_id            | core | string        | The ID of the endpoint.                                                                                    |
| vpc_endpoint_type          | core | string        | The type of endpoint.                                                                                      |
| vpc_id                     | core | string        | The ID of the VPC to which the endpoint is associated.                                                     |
