# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_instanceconnectendpoint.dataset.md

---
title: EC2 Instance Connect Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Instance Connect Endpoint
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_instanceconnectendpoint.dataset/index.html
---

# EC2 Instance Connect Endpoint

This table represents the EC2 Instance Connect Endpoint resource from Amazon Web Services.

```
aws.ec2_instanceconnectendpoint
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                               | Description |
| ----------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string        |
| account_id                    | core | string        |
| availability_zone             | core | string        | The Availability Zone of the EC2 Instance Connect Endpoint.                                                                                                                                                                                                                                                                                                                             |
| created_at                    | core | timestamp     | The date and time that the EC2 Instance Connect Endpoint was created.                                                                                                                                                                                                                                                                                                                   |
| dns_name                      | core | string        | The DNS name of the EC2 Instance Connect Endpoint.                                                                                                                                                                                                                                                                                                                                      |
| fips_dns_name                 | core | string        | <p/>                                                                                                                                                                                                                                                                                                                                                                                    |
| instance_connect_endpoint_arn | core | string        | The Amazon Resource Name (ARN) of the EC2 Instance Connect Endpoint.                                                                                                                                                                                                                                                                                                                    |
| instance_connect_endpoint_id  | core | string        | The ID of the EC2 Instance Connect Endpoint.                                                                                                                                                                                                                                                                                                                                            |
| network_interface_ids         | core | array<string> | The ID of the elastic network interface that Amazon EC2 automatically created when creating the EC2 Instance Connect Endpoint.                                                                                                                                                                                                                                                          |
| owner_id                      | core | string        | The ID of the Amazon Web Services account that created the EC2 Instance Connect Endpoint.                                                                                                                                                                                                                                                                                               |
| preserve_client_ip            | core | bool          | Indicates whether your client's IP address is preserved as the source. The value is <code>true</code> or <code>false</code>. <ul> <li> If <code>true</code>, your client's IP address is used when you connect to a resource. </li> <li> If <code>false</code>, the elastic network interface IP address is used when you connect to a resource. </li> </ul> Default: <code>true</code> |
| security_group_ids            | core | array<string> | The security groups associated with the endpoint. If you didn't specify a security group, the default security group for your VPC is associated with the endpoint.                                                                                                                                                                                                                      |
| state                         | core | string        | The current state of the EC2 Instance Connect Endpoint.                                                                                                                                                                                                                                                                                                                                 |
| state_message                 | core | string        | The message for the current state of the EC2 Instance Connect Endpoint. Can include a failure message.                                                                                                                                                                                                                                                                                  |
| subnet_id                     | core | string        | The ID of the subnet in which the EC2 Instance Connect Endpoint was created.                                                                                                                                                                                                                                                                                                            |
| tags                          | core | hstore        |
| vpc_id                        | core | string        | The ID of the VPC in which the EC2 Instance Connect Endpoint was created.                                                                                                                                                                                                                                                                                                               |
