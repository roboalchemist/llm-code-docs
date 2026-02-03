# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_egress_only_internet_gateway.dataset.md

---
title: Egress-Only Internet Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Egress-Only Internet Gateway
---

# Egress-Only Internet Gateway

An Egress-Only Internet Gateway in AWS is a VPC component that allows outbound-only communication from IPv6-enabled instances to the internet. It prevents unsolicited inbound traffic from reaching those instances, ensuring secure one-way connectivity. This is useful for workloads that need to initiate connections to the internet but should not be directly accessible from outside.

```
aws.ec2_egress_only_internet_gateway
```

## Fields

| Title                            | ID   | Type       | Data Type                                                             | Description |
| -------------------------------- | ---- | ---------- | --------------------------------------------------------------------- | ----------- |
| _key                             | core | string     |
| account_id                       | core | string     |
| attachments                      | core | json       | Information about the attachment of the egress-only internet gateway. |
| egress_only_internet_gateway_arn | core | string     |
| egress_only_internet_gateway_id  | core | string     | The ID of the egress-only internet gateway.                           |
| tags                             | core | hstore_csv |
