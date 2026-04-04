# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_vpc_connection.dataset.md

---
title: QuickSight VPC Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight VPC Connection
---

# QuickSight VPC Connection

QuickSight VPC Connection allows Amazon QuickSight to securely connect to data sources within a Virtual Private Cloud (VPC). It establishes a private network link so that QuickSight can access databases and services without exposing them to the public internet, improving security and compliance.

```
aws.quicksight_vpc_connection
```

## Fields

| Title               | ID   | Type          | Data Type                                                                                                                                                | Description |
| ------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| arn                 | core | string        | The Amazon Resource Name (ARN) of the VPC connection.                                                                                                    |
| availability_status | core | string        | The availability status of the VPC connection.                                                                                                           |
| created_time        | core | timestamp     | The time that the VPC connection was created.                                                                                                            |
| dns_resolvers       | core | array<string> | A list of IP addresses of DNS resolver endpoints for the VPC connection.                                                                                 |
| last_updated_time   | core | timestamp     | The time that the VPC connection was last updated.                                                                                                       |
| name                | core | string        | The display name for the VPC connection.                                                                                                                 |
| network_interfaces  | core | json          | A list of network interfaces.                                                                                                                            |
| role_arn            | core | string        | The ARN of the IAM role associated with the VPC connection.                                                                                              |
| security_group_ids  | core | array<string> | The Amazon EC2 security group IDs associated with the VPC connection.                                                                                    |
| status              | core | string        | The status of the VPC connection.                                                                                                                        |
| tags                | core | hstore_csv    |
| vpc_connection_id   | core | string        | The ID of the VPC connection that you're creating. This ID is a unique identifier for each Amazon Web Services Region in an Amazon Web Services account. |
| vpc_id              | core | string        | The Amazon EC2 VPC ID associated with the VPC connection.                                                                                                |
