# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_verified_access_endpoint.dataset.md

---
title: EC2 Verified Access Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Verified Access Endpoint
---

# EC2 Verified Access Endpoint

EC2 Verified Access Endpoint is an AWS resource that provides secure access to applications without requiring a traditional VPN. It allows you to define policies that verify user identity and device posture before granting access, ensuring that only trusted users and devices can connect. This helps improve security while simplifying remote access management.

```
aws.ec2_verified_access_endpoint
```

## Fields

| Title                                      | ID   | Type          | Data Type                                                                                                                                                                                             | Description |
| ------------------------------------------ | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                       | core | string        |
| account_id                                 | core | string        |
| application_domain                         | core | string        | The DNS name for users to reach your application.                                                                                                                                                     |
| attachment_type                            | core | string        | The type of attachment used to provide connectivity between the Amazon Web Services Verified Access endpoint and the application.                                                                     |
| cidr_options                               | core | json          | The options for a CIDR endpoint.                                                                                                                                                                      |
| creation_time                              | core | string        | The creation time.                                                                                                                                                                                    |
| deletion_time                              | core | string        | The deletion time.                                                                                                                                                                                    |
| description                                | core | string        | A description for the Amazon Web Services Verified Access endpoint.                                                                                                                                   |
| device_validation_domain                   | core | string        | Returned if endpoint has a device trust provider attached.                                                                                                                                            |
| domain_certificate_arn                     | core | string        | The ARN of a public TLS/SSL certificate imported into or created with ACM.                                                                                                                            |
| endpoint_domain                            | core | string        | A DNS name that is generated for the endpoint.                                                                                                                                                        |
| endpoint_type                              | core | string        | The type of Amazon Web Services Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified. |
| last_updated_time                          | core | string        | The last updated time.                                                                                                                                                                                |
| load_balancer_options                      | core | json          | The load balancer details if creating the Amazon Web Services Verified Access endpoint as load-balancertype.                                                                                          |
| network_interface_options                  | core | json          | The options for network-interface type endpoint.                                                                                                                                                      |
| policy_document                            | core | string        | The Verified Access policy document.                                                                                                                                                                  |
| policy_enabled                             | core | bool          | The status of the Verified Access policy.                                                                                                                                                             |
| rds_options                                | core | json          | The options for an RDS endpoint.                                                                                                                                                                      |
| security_group_ids                         | core | array<string> | The IDs of the security groups for the endpoint.                                                                                                                                                      |
| sse_specification                          | core | json          | The options in use for server side encryption.                                                                                                                                                        |
| status                                     | core | json          | The endpoint status.                                                                                                                                                                                  |
| tags                                       | core | hstore_csv    |
| verified_access_endpoint_id                | core | string        | The ID of the Amazon Web Services Verified Access endpoint.                                                                                                                                           |
| verified_access_endpoint_target_dns        | core | string        | The DNS name of the target.                                                                                                                                                                           |
| verified_access_endpoint_target_ip_address | core | string        | The IP address of the target.                                                                                                                                                                         |
| verified_access_group_id                   | core | string        | The ID of the Amazon Web Services Verified Access group.                                                                                                                                              |
| verified_access_instance_id                | core | string        | The ID of the Amazon Web Services Verified Access instance.                                                                                                                                           |
