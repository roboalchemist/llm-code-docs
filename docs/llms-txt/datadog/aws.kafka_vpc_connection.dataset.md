# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kafka_vpc_connection.dataset.md

---
title: MSK VPC Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MSK VPC Connection
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.kafka_vpc_connection.dataset/index.html
---

# MSK VPC Connection

MSK VPC Connection in AWS allows Amazon Managed Streaming for Apache Kafka (MSK) clusters to connect securely to client applications running in a Virtual Private Cloud (VPC). It establishes private connectivity without exposing traffic to the public internet, improving security and reducing latency. This resource is typically used when clients and MSK clusters are in different VPCs or accounts, enabling seamless communication through VPC peering or PrivateLink.

```
aws.kafka_vpc_connection
```

## Fields

| Title              | ID   | Type          | Data Type                                                                     | Description |
| ------------------ | ---- | ------------- | ----------------------------------------------------------------------------- | ----------- |
| _key               | core | string        |
| account_id         | core | string        |
| authentication     | core | string        | The authentication type of VPC connection.                                    |
| creation_time      | core | timestamp     | The creation time of the VPC connection.                                      |
| security_groups    | core | array<string> | The list of security groups for the VPC connection.                           |
| state              | core | string        | The state of VPC connection.                                                  |
| subnets            | core | array<string> | The list of subnets for the VPC connection.                                   |
| tags               | core | hstore        |
| target_cluster_arn | core | string        | The Amazon Resource Name (ARN) that uniquely identifies an MSK cluster.       |
| vpc_connection_arn | core | string        | The Amazon Resource Name (ARN) that uniquely identifies a MSK VPC connection. |
| vpc_id             | core | string        | The VPC Id for the VPC connection.                                            |
