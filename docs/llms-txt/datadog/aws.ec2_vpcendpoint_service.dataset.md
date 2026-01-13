# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_vpcendpoint_service.dataset.md

---
title: EC2 VPC Endpoint Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 VPC Endpoint Service
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_vpcendpoint_service.dataset/index.html
---

# EC2 VPC Endpoint Service

This table represents the EC2 VPC Endpoint Service resource from Amazon Web Services.

```
aws.ec2_vpcendpoint_service
```

## Fields

| Title                               | ID   | Type          | Data Type                                                                                                                                                      | Description |
| ----------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string        |
| acceptance_required                 | core | bool          | Indicates whether VPC endpoint connection requests to the service must be accepted by the service owner.                                                       |
| account_id                          | core | string        |
| availability_zones                  | core | array<string> | The Availability Zones in which the service is available.                                                                                                      |
| base_endpoint_dns_names             | core | array<string> | The DNS names for the service.                                                                                                                                 |
| manages_vpc_endpoints               | core | bool          | Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted.                     |
| owner                               | core | string        | The Amazon Web Services account ID of the service owner.                                                                                                       |
| payer_responsibility                | core | string        | The payer responsibility.                                                                                                                                      |
| private_dns_name                    | core | string        | The private DNS name for the service.                                                                                                                          |
| private_dns_name_verification_state | core | string        | The verification state of the VPC endpoint service. Consumers of the endpoint service cannot use the private name when the state is not <code>verified</code>. |
| private_dns_names                   | core | json          | The private DNS names assigned to the VPC endpoint service.                                                                                                    |
| service_id                          | core | string        | The ID of the endpoint service.                                                                                                                                |
| service_name                        | core | string        | The name of the service.                                                                                                                                       |
| service_region                      | core | string        | The Region where the service is hosted.                                                                                                                        |
| service_type                        | core | json          | The type of service.                                                                                                                                           |
| supported_ip_address_types          | core | array<string> | The supported IP address types.                                                                                                                                |
| tags                                | core | hstore        |
| vpc_endpoint_policy_supported       | core | bool          | Indicates whether the service supports endpoint policies.                                                                                                      |
