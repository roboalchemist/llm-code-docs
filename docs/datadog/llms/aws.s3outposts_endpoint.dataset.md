# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3outposts_endpoint.dataset.md

---
title: S3 on Outposts Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > S3 on Outposts Endpoint
---

# S3 on Outposts Endpoint

S3 on Outposts Endpoint is a resource that provides a network connection point for accessing Amazon S3 storage on AWS Outposts. It enables applications running within the Outpost to securely connect to S3 buckets deployed locally, ensuring low-latency data access and compliance with data residency requirements.

```
aws.s3outposts_endpoint
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                   | Description |
| ------------------------ | ---- | ---------- | --------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| access_type              | core | string     | The type of connectivity used to access the Amazon S3 on Outposts endpoint. |
| account_id               | core | string     |
| cidr_block               | core | string     | The VPC CIDR committed by this endpoint.                                    |
| creation_time            | core | timestamp  | The time the endpoint was created.                                          |
| customer_owned_ipv4_pool | core | string     | The ID of the customer-owned IPv4 address pool used for the endpoint.       |
| endpoint_arn             | core | string     | The Amazon Resource Name (ARN) of the endpoint.                             |
| failed_reason            | core | json       | The failure reason, if any, for a create or delete endpoint operation.      |
| network_interfaces       | core | json       | The network interface of the endpoint.                                      |
| outposts_id              | core | string     | The ID of the Outposts.                                                     |
| security_group_id        | core | string     | The ID of the security group used for the endpoint.                         |
| status                   | core | string     | The status of the endpoint.                                                 |
| subnet_id                | core | string     | The ID of the subnet used for the endpoint.                                 |
| tags                     | core | hstore_csv |
| vpc_id                   | core | string     | The ID of the VPC used for the endpoint.                                    |
