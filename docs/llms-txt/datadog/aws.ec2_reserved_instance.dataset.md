# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_reserved_instance.dataset.md

---
title: EC2 Reserved Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Reserved Instance
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_reserved_instance.dataset/index.html
---

# EC2 Reserved Instance

This table represents the EC2 Reserved Instance resource from Amazon Web Services.

```
aws.ec2_reserved_instance
```

## Fields

| Title                 | ID   | Type      | Data Type                                                                                                                                                    | Description |
| --------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string    |
| account_id            | core | string    |
| availability_zone     | core | string    | The Availability Zone in which the Reserved Instance can be used.                                                                                            |
| currency_code         | core | string    | The currency of the Reserved Instance. It's specified using ISO 4217 standard currency codes. At this time, the only supported currency is <code>USD</code>. |
| duration              | core | int64     | The duration of the Reserved Instance, in seconds.                                                                                                           |
| end                   | core | timestamp | The time when the Reserved Instance expires.                                                                                                                 |
| fixed_price           | core | float64   | The purchase price of the Reserved Instance.                                                                                                                 |
| instance_count        | core | int64     | The number of reservations purchased.                                                                                                                        |
| instance_tenancy      | core | string    | The tenancy of the instance.                                                                                                                                 |
| instance_type         | core | string    | The instance type on which the Reserved Instance can be used.                                                                                                |
| offering_class        | core | string    | The offering class of the Reserved Instance.                                                                                                                 |
| offering_type         | core | string    | The Reserved Instance offering type.                                                                                                                         |
| product_description   | core | string    | The Reserved Instance product platform description.                                                                                                          |
| recurring_charges     | core | json      | The recurring charge tag assigned to the resource.                                                                                                           |
| reserved_instance_arn | core | string    |
| reserved_instances_id | core | string    | The ID of the Reserved Instance.                                                                                                                             |
| scope                 | core | string    | The scope of the Reserved Instance.                                                                                                                          |
| start                 | core | timestamp | The date and time the Reserved Instance started.                                                                                                             |
| state                 | core | string    | The state of the Reserved Instance purchase.                                                                                                                 |
| tags                  | core | hstore    |
| usage_price           | core | float64   | The usage price of the Reserved Instance, per hour.                                                                                                          |
