# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_local_gateway.dataset.md

---
title: EC2 Local Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Local Gateway
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_local_gateway.dataset/index.html
---

# EC2 Local Gateway

EC2 Local Gateway is an AWS resource that enables communication between on-premises networks and Amazon VPCs through AWS Outposts. It provides a direct path for local data traffic, allowing workloads running on Outposts to connect to on-premises systems without routing through the AWS Region. This helps reduce latency and supports hybrid cloud architectures.

```
aws.ec2_local_gateway
```

## Fields

| Title            | ID   | Type   | Data Type                                                              | Description |
| ---------------- | ---- | ------ | ---------------------------------------------------------------------- | ----------- |
| _key             | core | string |
| account_id       | core | string |
| local_gateway_id | core | string | The ID of the local gateway.                                           |
| outpost_arn      | core | string | The Amazon Resource Name (ARN) of the Outpost.                         |
| owner_id         | core | string | The ID of the Amazon Web Services account that owns the local gateway. |
| state            | core | string | The state of the local gateway.                                        |
| tags             | core | hstore |
