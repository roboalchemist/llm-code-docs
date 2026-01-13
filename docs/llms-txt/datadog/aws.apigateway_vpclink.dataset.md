# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_vpclink.dataset.md

---
title: API Gateway VPC Link
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway VPC Link
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigateway_vpclink.dataset/index.html
---

# API Gateway VPC Link

This table represents the API Gateway VPC Link resource from Amazon Web Services.

```
aws.apigateway_vpclink
```

## Fields

| Title          | ID   | Type          | Data Type                                                                                                                                                                                                                                                            | Description |
| -------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key           | core | string        |
| account_id     | core | string        |
| description    | core | string        | The description of the VPC link.                                                                                                                                                                                                                                     |
| id             | core | string        | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink.                                                                                                                                                                               |
| name           | core | string        | The name used to label and identify the VPC link.                                                                                                                                                                                                                    |
| status         | core | string        | The status of the VPC link. The valid values are <code>AVAILABLE</code>, <code>PENDING</code>, <code>DELETING</code>, or <code>FAILED</code>. Deploying an API will wait if the status is <code>PENDING</code> and will fail if the status is <code>DELETING</code>. |
| status_message | core | string        | A description about the VPC link status.                                                                                                                                                                                                                             |
| tags           | core | hstore        |
| target_arns    | core | array<string> | The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same Amazon Web Services account of the API owner.                                                                                          |
