# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elb_load_balancer.dataset.md

---
title: Elastic Load Balancing Load Balancer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elastic Load Balancing Load Balancer
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.elb_load_balancer.dataset/index.html
---

# Elastic Load Balancing Load Balancer

An Elastic Load Balancing Load Balancer in AWS automatically distributes incoming application or network traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses. It improves availability, fault tolerance, and scalability by routing traffic only to healthy resources. Different types of load balancers are available, including Application, Network, and Classic, each optimized for specific use cases.

```gdscript3
aws.elb_load_balancer
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                                                                                                            | Description |
| ----------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                          | core | string        |
| account_id                    | core | string        |
| availability_zones            | core | array<string> | The Availability Zones for the load balancer.                                                                                                                                                                                                                                        |
| backend_server_descriptions   | core | json          | Information about your EC2 instances.                                                                                                                                                                                                                                                |
| canonical_hosted_zone_name    | core | string        | The DNS name of the load balancer. For more information, see Configure a Custom Domain Name in the Classic Load Balancers Guide.                                                                                                                                                     |
| canonical_hosted_zone_name_id | core | string        | The ID of the Amazon Route 53 hosted zone for the load balancer.                                                                                                                                                                                                                     |
| created_time                  | core | timestamp     | The date and time the load balancer was created.                                                                                                                                                                                                                                     |
| dns_name                      | core | string        | The DNS name of the load balancer.                                                                                                                                                                                                                                                   |
| health_check                  | core | json          | Information about the health checks conducted on the load balancer.                                                                                                                                                                                                                  |
| instance_states               | core | json          | Information about the health of the instances.                                                                                                                                                                                                                                       |
| instances                     | core | json          | The IDs of the instances for the load balancer.                                                                                                                                                                                                                                      |
| listener_descriptions         | core | json          | The listeners for the load balancer.                                                                                                                                                                                                                                                 |
| load_balancer_arn             | core | string        |
| load_balancer_attributes      | core | json          | Information about the load balancer attributes.                                                                                                                                                                                                                                      |
| load_balancer_name            | core | string        | The name of the load balancer.                                                                                                                                                                                                                                                       |
| policies                      | core | json          | The policies defined for the load balancer.                                                                                                                                                                                                                                          |
| policy_descriptions           | core | json          | Information about the policies.                                                                                                                                                                                                                                                      |
| scheme                        | core | string        | The type of load balancer. Valid only for load balancers in a VPC. If Scheme is internet-facing, the load balancer has a public DNS name that resolves to a public IP address. If Scheme is internal, the load balancer has a public DNS name that resolves to a private IP address. |
| security_groups               | core | array<string> | The security groups for the load balancer. Valid only for load balancers in a VPC.                                                                                                                                                                                                   |
| source_security_group         | core | json          | The security group for the load balancer, which you can use as part of your inbound rules for your registered instances. To only allow traffic from load balancers, add a security group rule that specifies this source security group as the inbound source.                       |
| subnets                       | core | array<string> | The IDs of the subnets for the load balancer.                                                                                                                                                                                                                                        |
| tags                          | core | hstore        |
| vpc_id                        | core | string        | The ID of the VPC for the load balancer.                                                                                                                                                                                                                                             |
