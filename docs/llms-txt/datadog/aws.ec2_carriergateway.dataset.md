# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_carriergateway.dataset.md

---
title: EC2 Carrier Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Carrier Gateway
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_carriergateway.dataset/index.html
---

# EC2 Carrier Gateway

This table represents the EC2 Carrier Gateway resource from Amazon Web Services.

```
aws.ec2_carriergateway
```

## Fields

| Title              | ID   | Type   | Data Type                                                               | Description |
| ------------------ | ---- | ------ | ----------------------------------------------------------------------- | ----------- |
| _key               | core | string |
| account_id         | core | string |
| carrier_gateway_id | core | string | The ID of the carrier gateway.                                          |
| owner_id           | core | string | The Amazon Web Services account ID of the owner of the carrier gateway. |
| state              | core | string | The state of the carrier gateway.                                       |
| tags               | core | hstore |
| vpc_id             | core | string | The ID of the VPC associated with the carrier gateway.                  |
