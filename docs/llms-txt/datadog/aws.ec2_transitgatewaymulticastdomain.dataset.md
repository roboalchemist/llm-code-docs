# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_transitgatewaymulticastdomain.dataset.md

---
title: Ec2 Transitgatewaymulticastdomain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ec2 Transitgatewaymulticastdomain
---

# Ec2 Transitgatewaymulticastdomain

This table represents the ec2_transitgatewaymulticastdomain resource from Amazon Web Services.

```
aws.ec2_transitgatewaymulticastdomain
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                                 | Description |
| ------------------------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string     |
| account_id                           | core | string     |
| creation_time                        | core | timestamp  | The time the transit gateway multicast domain was created.                                |
| options                              | core | json       | The options for the transit gateway multicast domain.                                     |
| owner_id                             | core | string     | The ID of the Amazon Web Services account that owns the transit gateway multicast domain. |
| state                                | core | string     | The state of the transit gateway multicast domain.                                        |
| tags                                 | core | hstore_csv |
| transit_gateway_id                   | core | string     | The ID of the transit gateway.                                                            |
| transit_gateway_multicast_domain_arn | core | string     | The Amazon Resource Name (ARN) of the transit gateway multicast domain.                   |
| transit_gateway_multicast_domain_id  | core | string     | The ID of the transit gateway multicast domain.                                           |
